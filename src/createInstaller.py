'''
Created on Apr 30, 2013

@author: Spencer Graffe
'''
import os
import subprocess

if __name__ == '__main__':
    
    # Create the .exe
    pyinstallerPath = os.path.abspath('../../../pyinstaller-2.0/pyinstaller.py')
    mainFilePath = os.path.abspath('main.py')
    
    print 'PyInstaller:', pyinstallerPath
    print 'Main File Path:', mainFilePath
    
    exeCommand = 'python "' + pyinstallerPath + '" --onedir --noconsole "' + mainFilePath + '"'
    
    print 'Executing:', exeCommand
    
    ps = subprocess.Popen(exeCommand)
    
    ps.wait()
    
    print '---------------------------------------'
    print 'Done!'
    print '---------------------------------------'