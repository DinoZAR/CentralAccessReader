'''
Created on Feb 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtGui import QMainWindow

from forms.math_dev_env_ui import Ui_MathDevEnv
from gui import configuration

class MathDevelopmentEnvironment(QMainWindow):
    '''
    Window used to develop the math patterns used in the math-to-prose engine.
    '''

    def __init__(self, parent=None):
        super(MathDevelopmentEnvironment, self).__init__(parent)
        
        self.ui = Ui_MathDevEnv()
        self.ui.setupUi(self)