'''
Created on Jun 21, 2013

@author: Spencer Graffe
'''
from threading import Thread
import platform
import re
import urllib2
import os
import subprocess
from src import misc

UPDATE_URL = r'http://www.cwu.edu/~atrc/centralaccessreader/'

# Get the correct setup file depending on architecture
SETUP_FILE = ''
if platform.system() == 'Windows':
    if platform.architecture()[0] == '64bit':
        SETUP_FILE = UPDATE_URL + 'CAR_Setup_64.exe'
        
SETUP_TEMP_FILE = misc.temp_path(os.path.join('update', os.path.basename(SETUP_FILE)))
VERSION_TEMP = misc.temp_path(os.path.join('update', 'version.txt'))

VERSION_THERE = UPDATE_URL + 'version.txt'
VERSION_HERE = misc.program_path('version.txt')

class GetUpdateThread(Thread):
    '''
    Used to check to see if there is an update for this program. If there is,
    then it will go ahead and download it. After it has downloaded it, it will
    then tell the GUI to display the Update button.
    '''
    
    def __init__(self, updateCallback):
        Thread.__init__(self)
        self._updateCallback = updateCallback
        
    def run(self):
        
        # Check the version number, if I can
        gotNewOne = False
        try:
            print 'Checking version number...'
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
                self._updateCallback()
            else:
                # Go online and grab the version number
                response = urllib2.urlopen(VERSION_THERE)
                contents = response.read()
                thereVersion = float(re.search(r'[0-9]*.[0-9]+', contents).group(0))
                
                if thereVersion > thisVersion:
                    # Download setup file
                    response = urllib2.urlopen(SETUP_FILE)
                    f = open(SETUP_TEMP_FILE, 'wb')
                    f.write(response.read())
                    f.close()
                    
                    # Save version number to signal I have completed transfer
                    fv = open(VERSION_TEMP, 'w')
                    fv.write(contents)
                    fv.close()
                    
                    self._updateCallback()     
        
        print 'Done checking for updates!'
                
def check_program_update():
    '''
    Checks to see if there is an update to this program. It pings the server for
    a version file and then compares that version number to the one here. 
    '''
    print 'Getting version number here...'
    # Get the version here
    versionHere = get_version_number(VERSION_HERE)
    print versionHere
    
    print 'Getting version number there...'
    # Get the version number there
    response = urllib2.urlopen(VERSION_THERE)
    stuff = response.read()
    versionThere = float(re.search(r'[0-9]+.[0-9]+', stuff).group(0))
    print versionThere
    
    return versionThere > versionHere

def get_version_number(versionFile):
    f = open(versionFile, 'r')
    stuff = f.read()
    f.close()
    return float(re.search(r'[0-9]+.[0-9]+', stuff).group(0))

class RunUpdateInstallerThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self._closeUpdateSignal = None
        
    def setUpdateFinishSignal(self, closeFunction):
        self._closeUpdateSignal = closeFunction
        
    def run(self):
        '''
        Runs the update installer. It will use the correct mechanisms depending on
        the platform.
        '''
        if os.path.exists(SETUP_TEMP_FILE):
            if platform.system() == 'Windows':
                p = subprocess.Popen('start /wait "" "' + SETUP_TEMP_FILE + '" /VERYSILENT', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p.wait()
                print 'stdout:', p.stdout.read()
                print 'stderr:', p.stderr.read()
                
        print 'Done installing new update!'
        self._closeUpdateSignal.emit()