'''
Created on May 21, 2014

@author: Spencer Graffe
'''
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QFont

from forms.math_pattern_editor_ui import Ui_MathPatternEditor

class MathPatternEditor(QWidget):
    '''
    Edits a math pattern. This widget is meant to be inside of a
    MathLibraryEditor.
    '''
    
    BAD_NAME_CHARACTERS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '\t', '^']
    
    nameChanged = pyqtSignal(object, unicode)

    def __init__(self, patternData, parent=None):
        super(MathPatternEditor, self).__init__(parent)
        
        self.ui = Ui_MathPatternEditor()
        self.ui.setupUi(self)
        
        self.connect_signals()
        
        # Set the font to monospace
        f = QFont('Monospace');
        f.setStyleHint(QFont.TypeWriter)
        self.ui.textEdit.setFont(f)
        
        self.pattern = patternData
        self.name = self.pattern.name

        if len(self.name) == 0:
            self.name = 'Untitled'
        
    def connect_signals(self):
        self.ui.nameEdit.editingFinished.connect(self._updateName)
        self.ui.textEdit.textChanged.connect(self._updateText)
        self.nameChanged.connect(self._setTextInName)

    @property
    def name(self):
        return self.pattern.name
    
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
            self.pattern.name = myName

        self.nameChanged.emit(self, self.pattern.name)
    
    @property
    def data(self):
        return self.pattern.data
    
    @data.setter
    def data(self, d):
        self.pattern.data = d
    
    def _updateName(self):
        self.name = unicode(self.ui.nameEdit.text())
    
    def _updateText(self):
        self.data = unicode(self.ui.textEdit.toPlainText())
        
    def _setTextInName(self, editor,  newText):
        self.ui.nameEdit.setText(newText)