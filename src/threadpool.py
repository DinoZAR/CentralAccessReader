'''
Created on Jul 11, 2013

@author: Spencer Graffe
'''
from multiprocessing import Process, Queue, Pipe, cpu_count
from threading import Thread, Lock
from Queue import Empty
import traceback
import time

class Pool(object):
    '''
    This is a process pool that uses processes to carry out tasks.
    '''

    def __init__(self, numProcesses=None):
        '''
        Creates and starts a pool of processes. If numProcesses is None, it will
        default either to the number of CPU cores or 2, whichever is greater.
        '''
        # Set default number of threads
        self._numProcesses = numProcesses
        if self._numProcesses is None:
            self._numProcesses = cpu_count()
            if self._numProcesses < 2:
                self._numProcesses = 2
        
        print 'Using', self._numProcesses, 'processes...'
        
        self._jobQueue = Queue()
        self._resultQueue = Queue()
        self._errorPipes = []
        self._cancelPipes = []
        self._pool = []
        self._taskIdCounter = 0
        self._taskCallbacks = {}
        self._taskCallbacksLock = Lock()
        self._resultDispatcher = None
        self._startResultDispatcher()
        self._startWorkers()
    
    def addTask(self, task, callback, args=(), kwargs={}):
        '''
        Adds a task to the pool. The callback must be a function that accepts
        one argument. The error callback, if provided, must accept the following
        arguments: (traceback, error)
        
        The callback is the only thing that doesn't have to be pickleable.
        Everything else, including the task, elements in args, and elements in
        kwargs must be pickleable. 
        
        The reason is because object references are only valid on the thread
        this Pool class resides. When those references are put in a completely
        different process, the memory addresses not only don't match up, they
        are also in a space that the new process can't access. Pickling is
        just a handy tool that serializes objects and reconstructs them in the
        new processes' address space.
        '''
        print 'Adding job!'
        job = {}
        job['task'] = task
        job['args'] = args
        job['kwargs'] = kwargs
        
        # Register callback in my results dictionary
        self._taskIdCounter += 1
        job['callback_id'] = self._taskIdCounter
        self._taskCallbacksLock.acquire()
        self._taskCallbacks[job['callback_id']] = callback
        self._taskCallbacksLock.release()
        
        self._jobQueue.put(job)
        
    def hasTasks(self):
        '''
        Returns whether this pool has tasks it hasn't completed yet.
        '''
        return not self._jobQueue.empty()
    
    def join(self):
        '''
        Returns after the pool has completely processed all tasks in the queue.
        '''
        while True:
            if self._jobQueue.empty():
                break

        for c in self._cancelPipes:
            c.send(True)
            
        self._resultDispatcher.stop()
        self._resultDispatcher.join()
            
        for t in self._pool:
            t.join()
            
    def stop(self):
        '''
        Stops the pool from processing more tasks. It will block until its
        threads have finished the tasks they were assigned before the stop call.
        '''
        for c in self._cancelPipes:
            c.send(True)
        
        self._jobQueue.close()
        
        self._resultDispatcher.stop()
        self._resultDispatcher.join()
        
        for t in self._pool:
            t.join()
            
    def terminate(self):
        '''
        Stops the pool immediately. All processes that may or may not be working
        on a task will be terminated immediately. Make sure those processes are 
        not modifying external resources.
        '''
        for c in self._cancelPipes:
            c.send(True)
            
        self._jobQueue.close()
        
        self._resultDispatcher.stop()
        self._resultDispatcher.join()
            
        for t in self._pool:
            t.terminate()
    
    def getErrors(self):
        '''
        Returns a list of errors that the thread pool has encountered, if any.
        The list is a series of (exception, traceback_string) tuples.
        
        Returns None if no errors exist.
        '''
        myErrors = []
        for e in self._errorPipes:
            if e.poll():
                myErrors.append(e.recv())
        
        if len(myErrors) > 0:
            return myErrors
        else:
            return None
            
    def _startWorkers(self):
        for i in range(self._numProcesses):
            myError, theirError = Pipe()
            myCancel, theirCancel = Pipe()
            p = Process(target=worker_process, args=(self._jobQueue, self._resultQueue, theirError, theirCancel))
            self._errorPipes.append(myError)
            self._cancelPipes.append(myCancel)
            self._pool.append(p)
            p.start()
            
    def _startResultDispatcher(self):
        '''
        Starts the thread that dispatches the results to the callback functions 
        '''
        self._resultDispatcher = ResultDispatcherThread(self._resultQueue, self._taskCallbacks, self._taskCallbacksLock)
        self._resultDispatcher.start()
        
def worker_process(jobQueue, resultQueue, errorPipe, cancelPipe):
    '''
    Function that the processes in the pool use to process tasks. It
    continually pulls from the job queue and reports exceptions using the
    error pipe. The cancel pipe allows this worker process to finish up the
    task it was working on and to stop.
    '''
    running = True
    while running:
        #print 'Checking for jobs!'
        # Get a job
        job = None
        try:
            job = jobQueue.get(block=True, timeout=0.01)
        except Empty:
            pass
        
        # Run the job
        if job is not None:
            try:
                print 'Working on job...'
                r = job['task'](*job['args'], **job['kwargs'])
                resultQueue.put((job['callback_id'], r))
            except Exception as e:
                print 'Something crappy happened!', traceback.format_exc()
                errorPipe.send((e, traceback.format_exc()))
                
        # Check for cancel
        if cancelPipe.poll():
            running = not cancelPipe.recv()
            
class ResultDispatcherThread(Thread):
    '''
    This thread is used to dispatch results from the pool. I'm doing it this
    way because I can't pickle instance methods, which is what Process requires.
    '''
    def __init__(self, resultQueue, taskCallbacks, taskCallbacksLock):
        Thread.__init__(self)
        self._running = True
        self._queue = resultQueue
        self._taskCallbacks = taskCallbacks
        self._taskCallbacksLock = taskCallbacksLock
        
    def run(self):
        while self._running:
            try:
                result = self._queue.get(block=True, timeout=0.01)
                taskId = result[0]
                taskResult = result[1]
                
                print 'Reporting result of task!'
                self._taskCallbacksLock.acquire()
                self._taskCallbacks[taskId](taskResult)
                del self._taskCallbacks[taskId]
                self._taskCallbacksLock.release()
            except Empty:
                pass
        
        # At this point, the thread is stopping. Get the rest of the results.
        while not self._queue.empty():
            try:
                result = self._queue.get(block=True, timeout=0.01)
                taskId = result[0]
                taskResult = result[1]
                
                print 'Reporting result of task!'
                
                self._taskCallbacksLock.acquire()
                self._taskCallbacks[taskId](taskResult)
                del self._taskCallbacks[taskId]
                self._taskCallbacksLock.release()
            except Empty:
                pass
    
    def stop(self):
        self._running = False 
