'''
Created on May 20, 2014

@author: Spencer Graffe
'''
import os

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QFileDialog

from forms.math_library_editor_ui import Ui_MathLibraryEditor
from gui.math_pattern_editor import MathPatternEditor
from math_library.library import MathLibrary

class MathLibraryEditor(QWidget):
    '''
    Editor widget that edits a math library.
    '''
    
    BAD_NAME_CHARACTERS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '\t', '^']
    
    nameChanged = pyqtSignal(object, unicode)

    def __init__(self, parent=None):
        super(MathLibraryEditor, self).__init__(parent)
        
        self.ui = Ui_MathLibraryEditor()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.library = MathLibrary()
        
        # Clear out the tabs
        self.ui.patternTabs.clear()
        
        # The file path of the last saved path
        self.filePath = ''
        
    def connect_signals(self):
        self.ui.patternTabs.tabCloseRequested.connect(self.closePattern)
        self.ui.nameEdit.editingFinished.connect(self._updateName)
        self.nameChanged.connect(self._setTextForName)
    
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
            
    def newPattern(self):
        '''
        Appends a new pattern to the library.
        '''
        pattern = MathPatternEditor()
        pattern.nameChanged.connect(self._patternNameChanged)
        self.ui.patternTabs.addTab(pattern, pattern.name)
    
    def openPattern(self):
        '''
        Appends a new pattern to the library from file.
        '''
        pass
    
    def closePattern(self, tabIndex):
        '''
        Closes the pattern at the tab index
        '''
        self.ui.patternTabs.removeTab(tabIndex)
    
    @property
    def name(self):
        return self.library.name
    
    @name.setter
    def name(self, n):
        # Clean all of the junk in it
        myName = n
        for bad in self.BAD_NAME_CHARACTERS:
            myName = myName.replace(bad, '')
        
        # Truncate it if greater than 255 characters
        if len(myName) > 255:
            myName = myName[:254]
        
        # Check to see if I have anything left. If I don't, then don't change
        # the name
        if len(myName) > 0:
            self.library.name = myName
        
        self.nameChanged.emit(self, self.library.name)
    
    def _patternNameChanged(self, editor, newName):
        i = self.ui.patternTabs.indexOf(editor)
        self.ui.patternTabs.setTabText(i, newName)
    
    def _updateName(self):
        self.name = unicode(self.ui.nameEdit.text())
        
    def _setTextForName(self, editor, newName):
        self.ui.nameEdit.setText(newName)