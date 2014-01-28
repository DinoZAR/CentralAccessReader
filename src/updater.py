'''
Created on Jun 21, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread, pyqtSignal
import platform
import re
import urllib2
import os
import subprocess
import misc

UPDATE_URL = r'https://archive.org/download/CARSetup64/'
#UPDATE_URL = r'file:///W:/Nifty%20Prose%20Articulator/'  # For testing purposes

# Get the correct setup file depending on architecture
SETUP_FILE = ''
if platform.system() == 'Windows':
    if platform.architecture()[0] == '64bit':
        SETUP_FILE = UPDATE_URL + 'CAR_Setup_64.exe'
elif platform.system() == 'Darwin':
    SETUP_FILE = UPDATE_URL + 'Central_Access_Reader.dmg'
    
SETUP_TEMP_FILE = misc.temp_path(os.path.join('update', os.path.basename(SETUP_FILE)))
VERSION_TEMP = misc.temp_path(os.path.join('update', 'version.txt'))

VERSION_THERE = UPDATE_URL + 'version.txt'
VERSION_HERE = misc.program_path('version.txt')

class GetUpdateThread(QThread):
    '''
    Used to check to see if there is an update for this program. If there is,
    then it will check to see if it the update was already downloaded. Then, it
    will prompt the GUI to either ask the user to download it or to install the
    update.
    '''
    showUpdate = pyqtSignal()
    
    def __init__(self):
        QThread.__init__(self)
        
    def run(self):
        
        # Check the version number, if I can
        gotNewOne = False
        try:
            gotNewOne = check_program_update()
        except Exception:
            print 'Couldn\'t check version number for some reason.'
        
        if gotNewOne:
            
            updateDirectory = os.path.dirname(SETUP_TEMP_FILE)
            
            # Check to see if my update directory exists
            if not os.path.isdir(updateDirectory):
                os.makedirs(updateDirectory)
                
            thisVersion = get_version_number(VERSION_HERE)
            
            # If I already got it downloaded and it is paired with the same
            # version that I just pulled, then don't re-download it.
            #
            # The version number only updates after the file has completely
            # downloaded.
            alreadyDownloaded = False
            
            if os.path.exists(SETUP_TEMP_FILE) and os.path.exists(VERSION_TEMP):
                downloadedVersion = get_version_number(VERSION_TEMP)
                if downloadedVersion > thisVersion:
                    alreadyDownloaded = True
            
            if alreadyDownloaded:
                self.showUpdate.emit()
            else:
                # Go online and grab the version number
                response = urllib2.urlopen(VERSION_THERE)
                contents = response.read()
                thereVersion = float(re.search(r'[0-9]*.[0-9]+', contents).group(0))
                
                if thereVersion > thisVersion:
#                     # Download setup file
#                     response = urllib2.urlopen(SETUP_FILE)
#                     f = open(SETUP_TEMP_FILE, 'wb')
#                     f.write(response.read())
#                     f.close()
                    
#                     # Save version number to signal I have completed transfer
#                     fv = open(VERSION_TEMP, 'w')
#                     fv.write(contents)
#                     fv.close()
                    self.showUpdate.emit()
                
def check_program_update():
    '''
    Checks to see if there is an update to this program. It pings the server for
    a version file and then compares that version number to the one here. 
    '''
    # Get the version here
    versionHere = get_version_number(VERSION_HERE)    
    
    # Get the version number there
    response = urllib2.urlopen(VERSION_THERE)
    stuff = response.read()
    versionThere = float(re.search(r'[0-9]+.[0-9]+', stuff).group(0))    
    
    return versionThere > versionHere

def is_update_downloaded():
    '''
    Says whether the update has been downloaded. Make sure to use other
    functions to check if an update does exist.
    '''
    # Check the version number in my temp and the version number on the server.
    # If they are the same, then my update has downloaded. Otherwise, no.
    try:
        versionHere = get_version_number(VERSION_TEMP)
        versionThere = urllib2.urlopen(VERSION_THERE)
        versionThere = float(re.search(r'[0-9]+.[0-9]+', versionThere.read()).group(0))
        return versionHere == versionThere
    except IOError:
        return False
    except Exception as e:
        raise e
    
def get_version_number(versionFile):
    f = open(versionFile, 'r')
    stuff = f.read()
    f.close()
    return float(re.search(r'[0-9]+.[0-9]+', stuff).group(0))

def save_server_version_to_temp():
    '''
    Downloads the version file from the update server and saves it to my temp.
    This must be called after the download has finished in order to finalize it.
    
    Returns the string contents of that version file.
    '''
    versionInfo = ''
    try:
        response = urllib2.urlopen(VERSION_THERE)
        contents = response.read()
        
        f = open(VERSION_TEMP, 'w')
        f.write(contents)
        f.close()
        
        versionInfo = contents
        
    except Exception:
        print 'ERROR: Could not save update version to temp.'
    
    return versionInfo

def run_exe(exePath):
    '''
    Runs a .exe on Windows in a 100% separate environment.
    '''
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    DETACHED_PROCESS = 0x00000008
    
    kwargs = {}
    kwargs.update(creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
    kwargs.update(close_fds=True)
    
    p = subprocess.Popen('"' + exePath + '"', **kwargs)
    
def open_dmg(dmgPath):
    '''
    Opens a .dmg in a Mac environment.
    '''
    kwargs = {}
    kwargs.update(close_fds=True)
    kwargs.update(shell=True)
    
    p = subprocess.Popen('open "' + dmgPath + '"', **kwargs)

def run_update_installer():
    '''
    This function will run the correct update installer depending on the machine
    this program is running on.
    '''
    if os.path.exists(SETUP_TEMP_FILE):
        if platform.system() == 'Windows':
            run_exe(SETUP_TEMP_FILE)
        elif platform.system() == 'Darwin':
            open_dmg(SETUP_TEMP_FILE)

# class RunUpdateInstallerThread(Thread):
#     
#     def __init__(self):
#         Thread.__init__(self)
#         self._closeUpdateSignal = None
#         
#     def setUpdateFinishSignal(self, closeFunction):
#         self._closeUpdateSignal = closeFunction
#         
#     def run(self):
#         '''
#         Runs the update installer. It will use the correct mechanisms depending on
#         the platform.
#         '''
#         run_update_installer()
#         print 'Done with update installer thread!'
#         self._closeUpdateSignal.emit()