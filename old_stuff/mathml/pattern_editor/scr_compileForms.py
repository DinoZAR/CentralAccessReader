'''
Created on Jun 17, 2012

All it does is it visits the forms package and compiles all of the .ui and .qrc 
files to Python files using a standard naming convention. It saves me the 
trouble of having to compile every change I make to each file individually, 
which is quite error-prone. The script will also skip over the .ui and .qrc 
files that have corresponding .py that are newer than itself.

@author: Spencer Graffe
'''

import os
from subprocess import check_output
from PyQt4 import uic

def main():
    
    print 'Finding forms and resources to compile...'
    
    mydir = os.path.join(os.getcwd(), 'forms/')
    
    for file in os.listdir(mydir):
        
        nameExt = os.path.splitext(file)
        
        # Use pyuic4 to compile the said file, that is if the corresponding .py file hasn't been created or
        # is older than the .ui file
        if nameExt[1] == '.ui':
            lastTime = os.path.getmtime(os.path.join(mydir, file))
            
            # Check to see if corresponding py file exists
            pyExportName = nameExt[0] + '_ui.py'
            if os.path.exists(os.path.join(mydir, pyExportName)):
                lastTime2 = os.path.getmtime(os.path.join(mydir, pyExportName))
                if lastTime2 < lastTime:
                    print 'Compiling', file
                    pyfile = open(os.path.join(mydir, pyExportName), 'w')
                    uic.compileUi(os.path.join(mydir, file), pyfile)
            
            else:
                print 'Compiling', file
                pyfile = open(os.path.join(mydir, pyExportName), 'w')
                uic.compileUi(os.path.join(mydir, file), pyfile)
                
        # Do the same routine here for the resource files.
        if nameExt[1] == '.qrc':
            lastTime = os.path.getmtime(os.path.join(mydir, file))
            
            # Check to see if corresponding py file exists
            pyExportName = nameExt[0] + '_rc.py'
            if os.path.exists(os.path.join(mydir, pyExportName)):
                lastTime2 = os.path.getmtime(os.path.join(mydir, pyExportName))
                if lastTime2 < lastTime:
                    print 'Compiling resource', file
                    data = check_output(['pyrcc4', os.path.join(mydir, file)])
                    pyfile = open(os.path.join(mydir, pyExportName), 'wb')
                    pyfile.write(data)
                    pyfile.close()
            
            else:
                print 'Compiling resource', file
                data = check_output(['pyrcc4', os.path.join(mydir, file)])
                pyfile = open(os.path.join(mydir, pyExportName), 'wb')
                pyfile.write(data)
                pyfile.close()
    
    print 'Done!'
    
if __name__ == '__main__':
    main()