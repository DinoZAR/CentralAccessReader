'''
Created on Jan 21, 2013

@author: Spencer
'''
import sys
import os.path
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QUrl, QMutex
from PyQt4 import QtCore
from PyQt4.QtWebKit import QWebPage, QWebInspector, QWebSettings
from lxml import etree
from src.forms.mainwindow_ui import Ui_MainWindow
from src.gui.settings import Settings
from src.gui.mathmlcodes_dialog import MathMLCodesDialog
from src.gui.configuration import Configuration
from src.gui.npa_webview import NPAWebView
from src.gui.bookmarks import BookmarksTreeModel, BookmarkNode
from src.mathml.tts import MathTTS
from src.mathml import pattern_editor
from src.speech.assigner import Assigner
from src.speech.worker import SpeechWorker
from src.docx.importer import DocxDocument

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
        
        # Set the math TTS using the internal pattern database
        self.mathTTS = MathTTS('mathml/parser_pattern_database.txt')
        
        # TTS states
        self.stopSpeech = True
        self.isFirst = False
        self.lastElement = ['', -1, '', -1]
        self.repeat = False
        self.repeatText = ' '
        
        # This class is used for assigning the different parts of the content
        # to a specific method of how to speak it
        self.assigner = Assigner()
        
        # Set up my speech driver and start it
        self.speechThread = SpeechWorker()
        
        self.speechThread.onWord.connect(self.onWord)
        self.speechThread.onFinish.connect(self.onSpeechFinished)   
        
        self.startPlayback.connect(self.speechThread.startPlayback)
        self.stopPlayback.connect(self.speechThread.stopPlayback)
        self.addToQueue.connect(self.speechThread.addToQueue)
        self.changeVolume.connect(self.speechThread.setVolume)
        self.changeRate.connect(self.speechThread.setRate)
        self.changeVoice.connect(self.speechThread.setVoice)
        
        self.speechThread.start()
        
        # Load the configuration file
        self.configuration = Configuration()
        self.configuration.loadFromFile('configuration.xml')
        self.updateSettings()
        
        # Used for refreshing the document later to make changes. Also store
        # the data for the document itself.
        self.lastDocumentFilePath = ''
        self.document = None
        
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        # Toolbar buttons
        self.ui.playButton.clicked.connect(self.playButton_clicked)
        self.ui.pauseButton.clicked.connect(self.pauseButton_clicked)
        self.ui.settingsButton.clicked.connect(self.settingsButton_clicked)
        self.ui.zoomInButton.clicked.connect(self.zoomInButton_clicked)
        self.ui.zoomOutButton.clicked.connect(self.zoomOutButton_clicked)
        
        # Main menu actions
        self.ui.actionOpen_HTML.triggered.connect(self.openHTML)
        self.ui.actionOpen_Docx.triggered.connect(self.openDocx)
        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionOpen_Pattern_Editor.triggered.connect(self.openPatternEditor)
        self.ui.actionShow_All_MathML.triggered.connect(self.showAllMathML)
        
        # Sliders
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        
        # Bookmark controls and widgets
        self.ui.bookmarksTreeView.clicked.connect(self.bookmarksTree_clicked)
        self.ui.bookmarkZoomInButton.clicked.connect(self.bookmarkZoomInButton_clicked)
        self.ui.bookmarkZoomOutButton.clicked.connect(self.bookmarkZoomOutButton_clicked)
        
    def updateSettings(self):
        
        # Update speech thread with my stuff
        self.changeVolume.emit(self.configuration.volume)
        self.changeRate.emit(self.configuration.rate)
        self.changeVoice.emit(self.configuration.voice)
        
        # Update main window sliders to match
        self.ui.rateSlider.setValue(self.configuration.rate)
        self.ui.volumeSlider.setValue(int(self.configuration.volume * 100))
        
        # Finally, save it all to file
        self.configuration.saveToFile('configuration.xml')
            
    def playButton_clicked(self):
        
        # Get list of string output for feeding into my speech
        outputList = self.assigner.getSpeech(unicode(self.ui.webView.selectedHtml()))
        
        for o in outputList:
            self.addToQueue.emit(o[0], o[1])
        
        if self.configuration.highlight_enable:
            self.javascriptMutex.lock()
            self.ui.webView.page().mainFrame().evaluateJavaScript('SetBeginning()')
            self.javascriptMutex.unlock()
            self.isFirst = True
        
        self.startPlayback.emit()
        
    def onWord(self, text, location, label, stream):
        
        if self.configuration.highlight_enable:
            if not self.isFirst:
                if label == "text":
                    if label != self.lastElement[2] or (location != self.lastElement[1]) or (stream != self.lastElement[3]):
                        self.javascriptMutex.lock()
                        self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
                        self.javascriptMutex.unlock()
                elif label == "math":
                    if (label != self.lastElement[2]) or (stream != self.lastElement[3]):
                        self.javascriptMutex.lock()
                        self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
                        self.javascriptMutex.unlock()
                elif label == "image":
                    if (label != self.lastElement[2]) or (stream != self.lastElement[3]):
                        self.javascriptMutex.lock()
                        self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
                        self.javascriptMutex.unlock()
                else:
                    self.javascriptMutex.lock()
                    self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
                    self.javascriptMutex.unlock()
            else:
                # Do this because the SetBeginning() function highlighted it
                self.isFirst = False
            
        # Store what the last element was that was being spoken
        self.lastElement = [text, location, label, stream]
        
    def onSpeechFinished(self):
        print 'Speech finished.'
        self.javascriptMutex.lock()
        self.ui.webView.page().mainFrame().evaluateJavaScript('ClearAllHighlights()')
        self.javascriptMutex.unlock()
        self.isFirst = False
        
    def pauseButton_clicked(self):
        self.isFirst = False
        self.stopPlayback.emit()

    def muteButton_clicked(self):
        pass
            
    def rateSlider_valueChanged(self, value):
        self.configuration.rate = value
        self.updateSettings()

    def volumeSlider_valueChanged(self, value):
        self.configuration.volume = float(value) / 100.0
        self.updateSettings()
        
    def settingsButton_clicked(self):
        dialog = Settings(self)
        dialog.exec_()
        self.configuration.loadFromFile('configuration.xml')
        self.updateSettings()
        
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
        
    def openDocx(self):
        savePath = os.path.dirname(os.path.realpath(__file__))
        savePath = savePath.replace('\\','/')
        savePath = str(savePath).rsplit('/',1).pop(0) + '/tests/'
        filePath = QtGui.QFileDialog.getOpenFileName(self, 'Open Docx...','./tests','(*.docx)')
        
        if len(filePath) > 0:
            url = os.path.join(os.getcwd(), 'import')
            baseUrl = QUrl.fromLocalFile(url)
            
            self.document = DocxDocument(str(filePath))
            docxHtml = self.document.getMainPage()
            
            self.assigner.prepare(docxHtml)
            self.ui.webView.setHtml(docxHtml, baseUrl)
            
            # Set the root bookmark for the tree model
            self.bookmarksModel = BookmarksTreeModel(self.document.getBookmarks())
            self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
            
            self.lastDocumentFilePath = filePath
            
    def quit(self):
        self.close()
        
    def openPatternEditor(self):
        
        from mathml.pattern_editor.gui.patterneditorwindow import PatternEditorWindow

        patternFilePath = 'mathml/parser_pattern_database.txt'
        
        self.patternWindow = PatternEditorWindow(patternFilePath, '')
        self.patternWindow.changedPattern.connect(self.onChangedPatternEditor)
        self.patternWindow.show()
        
    def onChangedPatternEditor(self, databaseFileName):
        self.mathTTS.setPatternDatabase(databaseFileName)
        
    def showAllMathML(self):
        self.mathmlDialog = MathMLCodesDialog(self.ttsEngine, self.assigner._maths)
        self.mathmlDialog.show()
        
    def bookmarksTree_clicked(self, index):
        node = index.internalPointer()
        self.javascriptMutex.lock()
        print 'Navigating to anchor:', node.anchorId
        self.ui.webView.page().mainFrame().evaluateJavaScript('GotoPageAnchor(' + node.anchorId + ');')
        self.javascriptMutex.unlock()
        
    def bookmarkZoomInButton_clicked(self):
        # Get the current font
        currentFont = self.ui.bookmarksTreeView.font()
        
        # Make it a litter bigger
        size = currentFont.pointSize()
        size += 2
        currentFont.setPointSize(size)
        
        # Set the font
        self.ui.bookmarksTreeView.setFont(currentFont)
        
    def bookmarkZoomOutButton_clicked(self):
        # Get the current font
        currentFont = self.ui.bookmarksTreeView.font()
        
        # Make it a litter smaller
        size = currentFont.pointSize()
        size -= 2
        if size < 4:
            size = 4
        currentFont.setPointSize(size)
        
        # Set the font
        self.ui.bookmarksTreeView.setFont(currentFont)
        
    def refreshDocument(self):
        if len(self.lastDocumentFilePath) > 0:
            url = os.path.join(os.getcwd(), 'import')
            baseUrl = QUrl.fromLocalFile(url)
            
            self.document = DocxDocument(str(self.lastDocumentFilePath))
            docxHtml = self.document.getMainPage()
            
            self.assigner.prepare(docxHtml)
            
            # Clear all of the caches
            QWebSettings.clearMemoryCaches()
            
            self.ui.webView.setHtml(docxHtml, baseUrl)
            
            # Set the root bookmark for the tree model
            self.bookmarksModel = BookmarksTreeModel(self.document.getBookmarks())
            self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
