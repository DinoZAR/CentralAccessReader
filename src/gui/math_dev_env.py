'''
Created on Feb 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtGui import QMainWindow, QApplication

from forms.math_dev_env_ui import Ui_MathDevEnv
from gui import configuration
from gui.pattern_editor import PatternEditor

class MathDevelopmentEnvironment(QMainWindow):
    '''
    Window used to develop the math patterns used in the math-to-prose engine.
    '''

    def __init__(self, parent=None):
        super(MathDevelopmentEnvironment, self).__init__(parent)
        
        self.ui = Ui_MathDevEnv()
        self.ui.setupUi(self)
        
        # Clear all the tabs in the patterns widget
        self.ui.patternTabs.clear()
        
        self.connect_signals()
        
    def connect_signals(self):
        
        # Random widgets
        self.ui.runButton.clicked.connect(self.runMathParser)
        self.ui.patternTabs.tabCloseRequested.connect(self.closePatternAtIndex)
        
        # File Menu
        self.ui.actionNew_Pattern.triggered.connect(self.newPattern)
        self.ui.actionOpen_Pattern.triggered.connect(self.openPattern)
        self.ui.actionPaste_MathML.triggered.connect(self.pasteMathML)
        self.ui.actionClose_Pattern.triggered.connect(self.closePattern)
        
    def runMathParser(self):
        '''
        Runs the current pattern in the tab, displaying output when it finishes.
        '''
        print 'Math parser running!'
        
    def newPattern(self):
        '''
        Adds a blank pattern as a tab.
        '''
        print 'Adding blank pattern!'
        newPattern = PatternEditor()
        self.ui.patternTabs.addTab(newPattern, 'Untitled')
        
    def openPattern(self):
        '''
        Calls up a file chooser to open a pattern database. It will default to
        the math database folder for convenience.
        '''
        print 'Opening a math pattern!'
    
    def pasteMathML(self):
        '''
        Pastes the MathML from the clipboard into the MathML editor, if any
        '''
        mime = QApplication.clipboard().mimeData()
        
        # Get the text from the clipboard
        if mime.hasHtml():
            self.ui.mathmlEditor.setMath(unicode(mime.html()))
            
        elif mime.hasText():
            self.ui.mathmlEditor.setMath(unicode(QApplication.clipboard().text()))
        
    def closePatternAtIndex(self, index):
        '''
        Closes the pattern editor at the specified index.
        '''
        self.ui.patternTabs.removeTab(index)
    
    def closePattern(self):
        '''
        Closes the current pattern open.
        '''
        if self.ui.patternTabs.count() > 0:
            self.ui.patternTabs.removeTab(self.ui.patternTabs.currentIndex())