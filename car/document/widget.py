'''
Created on Nov 15, 2013

@author: Spencer Graffe
'''
from HTMLParser import HTMLParser
import re
import os

from lxml import html
from lxml.etree import ParserError, XMLSyntaxError
from PyQt4.QtCore import QUrl, pyqtSignal, QMutex, QTimer, pyqtSlot, QMimeData
from PyQt4.QtGui import QWidget, QMessageBox, QFileDialog, QApplication
from PyQt4.QtWebKit import QWebInspector, QWebSettings

from car.export.html_single import HTMLSingleExportThread
from car.export.mp3 import MP3ExportThread
from car.export.mp3_by_page import MP3ByPageExportThread
from car.forms.document_widget_ui import Ui_DocumentWidget
from car.gui import configuration
from car.gui.search_settings import SearchSettings
from car import misc

class DocumentWidget(QWidget):
    '''
    Widget that encapsulates the interaction with a particular document.
    '''
    loadProgress = pyqtSignal(int, unicode)
    loadFinished = pyqtSignal()
    
    toggleSpeechPlayback = pyqtSignal()
    contentCommand = pyqtSignal(unicode)
    
    requestPaste = pyqtSignal()
    requestReadFromSelection = pyqtSignal()
    
    # unicode - navigation heading string
    # unicode - page number string
    requestUpdateNavigation = pyqtSignal(unicode, unicode)
    
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QWidget.__init__(self, parent)
        
        self.ui = Ui_DocumentWidget()
        self.ui.setupUi(self)
        
        self.webInspector = QWebInspector()
        self.ui.webView.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.webInspector.setPage(self.ui.webView.page())     
        
        # Get all of the search-related functions and group them so that I can
        # hide them at will.
        self.searchWidgets = []
        self.searchWidgets.append(self.ui.searchPrevious)
        self.searchWidgets.append(self.ui.searchNext)
        self.searchWidgets.append(self.ui.searchBox)
        self.searchWidgets.append(self.ui.searchSettingsButton)
        self.searchWidgets.append(self.ui.searchCloseButton)
        
        self._searchToggle = False
        self._searchSettings = {'match_case' : False,
                                'whole_word' : False}
        self._searchSettingsDialog = SearchSettings()
        self.showSearch(self._searchToggle)
        
        # Get all of the progress-related functions and group them
        self.progressWidgets = []
        self.progressWidgets.append(self.ui.progressLabel)
        self.progressWidgets.append(self.ui.progressBar)
        self.progressWidgets.append(self.ui.progressCancelButton)
        self.progressWidgets.append(self.ui.showFilesButton)
        self.hideProgressWidgets()
        
        # Document it is showing
        self.document = None
        self._lastExportFilePath = ''
        
        # TTS states
        self.ttsStates = {}
        self._resetTTSStates()
        
        # JavaScript lock
        self._javaLock = QMutex()
        
        # Export thread
        self.exportThread = None
        
        self.connect_signals()
        
    def connect_signals(self):
        '''
        Connects my controls to its corresponding functions.
        '''
        self.ui.webView.loadProgress.connect(self._reportLoadProgress)
        self.ui.webView.loadFinished.connect(self._reportMathTypeset)
        self.ui.webView.toggleSpeechPlayback.connect(self.toggleSpeechPlayback)
        self.ui.webView.contentCommand.connect(self.contentCommand)
        
        self.ui.searchPrevious.clicked.connect(self._searchPrevious)
        self.ui.searchNext.clicked.connect(self._searchNext)
        self.ui.searchBox.returnPressed.connect(self._searchNext)
        self.ui.searchSettingsButton.clicked.connect(self._showSearchSettings)
        self.ui.searchCloseButton.clicked.connect(self._hideSearch)
        
        self.ui.progressCancelButton.clicked.connect(self.hideProgressWidgets)
        self.ui.showFilesButton.clicked.connect(self._showFiles)
        
        self.ui.webView.requestCopy.connect(self.copyToClipboard)
        self.ui.webView.requestPaste.connect(self.requestPaste)
        self.ui.webView.requestReadFromSelection.connect(self.requestReadFromSelection)
        self.ui.webView.requestSaveSelectionToMP3.connect(self.saveMP3Selection)
        self.ui.webView.cursorMoved.connect(self._emitNavigationBarUpdate)
        
    def disconnectSignals(self):
        '''
        Disconnects all signals associated with this widget.
        '''
        pass
