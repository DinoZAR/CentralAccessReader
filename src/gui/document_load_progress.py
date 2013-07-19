'''
Created on Jul 19, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignal
from src.forms.document_load_progress_ui import Ui_DocumentLoadProgressDialog

class DocumentLoadProgressDialog(QDialog):
    '''
    This is a custom-made progress bar that looks better and I can control when
    it closes, not the other way around.
    '''
    canceled = pyqtSignal()

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_DocumentLoadProgressDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self._cancel)
    
    def setLabelText(self, newText):
        self.ui.label.setText(newText)
        
    def setProgress(self, percent):
        self.ui.progressBar.setValue(percent)
        
    def _cancel(self):
        '''
        Reports to everyone that the operation was canceled and closes itself.
        '''
        self.canceled.emit()