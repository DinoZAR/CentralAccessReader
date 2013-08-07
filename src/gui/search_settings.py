'''
Created on Jun 4, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QDialog, QWidget

from forms.search_settings_ui import Ui_SearchSettings

class SearchSettings(QDialog):
    '''
    classdocs
    '''
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.ui = Ui_SearchSettings()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.mainConfig = None
        
    def connect_signals(self):
        self.ui.wholeWordCheckBox.toggled.connect(self.setWholeWord)
        self.ui.matchCaseCheckBox.toggled.connect(self.setMatchCase)
        self.ui.okButton.clicked.connect(self.close)
        
    def setConfig(self, config):
        self.mainConfig = config
        
        # Set the checkboxes
        self.ui.wholeWordCheckBox.blockSignals(True)
        self.ui.wholeWordCheckBox.setChecked(self.mainConfig.search_whole_word)
        self.ui.wholeWordCheckBox.blockSignals(False)
        
        self.ui.matchCaseCheckBox.blockSignals(True)
        self.ui.matchCaseCheckBox.setChecked(self.mainConfig.search_match_case)
        self.ui.matchCaseCheckBox.blockSignals(False)
    
    def setWholeWord(self, isWholeWord):
        print 'isWholeWord:', isWholeWord
        self.mainConfig.search_whole_word = isWholeWord
    
    def setMatchCase(self, isMatchCase):
        print 'isMatchCase:', isMatchCase
        self.mainConfig.search_match_case = isMatchCase
        