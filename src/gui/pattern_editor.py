'''
Created on Feb 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtGui import QWidget, QFont

from forms.pattern_editor_ui import Ui_PatternEditor

class PatternEditor(QWidget):
    '''
    Very basic editor for a pattern database. It holds the GUI (just a
    QPlainTextEdit) and properties about where the pattern file was at.
    '''
    
    def __init__(self, parent=None):
        super(PatternEditor, self).__init__(parent)
        
        self.ui = Ui_PatternEditor()
        self.ui.setupUi(self)
        
        # Set the font to monospace
        f = QFont('Monospace');
        f.setStyleHint(QFont.TypeWriter)
        self.ui.textEditor.setFont(f)
        
        self.filePath = ''
        
    def setFile(self, filePath):
        self.filePath = filePath
        
        with open(filePath, 'r') as f:
            self.ui.textEditor.setPlainText(f.read())
            
    def getContent(self):
        return unicode(self.ui.textEditor.toPlainText())