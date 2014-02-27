'''
Created on Feb 20, 2014

@author: Spencer Graffe
'''
import os

from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog

try:
    from mathml_fast.tts import MathTTS
except ImportError:
    print 'Importing slower version of MathTTS...'
    from mathml.tts import MathTTS

from forms.math_dev_env_ui import Ui_MathDevEnv
from gui.pattern_editor import PatternEditor
import misc

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
        
        # Set the initial pattern database as nothing
        self.mathTTS = MathTTS()
        
        self.connect_signals()
        
    def connect_signals(self):
        
        # Random widgets
        self.ui.runButton.clicked.connect(self.runMathParser)
        self.ui.patternTabs.tabCloseRequested.connect(self.closePatternAtIndex)
        
        # File Menu
        self.ui.actionNew_Pattern.triggered.connect(self.newPattern)
        self.ui.actionOpen_Pattern.triggered.connect(self.openPattern)
        self.ui.actionPaste_MathML.triggered.connect(self.pasteMathML)
        self.ui.actionSave_Pattern.triggered.connect(self.savePattern)
        self.ui.actionSave_As.triggered.connect(self.saveAsPattern)
        self.ui.actionClose_Pattern.triggered.connect(self.closePattern)
        
    def runMathParser(self):
        '''
        Runs the current pattern in the tab, displaying output when it finishes.
        '''
        print 'Math parser running!'
        
        # Check if it has a file associated with it. If it doesn't, then it
        # needs to write off to temp
        curr = self.currentPatternEditor()
        if curr is not None:
            
            if len(curr.filePath) > 0:
                self.mathTTS.setPatternDatabase(curr.filePath)
            else:
                temp = misc.temp_path('tmp.txt')
                with open(temp, 'w') as f:
                    f.write(unicode(curr.toPlainText()))
                self.mathTTS.setPatternDatabase(temp)
                
            # Run the math parser
            mathOutput = self.mathTTS.parse(self.ui.mathmlEditor.getMath())
            
            # Set the output controls to their new values
            self.ui.mathProseOutput.setText(mathOutput)
    
    def currentPatternEditor(self):
        '''
        Returns the current pattern editor.
        '''
        if self.ui.patternTabs.count() > 0:
            return self.ui.patternTabs.currentWidget()
        else:
            return None
        
    def newPattern(self):
        '''
        Adds a blank pattern as a tab.
        '''
        print 'Adding blank pattern!'
        newPattern = PatternEditor()
        self.ui.patternTabs.addTab(newPattern, 'Untitled')
        self.ui.patternTabs.setCurrentWidget(newPattern)
        
    def openPattern(self):
        '''
        Calls up a file chooser to open a pattern database. It will default to
        the math database folder for convenience.
        '''
        print 'Opening a math pattern!'
        filePath = unicode(QFileDialog.getOpenFileName(self, 'Open pattern database...', misc.program_path('src/math_patterns'),'(*.txt)'))
        if len(filePath) > 0:
            newPattern = PatternEditor()
            newPattern.setFile(filePath)
            self.ui.patternTabs.addTab(newPattern, os.path.splitext(os.path.basename(filePath))[0])
            self.ui.patternTabs.setCurrentWidget(newPattern)
    
    def savePattern(self):
        '''
        Saves the current pattern.
        '''
        print 'Save pattern!'
        curr = self.currentPatternEditor()
        
        if len(curr.filePath) > 0:
            with open(curr.filePath, 'w') as f:
                f.write(curr.getContent())
        
        else:
            self.saveAsPattern()
    
    def saveAsPattern(self):
        '''
        Saves the current pattern in a different place.
        '''
        print 'Save As!'
        curr = self.currentPatternEditor()
        
        newPath = unicode(QFileDialog.getSaveFileName(self, 'Save pattern database...', misc.program_path('src/math_patterns'), '(*.txt)'))
        if len(newPath) > 0:
            curr.filePath = newPath
            with open(curr.filePath, 'w') as f:
                f.write(curr.getContent())
            self.ui.patternTabs.setTabText(self.ui.patternTabs.currentIndex(), os.path.splitext(os.path.basename(newPath))[0])
    
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