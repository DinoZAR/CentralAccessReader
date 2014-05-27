'''
Created on May 21, 2014

@author: Spencer Graffe
'''
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QFont

from src.forms.math_pattern_editor_ui import Ui_MathPatternEditor

class MathPatternEditor(QWidget):
    '''
    Edits a math pattern. This widget is meant to be inside of a
    MathLibraryEditor.
    '''
    
    nameChanged = pyqtSignal(object, unicode)

    def __init__(self, patternData, parent=None):
        super(MathPatternEditor, self).__init__(parent)
        
        self.ui = Ui_MathPatternEditor()
        self.ui.setupUi(self)
        
        self.connect_signals()
        
        # Set the font to monospace
        f = QFont('Monospace')
        f.setStyleHint(QFont.TypeWriter)
        self.ui.textEdit.setFont(f)
        
        self.pattern = patternData
        self.name = self.pattern.name
        self.ui.textEdit.setPlainText(self.pattern.data)

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
        if len(n) > 0:
            self.pattern.name = n
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