'''
Created on May 2, 2013

Contains some very useful but otherwise random functions and classes that are
practically universally applicable.

@author: Spencer Graffe
'''
import sys
import os
from threading import Thread
from PyQt4 import QtGui

def resource_path(resourceFile, forceDir=False):
    '''
    Returns the correct path to the resource file. This path will change
    depending on whether we are in a "frozen" distribution or in a development
    context
    '''
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
        if forceDir:
            print 'Resource:', os.path.join(basedir, os.path.normpath(resourceFile))
            return os.path.join(basedir, os.path.normpath(resourceFile))
        else:
            print 'Resource:', os.path.join(basedir, os.path.basename(resourceFile))
            return os.path.join(basedir, os.path.basename(resourceFile))
    else:
        print 'Resource:', os.path.abspath(resourceFile)
        return os.path.abspath(resourceFile)
    

class UpdateQtThread(Thread):
    '''
    Used to process events in the PyQt main thread while something else is
    hogging up my main thread.
    '''
    def __init__(self):
        Thread.__init__(self)
        self._stopping = False
        
    def run(self):
        while not self._stopping:
            QtGui.qApp.processEvents()
    
    def stop(self):
        self._stopping = True
    