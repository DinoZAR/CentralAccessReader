'''
Created on Jul 10, 2013

@author: Spencer Graffe
'''
import traceback
from PyQt4.QtCore import QThread, pyqtSignal
from docx.importer import DocxDocument

class DocxImporterThread(QThread):
    '''
    This thread is used to import a .docx document, report its progress, and
    then return the document that it parsed.
    '''
    reportProgress = pyqtSignal(int)
    reportError = pyqtSignal(Exception, str)
    reportText = pyqtSignal(str)
    
    def __init__(self, filePath):
        QThread.__init__(self)
        self._filePath = filePath
        self._docx = None
        self._html = ''
        self._bookmarks = None
        self._pages = None
        self._stop = False
        
    def run(self):
        
        def myProgressCallback(percentage):
            self.reportProgress.emit(percentage)
            
        def myCheckCancel():
            return self._stop
        
        try:
            self._docx = DocxDocument(self._filePath, myProgressCallback, myCheckCancel)
            
            if not self._stop:
                self._html = self._docx.getMainPage()
                self._bookmarks = self._docx.getHeadings()
                self._pages = self._docx.getPages()
            
        except Exception as ex2:
            print 'ERROR: The .docx document didn\'t import.'
            self.reportError.emit(ex2, traceback.format_exc())
        
    def stop(self):
        self._stop = True
        
    def isSuccessful(self):
        '''
        Returns whether the importer successfully finished parsing the .docx
        '''
        return not self._stop
    
    def getFilePath(self):
        return self._filePath
    
    def getDocument(self):
        return self._docx
    
    def getHTML(self):
        return self._html
    
    def getHeadings(self):
        return self._bookmarks
    
    def getPages(self):
        return self._pages