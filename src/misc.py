'''
Created on May 2, 2013

Contains some very useful but otherwise random functions and classes that are
practically universally applicable.

@author: Spencer Graffe
'''
import sys
import os
import platform
from threading import Thread
from PyQt4 import QtGui

_PROGRAM_ROOT = 'Nifty Prose Articulator'

def program_path(resourceFile):
    '''
    Returns the path to the program installation folder, whether it is in a
    development environment or in an installed environment.
    ''' 
    if getattr(sys, 'frozen', None):
        myPath = os.path.join(sys._MEIPASS, resourceFile)
        return myPath
    else:
        myPath = os.path.abspath('../' + resourceFile)
        return myPath
    
def app_data_path(resourceFile):
    '''
    Returns the path to the resource file stored in the app data. This path will
    be different on different operating systems.
    '''
    newPath = ''
    if 'Windows' in platform.system():
        newPath = os.path.join(os.path.join(os.environ['APPDATA'], _PROGRAM_ROOT), resourceFile)
    
    return newPath

def temp_path(resourceFile):
    '''
    Returns the path to the resource file relative to the temporary directory.
    This directory will be different depending on the operating system.
    '''
    newPath = ''
    if 'Windows' in platform.system():
        newPath = os.path.join(os.path.join(os.environ['TEMP'], _PROGRAM_ROOT), resourceFile)
    
    return newPath
    
def clean_XML_input(input):  
      
    print 'Input:', [input]
    
    if input:  
              
        import re  
          
        # unicode invalid characters  
        RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + u'|' + u'([{0}-{1}][^{2}-{3}])|([^{4}-{5}][{6}-{7}])|([{8}-{9}]$)|(^[{10}-{11}])'.format(
                        unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))
        input = re.sub(RE_XML_ILLEGAL, "", input)  
                          
        # ascii control characters  
        input = re.sub(r"[\x01-\x1F\x7F]", "", input)  
              
    return input
    
def js_command(functionName, args):
    '''
    Returns a correctly formatted JavaScript function call that is called
    <functionName> and uses a list of args as [arg1, arg2, ...]
    '''
    commandString = functionName + '('
    
    if len(args) > 0:
        for i in args:
            if isinstance(i, bool):
                if i:
                    commandString += 'true'
                else:
                    commandString += 'false'
            elif isinstance(i, basestring):
                commandString += '\"' + i + '\"'
            else:
                commandString += str(i)
            commandString += ','
            
        # Remove last comma
        commandString = commandString[:-1]
    
    # Add closing parenthesis
    commandString += ')'
    
    return commandString
    

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
    