'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
import os
import platform
if __name__ == '__main__':
    
    
    myRoot = 'Nifty Prose Articulator'
    myFile = 'stuff.txt'
    
    if 'Windows' in platform.system():
        print 'App Data:', os.path.join(os.path.join(os.environ['APPDATA'], myRoot), myFile)
        print 'Temp:', os.path.join(os.path.join(os.environ['TEMP'], myRoot), myFile)