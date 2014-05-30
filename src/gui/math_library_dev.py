'''
Created on May 20, 2014

@author: Spencer Graffe
'''
import os

from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QMessageBox, qApp

from src.forms.math_library_dev_ui import Ui_MathLibraryDev
from src.gui.math_library_editor import MathLibraryEditor
from src.gui import configuration
from src.math_library.library import MathLibrary
try:
    from src.math_to_prose_fast.tts import MathTTS
except ImportError as ex:
    print 'Loading slower MathTTS...', ex
    from src.math_to_prose.tts import MathTTS
from src.speech import driver

class MathLibraryDev(QMainWindow):
    '''
    Provides a development environment for the math libraries, allowing users to
    create and modify their own.
    '''

    def __init__(self, parent=None):
        super(MathLibraryDev, self).__init__(parent)
        
        self.ui = Ui_MathLibraryDev()
        self.ui.setupUi(self)
        
        # Adjust some splitter handles
        self.ui.splitter.setSizes([1000, 500])

        self._mathTTS = MathTTS()

        # Set up the TTS driver (use settings from configuration of before)
        self._ttsEngine = driver.get_driver()
        self._ttsEngine.setVolume(configuration.getInt('Volume'))
        self._ttsEngine.setRate(configuration.getInt('Rate'))
        self._ttsEngine.setVoice(configuration.getValue('Voice'))

        # Clear the tabs
        self.ui.libraryTabs.clear()
        
        self.connect_signals()
    
    def connect_signals(self):
        # File menu
        self.ui.actionNew_Library.triggered.connect(self.newLibrary)
        self.ui.actionOpen_Library.triggered.connect(self.openLibrary)
        self.ui.actionSave.triggered.connect(self.saveCurrent)
        self.ui.actionSave_As.triggered.connect(self.saveAsCurrent)
        
        self.ui.actionNew_Pattern.triggered.connect(self.newPattern)
        self.ui.actionOpen_Pattern.triggered.connect(self.openPattern)
        
        # MathML menu
        self.ui.actionFrom_Clipboard.triggered.connect(self.importMathFromClipboard)
        
        # Controls
        self.ui.libraryTabs.tabCloseRequested.connect(self.closeLibrary)
        self.ui.runButton.clicked.connect(self.runCurrentLibrary)
        
    def currentLibraryEditor(self):
        return self.ui.libraryTabs.currentWidget()
    
    def importMathFromClipboard(self):
        '''
        Pastes the MathML from the clipboard into the MathML editor, if any.
        '''
        mime = QApplication.clipboard().mimeData()
        
        # Get the text from the clipboard
        if mime.hasHtml():
            self.ui.mathmlEditor.setMath(unicode(mime.html()))
            
        elif mime.hasText():
            self.ui.mathmlEditor.setMath(unicode(QApplication.clipboard().text()))
    
    def newLibrary(self):
        '''
        Appends a new math library to the editor.
        '''
        w = MathLibraryEditor()
        w.nameChanged.connect(self._updateLibraryName)
        self.ui.libraryTabs.addTab(w, w.name)

    def openLibrary(self):
        '''
        Opens a library from file.
        '''
        filePath = unicode(QFileDialog.getOpenFileName(self, 'Open Math Library',
                                                       os.path.expanduser('~/Desktop'),
                                                       'Math Library (*.mathlib)'))
        if len(filePath) > 0:
            lib = MathLibrary(filePath)
            w = MathLibraryEditor(library=lib)
            w.nameChanged.connect(self._updateLibraryName)
            self.ui.libraryTabs.addTab(w, w.name)

    def newPattern(self):
        '''
        Appends a new pattern to the current library.
        '''
        editor = self.currentLibraryEditor()
        if editor is not None:
            editor.newPattern()
            
    def openPattern(self):
        '''
        Appends a new pattern to the library from file.
        '''
        editor = self.currentLibraryEditor()
        if editor is not None:
            editor.openPattern()
    
    def closeLibrary(self, tabIndex):
        '''
        Closes the library at the tab location.
        '''
        self.ui.libraryTabs.removeTab(tabIndex)
    
    def saveCurrent(self):
        '''
        Saves the current library.
        '''
        self.currentLibraryEditor().save()

    def saveAsCurrent(self):
        '''
        Saves the current library using Save As.
        '''
        self.currentLibraryEditor().saveAs()

    def runCurrentLibrary(self):
        '''
        Runs the current library with the MathML.
        '''
        self.ui.proseOutput.setText('Compiling...')
        qApp.processEvents()
        editor = self.currentLibraryEditor()
        if editor is not None:
            lib = editor.library
            pattern = editor.currentPattern()
            if pattern is not None:
                try:
                    self._mathTTS.setMathLibrary(lib, pattern)
                    prose = self._mathTTS.parse(self.ui.mathmlEditor.getMath())
                    self.ui.proseOutput.setText(prose)
                    self._ttsEngine.stop()
                    self._ttsEngine.setSpeechGenerator([(prose, 'math')])
                    self._ttsEngine.start()
                except Exception as ex:
                    self.ui.proseOutput.setText('')
                    QMessageBox.information(self, 'Didn\'t parse correctly', 'Math library did not parse correctly:\n{0}'.format(ex), QMessageBox.Ok)
            else:
                self.ui.proseOutput.setText('')
        else:
            self.ui.proseOutput.setText('')
    
    def _updateLibraryName(self, editor, name):
        i = self.ui.libraryTabs.indexOf(editor)
        self.ui.libraryTabs.setTabText(i, name)