'''
Created on Jul 2, 2013

@author: Spencer Graffe
'''
from PySide.QtGui import QWidget
from forms.prepare_speech_progress_ui import Ui_PrepareSpeechProgressWidget
import misc

class PrepareSpeechProgressWidget(QWidget):
    '''
    This widget floats on the main window pointing to the play button, giving
    an indication that something is happening.
    '''

    def __init__(self, widgetToShowUnder, parent=None):
        QWidget.__init__(self, parent)
        
        self._otherWidget = widgetToShowUnder
        self._otherWidget.moveEvent = self.otherWidgetMoveEvent
        
        self.ui = Ui_PrepareSpeechProgressWidget()
        self.ui.setupUi(self)
        
        self._offsetX = -8
        self._offsetY = 55
        
    def otherWidgetMoveEvent(self, event):
        newPosition = self._otherWidget.mapTo(self._otherWidget.window(), event.pos())
        self.move(newPosition.x() + 6, newPosition.y() + self._offsetY)
        
    def updatePos_splitterMoved(self, x, y):
        newPosition = self._otherWidget.mapTo(self._otherWidget.window(), self._otherWidget.pos())
        self.move(newPosition.x() + self._offsetX, newPosition.y() + self._offsetY)
        
    def updatePos(self):
        newPosition = self._otherWidget.mapTo(self._otherWidget.window(), self._otherWidget.pos())
        self.move(newPosition.x() + self._offsetX, newPosition.y() + self._offsetY)
        
    def setProgress(self, percent):
        self.ui.progressBar.setValue(percent)
        
    