'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
from PyQt4.QtWebKit import QWebView, QWebPage
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication
import webbrowser
import os
from src import misc

class NPAWebView(QWebView):
    '''
    This subclass is meant to override some of the mouse behavior, most notably the zoom feature.
    '''

    def __init__(self, mainWindow, parent=None):
        '''
        Constructor
        '''
        QWebView.__init__(self, parent)
        self.mainWindow = mainWindow
        self.setAcceptDrops(True)
        self.myZoomFactor = 1.0
        
        self.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        
        # Disable the context menu if in a release environment
        if misc.is_release_environment():
            def nothing(s, event):
                pass
            self.contextMenuEvent = nothing
            
        self.linkClicked.connect(self.myLinkClicked)
        
    def dragEnterEvent(self, e):
        print 'I\'m bringing something into CAR!'
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()
            
    def dragMoveEvent(self, event):
        print 'Moving the drag-n-drop item!'
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, e):
        print 'Dropping the cargo!'
        if e.mimeData().hasUrls:
            e.setDropAction(Qt.CopyAction)
            e.accept()
            url = unicode(e.mimeData().urls()[0].toLocalFile())
            
            if os.path.splitext(url)[1] == '.docx':
                self.mainWindow.openDocx(url)
        
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
        
    def selectAll(self):
        self.page().triggerAction(QWebPage.SelectAll)
        
    def keyPressEvent(self, event):
        
        # Ctrl+A should do Select All
        if (event.key() == Qt.Key_A) and (event.nativeModifiers() and Qt.ControlModifier):
            self.page().triggerAction(QWebPage.SelectAll)
            
        event.ignore()
        
    def keyReleaseEvent(self, event):
        event.ignore()
        
    def getZoom(self):
        return self.myZoomFactor
        
    def setZoom(self, newZoom):
        self.myZoomFactor = newZoom
        self.setZoomFactor(newZoom)
        self.update()
        
    def zoomIn(self):
        '''
        Called by application to zoom the view in.
        '''
        self.myZoomFactor += 0.1
        if self.myZoomFactor > 20.0:
            self.myZoomFactor = 20.0
        self.setZoomFactor(self.myZoomFactor)
        self.update()
    
    def zoomOut(self):
        '''
        Called by application to zoom the view out.
        '''
        self.myZoomFactor -= 0.1
        if self.myZoomFactor < 0.2:
            self.myZoomFactor = 0.2
        self.setZoomFactor(self.myZoomFactor)
        self.update()
        
    def myLinkClicked(self, url):
        webbrowser.open_new(str(url.toString()))