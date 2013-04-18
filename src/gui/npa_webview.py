'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
from PyQt4.QtWebKit import QWebView
from PyQt4.QtCore import Qt

class NPAWebView(QWebView):
    '''
    This subclass is meant to override some of the mouse behavior, most notably the zoom feature.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QWebView.__init__(self, parent)
        
        self.isControlPressed = False
        self.myZoomFactor = 1.0
        
    def wheelEvent(self, event):
        if self.isControlPressed:
            # Zoom the window
            if event.delta() > 0:
                self.myZoomFactor -= 0.1
                if self.myZoomFactor < 0.2:
                    self.myZoomFactor = 0.2
                self.setZoomFactor(self.myZoomFactor)
                self.update()
            else:
                self.myZoomFactor += 0.1
                if self.myZoomFactor > 20.0:
                    self.myZoomFactor = 20.0
                self.setZoomFactor(self.myZoomFactor)
                self.update()
        else:
            # Otherwise, just scroll it
            self.page().mainFrame().scroll(0, -event.delta())
        
        event.ignore()
        
    def keyPressEvent(self, event):
        #super(NPAWebView, self).keyPressEvent(event)
        if event.key() == Qt.Key_Control:
            self.isControlPressed = True
        
        event.ignore()
        
    def keyReleaseEvent(self, event):
        #super(NPAWebView, self).keyReleaseEvent(event)
        if event.key() == Qt.Key_Control:
            self.isControlPressed = False
            
        event.ignore()
        
        