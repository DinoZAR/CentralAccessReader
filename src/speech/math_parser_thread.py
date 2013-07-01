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
    mathParsed = pyqtSignal(tuple)
    queueLock = QMutex()
    mathTTSLock = QMutex()
    
    def __init__(self, mathTTS):
        QThread.__init__(self)
        self._mathTTS = mathTTS
        self._mathQueue = []
    
    def run(self):
        while True:
            if self._mathTTS != None:
                if len(self._mathQueue) > 0:
                    # Keep using the math database to parse math equations. Then, 
                    # publish the parsed math out to whatever needs it.
                    self.queueLock.lock()
                    math = self._mathQueue.pop(0)
                    self.queueLock.unlock()
                    
                    self.mathTTSLock.lock()
                    prose = self._mathTTS.parse(math[1]['mathml'])
                    self.mathTTSLock.unlock()
                    
                    math[1]['parsed'] = True
                    math[1]['prose'] = prose
                    
                    self.mathParsed.emit(math)
    
    def setMathDatabase(self, newMathTTS):
        '''
        Changes the math database that this parser is using. It should be a 
        MathTTS object.
        '''
        self.mathTTSLock.lock()
        self._mathTTS = newMathTTS
        self.mathTTSLock.unlock()
        
    def addToQueue(self, mathData):
        '''
        Adds some math data to the queue.
        '''
        self.queueLock.lock()
        self._mathQueue.append(mathData)
        self.queueLock.unlock()
        
    def clearQueue(self):
        '''
        Removes all of the items in its queue.
        '''
        self.queueLock.lock()
        self._mathQueue = []
        self.queueLock.unlock()
        
        