'''
Created on Jun 21, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QDialog, QWidget, QMovie
from PyQt4.QtCore import QByteArray, Qt

from src.forms.update_in_progress_ui import Ui_UpdateInstallProgressDialog
from src.forms import resource_rc

class UpdateInstallProgressDialog(QDialog):
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.ui = Ui_UpdateInstallProgressDialog()
        self.ui.setupUi(self)
        
        # Swap out the label with the gif to a movie that will actually display
        # it correctly.
        self.window = self.ui.updateIconLabel
        self.movie = QMovie(':/icons/icons/update-in-progress.gif', QByteArray(), self)
        
        # Run the GIF
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.window.setMovie(self.movie)
        self.movie.start()