'''
Created on May 2, 2013

Contains some very useful but otherwise random functions and classes that are
practically universally applicable.

@author: Spencer Graffe
'''
import sys
import os
import platform
import subprocess
import inspect
from PyQt4.QtCore import QThread, pyqtSignal

_PROGRAM_ROOT = 'Central Access Reader'

REPORT_BUG_URL = 'http://www.cwu.edu/central-access/report-bug-central-access-reader'
SURVEY_URL = 'http://www.cwu.edu/central-access/central-access-reader-survey'

MATHML_PATTERNS_FOLDER = 'src/math_patterns'

def program_path(resourceFile):
    '''
    Returns the path to the program installation folder, whether it is in a
    development environment or in an installed environment.
    ''' 
    if getattr(sys, 'frozen', None):
        if getattr(sys, '_MEIPASS', None):
            # This is a PyInstaller-packaged program
            myPath = os.path.join(sys._MEIPASS, resourceFile)
            return myPath
        else:
            # This is an app-packaged program (for Mac)
            myPath = os.path.join(os.environ['RESOURCEPATH'], resourceFile)
            return myPath
    else:
        myPath = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(inspect.getsourcefile(program_path))), resourceFile))
        return myPath
    
def app_data_path(resourceFile):
    '''
    Returns the path to the resource file stored in the app data. This path will
    be different on different operating systems.
    '''
    newPath = ''
    if sys.platform == 'win32':
        newPath = os.path.join(os.environ['APPDATA'], _PROGRAM_ROOT, resourceFile)
    elif sys.platform == 'darwin':
        newPath = os.path.join('/Users/', os.environ['USER'], 'Library/Application Support/', _PROGRAM_ROOT, resourceFile)
    
    return newPath

def temp_path(resourceFile):
    '''
    Returns the path to the resource file relative to the temporary directory.
    This directory will be different depending on the operating system.
    '''
    newPath = ''
    if sys.platform == 'win32':
        newPath = os.path.join(os.environ['TEMP'], _PROGRAM_ROOT, resourceFile)
    if sys.platform == 'darwin':
        newPath = os.path.join(os.environ['TMPDIR'], _PROGRAM_ROOT, resourceFile)
    
    return newPath

def pattern_databases():
    '''
    Returns a list of file paths of the databases that are in this program. This
    will omit the ones with an underscore at the beginning, since those are
    meant to be used in other patterns, not in of themselves.
    '''
    fileList = {}
    
    for f in os.listdir(program_path(MATHML_PATTERNS_FOLDER)):
        p = os.path.join(program_path(MATHML_PATTERNS_FOLDER), f)
        if os.path.isfile(p):
            if os.path.basename(p)[0] != '_' and os.path.splitext(p)[1] == '.txt':
                fileList[os.path.splitext(os.path.basename(p))[0]] = p
            
    return fileList

def is_release_environment():
    '''
    Returns whether this program instance is in a release environment. Returns
    True if it is, False if it is not, which means this program instance is in
    a development environment.
    '''
    if getattr(sys, 'frozen', None):
        return True
    else:
        return False
    
def is_number(numberString):
    '''
    Checks if the string is an integer. It only returns True or False.
    '''
    try:
        int(numberString)
        return True
    except ValueError:
        return False

def clean_XML_input(input):  
    
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
    
    #print 'JavaScript:', commandString
    
    return commandString

def open_file_browser_to_location(filePath):
    '''
    Creates the process to open a file browser with the file selected.
    '''
    if sys.platform == 'win32':
        subprocess.Popen(r'explorer /select,"' + os.path.abspath(filePath) + '"')
    if sys.platform == 'darwin':
        appleScript = '''
set p to "''' + filePath + '''"

tell application "Finder"
    reveal POSIX file p as text
    activate
end tell
'''
        osa = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        osa.communicate(appleScript)[0]

def prepare_bug_report(traceback, configuration, detailMessage=None):
    '''
    Returns a string representing the bug report that should be sent.
    '''
    out = 'Bug Report:\n---------------------------------------\n'
    
    # Platform
    out += 'Platform: ' + platform.system()
    if platform.system() == 'Windows':
        # Add some other data to it
        data = platform.win32_ver()
        out += ' ' + data[0] + ' ' + data[1] + ' ' + data[2] + '\n'
    else:
        out += '\n'
        
    
    # Traceback
    out += 'Traceback:\n' + traceback + '\n'
    
    # Settings
    out += configuration.getBugReportString()
    
    # Details
    if detailMessage != None:
        out += '\nDetails:\n'
        out += '--------------\n'
        out += detailMessage
    
    return out

class UpdateQtThread(QThread):
    '''
    Used to process events in the PyQt main thread while something else is
    hogging up my main thread.
    '''
    
    updateGUI = pyqtSignal()
    
    def __init__(self):
        QThread.__init__(self)
        self._stopping = False
        
    def run(self):
        print 'Gui updator running...'
        while not self._stopping:
            self.updateGUI.emit()
    
    def stop(self):
        self._stopping = True
    
