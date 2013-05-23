'''
Created on Jan 21, 2013

@author: Spencer
'''
import os
import webbrowser
import traceback
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QUrl, QMutex
from PyQt4 import QtCore
from PyQt4.QtWebKit import QWebPage, QWebInspector, QWebSettings
from lxml import etree
from src.forms.mainwindow_ui import Ui_MainWindow
from src.gui.color_settings import ColorSettings
from src.gui.speech_settings import SpeechSettings
from src.gui.mathmlcodes_dialog import MathMLCodesDialog
from src.gui.configuration import Configuration
from src.gui.npa_webview import NPAWebView
from src.gui.bookmarks import BookmarksTreeModel, BookmarkNode
from src.gui.pages import PagesTreeModel, PageNode
from src.gui.about import AboutDialog
from src.gui.bug_reporter import BugReporter
from src.mathml.tts import MathTTS
from src.mathml import pattern_editor
from src.speech.assigner import Assigner
from src.speech.worker import SpeechWorker
from src.docx.importer import DocxDocument
from src.misc import app_data_path, temp_path, program_path, js_command, UpdateQtThread
from src import misc

class MainWindow(QtGui.QMainWindow):
    loc = 0
    len = 0
    jumped = False
    
    # TTS control signals
    startPlayback = QtCore.pyqtSignal()
    stopPlayback = QtCore.pyqtSignal()
    addToQueue = QtCore.pyqtSignal(str, str)
    
    changeVolume = QtCore.pyqtSignal(float)
    changeRate = QtCore.pyqtSignal(int)
    changeVoice = QtCore.pyqtSignal(str)
    
    # JavaScript mutex
    javascriptMutex = QMutex()
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Replace the web view in my designer with my custom web view
        self.ui.webViewLayout.removeWidget(self.ui.webView)
        self.ui.webView.close()
        self.ui.webView = NPAWebView(self.ui.centralwidget)
        self.ui.webViewLayout.addWidget(self.ui.webView, 1)
        self.ui.webViewLayout.update()
        
        # Connect all of my signals
        self.connect_signals()
        
        # This is the tree model used to store our bookmarks
        self.bookmarksModel = BookmarksTreeModel(BookmarkNode(None, 'Something'))
        self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
        
        # This is my web inspector for debugging my JavaScript code
        self.webInspector = QWebInspector()
        self.ui.webView.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.webInspector.setPage(self.ui.webView.page())
        
        # Set the math TTS using the internal pattern database
        self.mathTTS = MathTTS(program_path('src/mathml/parser_pattern_database.txt'))
        
        # TTS states
        self.ttsPlaying = False
        self.stopSpeech = True
        self.isFirst = False
        self.hasWorded = False;
        self.lastElement = ['', -1, '', -1]
        self.repeat = False
        self.repeatText = ' '
        
        # This class is used for assigning the different parts of the content
        # to a specific method of how to speak it
        self.assigner = Assigner()
        
        # Set up my speech driver and start it
        self.speechThread = SpeechWorker()
        
        self.speechThread.onWord.connect(self.onWord)
        self.speechThread.onEndStream.connect(self.onEndStream)
        self.speechThread.onFinish.connect(self.onSpeechFinished)   
        
        self.startPlayback.connect(self.speechThread.startPlayback)
        self.stopPlayback.connect(self.speechThread.stopPlayback)
        self.addToQueue.connect(self.speechThread.addToQueue)
        self.changeVolume.connect(self.speechThread.setVolume)
        self.changeRate.connect(self.speechThread.setRate)
        self.changeVoice.connect(self.speechThread.setVoice)
        
        self.speechThread.start()
        
        # Create the general-purpose progress dialog
        self.progressDialog = QtGui.QProgressDialog('Stuff', 'Cancel', 0, 100, self)
        
        # Load the configuration file
        self.configuration = Configuration()
        self.configuration.loadFromFile(app_data_path('configuration.xml'))
        self.updateSettings()
        
        # Set the zoom of the content view (separate from the bookmarks zoom)
        self.ui.webView.setZoom(self.configuration.zoom_content)
        
        # Used for refreshing the document later to make changes. Also store
        # the data for the document itself.
        self.lastDocumentFilePath = ''
        self.document = None
        
        # Show the tutorial if I user hasn't seen it yet
        if self.configuration.showTutorial:
            self.openTutorial()
            
            # Immediately turn the switch off
            self.configuration.showTutorial = False
            self.updateSettings()
            
    def closeEvent(self, event):
        self.configuration.zoom_content = self.ui.webView.getZoom()
        self.configuration.saveToFile(app_data_path('configuration.xml'))
        
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        # Toolbar buttons
        self.ui.playButton.clicked.connect(self.playButton_clicked)
        self.ui.pauseButton.clicked.connect(self.pauseButton_clicked)
        self.ui.colorSettingsButton.clicked.connect(self.colorSettingsButton_clicked)
        self.ui.speechSettingsButton.clicked.connect(self.speechSettingsButton_clicked)
        self.ui.saveToMP3Button.clicked.connect(self.saveToMP3Button_clicked)
        self.ui.zoomInButton.clicked.connect(self.zoomInButton_clicked)
        self.ui.zoomOutButton.clicked.connect(self.zoomOutButton_clicked)
        
        # Main menu actions
        self.ui.actionOpen_Docx.triggered.connect(self.showOpenDocxDialog)
        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionOpen_Pattern_Editor.triggered.connect(self.openPatternEditor)
        self.ui.actionShow_All_MathML.triggered.connect(self.showAllMathML)
        self.ui.actionTutorial.triggered.connect(self.openTutorial)
        self.ui.actionAbout.triggered.connect(self.openAboutDialog)
        self.ui.actionReport_a_Bug.triggered.connect(self.openReportBugWindow)
        self.ui.actionTake_A_Survey.triggered.connect(self.openSurveyWindow)
        
        # Sliders
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        
        # Bookmark and page controls and widgets
        self.ui.bookmarksTreeView.clicked.connect(self.bookmarksTree_clicked)
        self.ui.pagesTreeView.clicked.connect(self.pagesTree_clicked)
        self.ui.bookmarkZoomInButton.clicked.connect(self.bookmarkZoomInButton_clicked)
        self.ui.bookmarkZoomOutButton.clicked.connect(self.bookmarkZoomOutButton_clicked)
        self.ui.expandBookmarksButton.clicked.connect(self.expandBookmarksButton_clicked)
        self.ui.collapseBookmarksButton.clicked.connect(self.collapseBookmarksButton_clicked)
        
    def updateSettings(self):
        
        # Update speech thread with my stuff
        self.changeVolume.emit(self.configuration.volume)
        self.changeRate.emit(self.configuration.rate)
        self.changeVoice.emit(self.configuration.voice)
        
        # Update main window sliders to match
        self.ui.rateSlider.setValue(self.configuration.rate)
        self.ui.volumeSlider.setValue(int(self.configuration.volume))
        
        # Zoom settings
        currentFont = self.ui.bookmarksTreeView.font()
        currentFont.setPointSize(self.configuration.zoom_navigation_ptsize)
        self.ui.bookmarksTreeView.setFont(currentFont)
        self.ui.pagesTreeView.setFont(currentFont)
        
        # Finally, save it all to file
        self.configuration.saveToFile(app_data_path('configuration.xml'))
            
    def playButton_clicked(self):
        
        # Stop whatever the speech thread may be saying
        self.stopPlayback.emit()
        
        # Wait for the speech to quit completely
        while self.ttsPlaying:
            QtGui.qApp.processEvents()
        
        # Get list of string output for feeding into my speech
        outputList = []
        self.javascriptMutex.lock()
        selectedHTML = self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('GetSelectionHTML', [])).toString()
        self.javascriptMutex.unlock()
        print 'HTML Content:', [unicode(selectedHTML)]
        outputList = self.assigner.getSpeech(unicode(selectedHTML), self.configuration)
        
        print 'Output:', outputList
        
        # Add my words to the queue
        for o in outputList:
            self.addToQueue.emit(o[0], o[1])
        
        self.javascriptMutex.lock()
        self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('SetBeginning', [self.configuration.highlight_line_enable, outputList[0][1]]))
        self.javascriptMutex.unlock()
        
        self.isFirst = True
        self.lastElement = ['', -1, '', -1]
        
        self.startPlayback.emit()
        
        self.ttsPlaying = True
        self.setSettingsEnableState()
        
    def onWord(self, offset, length, label, stream):
        
        print 'On Word!', offset, length, label, stream
        
        self.hasWorded = True
        
        if label == 'text':
            if (self.lastElement[3] != stream) and (self.lastElement[3] >= 0):
                self.javascriptMutex.lock()
                self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('HighlightNextElement', [self.configuration.highlight_line_enable, str(label), str(self.lastElement[2])]))
                self.javascriptMutex.unlock()
            self.javascriptMutex.lock()
            self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('HighlightWord', [self.configuration.highlight_line_enable, offset, length]))
            self.javascriptMutex.unlock()
            self.isFirst = False
        elif label == 'math':
            if not self.isFirst:
                if label != self.lastElement[2] or stream != self.lastElement[3] and (self.lastElement[3] >= 0):
                    self.javascriptMutex.lock()
                    self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('HighlightNextElement', [self.configuration.highlight_line_enable, str(label), str(self.lastElement[2])]))
                    self.javascriptMutex.unlock()
            else:
                self.isFirst = False
        elif label == 'image':
            if not self.isFirst:
                if label != self.lastElement[2] or stream != self.lastElement[3] and (self.lastElement[3] >= 0):
                    self.javascriptMutex.lock()
                    self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('HighlightNextElement', [self.configuration.highlight_line_enable, str(label), str(self.lastElement[2])]))
                    self.javascriptMutex.unlock()
            else:
                self.isFirst = False
        else:
            print 'ERROR: I don\'t know what this label refers to for highlighting:', label
        
        self.lastElement = [offset, length, label, stream]
        
    def onEndStream(self, stream, label):
        print 'Stream ended!', stream, label
        
        #if (not self.hasWorded) and (label == 'text') and (not self.isFirst):
        #    self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('HighlightWord', [self.configuration.highlight_line_enable, str(label), str(self.lastElement[2])]))
            
        self.hasWorded = False
        self.isFirst = False
        
    def onSpeechFinished(self):
        print 'Speech finished.'
        self.javascriptMutex.lock()
        self.ui.webView.page().mainFrame().evaluateJavaScript('ClearAllHighlights()')
        self.javascriptMutex.unlock()
        self.isFirst = False
        self.ttsPlaying = False
        self.lastElement = ['', -1, '', -1]
        self.setSettingsEnableState()
        
    def pauseButton_clicked(self):
        self.isFirst = False
        self.stopPlayback.emit()
        self.ttsPlaying = False
        self.setSettingsEnableState()

    def muteButton_clicked(self):
        pass
            
    def rateSlider_valueChanged(self, value):
        self.configuration.rate = value
        self.updateSettings()

    def volumeSlider_valueChanged(self, value):
        self.configuration.volume = value
        self.updateSettings()
        
    def colorSettingsButton_clicked(self):
        dialog = ColorSettings(self)
        result = dialog.exec_()
        self.configuration.loadFromFile(app_data_path('configuration.xml'))
        if result == ColorSettings.RESULT_NEED_REFRESH:
            print 'Color settings needing refresh...'
            self.refreshDocument()
        self.updateSettings()
        
    def speechSettingsButton_clicked(self):
        dialog = SpeechSettings(self)
        dialog.exec_()
        self.configuration.loadFromFile(app_data_path('configuration.xml'))
        self.updateSettings()
        
    def saveToMP3Button_clicked(self):
        # Generate a filename that is basically the original file but with the
        # .mp3 extension at the end
        defaultFileName = os.path.splitext(str(self.lastDocumentFilePath))[0] + '.mp3'
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save MP3...', defaultFileName, '(*.mp3)')
        print 'Saving to...', fileName
        if len(fileName) > 0:
            print 'Got a saved place!'
            
            # Show a progress dialog
            self.progressDialog.setWindowModality(Qt.WindowModal)
            self.progressDialog.setWindowTitle('Saving to MP3...')
            self.progressDialog.setLabelText('Generating speech...')
            self.progressDialog.setValue(0)
            self.progressDialog.show()
            QtGui.qApp.processEvents()
            
            # Get my speech output list
            outputList = []
            selectedHTML = self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('GetSelectionHTML', [])).toString()
            outputList = self.assigner.getSpeech(unicode(selectedHTML), self.configuration)
                
            
            # Get the progress of the thing from the speech thread
            def myOnProgress(percent):
                self.progressDialog.setValue(percent)
                QtGui.qApp.processEvents()
                
            def myOnProgressLabel(newLabel):
                self.progressDialog.setLabelText(newLabel)
                QtGui.qApp.processEvents()
                
            self.speechThread.onProgress.connect(myOnProgress)
            self.speechThread.onProgressLabel.connect(myOnProgressLabel)
            self.progressDialog.canceled.connect(self.speechThread.stopMP3)
            self.speechThread.saveToMP3(str(fileName), outputList)
            
            # Just hide it so that we can use it later
            self.progressDialog.hide()
            
            # Show a message box saying the file was successfully saved
            if not self.speechThread.mp3Interrupted():
                messageBox = QtGui.QMessageBox()
                messageText = 'Success!\nYour MP3 was saved as:\n' + str(fileName)
                messageBox.setText(messageText)
                messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
                messageBox.setDefaultButton(QtGui.QMessageBox.Ok)
                messageBox.setWindowTitle('MP3 Saved Successfully')
                messageBox.setIcon(QtGui.QMessageBox.Information)
                messageBox.exec_()
        
    def zoomInButton_clicked(self):
        self.ui.webView.zoomIn()
    
    def zoomOutButton_clicked(self):
        self.ui.webView.zoomOut()
            
    def openHTML(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open HTML...','./tests','(*.html)')
        f = open(fileName, 'r')
        content = f.read()
        f.close()
        self.assigner.prepare(content)
        baseUrl = QUrl.fromLocalFile(fileName)
        self.ui.webView.setHtml(content, baseUrl)
        
    def openDocx(self, filePath):
        
        t = UpdateQtThread()
        try:
            if len(filePath) > 0:
                url = temp_path('import')
                baseUrl = QUrl.fromLocalFile(url)
                print 'Base url:', url
                
                # Show a progress dialog
                self.progressDialog.setWindowModality(Qt.WindowModal)
                self.progressDialog.setWindowTitle('Opening Word document...')
                self.progressDialog.setLabelText('Reading ' + os.path.basename(str(filePath)) + '...')
                self.progressDialog.setValue(0)
                self.progressDialog.show()
                QtGui.qApp.processEvents()
                    
                # Run a separate thread for updating my stuff
                t.start()
                
                self.document = DocxDocument(str(filePath))
                docxHtml = self.document.getMainPage()
                
                # Clear the cache in the web view
                QWebSettings.clearIconDatabase()
                QWebSettings.clearMemoryCaches()
                
                self.assigner.prepare(docxHtml)
                self.ui.webView.setHtml(docxHtml, baseUrl)
                
                # Get and set the bookmarks
                self.bookmarksModel = BookmarksTreeModel(self.document.getBookmarks())
                self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
                self.ui.bookmarksTreeView.expandAll()
                
                # Get and set the pages
                self.pagesModel = PagesTreeModel(self.document.getPages())
                self.ui.pagesTreeView.setModel(self.pagesModel)
                self.ui.pagesTreeView.expandAll()
                
                self.lastDocumentFilePath = filePath
                
                t.stop()
                t.join()
                self.progressDialog.hide()
        
        except Exception as e:
            t.stop()
            t.join()
            self.progressDialog.hide()
            out = misc.prepare_bug_report(traceback.format_exc(), self.configuration)
            dialog = BugReporter(out)
            dialog.exec_()
        
    def showOpenDocxDialog(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self, 'Open Docx...',os.path.join(os.path.expanduser('~'), 'Documents'),'(*.docx)')
        self.openDocx(filePath)
            
    def openTutorial(self):
        self.openDocx(program_path('Tutorial.docx'))
            
    def openAboutDialog(self):
        dialog = AboutDialog()
        dialog.exec_()
        
    def openReportBugWindow(self):
        webbrowser.open_new(misc.REPORT_BUG_URL)
        
    def openSurveyWindow(self):
        webbrowser.open_new(misc.SURVEY_URL)
            
    def quit(self):
        self.close()
        
    def openPatternEditor(self):
        
        from mathml.pattern_editor.gui.patterneditorwindow import PatternEditorWindow

        patternFilePath = program_path('mathml/parser_pattern_database.txt')
        
        self.patternWindow = PatternEditorWindow(patternFilePath, '')
        self.patternWindow.changedPattern.connect(self.onChangedPatternEditor)
        self.patternWindow.show()
        
    def onChangedPatternEditor(self, databaseFileName):
        self.mathTTS.setPatternDatabase(databaseFileName)
        
    def showAllMathML(self):
        self.mathmlDialog = MathMLCodesDialog(self.assigner._maths)
        self.mathmlDialog.show()
        
    def bookmarksTree_clicked(self, index):
        node = index.internalPointer()
        self.javascriptMutex.lock()
        self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('GotoPageAnchor', [node.anchorId]))
        self.javascriptMutex.unlock()
        
    def pagesTree_clicked(self, index):
        node = index.internalPointer()
        self.javascriptMutex.lock()
        self.ui.webView.page().mainFrame().evaluateJavaScript(js_command('GotoPageAnchor', [node.anchorId]))
        self.javascriptMutex.unlock()
        
    def bookmarkZoomInButton_clicked(self):
        # Get the current font
        currentFont = self.ui.bookmarksTreeView.font()
        
        # Make it a litter bigger
        self.configuration.zoom_navigation_ptsize += 2
        currentFont.setPointSize(self.configuration.zoom_navigation_ptsize)
        
        # Set the font
        self.ui.bookmarksTreeView.setFont(currentFont)
        self.ui.pagesTreeView.setFont(currentFont)
        
    def bookmarkZoomOutButton_clicked(self):
        # Get the current font
        currentFont = self.ui.bookmarksTreeView.font()
        
        # Make it a litter smaller
        self.configuration.zoom_navigation_ptsize -= 2
        if self.configuration.zoom_navigation_ptsize < 4:
            self.configuration.zoom_navigation_ptsize = 4
        currentFont.setPointSize(self.configuration.zoom_navigation_ptsize)
        
        # Set the font
        self.ui.bookmarksTreeView.setFont(currentFont)
        self.ui.pagesTreeView.setFont(currentFont)
        
    def expandBookmarksButton_clicked(self):
        self.ui.bookmarksTreeView.expandAll()
        
    def collapseBookmarksButton_clicked(self):
        self.ui.bookmarksTreeView.collapseAll()
        
    def refreshDocument(self):
        if len(self.lastDocumentFilePath) > 0:
            self.openDocx(self.lastDocumentFilePath)
            
    def setSettingsEnableState(self):
        '''
        Disables or enables the TTS sliders depending on whether we are playing
        back right now or not.
        '''
        if self.ttsPlaying:
            self.ui.rateSlider.setEnabled(False)
            self.ui.volumeSlider.setEnabled(False)
            self.ui.colorSettingsButton.setEnabled(False)
            self.ui.speechSettingsButton.setEnabled(False)
            self.ui.saveToMP3Button.setEnabled(False)
            self.ui.playButton.setEnabled(False)
        else:
            self.ui.rateSlider.setEnabled(True)
            self.ui.volumeSlider.setEnabled(True)
            self.ui.colorSettingsButton.setEnabled(True)
            self.ui.speechSettingsButton.setEnabled(True)
            self.ui.saveToMP3Button.setEnabled(True)
            self.ui.playButton.setEnabled(True)