'''
Created on Jun 25, 2013

@author: GraffeS
'''
from PyQt4.QtGui import QDialog, QWidget, QMessageBox
from src.forms.update_prompt_ui import Ui_UpdatePromptDialog

class UpdatePromptDialog(QDialog):


    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.ui = Ui_UpdatePromptDialog()
        self.ui.setupUi(self)
        
        self.connect_signals()
        
    def connect_signals(self):
        self.ui.yesButton.clicked.connect(self.yesButtonClicked)
        self.ui.noButton.clicked.connect(self.noButtonClicked)
        
    def yesButtonClicked(self):
        self.done(QMessageBox.Yes)
    
    def noButtonClicked(self):
        self.done(QMessageBox.No)
        