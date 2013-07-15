'''
Created on Jul 15, 2013

Provides a flexible way to map a list with a function using multiple threads.
It also has the ability to be stopped at anytime and has the ability to implant
progress hooks.

@author: Spencer Graffe
'''
from multiprocessing import Process, Manager, cpu_count, Queue, Pipe
from Queue import Empty
from threading import Thread
import traceback

class ThreadMapper(object):
    '''
    This class allows one to provide a list that should be mapped by a function
    in a multithreaded manner. However, one can also add additional arguments
    to the function while also registering a progress hook to watch the progress
    and a cancel hook to cancel the operation.
    '''
    
    def __init__(self, ls, func, args=(), kwargs={}, numThreads=None, progressHook=None, cancelHook=None):
        self._func = func
        self._args = args
        self._kwargs = kwargs
        
        # Hooks
        self._progressHook = progressHook
        self._cancelHook = cancelHook
        
        # Progress
        self._progressQueue = Queue()
        
        # Errors
        self._errorQueue = Queue()
        
        # Threads
        self._manager = Manager()
        self._lsProxy = self._manager.list(ls)
        self._numThreads = numThreads
        if numThreads is None:
            self._numThreads = cpu_count()
        self._pool = {}
        self._hookManager = None
        
    def start(self):
        '''
        Runs the mapper. It will report progress on the progress hook and listen
        to the cancel hook if it needs to cancel prematurely.
        
        It will return once all threads have been started and queued. You must
        use join() if you want to wait for the mapper to finish.
        '''
        # Figure out the slices of the list that each process should process
        sliceRanges = []
        for i in range(self._numThreads):
            factor = len(self._lsProxy) / self._numThreads
            sliceRanges.append((i * factor, (i + 1) * factor))
        
        # Check that I have as many slice ranges as number of processes
        while len(sliceRanges) < self._numThreads:
            sliceRanges.append((0, 0))
            
        # Add the remaining indices to my last slice if there is a remainder
        sliceRanges[-1] = (sliceRanges[-1][0], sliceRanges[-1][1] + (len(self._lsProxy) % self._numThreads))

        print 'Number of threads:', self._numThreads
        print 'Number of tasks:', len(self._lsProxy)
        print 'Slice ranges:', sliceRanges
        
        # Start all of my processes
        for i in range(self._numThreads):
            myCancel, theirCancel = Pipe()
            p = Process(target=worker_func, args=(i, sliceRanges[i], self._lsProxy, self._func, self._progressQueue, self._errorQueue, theirCancel), 
                        kwargs={'args' : self._args, 'kwargs' : self._kwargs})
            self._pool[i] = [p, myCancel, 0]
            p.start()
        
        # Start the hook manager, which will report the progress and check for
        # cancel
        self._hookManager = HookManager(self._pool, self._progressQueue, self._progressHook, self._cancelHook)
        self._hookManager.start()
    
    def success(self):
        '''
        Returns whether the mapper was successful in completing its task. It
        will return False if a function errored out or if the cancel hook told
        the map to end prematurely.
        '''
        return self._hookManager._finished and (len(self.errors()) == 0)
    
    def errors(self):
        '''
        Returns a list of all of the errors that I have encountered, if any.
        '''
        l = []
        while not self._errorQueue.empty():
            try:
                data = self._errorQueue.get()
                l.append(data)
            except Empty:
                pass
        return l

    def results(self):
        '''
        Returns the results of the calculation. Make sure that the mapper is
        done first!
        '''
        return list(self._lsProxy)
    
    def join(self):
        '''
        Blocks execution until the mapper is finished.
        '''
        while True:
            someAlive = False
            for k in self._pool.keys():
                someAlive = someAlive or self._pool[k][0].is_alive()
            if not someAlive:
                break
            
        print 'All pools are done! Killing hook manager...'
        
        # Stop the hook manager
        self._hookManager.stop()
        self._hookManager.join()
        
class HookManager(Thread):
    '''
    Thread that manages the hooks in my multithreaded mapper.
    '''
    def __init__(self, threadPool, progressQueue, progressHook, cancelHook):
        Thread.__init__(self)
        self._running = True
        self._pool = threadPool
        self._progressQueue = progressQueue
        self._progressHook = progressHook
        self._cancelHook = cancelHook
        self._finished = False
        
    def run(self):
        notInterrupted = True
        while self._running:
            
            # See if I need to cancel
            if self._cancelHook is not None:
                if self._cancelHook():
                    notInterrupted = False
                    for k in self._pool.keys():
                        self._pool[k][1].send(True)
                        
            # See if I have stuff in my progress queue
            try:
                item = self._progressQueue.get_nowait()
                self._pool[item[0]][2] = item[1]
                if self._progressHook is not None:
                    # Calculate the total progress from all of my threads and
                    # report it
                    accum = 0
                    for k in self._pool.keys():
                        accum += self._pool[k][2]
                    print 'Progress:', accum / len(self._pool)
                    self._progressHook(accum / len(self._pool))
            except Empty:
                pass
            
            # Check if everyone is dead
            someAlive = False
            for k in self._pool.keys():
                someAlive = someAlive or self._pool[k][0].is_alive()
                
            if not someAlive:
                break

        print 'Finished up tasks in threads...'

        # If I finished processing the tasks, finish reporting the progress
        if notInterrupted:
            while not self._progressQueue.empty():
                try:
                    item = self._progressQueue.get_nowait()
                    self._pool[item[0]][2] = item[1]
                    if self._progressHook is not None:
                        # Calculate the total progress from all of my threads and
                        # report it
                        accum = 0
                        for k in self._pool.keys():
                            accum += self._pool[k][2]
                        self._progressHook(accum / len(self._pool))
                except Empty:
                    pass
        
        self._finished = notInterrupted
    
    def stop(self):
        self._running = False
        
    
def worker_func(workerId, jobSlice, lsProxy, func, progressQueue, errorQueue, cancelPipe, args=(), kwargs={}):
    '''
    Function that each thread in the mapper runs.
    '''
    print 'Running function in worker...'
    try:
        mylist = lsProxy[jobSlice[0]:jobSlice[1]]
        for i in range(len(mylist)):
            if cancelPipe.poll():
                break
            mylist[i] = func(mylist[i], *args, **kwargs)
            progressQueue.put((workerId, int(float(i + 1) / len(mylist) * 100.0)))
        lsProxy[jobSlice[0]:jobSlice[1]] = mylist
    
    except Exception as e:
        print 'Got an exception, foo!'
        tb = traceback.format_exc()
        errorQueue.put((e, tb))