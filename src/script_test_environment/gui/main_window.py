'''
Created on Apr 1, 2013

@author: GraffeS
'''
import os

from PyQt4 import QtGui
from PyQt4.QtCore import QUrl

from src.script_test_environment.forms.mainwindow_ui import Ui_MainWindow
from src.script_test_environment.script_editor import ScriptEditor

from src import docx

class MainWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Clear all of the tabs on the widget
        while self.ui.javascriptTabs.count() > 0:
            self.ui.javascriptTabs.removeTab(0)
            
        # Document filename
        self.docxFile = ''
            
        # Create one new one
        newTab = ScriptEditor()
        self.ui.javascriptTabs.addTab(newTab, 'untitled')
        
        # Connect all of my signals
        self.ui.actionNew_Script.triggered.connect(self.newScript)
        self.ui.actionOpen_Docx.triggered.connect(self.openDocx)
        self.ui.actionOpen_Javascript.triggered.connect(self.openScript)
        self.ui.actionSave_Current.triggered.connect(self.saveCurrentScript)
        self.ui.actionSave_All.triggered.connect(self.saveAllScripts)
        
        self.ui.javascriptTabs.tabCloseRequested.connect(self.onTabClose)
        
        self.ui.resetButton.clicked.connect(self.resetDocx)
        
        self.ui.runButton.clicked.connect(self.runScript)
    
    def newScript(self):
        print 'Adding new script...'
        newTab = ScriptEditor()
        self.ui.javascriptTabs.addTab(newTab, newTab.label)
        
    def openDocx(self):
        print 'Opening document...'
        
        newFile = QtGui.QFileDialog.getOpenFileName()
        if len(newFile) > 0:
            self.docxFile = str(newFile)
            url = os.path.join(os.getcwd(), '../import')
            baseUrl = QUrl.fromLocalFile(url)
            content = docx.getHtmlAndNavigation(str(self.docxFile))[0]
            self.ui.documentView.setHtml(content, baseUrl)
        
        print 'Done!'
        
    def openScript(self):
        print 'Opening script...'
        
        newFile = QtGui.QFileDialog.getOpenFileName()
        
        if len(newFile) > 0:
            newTab = ScriptEditor(filename=str(newFile))
            self.ui.javascriptTabs.addTab(newTab, newTab.label)
            self.ui.javascriptTabs.setCurrentIndex(self.ui.javascriptTabs.count() - 1)

    def saveScript(self, index):
        # Check to see if it is modified. If not, don't do anything
        current = self.ui.javascriptTabs.widget(index)
        
        if current.modified:
            if len(current.filename) > 0:
                f = open(current.filename, 'w')
                f.write(current.editor.text())
                f.close()
                
                current.modified = False
                
                return True
            else:
                newFile = QtGui.QFileDialog.getSaveFileName()
        
                if len(newFile) > 0:
                    f.open(newFile, 'w')
                    f.write(current.editor.text())
                    f.close()
                    
                    current.filename = newFile
                    current.modified = False
                    
                    return True
                else:
                    return False
            
    def saveCurrentScript(self):
        print 'Saving current script...'
        index = self.ui.javascriptTabs.currentIndex()
        self.saveScript(index)
        
    def saveAllScripts(self):
        print 'Saving all scripts...'
        for i in range(self.ui.javascriptTabs.count()):
            self.saveScript(i)
        
    def onTabClose(self, index):
        print 'Tab closing:', index
        
        if self.ui.javascriptTabs.widget(index).modified:
            quit_msg = "Do you want to save?"
            reply = QtGui.QMessageBox.question(self, 'Save Script?', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                saved = self.saveScript(index)
                if saved:
                    self.ui.javascriptTabs.removeTab(index)
            else:
                self.ui.javascriptTabs.removeTab(index)
        else:
            self.ui.javascriptTabs.removeTab(index)
            
    def resetDocx(self, e):
        print 'Resetting document...'
        if len(self.docxFile) > 0:
            content = docx.getHtmlAndNavigation(str(self.docxFile))[0]
            baseUrl = QUrl.fromLocalFile(os.path.join(os.getcwd(), '../import'))
            self.ui.documentView.setHtml(content, baseUrl)
            
    def runScript(self):
        print 'Running:', str(self.ui.commandLine.text())
        self.ui.documentView.page().mainFrame().evaluateJavaScript(self.ui.commandLine.text())
            
    def quit(self):
        self.close()
                