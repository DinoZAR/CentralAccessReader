'''
Created on Jun 4, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QDialog, QWidget

from src.forms.search_settings_ui import Ui_SearchSettings

class SearchSettings(QDialog):
    '''
    classdocs
    '''
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.ui = Ui_SearchSettings()
        self.ui.setupUi(self)
        self.connect_signals()
        
    def connect_signals(self):
        
        self.ui.okButton.clicked.connect(self.close)