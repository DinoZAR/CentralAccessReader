'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
from PyQt4.QtWebKit import QWebView, QWebPage
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication
import webbrowser
import os
import misc

class NPAWebView(QWebView):
    '''
    This subclass is meant to override some of the mouse behavior, most notably the zoom feature.
    '''
    
    ZOOM_LEVELS = [.25, .5, .75, 1, 1.25, 1.5, 2, 3, 4, 5, 7, 9, 12]
    DEFAULT_ZOOM_INDEX = 3

    def __init__(self, mainWindow, parent=None):
        '''
        Constructor
        '''
        QWebView.__init__(self, parent)
        self.mainWindow = mainWindow
        self.setAcceptDrops(True)
        self._zoomIndex = self.DEFAULT_ZOOM_INDEX
        
        self.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        
        # Disable the context menu if in a release environment
        if misc.is_release_environment():
            def nothing(s, event):
                pass
            self.contextMenuEvent = nothing
            
        self.linkClicked.connect(self.myLinkClicked)
        
        self._keyboardNavEnabled = True
        
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            url = unicode(e.mimeData().urls()[0].toLocalFile())
            ext = os.path.splitext(url)[1]
            if ext == '.docx' or ext == '.doc':
                e.setDropAction(Qt.CopyAction)
                e.accept()
            else:
                e.ignore()
        else:
            e.ignore()
            
    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            url = unicode(e.mimeData().urls()[0].toLocalFile())
            ext = os.path.splitext(url)[1]
            if ext == '.docx' or ext == '.doc':
                e.setDropAction(Qt.CopyAction)
                e.accept()
            else:
                e.ignore()
        else:
            e.ignore()
            
    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            e.setDropAction(Qt.CopyAction)
            e.accept()
            url = unicode(e.mimeData().urls()[0].toLocalFile())
            if os.path.splitext(url)[1] == '.docx':
                self.mainWindow.activateWindow()
                self.mainWindow.raise_()
                self.mainWindow.openDocx(url)
            elif os.path.splitext(url)[1] == '.doc':
                self.mainWindow.showDocNotSupported()
        
    def wheelEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if modifiers and Qt.ControlModifier:
            # Zoom the window
            if event.delta() > 0:
                self._zoomIndex -= 1
                if self._zoomIndex < 0:
                    self._zoomIndex = 0
                self.setZoomFactor(self.ZOOM_LEVELS[self._zoomIndex])
                self.update()
            else:
                self._zoomIndex += 1
                if self._zoomIndex >= len(self.ZOOM_LEVELS):
                    self._zoomIndex = len(self.ZOOM_LEVELS) - 1
                self.setZoomFactor(self.ZOOM_LEVELS[self._zoomIndex])
                self.update()
        else:
            # Otherwise, just scroll it
            self.page().mainFrame().scroll(0, -event.delta())
        
        event.ignore()
        
    def selectAll(self):
        self.page().triggerAction(QWebPage.SelectAll)
        
    def keyPressEvent(self, event):
        
        # Ctrl+A (Select All)
        if (event.key() == Qt.Key_A) and (event.nativeModifiers() and Qt.ControlModifier):
            self.page().triggerAction(QWebPage.SelectAll)
            event.ignore()
        
        elif event.key() == Qt.Key_Space:
            self.mainWindow.toggleSpeech()
        
        if self._keyboardNavEnabled:
            # Arrow Up
            if event.key() == Qt.Key_Up:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorUp', []))
                event.ignore()
    
            # Arrow Down
            elif event.key() == Qt.Key_Down:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorDown', []))
                event.ignore()
                
            # Arrow left
            elif event.key() == Qt.Key_Left:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorLeft', []))
                event.ignore()
    
            # Arrow right
            elif event.key() == Qt.Key_Right:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorRight', []))
                event.ignore()
                
            # Home
            elif event.key() == Qt.Key_Home:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToStart', []))
                event.ignore()

            # End                
            elif event.key() == Qt.Key_End:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToEnd', []))
                event.ignore()
                
            # Page Up
            elif event.key() == Qt.Key_PageUp:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToPreviousBookmark', []))
            
            # Page Down
            elif event.key() == Qt.Key_PageDown:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToNextBookmark', []))
        
    def keyReleaseEvent(self, event):
        event.ignore()
        
    def getZoom(self):
        '''
        Gets the current zoom factor of my web view
        '''
        return self.ZOOM_LEVELS[self._zoomIndex]
        
    def setZoom(self, newZoom):
        '''
        Sets the zoom level that most closely matches my levels
        '''
        deltas = []
        for i in range(len(self.ZOOM_LEVELS)):
            deltas.append((i, abs(self.ZOOM_LEVELS[i] - newZoom)))
        deltas = sorted(deltas, key=lambda x : x[1])
        self._zoomIndex = deltas[0][0]
        self.setZoomFactor(self.ZOOM_LEVELS[self._zoomIndex])
        self.update()
        
        # Scroll view to the highlight cursor
        self.page().mainFrame().evaluateJavaScript(misc.js_command('ScrollToHighlight', [True]))
        
    def zoomIn(self):
        '''
        Called by application to zoom the view in.
        '''
        self._zoomIndex += 1
        if self._zoomIndex >= len(self.ZOOM_LEVELS):
            self._zoomIndex = len(self.ZOOM_LEVELS) - 1
        self.setZoomFactor(self.ZOOM_LEVELS[self._zoomIndex])
        self.update()
        
        # Scroll view to the highlight cursor
        self.page().mainFrame().evaluateJavaScript(misc.js_command('ScrollToHighlight', [True]))
    
    def zoomOut(self):
        '''
        Called by application to zoom the view out.
        '''
        self._zoomIndex -= 1
        if self._zoomIndex < 0:
            self._zoomIndex = 0
        self.setZoomFactor(self.ZOOM_LEVELS[self._zoomIndex])
        self.update()
        
        # Scroll view to the highlight cursor
        self.page().mainFrame().evaluateJavaScript(misc.js_command('ScrollToHighlight', [True]))
        
    def zoomReset(self):
        '''
        Called by application to reset the zoom factor to 1.0
        '''
        self._zoomIndex = self.DEFAULT_ZOOM_INDEX
        self.setZoomFactor(self.ZOOM_LEVELS[self._zoomIndex])
        self.update()
        
        # Scroll view to the highlight cursor
        self.page().mainFrame().evaluateJavaScript(misc.js_command('ScrollToHighlight', [True]))
        
    def myLinkClicked(self, url):
        webbrowser.open_new(str(url.toString()))
    
    def setKeyboardNavEnabled(self, isEnabled):
        '''
        Sets whether the keyboard navigation is enabled or disabled. One would
        want to disable it if they wanted to manipulate the highlighter, like
        a TTS engine.
        '''
        self._keyboardNavEnabled = isEnabled