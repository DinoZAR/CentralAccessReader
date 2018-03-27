'''
Created on Feb 20, 2013

@author: Spencer Graffe
'''
import traceback
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QStandardItemModel, QStandardItem, QFont
from mathml.pattern_editor.forms.patterneditorwindow_ui import Ui_PatternEditorWindow
from mathml.tts import MathTTS

class PatternEditorWindow(QtGui.QMainWindow):
    
    # My custom signals
    changedPattern = QtCore.pyqtSignal(str)

    def __init__(self, databaseFile, lastMathML, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_PatternEditorWindow()
        self.ui.setupUi(self)
        
        # Make the fonts bigger
        font = QFont()
        font.setPointSize(12)
        font.setFamily('Consolas')
        font.setFixedPitch(True)
        self.ui.databaseEditor.setFont(font)
        self.ui.mathmlEditor.setFont(font)
        
        self.currentFile = databaseFile.strip()
        
        # If I actually got something, then let's load the file in
        if len(self.currentFile) > 0:
            try:
                f = open(self.currentFile, 'r')
                contents = f.read()
                f.close()
                self.ui.databaseEditor.setText(contents)
            except IOError:
                print 'Database file doesn\'t exist! Resetting to nothing...'
                self.currentFile = ''
        
        try:
            self.mathTTS = MathTTS(databaseFile)
        except Exception:
            self.mathTTS = None
        
#         self.stagesModel = QStandardItemModel()
#         self.stageTrees = []
#         self.updateStagesModel()
        
        self.ui.mathmlEditor.setText(unicode(lastMathML))
        
        self.connect_signals()
        
    def connect_signals(self):
        self.ui.speakButton.clicked.connect(self.speakButton_clicked)
#         self.ui.expandAllButton.clicked.connect(self.expandButton_clicked)
#         self.ui.collapseAllButton.clicked.connect(self.collapseButton_clicked)
        
        self.ui.actionNew.triggered.connect(self.actionNew_triggered)
        self.ui.actionOpen.triggered.connect(self.actionOpen_triggered)
        self.ui.actionOpen_MathML.triggered.connect(self.actionOpen_MathML_triggered)
        self.ui.actionSave.triggered.connect(self.actionSave_triggered)
        self.ui.actionSave_As.triggered.connect(self.actionSaveAs_triggered)
        self.ui.actionQuit.triggered.connect(self.actionQuit_triggered)
        
    def speakButton_clicked(self):
        print 'Speak button pressed!'
        self.stageTrees = []
        
        # Clear console
        self.ui.consoleTextBox.clear()
        
        try:
            stuff = self.mathTTS.parse(unicode(self.ui.mathmlEditor.text()), stageSink=self.stageTrees)
        
            # Output what the text was
            self.ui.outputText.setPlainText(stuff)
            
            self.ui.consoleTextBox.appendPlainText('Success!')
            
        except Exception as ex:
            stuff = traceback.format_exc()
            self.ui.consoleTextBox.appendPlainText('Failed...\n')
            self.ui.consoleTextBox.appendPlainText(stuff)
            
        
#     def expandButton_clicked(self):
#         self.ui.stagesTreeView.expandAll()
#     
#     def collapseButton_clicked(self):
#         self.ui.stagesTreeView.collapseAll()
#         
#     def updateStagesModel(self):
#         '''
#         Used to update the tree model for the Stages tree
#         '''
#         self.stagesModel.clear()
#         parent = self.stagesModel.invisibleRootItem();
#         
#         i = 0
#         for stage in self.stageTrees:
#             i += 1
#             stageItem = QStandardItem(stage.replaceVariable)
#             stageItem.setEditable(False)
#             
#             item = QStandardItem(self._buildTreeStringLabel(stage))
#             item.setEditable(False)
#             self._addChildrenToParent(stage, item)
#             
#             stageItem.appendRow(item)
#             parent.appendRow(stageItem)
#             
#         self.ui.stagesTreeView.setModel(self.stagesModel)
#         
#     def _addChildrenToParent(self, replaceParentNode, standardItemParent):
#         if len(replaceParentNode.expressions) > 0:
#             for e in replaceParentNode.expressions:
#                 if isinstance(e, list):
#                     listItem = QStandardItem('+')
#                     listItem.setEditable(False)
#                     for e2 in e:
#                         item = QStandardItem(self._buildTreeStringLabel(e2))
#                         item.setEditable(False)
#                         self._addChildrenToParent(e2, item)
#                         listItem.appendRow(item)
#                     standardItemParent.appendRow(listItem)
#                     
#                 else:
#                     item = QStandardItem(self._buildTreeStringLabel(e))
#                     item.setEditable(False)
#                     self._addChildrenToParent(e, item)
#                     standardItemParent.appendRow(item)
#                 
#         if len(replaceParentNode.children) > 0:
#             for c in replaceParentNode.children:
#                 item = QStandardItem(self._buildTreeStringLabel(c))
#                 item.setEditable(False)
#                 self._addChildrenToParent(c, item)
#                 standardItemParent.appendRow(item)
                
#     def _buildTreeStringLabel(self, replaceTree):
#         '''
#         Builds the label for the stages tree based on the replace tree given
#         '''
#         myString = replaceTree.value + '   (' + replaceTree._getTypeString() + ')'
#         if replaceTree.parent != None:
#             myString += '    -> Parent: '
#             myString += replaceTree.parent.value + ' (' + replaceTree.parent._getTypeString() + ')'
#         return myString
        
    def actionNew_triggered(self):
        print 'New was triggered!'
        self.ui.databaseEditor.clear()
        self.currentFile = ''
        self.changedPattern.emit(self.currentFile)
        self.mathTTS.setPatternDatabase(self.currentFile)
        
    def actionOpen_triggered(self):
        print 'Open was triggered!'
        
        newFile = QtGui.QFileDialog.getOpenFileName(self, 'Open pattern database file...')
        
        if len(newFile) > 0:
            self.currentFile = newFile
            f = open(self.currentFile, 'r')
            contents = f.read()
            f.close()
            self.ui.databaseEditor.setText(contents)
            
            self.changedPattern.emit(self.currentFile)
            self.mathTTS.setPatternDatabase(self.currentFile)
            
    def actionOpen_MathML_triggered(self):
        print 'Open MathML was triggered!'
        
        newFile = QtGui.QFileDialog.getOpenFileName(self, 'Open MathML file...')
        
        if len(newFile) > 0:
            f = open(newFile, 'r')
            contents = f.read()
            f.close()
            self.ui.mathmlEditor.setText(contents)
        
    def actionSave_triggered(self):
        print 'Save was triggered!'
        
        if len(self.currentFile) == 0:
            # Perform a Save As instead
            self.actionSaveAs_triggered()
        else:
            f = open(self.currentFile, 'w')
            f.write(unicode(self.ui.databaseEditor.text()))
            f.close()
            
            self.changedPattern.emit(self.currentFile)
            
            if self.mathTTS == None:
                try:
                    self.mathTTS = MathTTS(self.currentFile)
                except Exception:
                    pass
            else:
                self.mathTTS.setPatternDatabase(self.currentFile)
        
    def actionSaveAs_triggered(self):
        print 'Save As was triggered!'
        newFileName = QtGui.QFileDialog.getSaveFileName(self, 'Save pattern database file...')
        if len(newFileName) > 0:
            self.currentFile = newFileName
            f = open(self.currentFile, 'w')
            f.write(unicode(self.ui.databaseEditor.text()))
            f.close()
            
            self.changedPattern.emit(self.currentFile)
            self.mathTTS.setPatternDatabase(self.currentFile)
        
    def actionQuit_triggered(self):
        print 'Quit was triggered!'