'''
Created on May 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtGui import QMainWindow, QFileDialog, QApplication

from forms.math_library_dev_ui import Ui_MathLibraryDev
from gui.math_library_editor import MathLibraryEditor

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
        self.ui.actionFrom_Clipboard.triggered.connect(self.importMathFromClipboard)
        self.ui.actionNew_Library.triggered.connect(self.newMathLibrary)
    
    def importMathFromClipboard(self):
        '''
        Pastes the MathML from the clipboard into the MathML editor, if any
        '''
        mime = QApplication.clipboard().mimeData()
        
        # Get the text from the clipboard
        if mime.hasHtml():
            self.ui.mathmlEditor.setMath(unicode(mime.html()))
            
        elif mime.hasText():
            self.ui.mathmlEditor.setMath(unicode(QApplication.clipboard().text()))
    
    def newMathLibrary(self):
        '''
        Appends a new math library to the editor.
        '''
        w = MathLibraryEditor()
        self.ui.libraryTabs.addTab(w, w.tabTitle())