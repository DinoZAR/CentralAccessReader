'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
import webbrowser
import re

from PyQt4.QtWebKit import QWebView, QWebPage
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4.QtGui import QApplication, QMenu, QAction, QKeySequence

from car import misc

class NPAWebView(QWebView):
    '''
    This subclass is meant to override some of the mouse behavior, most notably the zoom feature.
    '''
    ZOOM_LEVELS = [.25, .5, .75, 1, 1.25, 1.5, 2, 3, 4, 5, 7, 9, 12, 15, 18, 21]
    DEFAULT_ZOOM_INDEX = 3
    
    toggleSpeechPlayback = pyqtSignal()
    contentCommand = pyqtSignal(unicode)
    
    cursorMoved = pyqtSignal()
    
    # Signals for my custom context menu
    requestCopy = pyqtSignal()
    requestPaste = pyqtSignal()
    requestReadFromSelection = pyqtSignal()
    requestSaveSelectionToMP3 = pyqtSignal()

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QWebView.__init__(self, parent)
        self._zoomIndex = self.DEFAULT_ZOOM_INDEX
        
        self.setAcceptDrops(False)
        
        self.setMouseTracking(True)
        
        self.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
            
        self.linkClicked.connect(self.myLinkClicked)
        self._keyboardNavEnabled = True
        
        # Create my copy shortcut
        self.copyAction = QAction('Copy', self)
        self.copyAction.triggered.connect(self.copyToClipboard)
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.addAction(self.copyAction)
    
    def contextMenuEvent(self, ev):
        '''
        Make up my own context menu called when user right-clicks on window.
        '''
        menu = QMenu()
        menu.addAction(self.copyAction)
        menu.addAction('Paste', self.requestPaste)
        menu.addSeparator()
        menu.addAction('Start Reading From Selection', self.requestReadFromSelection)
        menu.addAction('Save Selection to MP3', self.requestSaveSelectionToMP3)
        menu.exec_(ev.globalPos())
        
    def copyToClipboard(self):
        self.requestCopy.emit()
        
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
            self.toggleSpeechPlayback.emit()
        
        if self._keyboardNavEnabled:
            # Arrow Up
            if event.key() == Qt.Key_Up:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorUp', []))
                self.cursorMoved.emit()
                event.ignore()
    
            # Arrow Down
            elif event.key() == Qt.Key_Down:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorDown', []))
                self.cursorMoved.emit()
                event.ignore()
                
            # Arrow left
            elif event.key() == Qt.Key_Left:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorLeft', []))
                self.cursorMoved.emit()
                event.ignore()
    
            # Arrow right
            elif event.key() == Qt.Key_Right:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorRight', []))
                self.cursorMoved.emit()
                event.ignore()
                
            # Home
            elif event.key() == Qt.Key_Home:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToStart', []))
                self.cursorMoved.emit()
                event.ignore()

            # End                
            elif event.key() == Qt.Key_End:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToEnd', []))
                self.cursorMoved.emit()
                event.ignore()
                
            # Page Up
            elif event.key() == Qt.Key_PageUp:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToPreviousBookmark', []))
                self.cursorMoved.emit()
                event.ignore()
            
            # Page Down
            elif event.key() == Qt.Key_PageDown:
                self.page().mainFrame().evaluateJavaScript(misc.js_command('MoveCursorToNextBookmark', []))
                self.cursorMoved.emit()
                event.ignore()
        
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
        # Check if the link was actually a command from a button
        m = re.search('Central Access Reader/command/[a-zA-Z]*', unicode(url))
        if m is not None:
            # Get the command string out and emit it as a signal
            command = m.group(0).split('/')[2]
            self.contentCommand.emit(command)
            
        else:
            webbrowser.open_new(str(url.toString()))
    
    def setKeyboardNavEnabled(self, isEnabled):
        '''
        Sets whether the keyboard navigation is enabled or disabled. One would
        want to disable it if they wanted to manipulate the highlighter, like
        a TTS engine.
        '''
        self._keyboardNavEnabled = isEnabled