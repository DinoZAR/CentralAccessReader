'''
Created on Apr 1, 2013

@author: GraffeS
'''
import os

from PyQt4.QtGui import QWidget, QVBoxLayout
from PyQt4.Qsci import QsciScintilla, QsciLexerJavaScript

class ScriptEditor(QWidget):
    '''
    classdocs
    '''


    def __init__(self, filename='', parent=None):
        '''
        Constructor
        '''
        QWidget.__init__(self, parent)
        
        self.filename = filename
        self.label = 'untitled'
        self.modified = False
        
        self.layout = QVBoxLayout(self)
        self.editor = QsciScintilla()
        self.layout.addWidget(self.editor, stretch=1)
        
        # Give the editor its content
        if len(filename) > 0:
            # Open the file and read in its contents
            f = open(filename, 'r')
            contents = f.read()
            self.editor.setText(contents)
            f.close()
            
            self.label = os.path.basename(filename)
        
        # Setup the features of the editor
        lexer = QsciLexerJavaScript()
        self.editor.setLexer(lexer)
        
        # Connect signals
        self.editor.textChanged.connect(self.onTextChanged)
        
    def hasFile(self):
        return len(self.filename) > 0
    
    def onTextChanged(self):
        self.modified = True