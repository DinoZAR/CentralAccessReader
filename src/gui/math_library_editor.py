'''
Created on May 20, 2014

@author: Spencer Graffe
'''
import os

from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QFileDialog, QMenu

from src.forms.math_library_editor_ui import Ui_MathLibraryEditor
from src.gui.math_pattern_editor import MathPatternEditor
from src.gui.general_tree import GeneralTree
from src.math_library.library import MathLibrary, MathPattern

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
        
        # Create the model for the tree and set it
        self._treeModel = GeneralTree(self.library)
        self._treeModel.addChildrenRule(0, lambda x: x.patterns)
        self._treeModel.addDisplayRule(1, lambda x: x.name)
        self.ui.treeView.setModel(self._treeModel)

        # Add context menu to the tree (like removal)
        self.ui.treeView.contextMenuEvent = self._treeContextMenuEvent

        # Clear out the tabs
        self.ui.patternTabs.clear()

        # Set the splitter so that more of the patterns show rather than tree
        self.ui.splitter.setSizes([500, 1000])
        
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
        newPattern = MathPattern()
        self.library.patterns.append(newPattern)
        self._treeModel.update()
        
        patternEditor = MathPatternEditor(newPattern)
        patternEditor.nameChanged.connect(self._patternNameChanged)
        
        self.ui.patternTabs.addTab(patternEditor, patternEditor.name)
    
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

    def removeSelectedPattern(self):
        selected = self.ui.treeView.selectedIndexes()

        for s in selected:
            pattern = s.internalPointer().data
            print 'Selected:', pattern

    
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

    def _treeContextMenuEvent(self, ev):
        print 'Context menu!', ev
        menu = QMenu()
        menu.addAction('Remove', self.removeSelectedPattern)
        menu.exec_(ev.globalPos())
