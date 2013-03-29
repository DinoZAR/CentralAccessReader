'''
Created on Jan 21, 2013

@author: Spencer
'''
import sys
import os.path
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QUrl, QDir
from PyQt4.QtWebKit import QWebPage
from src.forms.mainwindow_ui import Ui_MainWindow
from src.gui.settings import Settings
from src.gui.mathmlcodes_dialog import MathMLCodesDialog
from src import pyttsx, docx
from src.mathml.tts import MathTTS
from src.mathml import pattern_editor
from src.speech.assigner import Assigner
from src.gui.bookmarks import BookmarksTreeModel, BookmarkNode

class MainWindow(QtGui.QMainWindow):
    loc = 0
    len = 0
    jumped = False
    
    def __init__(self, ttsEngine, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        #self.ui.webView.setUrl(QUrl('tests/test_file.html'))
        
        # Set the TTS engine and connect all of its callbacks
        self.ttsEngine = ttsEngine
        self.ttsEngine.connect('started-word', self.onWord)
        
        self.mathTTS = MathTTS('mathml/parser_pattern_database.txt')
        
        #sets pyttsx to the currently saved settings in ttsSettings.txt
        d = open('ttsSettings.txt', 'r+')
        self.sVol = float(d.readline())
        self.sRate = float(d.readline())
        self.sVoice = d.readline()
        d.close()
        self.ttsEngine.setProperty('rate', self.sRate)
        self.ttsEngine.setProperty('volume', self.sVol)
        self.ttsEngine.setProperty('voice', self.sVoice)
        self.ui.rateLabel.setText(str(int(self.sRate)))
        self.ui.volLabel.setText(str(int(self.sVol*100)))
        self.ui.rateSlider.setValue(self.sRate)
        self.ui.volumeSlider.setValue(self.sVol* 100)
        self.stop = True
        
        self.repeat = False
        self.repeatText = ' '
        
        # This class is used for assigning the different parts of the content
        # to a specific method of how to speak it
        self.assigner = Assigner()
        
        # This is the tree model used to store our bookmarks
        self.bookmarksModel = BookmarksTreeModel(BookmarkNode(None, 'Something'))
        self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
        
        self.connect_signals()
        
        
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
        #self.ui.muteButton.clicked.connect(self.muteButton_clicked)
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        
        # For the bookmarks
        self.ui.bookmarksTreeView.clicked.connect(self.bookmarksTree_clicked)
        
        # Test buttons for moving selection around
        self.ui.nextWordButton.clicked.connect(self.nextWord_clicked)
        self.ui.lastWordButton.clicked.connect(self.lastWord_clicked)
        
    def onWord(self, name, location, length):
        print name, location, length
        move = location - self.loc
        jump = location - self.loc - self.len
        self.loc = location
        self.len = length
        if(move > 0):
            moved = True
        if(jump>5):
            self.jumped = not self.jumped
            if(self.jumped):
                self.ui.webView.page().setContentEditable(True)
                self.ui.webView.triggerPageAction(QWebPage.MoveToNextChar)
                self.ui.webView.triggerPageAction(QWebPage.MoveToNextChar)
                self.ui.webView.triggerPageAction(QWebPage.MoveToNextChar)
                self.ui.webView.triggerPageAction(QWebPage.SelectEndOfLine)
                self.ui.webView.page().setContentEditable(False)
        if(self.jumped):
            self.ui.webView.page().setContentEditable(True)
            self.ui.webView.page().setContentEditable(False)
        elif(moved):
            self.ui.webView.page().setContentEditable(True)
            self.ui.webView.triggerPageAction(QWebPage.MoveToNextChar)
            self.ui.webView.triggerPageAction(QWebPage.MoveToNextChar)
            self.ui.webView.triggerPageAction(QWebPage.SelectNextWord)
            self.ui.webView.page().setContentEditable(False)
        if self.stop:
            #print 'Stopping...'
            self.repeat = False
            self.ttsEngine.stop()
            self.ttsEngine = pyttsx.init()
            self.stop = False

            
    def playButton_clicked(self):
        self.loc = 0
        
        if len(unicode(self.ui.webView.selectedText())) == 0:
            self.ui.webView.triggerPageAction(QWebPage.SelectAll)
        elif len(unicode(self.ui.webView.selectedText()).split()) == 1:
            self.ui.webView.triggerPageAction(QWebPage.SelectEndOfDocument)
            
        print unicode(self.ui.webView.selectedHtml(), 'utf-8')
        
        output = self.assigner.getSpeech(unicode(self.ui.webView.selectedHtml()))
        
        self.ui.webView.page().setContentEditable(True)
        self.ui.webView.triggerPageAction(QWebPage.MoveToPreviousChar)
        self.ui.webView.triggerPageAction(QWebPage.SelectNextWord)
        self.ui.webView.page().setContentEditable(False)
        
        self.stop = False
        self.ttsEngine.say(output)
        self.ttsEngine.runAndWait()
        
        
    def pauseButton_clicked(self):
        self.stop = True

    def muteButton_clicked(self):
        if self.ttsEngine.getProperty('volume') > 0:
            self.mVol = self.ttsEngine.getProperty('volume')
            self.ttsEngine.setProperty('volume', 0.0)
        else:
            self.ttsEngine.setProperty('volume',self.mVol)
            
    def rateSlider_valueChanged(self, value):
        self.ttsEngine.setProperty('rate', value)
        self.ui.rateLabel.setText(str(value))
        

    def volumeSlider_valueChanged(self, value):
        self.ttsEngine.setProperty('volume', value/100)
        self.ui.volLabel.setText(str(value))
        
    def settingsButton_clicked(self):
        f = open('ttsSettings.txt', 'w')
        self.vol = self.ui.volumeSlider.value()/100.0
        f.write(str(self.vol))
        f.write('\n')
        f.write(str(self.ui.rateSlider.value()))
        f.write('\n')
        f.write(str(self.sVoice))
        f.close()
        dialog = Settings(self.ttsEngine)
        dialog.exec_()
        d = open('ttsSettings.txt', 'r')
        self.sVol = float(d.readline())
        self.sRate = float(d.readline())
        self.sVoice = d.readline()
        self.ttsEngine.setProperty('rate', self.sRate)
        self.ttsEngine.setProperty('volume', self.sVol)
        self.ttsEngine.setProperty('voice', self.sVoice)
        self.ui.rateLabel.setText(str(self.sRate))
        self.ui.volLabel.setText(str(self.sVol*100))
        self.ui.rateSlider.setValue(self.sRate)
        self.ui.volumeSlider.setValue(self.sVol* 100)
        
        
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
        self.ui.webView.page().mainFrame().evaluateJavaScript('GotoPageAnchor(' + node.anchorId + ');')
        
    def nextWord_clicked(self):
        self.ui.webView.page().mainFrame().evaluateJavaScript('SetHighlight();')
        self.ui.webView.triggerPageAction(QWebPage.SelectNextChar)
        
    def lastWord_clicked(self):
        self.ui.webView.triggerPageAction(QWebPage.SelectPreviousWord)
        
