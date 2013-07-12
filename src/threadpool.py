'''
Created on Jul 11, 2013

@author: Spencer Graffe
'''
from multiprocessing import cpu_count
from threading import Thread
from Queue import Queue, Empty

class Pool(object):
    '''
    This is a thread pool that uses threads to carry out tasks.
    '''

    def __init__(self, numThreads=None):
        '''
        Creates and starts a pool of threads. If numThreads is None, it will
        default either to the number of CPU cores or 2, whichever is greater.
        '''
        # Set default number of threads
        if numThreads is None:
            numThreads = cpu_count()
            if numThreads < 2:
                numThreads = 2
        
        print 'Using', numThreads, 'threads...'
        
        self._queue = Queue()
        self._pool = []
        for i in range(numThreads):
            t = PoolWorker(self._queue)
            self._pool.append(t)
            t.start()
    
    def addTask(self, task, callback, args=(), kwargs={}):
        '''
        Adds a task to the pool.
        '''
        job = {}
        job['task'] = task
        job['args'] = args
        job['kwargs'] = kwargs
        job['callback'] = callback
        self._queue.put(job)
    
    def join(self):
        '''
        Returns when the pool has completely processed all tasks in the queue.
        '''
        # Make sure queue is empty
        while True:
            if self._queue.empty():
                break
            
        # Wait for all of my threads to finish
        for t in self._pool:
            t.stop()
            t.join()
            
    def stop(self):
        '''
        Stops the pool from processing more tasks. It will block until its
        threads have finished the tasks they were assigned before the stop call.
        '''
        # Stop them all
        for t in self._pool:
            t.stop()
        
        # Join them all
        for t in self._pool:
            t.join()
            
    
class PoolWorker(Thread):
    '''
    This is a worker thread that functions in a pool. It continually pulls tasks
    it needs to process and processes them. It can be interrupted gracefully at
    any time.
    
    It uses the callback to report the results of the task it ran.
    '''
    
    def __init__(self, jobQueue):
        Thread.__init__(self)
        self._queue = jobQueue
        self._running = True
        
    def run(self):
        while self._running:
            
            # Get the job
            job = None
            try:
                job = self._queue.get_nowait()
            except Empty:
                pass
            
            # Run a job if I got one
            if job is not None:
                job['callback'](job['task'](*job['args'], **job['kwargs']))
                
    def stop(self):
        self._running = False