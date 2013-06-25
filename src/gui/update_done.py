'''
Created on Jun 24, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QDialog, QWidget
from src.forms.update_done_ui import Ui_UpdateDoneDialog

class UpdateDoneDialog(QDialog):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.ui = Ui_UpdateDoneDialog()
        self.ui.setupUi(self)
        
        self.ui.okButton.clicked.connect(self.onBeingDone)
        
    def onBeingDone(self):
        self.done(0)