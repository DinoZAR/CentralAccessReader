'''
Created on Jul 19, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignal, Qt
from forms.document_load_progress_ui import Ui_DocumentLoadProgressDialog

class DocumentLoadProgressDialog(QWidget):
    '''
    This is a custom-made progress bar that looks better and I can control when
    it closes, not the other way around.
    '''
    canceled = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.ui = Ui_DocumentLoadProgressDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self._cancel)
        
        self.setFixedSize(self.size())
        
        self._closeDisabled = False
    
    def setLabelText(self, newText):
        self.ui.label.setText(newText)
        
    def setProgress(self, percent):
        self.ui.progressBar.setValue(percent)
        
    def closeEvent(self, ev):
        if self._closeDisabled:
            ev.ignore()
        else:
            self.canceled.emit()
            ev.accept()
                
    def disableCancel(self):
        '''
        Disables the cancel button. It's useful when you are at a part that is
        either dangerous, bad, or impossible to exit from.
        '''
        self._closeDisabled = True
        self.ui.cancelButton.setEnabled(False)
        
    def enableCancel(self):
        '''
        Enables the cancel button. If you disabled it before and now want it
        enabled, use this function.
        '''
        self._closeDisabled = False
        self.ui.cancelButton.setEnabled(True)
        
    def _cancel(self):
        '''
        Reports to everyone that the operation was canceled and closes itself.
        '''
        self.canceled.emit()