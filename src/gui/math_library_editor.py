'''
Created on May 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtGui import QWidget

from forms.math_library_editor_ui import Ui_MathLibraryEditor

class MathLibraryEditor(QWidget):
    '''
    Editor widget that edits a math library.
    '''

    def __init__(self, parent=None):
        super(MathLibraryEditor, self).__init__(parent)
        
        self.ui = Ui_MathLibraryEditor()
        self.ui.setupUi(self)
        
        self.connect_signals()
        
    def connect_signals(self):
        pass
    
    def tabTitle(self):
        '''
        Returns the title that a tab widget should use for this tab.
        '''
        return 'Untitled'