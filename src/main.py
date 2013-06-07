'''
Created on Jan 21, 2013

@author: Spencer
'''
import sys
import os
from PyQt4.QtGui import QApplication

# Because we have local stuff, we need to append this local directory
# to the Python path
sys.path.append(os.path.abspath('..'))

from src.misc import program_path, app_data_path, temp_path

from src.gui.main_window import MainWindow

def main():
    
    print 'Starting Central Access Reader...'
    
    # Check to see if my folders in my different paths exist. If they don't,
    # make them
    if not os.path.exists(os.path.dirname(program_path('test.txt'))):
        os.makedirs(os.path.dirname(program_path('test.txt')))
    if not os.path.exists(os.path.dirname(app_data_path('test.txt'))):
        os.makedirs(os.path.dirname(app_data_path('test.txt')))
    if not os.path.exists(os.path.dirname(temp_path('test.txt'))):
        os.makedirs(os.path.dirname(temp_path('test.txt')))
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()