'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
from PyQt4.QtWebKit import QWebView, QWebPage
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication

class NPAWebView(QWebView):
    '''
    This subclass is meant to override some of the mouse behavior, most notably the zoom feature.
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QWebView.__init__(self, parent)
        
        self.myZoomFactor = 1.0
        
    def wheelEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if modifiers and Qt.ControlModifier:
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
        
        # Ctrl+A should do Select All
        print 'Control pressed', QApplication.keyboardModifiers() and Qt.ControlModifier
        if (event.modifiers() and Qt.ControlModifier) and (event.key == Qt.Key_A):
            print 'Ctrl A-ing !'
            self.pageAction(QWebPage.MoveToStartOfDocument)
            self.pageAction(QWebPage.SelectEndOfDocument)
            
        event.ignore()
        
    def keyReleaseEvent(self, event):
            
        event.ignore()
        
        