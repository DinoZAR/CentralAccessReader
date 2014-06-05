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
from src import languages

class MathLibraryEditor(QWidget):
    '''
    Editor widget that edits a math library.
    '''
    
    nameChanged = pyqtSignal(object, unicode)
    authorChanged = pyqtSignal(object, unicode)
    languageChanged = pyqtSignal(object, unicode)

    def __init__(self, library=None, parent=None):
        super(MathLibraryEditor, self).__init__(parent)
        
        self.ui = Ui_MathLibraryEditor()
        self.ui.setupUi(self)
        self.connect_signals()

        if library is None:
            self.library = MathLibrary()
        else:
            self.library = library
        self.name = self.library.name
        self.author = self.library.author
        
        # Create the model for the tree and set it
        self._treeModel = GeneralTree(self.library)
        self._treeModel.addChildrenRule(0, lambda x: x.patterns)
        self._treeModel.addDisplayRule(1, lambda x: x.name)
        self.ui.treeView.setModel(self._treeModel)

        # Set the content for the language combo box
        self.ui.languageCombo.blockSignals(True)
        for item in sorted(languages.CODES.items(), key=lambda x: x[1]):
            self.ui.languageCombo.addItem(item[1], item[0])
        self.ui.languageCombo.blockSignals(False)
        self.language = self.library.languageCode

        # Add context menu to the tree
        self.ui.treeView.contextMenuEvent = self._treeContextMenuEvent

        # Clear out the tabs and set the pattern widget map
        self.ui.patternTabs.clear()
        self._patternWidgetMap = {}

        # Set the splitter so that more of the patterns show rather than tree
        self.ui.splitter.setSizes([500, 1000])
        
    def connect_signals(self):
        self.ui.patternTabs.tabCloseRequested.connect(self.closePattern)
        self.ui.nameEdit.editingFinished.connect(self._updateName)
        self.ui.authorEdit.editingFinished.connect(self._updateAuthor)
        self.ui.treeView.clicked.connect(self._showPattern)
        self.ui.languageCombo.currentIndexChanged.connect(self._updateLanguage)

        self.nameChanged.connect(self._setTextForName)
        self.authorChanged.connect(self._setTextForAuthor)
        self.languageChanged.connect(self._setLanguageInCombo)
    
    def save(self):
        '''
        Saves the library to file. If it hadn't saved it before, it will ask the
        user where to save it.
        '''
        if len(self.library.filePath) == 0:
            self.saveAs()
        else:
            self.library.write(self.library.filePath)
            
    def export(self):
        '''
        Saves the library to file. It asks the user where they want to save
        the library.
        '''
        myPath = unicode(QFileDialog.getSaveFileName(self, 'Export Math Library',
                                                     os.path.expanduser('~/Desktop'),
                                                     'Library (*.mathlib)'))
        if len(myPath) > 0:
            self.library.filePath = myPath
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

        self._patternWidgetMap[newPattern] = patternEditor
        
        self.ui.patternTabs.addTab(patternEditor, patternEditor.name)
        self.ui.patternTabs.setCurrentWidget(patternEditor)
    
    def openPattern(self):
        '''
        Appends patterns to the library from files.
        '''
        patternPaths = QFileDialog.getOpenFileNames(self, 'Open Patterns',
                                                    os.path.expanduser('~/Desktop'),
                                                    'All files (*.*)')
        if len(patternPaths) > 0:
            for patternPath in patternPaths:
                myPath = unicode(patternPath)
                name = os.path.splitext(os.path.basename(myPath))[0]
                with open(myPath, 'r') as f:
                    data = f.read()
                newPattern = MathPattern(name, data)

                self.library.patterns.append(newPattern)
                self._treeModel.update()

                patternEditor = MathPatternEditor(newPattern)
                patternEditor.nameChanged.connect(self._patternNameChanged)

                self._patternWidgetMap[newPattern] = patternEditor

                self.ui.patternTabs.addTab(patternEditor, patternEditor.name)
                self.ui.patternTabs.setCurrentWidget(patternEditor)

    def closePattern(self, tabIndex):
        '''
        Closes the pattern at the tab index
        '''
        pattern = self.ui.patternTabs.widget(tabIndex).pattern
        del self._patternWidgetMap[pattern]
        self.ui.patternTabs.removeTab(tabIndex)

    def removeSelectedPattern(self):
        selected = self.ui.treeView.selectedIndexes()

        for s in selected:
            pattern = s.internalPointer().data

            if pattern in self._patternWidgetMap:
                i = self.ui.patternTabs.indexOf(self._patternWidgetMap[pattern])
                self.ui.patternTabs.removeTab(i)
                del self._patternWidgetMap[pattern]

            self.library.patterns.remove(pattern)
            self._treeModel.update()

    def currentPattern(self):
        editor = self.ui.patternTabs.currentWidget()
        if editor is not None:
            return editor.pattern
        else:
            return None
    
    @property
    def name(self):
        return self.library.name
    
    @name.setter
    def name(self, n):
        if len(n) > 0:
            self.library.name = n
        
        self.nameChanged.emit(self, self.library.name)

    @property
    def author(self):
        return self.library.author

    @author.setter
    def author(self, a):
        if len(a) > 0:
            self.library.author = a
        self.authorChanged.emit(self, self.library.author)

    @property
    def language(self):
        return self.library.languageCode

    @language.setter
    def language(self, lan):
        if len(lan) > 0:
            self.library.languageCode = unicode(lan)
        self.languageChanged.emit(self, self.library.languageCode)
    
    def _patternNameChanged(self, editor, newName):
        i = self.ui.patternTabs.indexOf(editor)
        self.ui.patternTabs.setTabText(i, newName)
    
    def _updateName(self):
        self.name = unicode(self.ui.nameEdit.text())
        
    def _setTextForName(self, editor, newName):
        self.ui.nameEdit.setText(newName)

    def _updateAuthor(self):
        self.author = unicode(self.ui.authorEdit.text())

    def _setTextForAuthor(self, editor, newAuthor):
        self.ui.authorEdit.setText(newAuthor)

    def _updateLanguage(self, index):
        self.language = unicode(self.ui.languageCombo.itemData(index).toString())

    def _setLanguageInCombo(self, editor, language):
        i = self.ui.languageCombo.findData(language)
        self.ui.languageCombo.setCurrentIndex(i)

    def _treeContextMenuEvent(self, ev):
        menu = QMenu()
        menu.addAction('Remove', self.removeSelectedPattern)
        menu.exec_(ev.globalPos())

    def _showPattern(self, modelIndex):
        '''
        Shows a pattern from the tree view using the model index.
        '''
        pattern = modelIndex.internalPointer().data

        if not pattern in self._patternWidgetMap:
            patternEditor = MathPatternEditor(pattern)
            patternEditor.nameChanged.connect(self._patternNameChanged)

            self._patternWidgetMap[pattern] = patternEditor

            self.ui.patternTabs.addTab(patternEditor, patternEditor.name)
            self.ui.patternTabs.setCurrentWidget(patternEditor)
        else:
            w = self._patternWidgetMap[pattern]
            self.ui.patternTabs.setCurrentWidget(w)