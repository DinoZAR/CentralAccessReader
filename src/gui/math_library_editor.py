'''
Created on May 20, 2014

@author: Spencer Graffe
'''
import os

from PyQt4.QtGui import QWidget, QFileDialog

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
        self.updatePatternTabs()
        
        # The file path of the last saved path
        self.filePath = ''
        
        self.connect_signals()
        
    def connect_signals(self):
        self.ui.patternTabs.tabCloseRequested.connect(self.closePattern)
    
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
        if len(self.filePath) == 0:
            self.saveAs()
        else:
            self.library.write(self.filePath)
            
    def saveAs(self):
        '''
        Saves the library to file. It asks the user where they want to save
        the library.
        '''
        myPath = unicode(QFileDialog.getSaveFileName(self, 'Save Math Library',
                                                     os.path.expanduser('~/Desktop'),
                                                     'Library (*.mathlib)'))
        
        if len(myPath) > 0:
            self.filePath = myPath
            self.save()
    
    def updatePatternTabs(self):
        '''
        Updates the tabs for the patterns.
        '''
        pass
    
    def closePattern(self, tabIndex):
        '''
        Closes the pattern at the tab index
        '''
        self.ui.patternsTab.removeTab(tabIndex)
        
        