'''
Created on Sep 16, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignal
from forms.save_mp3_pages_dialog_ui import Ui_SaveMP3ByPageDialog

class SaveMP3PagesDialog(QDialog):
    '''
    classdocs
    '''
    canceled = pyqtSignal()

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        
        self.ui = Ui_SaveMP3ByPageDialog()
        self.ui.setupUi(self)
        
        self.ui.cancelButton.clicked.connect(self.canceled)
    
    def setStatusLabel(self, labelText):
        self.ui.statusLabel.setText(labelText)
    
    def setStatusProgress(self, progress):
        self.ui.statusProgressBar.setValue(progress)
    
    def setPageLabel(self, labelText):
        self.ui.pageLabel.setText(labelText)
    
    def setPageProgress(self, progress):
        self.ui.pageProgressBar.setValue(progress)
        
    def closeEvent(self, event):
        self.canceled.emit()