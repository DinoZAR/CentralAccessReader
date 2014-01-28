'''
Created on Dec 16, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QApplication
from lxml import html
from document import Document, html_cleaner

class ClipboardDocument(Document):
    '''
    This document will display the contents of the clipboard.
    '''

    def __init__(self, filePath, progressHook, cancelHook):
        Document.__init__(self, filePath, progressHook, cancelHook)
        self._name = 'Clipboard'
        
        self._progressHook(0, 'Reading from clipboard...')
        
        mime = QApplication.clipboard().mimeData()
        
        if mime.hasHtml():
            myHtml = html_cleaner.clean(html.fromstring(unicode(mime.html())), progressHook=self._progressHook, cancelHook=self._cancelHook)
            self._contentDOM.append(myHtml)
            
        elif mime.hasText():
            self._contentDOM.text = unicode(QApplication.clipboard().text())
        
        else:
            self._contentDOM.text = 'Did not recognize content in clipboard.'
            
        self._mapMathEquations()