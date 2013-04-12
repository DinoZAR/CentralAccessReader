'''
Created on Jan 21, 2013

@author: Spencer
'''
import sys
import os.path
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QUrl, QDir
from PyQt4 import QtCore
from PyQt4.QtWebKit import QWebPage, QWebInspector, QWebSettings
from lxml import etree
from src.forms.mainwindow_ui import Ui_MainWindow
from src.gui.settings import Settings
from src.gui.mathmlcodes_dialog import MathMLCodesDialog
from src.gui.configuration import Configuration
from src import pyttsx, docx
from src.mathml.tts import MathTTS
from src.mathml import pattern_editor
from src.speech.assigner import Assigner
from src.speech.worker import SpeechWorker
from src.gui.bookmarks import BookmarksTreeModel, BookmarkNode

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
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
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
        
        # Used for refreshing the document later to make changes
        self.lastDocumentFilePath = ''
        
        
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        
        self.ui.playButton.clicked.connect(self.playButton_clicked)
        self.ui.pauseButton.clicked.connect(self.pauseButton_clicked)
        self.ui.settingsButton.clicked.connect(self.settingsButton_clicked)
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        self.ui.repeatButton.clicked.connect(self.repeatButton_clicked)
        self.ui.actionOpen_HTML.triggered.connect(self.openHTML)
        self.ui.actionOpen_Docx.triggered.connect(self.openDocx)
        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionOpen_Pattern_Editor.triggered.connect(self.openPatternEditor)
        self.ui.actionShow_All_MathML.triggered.connect(self.showAllMathML)
        
        # self.ui.muteButton.clicked.connect(self.muteButton_clicked)
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        
        # For the bookmarks
        self.ui.bookmarksTreeView.clicked.connect(self.bookmarksTree_clicked)
        
    def updateSettings(self):
        
        # Update speech thread with my stuff
        self.changeVolume.emit(self.configuration.volume)
        self.changeRate.emit(self.configuration.rate)
        self.changeVoice.emit(self.configuration.voice)
        
        # Update main window sliders to match
        self.ui.rateSlider.setValue(self.configuration.rate)
        self.ui.volumeSlider.setValue(int(self.configuration.volume * 100))
        
        self.ui.rateLabel.setText(str(self.configuration.rate))
        self.ui.volumeLabel.setText(str(int(self.configuration.volume * 100)))
        
        # Finally, save it all to file
        self.configuration.saveToFile('configuration.xml')
            
    def playButton_clicked(self):
        
        # Get list of string output for feeding into my speech
        outputList = self.assigner.getSpeech(unicode(self.ui.webView.selectedHtml()))
        
        for o in outputList:
            self.addToQueue.emit(o[0], o[1])
        
        self.ui.webView.page().mainFrame().evaluateJavaScript('SetBeginning()')
        self.isFirst = True
        
        self.startPlayback.emit()
        
    def onWord(self, text, location, label, stream):
        
        if not self.isFirst:
            if label == "text":
                if label != self.lastElement[2] or (location != self.lastElement[1]) or (stream != self.lastElement[3]):
                    self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
            elif label == "math":
                if label != self.lastElement[2]:
                    self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
            elif label == "image":
                if label != self.lastElement[2]:
                    self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
            else:
                self.ui.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement()')
        else:
            # Do this because the SetBeginning() function highlighted it
            self.isFirst = False
            
        # Store what the last element was that was being spoken
        self.lastElement = [text, location, label, stream]
        
    def onSpeechFinished(self):
        print 'Speech finished.'
        self.ui.webView.page().mainFrame().evaluateJavaScript('ClearHighlight()');
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
        
    def repeatButton_clicked(self):
        self.repeat = not self.repeat
        self.repeatText = self.assigner.getSpeech(unicode(self.ui.webView.selectedHtml()))
        self.size = self.assigner.getSpeech(unicode(self.ui.webView.selectedHtml())).__len__()
        
        if self.repeat:
            
            self.stop = False
            self.ui.webView.page().setContentEditable(True)
            self.ui.webView.triggerPageAction(QWebPage.MoveToPreviousChar)
            self.ui.webView.triggerPageAction(QWebPage.SelectNextWord)
            self.ui.webView.page().setContentEditable(False)
            
            while not self.stop:
                self.loc = 0
                
                if self.ttsEngine._inLoop:
                    self.ttsEngine.endLoop()
                self.ttsEngine.say(self.repeatText)
                self.ttsEngine.runAndWait()
                self.ui.webView.page().setContentEditable(True)
                self.ui.webView.triggerPageAction(QWebPage.MoveToNextChar)
                for x in range(0,self.size):
                    self.ui.webView.triggerPageAction(QWebPage.MoveToPreviousChar)
                self.ui.webView.triggerPageAction(QWebPage.MoveToPreviousChar)
                self.ui.webView.triggerPageAction(QWebPage.SelectNextWord)
                self.ui.webView.page().setContentEditable(False)
            
        else:
            self.stop = True
        
            
            
    def openHTML(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open HTML','./tests','(*.html)')
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
        filePath = QtGui.QFileDialog.getOpenFileName(self, 'Open HTML','./tests','(*.docx)')
        
        if len(filePath) > 0:
            url = os.path.join(os.getcwd(), 'import')
            baseUrl = QUrl.fromLocalFile(url)
            
            docxHtml = docx.getHtmlAndNavigation(str(filePath))
            
            self.assigner.prepare(docxHtml[0])
            self.ui.webView.setHtml(docxHtml[0], baseUrl)
            
            # Set the root bookmark for the tree model
            self.bookmarksModel = BookmarksTreeModel(docxHtml[1])
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
        print 'Change fired!'
        self.mathTTS.setPatternDatabase(databaseFileName)
        
    def showAllMathML(self):
        self.mathmlDialog = MathMLCodesDialog(self.ttsEngine, self.assigner._maths)
        self.mathmlDialog.show()
        
    def bookmarksTree_clicked(self, index):
        node = index.internalPointer()
        
        # Do the anchor navigation
        print 'Node anchor id:', node.anchorId
        self.ui.webView.page().mainFrame().evaluateJavaScript('GotoPageAnchor(' + node.anchorId + ');')
        
    def refreshDocument(self):
        if len(self.lastDocumentFilePath) > 0:
            url = os.path.join(os.getcwd(), 'import')
            baseUrl = QUrl.fromLocalFile(url)
            
            docxHtml = docx.getHtmlAndNavigation(str(self.lastDocumentFilePath))
            
            self.assigner.prepare(docxHtml[0])
            
            # Clear all of the caches
            QWebSettings.clearMemoryCaches()
            
            self.ui.webView.setHtml(docxHtml[0], baseUrl)
            
            # Set the root bookmark for the tree model
            self.bookmarksModel = BookmarksTreeModel(docxHtml[1])
            self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
