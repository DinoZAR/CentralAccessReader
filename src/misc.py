'''
Created on May 2, 2013

@author: Spencer Graffe
'''
import sys
import os

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