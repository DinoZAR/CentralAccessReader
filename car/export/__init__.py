'''
Created on Dec 18, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread, pyqtSignal

class ExportThread(QThread):
    '''
    Provides base abstract class that all other export threads must adhere to.
    '''
    # Emits to update others about the progress of this thread, in the following
    # form: percentage (0-100), labelDescribingState
    progress = pyqtSignal(int, unicode)
    
    success = pyqtSignal()
    
    def __init__(self, document, htmlContent, tempDirectory):
        super(ExportThread, self).__init__()
        self._document = document
        self._htmlContent = htmlContent
        self._tempDirectory = tempDirectory
        self._filePath = ''
        
        # NOTE: Implementations MUST check this flag to make sure if it should
        # continue exporting. 
        self._running = True
        self.isSuccess = False
    
    @staticmethod
    def description():
        '''
        Returns the description label for the export type. Every subclass must
        override this.
        '''
        return 'Unknown'
        
    def run(self):
        '''
        Runs the thread. Checks that prerequisites are met before it begins the
        operation.
        '''
        if len(self._filePath) == 0:
            return
        self.isSuccess = False
        
    def stop(self):
        '''
        Stops the current export operation (or at least it should).
        '''
        self._running = False
    
    @staticmethod
    def getDefaultPath(inputFilePath):
        '''
        Should return the default file path given an input file path. Can also
        return a directory too.
        '''
        pass
    
    def setFilePath(self, newFilePath):
        '''
        Sets the destination file path.
        '''
        self._filePath = newFilePath