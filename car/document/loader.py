'''
Created on Nov 15, 2013

@author: Spencer Graffe
'''
import os
import traceback

try:
    from PyQt4.QtCore import QThread, pyqtSignal
except ImportError:
    from PyQt5.QtCore import QThread, pyqtSignal

from car.document.docx.docx_document import DocxDocument
from car.document.clipboard_document import ClipboardDocument
from PyQt4.QtGui import QMessageBox

class DocumentLoadingThread(QThread):
    '''
    This QThread loads in a document asynchronously. It will then tell the GUI
    when it is finished, presenting the document.
    '''
    
    progress = pyqtSignal(int, unicode)
    error = pyqtSignal(object)

    def __init__(self, fileName, isClipboard=False):
        '''
        Constructor
        '''
        QThread.__init__(self)
        
        self._fileName = fileName
        self._isClipboard = isClipboard
        self._success = False
        self._doc = None
        self._canceled = False
    
    def run(self):
        
        self._success = False
        
        try:
            if not self._isClipboard:
                # Check which document goes to this extension
                ext = os.path.splitext(os.path.basename(self._fileName))[1].lower()
                if ext == '.docx':
                    self._doc = DocxDocument(self._fileName, self._reportProgress, self._isCanceled)
            else:
                self._doc = ClipboardDocument('', self._reportProgress, self._isCanceled)
        except Exception as e:
            print 'Could not read file', self._fileName, ':', e
            #QMessageBox.about(self, "File Import Error", "The document you are trying to import is corrupt.")
            traceback.print_exc()
            self._success = False
            self.error.emit(e)
            return
        
        self._success = not self._isCanceled()
            
    def _reportProgress(self, percent, label):
        self.progress.emit(percent, label)
        
    def _isCanceled(self):
        return self._canceled
    
    def stop(self):
        self._canceled = True
        
    def isSuccess(self):
        return self._success
    
    def getDocument(self):
        if self._success:
            return self._doc
        else:
            return None