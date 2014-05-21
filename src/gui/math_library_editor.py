'''
Created on May 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtGui import QWidget

from forms.math_library_editor_ui import Ui_MathLibraryEditor
from math_library.library import MathLibrary

class MathLibraryEditor(QWidget):
    '''
    Editor widget that edits a math library.
    '''

    def __init__(self, parent=None):
        super(MathLibraryEditor, self).__init__(parent)
        
        self.ui = Ui_MathLibraryEditor()
        self.ui.setupUi(self)
        
        self.library = MathLibrary()
        
        self.connect_signals()
        
    def connect_signals(self):
        pass
    
    def tabTitle(self):
        '''
        Returns the title that a tab widget should use for this tab.
        '''
        return self.library.title
    
    def save(self):
        '''
        Saves the library to file. If it hadn't saved it before, it will ask the
        user where to save it.
        '''
        pass