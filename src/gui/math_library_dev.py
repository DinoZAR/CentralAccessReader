'''
Created on May 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtGui import QMainWindow, QApplication

from src.forms.math_library_dev_ui import Ui_MathLibraryDev
from src.gui.math_library_editor import MathLibraryEditor

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
        self.ui.splitter.setSizes([1000,500])
        
        # Clear the tabs
        self.ui.libraryTabs.clear()
        
        self.connect_signals()
    
    def connect_signals(self):
        # File menu
        self.ui.actionNew_Library.triggered.connect(self.newLibrary)
        self.ui.actionSave.triggered.connect(self.saveCurrent)
        
        self.ui.actionNew_Pattern.triggered.connect(self.newPattern)
        
        # MathML menu
        self.ui.actionFrom_Clipboard.triggered.connect(self.importMathFromClipboard)
        
        # Controls
        self.ui.libraryTabs.tabCloseRequested.connect(self.closeLibrary)
        
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
    
    def _updateLibraryName(self, editor, name):
        i = self.ui.libraryTabs.indexOf(editor)
        self.ui.libraryTabs.setTabText(i, name)