'''
Created on May 20, 2013

@author: GraffeS
'''
from PyQt4 import QtGui
import webbrowser

from src.forms.bug_report_ui import Ui_BugReporter
from src import misc

class BugReporter(QtGui.QDialog):
    '''
    classdocs
    '''
    def __init__(self, bugReportText, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_BugReporter()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.ui.bugReportTextBox.setText(bugReportText)
    
    def connect_signals(self):
        self.ui.copyReportButton.clicked.connect(self.copyReportButton_clicked)
        self.ui.letUsKnowButton.clicked.connect(self.letUsKnowButton_clicked)
        self.ui.noThanksButton.clicked.connect(self.noThanksButton_clicked)
    
    def copyReportButton_clicked(self):
        # Copy report to clipboard
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(self.ui.bugReportTextBox.toPlainText())
    
    def letUsKnowButton_clicked(self):
        webbrowser.open(misc.REPORT_BUG_URL)
    
    def noThanksButton_clicked(self):
        self.done(0)