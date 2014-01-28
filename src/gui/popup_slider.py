'''
Created on Dec 4, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import pyqtSignal, Qt, QPoint
from PyQt4.QtGui import QWidget
from forms.popup_slider_ui import Ui_PopupSlider

class PopupSlider(QWidget):
    '''
    This widget serves as a popup slider that shows up at a specific position.
    When the focus leaves the slider, the widget disappears.
    '''
    
    valueChanged = pyqtSignal(int)

    def __init__(self, widget, parent=None):
        '''
        Constructor
        '''
        QWidget.__init__(self, parent)
        
        self.ui = Ui_PopupSlider()
        self.ui.setupUi(self)
        
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        
        self.ui.slider.valueChanged.connect(self.valueChanged)
        
        # Calculate the position to set the widget
        pos = widget.pos()
        pos = widget.parentWidget().mapToGlobal(pos)
        
        # Move to center of widget
        pos.setX(pos.x() + (widget.size().width() / 2.0))
        
        # Set offset to have the arrow pointing at the correct place
        diff = QPoint(-197, widget.size().height())
        self.move(pos + diff)
        
    def setValue(self, val):
        self.ui.slider.setValue(val)