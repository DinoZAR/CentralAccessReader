'''
Created on May 6, 2013

@author: GraffeS
'''
from PyQt4.QtGui import QDialog, QWidget
from src.forms.about_ui import Ui_AboutDialog

class AboutDialog(QDialog):
    '''
    Shows the about information for the program.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QWidget.__init__(self, parent)
        
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)