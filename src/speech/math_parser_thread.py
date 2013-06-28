'''
Created on Jun 28, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread, QMutex, pyqtSignal


class MathParserThread(QThread):
    '''
    This thread is used to continuously parse math equations and then post them
    to the assigner when they are done.
    '''
    
    mathParsed = pyqtSignal(dict)
    
    queueLock = QMutex()
    mathDatabaseLock = QMutex()

    def __init__(self, mathDatabase):
        QThread.__init__(self)
        self._mathDatabase = mathDatabase
        self._mathQueue = []
    
    def run(self):
        pass
    
    def setMathDatabase(self, newMathDatabase):
        '''
        Changes the math database that this parser is using.
        '''
        self.mathDatabaseLock.lock()
        self._mathDatabase = newMathDatabase
        self.mathDatabaseLock.unlock()
        
    def addToQueue(self, mathData):
        '''
        Adds some math data to the queue.
        '''
        self.queueLock.lock()
        self._mathQueue.append(mathData)
        self.queueLock.unlock()