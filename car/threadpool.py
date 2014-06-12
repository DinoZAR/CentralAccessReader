'''
Created on Jan 7, 2014

@author: Spencer Graffe
'''
import time
from PyQt5.QtCore import QThread, QMutex, QSignalMapper, pyqtSignal

class ThreadPool(QThread):
    '''
    Pool used to run QThreads as jobs. For a job to be cancellable, the
    QThread must implement stop(). Otherwise, it will be forcefully terminated.
    '''
    _poolLock = QMutex()
    _queueLock = QMutex()
    
    jobsStarted = pyqtSignal()
    jobsFinished = pyqtSignal()

    def __init__(self, numThreads=4):
        super(ThreadPool, self).__init__()
        self._pool = []
        self._queue = []
        self._threadId = 0
        self._maxThreads = numThreads
        self._running = True
        self._mapper = QSignalMapper()
        self._mapper.mapped.connect(self._removeThread)
    
    def run(self):
        while self._running:
            if self._queueLock.tryLock():
                self._poolLock.lock()
                while len(self._pool) < self._maxThreads:
                    if len(self._queue) > 0:
                        
                        if len(self._pool) == 0:
                            self.jobsStarted.emit()
                        
                        job = self._queue.pop(0)
                        self._mapper.setMapping(job, self._threadId)
                        job.finished.connect(self._mapper.map)
                        #job.terminated.connect(self._mapper.map)
                        self._pool.append((job, self._threadId))
                        self._threadId += 1
                        job.start()
                    else:
                        break
                self._poolLock.unlock()
                self._queueLock.unlock()
            
            time.sleep(0.2)
    
    def stop(self):
        self._running = False
        
    def cancelJobs(self):
        self._queueLock.lock()
        self._poolLock.lock()
        
        # Clean out and terminate all jobs in pool
        while len(self._pool) > 0:
            job = self._pool.pop()
            jobStop = getattr(job[0], "stop", None)
            if callable(jobStop):
                job[0].stop()
            else:
                job[0].terminate()
        
        # Clean out queue
        self._queue = []
        
        self._poolLock.unlock()
        self._queueLock.unlock()
    
    def addJob(self, jobThread):
        self._queueLock.lock()
        self._queue.append(jobThread)
        self._queueLock.unlock()
    
    def _removeThread(self, threadId):
        self._queueLock.lock()
        self._poolLock.lock()
        
        for i in range(len(self._pool)):
            if self._pool[i][1] == threadId:
                self._pool.pop(i)
                break
            
        if len(self._pool) == 0 and len(self._queue) == 0:
            self.jobsFinished.emit()
        
        self._poolLock.unlock()
        self._queueLock.unlock()
        