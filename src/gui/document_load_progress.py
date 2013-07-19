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
        
    def disableCancel(self):
        '''
        Disables the cancel button. It's useful when you are at a part that is
        either dangerous, bad, or impossible to exit from.
        '''
        self.ui.cancelButton.setEnabled(False)
        
    def enableCancel(self):
        '''
        Enables the cancel button. If you disabled it before and now want it
        enabled, use this function.
        '''
        self.ui.cancelButton.setEnabled(True)
        
    def _cancel(self):
        '''
        Reports to everyone that the operation was canceled and closes itself.
        '''
        self.canceled.emit()