#         try:
#             self.loadProgress.disconnect()
#         except Exception as e:
#             print e
#             
#         try:
#             self.loadFinished.disconnect()
#         except Exception as e:
#             print e
#             
#         try:
#             self.toggleSpeechPlayback.disconnect()
#         except Exception as e:
#             print e
#         
#         try:
#             self.contentCommand.disconnect()
#         except Exception as e:
#             print e

    def copyToClipboard(self):
        '''
        Copies the content selected by user to the clipboard. It will also clean
        up some things so that it works more nicely (like copying math
        equations, for instance).
        '''
        myHtml = html.fromstring(unicode(self.ui.webView.selectedHtml()))
        
        # Get all math equations rendered as SVGs and replace them with MathML
        maths = myHtml.xpath(".//span[@class='mathmlEquation']")
        for i in range(len(maths)):
            
            # Get the ID for the replacement
            query = maths[i].xpath(".//span[@class='MathJax_SVG']")
            if len(query) > 0:
                myId = query[0].get('id')
                myMathML = self.document.getMathMLFromID(myId)
                
                # Replace the span with my MathML
                maths[i].replace(query[0], myMathML)
        
        # Get the content I am selecting
        myData = QMimeData()
        myData.setHtml(html.tostring(myHtml))
        QApplication.clipboard().setMimeData(myData)
    
    def showSearch(self, isShown):
        '''
        Shows or hides the search items.
        '''
        for w in self.searchWidgets:
            w.setVisible(isShown)
        
        if isShown:
            self.ui.searchBox.selectAll()
            self.ui.searchBox.setFocus()
        
    def _hideSearch(self):
        self.showSearch(False)
        self._searchToggle = False
        
    def showProgressWidgets(self):
        for w in self.progressWidgets:
            w.show()
            
    def hideProgressWidgets(self):
        for w in self.progressWidgets:
            w.hide()
            
    def setDocument(self, doc):
        '''
        Sets the document to the view in this widget. It will start emitting
        signals for the loading process.
        '''
        url = misc.temp_path('import')
        baseUrl = QUrl.fromLocalFile(url)
        
        # Clear all of the caches
        QWebSettings.clearIconDatabase()
        QWebSettings.clearMemoryCaches()

        self.document = doc
        self.ui.webView.page().mainFrame().addToJavaScriptWindowObject('AlmightyGod', self);
        self.ui.webView.page().mainFrame().setHtml(self.document.getMainPage(), baseUrl)
        
        if not misc.is_release_environment():
            self.webInspector.setPage(self.ui.webView.page())
        
    def refreshDocument(self):
        '''
        Refreshes the document. One may do this when updating the CSS, for
        example.
        '''
        self._runJavaScript('RefreshDocument', [])
        
    def setContentFocus(self):
        '''
        Brings the keyboard focus to the content window.
        '''
        self.ui.webView.setFocus()
        
    def zoomIn(self):
        self.ui.webView.zoomIn()
        return self.getZoom()
    
    def zoomOut(self):
        self.ui.webView.zoomOut()
        return self.getZoom()
    
    def zoomReset(self):
        self.ui.webView.zoomReset()
        return self.getZoom()
    
    def getZoom(self):
        return self.ui.webView.getZoom()
    
    def setZoom(self, val):
        self.ui.webView.setZoom(val)
        
    def gotoAnchor(self, anchorId):
        '''
        Moves the view to the new anchor ID. This is for navigation between
        headings.
        '''
        self._runJavaScript('GotoPageAnchor', [anchorId])
        self.setContentFocus()
        
    def gotoPage(self, pageAnchorId):
        '''
        Moves the view to the specified page number.
        '''
        self._runJavaScript('GotoPageAnchor', [pageAnchorId])
        self.setContentFocus()
        
    def toggleSearchBar(self):
        '''
        Toggles the search bar.
        '''
        self._searchToggle = not self._searchToggle
        self.showSearch(self._searchToggle)
        
    def setKeyboardNavEnabled(self, isEnabled):
        '''
        Sets whether the keyboard navigation is enabled or not.
        '''
        self.ui.webView.setKeyboardNavEnabled(isEnabled)
        
        for w in self.searchWidgets:
            w.setEnabled(isEnabled)
        
    def setStreamBeginning(self):
        '''
        Sets up the highlighter for streaming. Returns the first chunk of
        content to be read as an lxml element.
        '''
        contents = unicode(self._runJavaScript('StartHighlighting', []).toString())
        
        # Convert the HTML to DOM
        root = None
        try:
            root = html.fromstring(contents)
        except XMLSyntaxError:
            root = html.Element('p')
        
        return root
    
    def hasMoreSpeech(self):
        '''
        Returns whether there is more speech to deliver.
        '''
        return self._runJavaScript('HasMoreElements', []).toBool()
    
    def streamNextElement(self):
        '''
        Returns the next element to stream. The element is an lxml element.
        '''
        nextContent = unicode(self._runJavaScript('StreamNextElement', []).toString())
        
        # Create the HTML DOM from content
        elem = None
        if len(nextContent) > 0:
            try:
                isMatch = re.search(r'<.+>', nextContent)
                if isMatch is None:
                    elem = html.Element('p')
                    h = HTMLParser()
                    elem.text = h.unescape(nextContent)
                else:
                    elem = html.fromstring(nextContent)
            except ParserError as e:
                elem = html.Element('p')
        else:
            elem = html.Element('p')
            
        return elem
    
    def selectAll(self):
        '''
        Selects all of the text in the content, much like a user would by
        pressing Ctrl-A.
        '''
        self.ui.webView.selectAll()
    
    def clearAllHighlights(self):
        '''
        Clears the highlights from the content.
        '''
        self._runJavaScript('ClearAllHighlights', [])
        
    def setHighlightToBeginning(self):
        '''
        Sets the highlight back to the beginning. It will create the highlight
        if one doesn't exist.
        '''
        self._runJavaScript('SetHighlightToBeginning', [])
        
    def getSelectionHTML(self):
        '''
        Returns an lxml element representing the currently selected HTML.
        '''
        selectedHTML = unicode(self._runJavaScript('GetSelectionHTML', []).toString())
        return html.fromstring(selectedHTML)
    
    def getBodyHTML(self):
        '''
        Gets the body portion of the HTML currently in the content view. Returns
        an lxml element representing it.
        '''
        htmlString = unicode(self._runJavaScript('GetBodyHTML', []).toString())
        return html.fromstring(htmlString)
    
    def getEntireHTML(self):
        return html.fromstring(unicode(self.ui.webView.page().mainFrame().toHtml()))
    
    def clearUserSelection(self):
        '''
        Clears the user selection.
        '''
        self._runJavaScript('ClearUserSelection', [])
    
    def onStart(self, offset, length, label, stream, word):
        pass
        #self._runJavaScript('StartHighlighting', [])
    
    def onWord(self, offset, length, label, stream, word, isFirst):
        '''
        Sets the highlighter to the next location.
        '''
        
        lastElement = self.ttsStates['lastElement']
        self.ttsStates['hasWorded'] = True
        
        if label == 'text':
            self._runJavaScript('HighlightNextWord', [configuration.getBool('HighlightLineEnable', True), unicode(word), offset, length, configuration.getBool('FollowInsideParagraph', True)])
            
        elif label == 'math':
            if label != lastElement[2] or stream != lastElement[3] and (lastElement[3] >= 0):
                self._runJavaScript('HighlightNextMath', [configuration.getBool('HighlightLineEnable', True)])
                    
        elif label == 'image':
            if label != lastElement[2] or stream != lastElement[3] and (lastElement[3] >= 0):
                self._runJavaScript('HighlightNextImage', [configuration.getBool('HighlightLineEnable', True)])
        else:
            print 'ERROR: I don\'t know what this label refers to for highlighting:', label
        
        self.ttsStates['lastElement'] = [offset, length, label, stream]
        self._emitNavigationBarUpdate()
    
    def onEndStream(self, stream, label):
        '''
        Lets the highlighter know that a stream has ended. In other words, a
        particular kind of content has ended.
        '''
        pass
    
    def onSpeechFinished(self):
        '''
        Lets the highlighter know that speech playback has ended.
        '''
        # Tell JavaScript to not highlight further
        self._runJavaScript('StopHighlighting', [])  
        self._resetTTSStates()
        self.ui.webView.setFocus()
        
    def saveToHTML(self):
        '''
        Saves the document to HTML.
        '''
        if self._checkExportThreadRunning():
            
            content = self.getEntireHTML()
            
            self.exportThread = HTMLSingleExportThread(self.document, content, self.document._tempFolder) 
            
            defaultFileName = self.exportThread.getDefaultPath(self.document.getFilePath())
            fileName = unicode(QFileDialog.getSaveFileName(self, 'Export HTML...', defaultFileName, '(*.html)'))
             
            if len(fileName) > 0:
                self._startExportThread(fileName)
        
    def saveMP3ByPage(self):
        '''
        Saves the entire document to MP3 to a folder, split by page.
        '''
        if self._checkExportThreadRunning():
            
            self.exportThread = MP3ByPageExportThread(self.document, self.getBodyHTML(), self.document._tempFolder)
            
            # NOTE: Getting the parent directory of the default path, since the
            # actual path refers to a directory that doesn't exist
            defaultFolder = os.path.dirname(self.exportThread.getDefaultPath(self.document.getFilePath()))
            folder = unicode(QFileDialog.getSaveFileName(self, 'Select Folder to Save MP3s', defaultFolder))
                                                 
            if len(folder) > 0:
                self._startExportThread(folder)
    
    def saveMP3All(self):
        '''
        Saves the entire document to MP3
        '''
        self.clearAllHighlights()
        self.selectAll()
        self.saveMP3Selection()
    
    def saveMP3Selection(self):
        '''
        Saves the current selection to MP3.
        '''
        # Get the selection first and reset
        myHTML = self.getSelectionHTML()
        self.setHighlightToBeginning()
        self.clearUserSelection()
        
        if self._checkExportThreadRunning():
            
            self.exportThread = MP3ExportThread(self.document, myHTML, self.document._tempFolder)
        
            defaultFileName = self.exportThread.getDefaultPath(self.document.getFilePath())
            fileName = unicode(QFileDialog.getSaveFileName(self, 'Save MP3...', defaultFileName, '(*.mp3)'))
                
            if len(fileName) > 0:
                self._startExportThread(fileName)
                
    def _runJavaScript(self, jsFunction, args):
        '''
        Runs the JavaScript function along with its list of arguments. Returns
        the result of the computation.
        
        jsFunction - string representing name of function
        args - list of arguments. They will be converted to a form JavaScript
        understands. Does not support generic Python objects.
        '''
        self._javaLock.lock()
        results = self.ui.webView.page().mainFrame().evaluateJavaScript(misc.js_command(jsFunction, args))
        self._javaLock.unlock()
        return results
    
    def _printJavaScriptConsoleMessage(self, message, lineNum, idString):
        '''
        Allows me to print out the console messages coming from my JavaScript.
        This way I don't have to use the web inspector each time.
        '''
        print 'JavaScript - ' + str(lineNum) + ':', unicode(message)
            
    def _checkExportThreadRunning(self):
        '''
        Checks whether there is an export thread already running on this
        document. If so, it will ask the user if they want to cancel current
        one to be replaced with a different one.
        
        Returns True if procedure should continue, False otherwise
        '''
        if self.exportThread is not None:
            if self.exportThread.isRunning():
                result = self._showCancelExport()
                if result:
                    self.exportThread.stop()
                    self.hideProgressWidgets()
                    while self.exportThread.isRunning():
                        pass
                else:
                    return False
        
        return True
    
    def _startExportThread(self, fileName):
        self._lastExportFilePath = fileName
        self.exportThread.setFilePath(fileName)
        
        # Connect all of the signals
        self.exportThread.progress.connect(self._exportProgress)
        self.exportThread.finished.connect(self._exportFinished)
        self.ui.progressCancelButton.clicked.connect(self.exportThread.stop)
        
        # Set the progress to default values
        self.ui.progressBar.setValue(0)
        self.ui.progressLabel.setText('Starting up...')
        
        # Show the progress widgets
        self.showProgressWidgets()
        self.ui.showFilesButton.hide()
        
        # Start the export
        self.exportThread.start()
        
    def _exportProgress(self, percent, label):
        self.ui.progressBar.setValue(percent)
        self.ui.progressLabel.setText(label)
    
    def _exportFinished(self):
        if self.exportThread.isSuccess:
            self.hideProgressWidgets()
            self.ui.progressLabel.show()
            self.ui.progressLabel.setText('Export Successful!')
            self.ui.showFilesButton.show()
        
        else:
            # If the cancel button was already pressed, the widgets will already
            # be hidden, so no point in showing them that the export has failed.
            #
            # However, if the progress widgets are in view, then it means it did
            # fail because we didn't cancel it
            
            # Hide everything but what we need
            self.ui.progressBar.hide()
            self.ui.showFilesButton.hide()
            
            self.ui.progressLabel.setText('Export failed.')
    
    def _showCancelExport(self):
        '''
        Shows a dialog asking the user if they want to cancel the current
        export. If they want to, then the current export is canceled and the
        export routine runs as normal. Returns True if the user wants to cancel,
        False otherwise.
        '''
        d = QMessageBox()
        d.setText('Export is already in progress. Want to cancel it?')
        d.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        d.setDefaultButton(QMessageBox.No)
        d.setIcon(QMessageBox.Question)
        result = d.exec_()
        if result == QMessageBox.Yes:
            return True
        else:
            return False
    
    def _showSearchSettings(self):
        '''
        Shows the dialog for settings the search settings.
        '''
        self._searchSettingsDialog.setConfig(self._searchSettings)
        self._searchSettingsDialog.show()
    
    def _searchPrevious(self):
        '''
        Searches before the current highlight for the words.
        '''
        text = unicode(self.ui.searchBox.text())
        args = [text, False, self._searchSettings['whole_word'], self._searchSettings['match_case']]
        result = self._runJavaScript('SearchForText', args)
        if not result:
            message = QMessageBox()
            message.setText('No other occurrences of "' + text + '" in document.')
            message.exec_()
    
    def _searchNext(self):
        '''
        Searches after the current highlight for the words.
        '''
        text = unicode(self.ui.searchBox.text())
        args = [text, True, self._searchSettings['whole_word'], self._searchSettings['match_case']]
        result = self._runJavaScript('SearchForText', args)
        if not result:
            message = QMessageBox()
            message.setText('No other occurrences of "' + text + '" in document.')
            message.exec_()
        
    def _reportLoadProgress(self, percent):
        '''
        Signals the loading progress of the document into the view. This does
        not count math equation typesetting yet.
        '''
        self.loadProgress.emit(percent, 'Loading document into view...')
        
    def _reportMathTypeset(self):
        '''
        Reports whether the math is finished typesetting or the progress if it
        hasn't yet. Uses signals so that the main GUI thread remains responsive.
        '''
        if not self._runJavaScript('IsMathTypeset', []).toBool():
            percent = int(self._runJavaScript('GetMathTypesetProgress', []).toInt()[0])
            self.loadProgress.emit(percent, 'Typesetting math equations...')
            QTimer.singleShot(100, self._reportMathTypeset)
        else:
            self.loadFinished.emit()
        
    def _resetTTSStates(self):
        self.ttsStates = {'lastElement' : ['', -1, '', -1], 
                          'hasWorded' : False}
    
    def _showFiles(self):
        misc.open_file_browser_to_location(self._lastExportFilePath)
        self.hideProgressWidgets()
        self.ui.showFilesButton.hide()
    
    @pyqtSlot()
    def _emitNavigationBarUpdate(self):
        '''
        Gets the current heading and page IDs that the highlight is at and emits
        the signal to tell everyone about it.
        '''
        newHeading = unicode(self._runJavaScript('GetCurrentHeading', []).toString())
        newPage = unicode(self._runJavaScript('GetCurrentPage', []).toString())
        
        self.requestUpdateNavigation.emit(newHeading, newPage)