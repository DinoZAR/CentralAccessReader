'''
Created on May 6, 2013

@author: GraffeS
'''
from PyQt4.QtGui import QDialog

from car.forms.about_ui import Ui_AboutDialog
from car.misc import program_path

class AboutDialog(QDialog):
    '''
    Shows the about information for the program.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        
        versionFile = open(program_path('version.txt'), 'r')
        self.ui.versionLabel.setText(versionFile.read())
        versionFile.close()