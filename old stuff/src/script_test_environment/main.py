'''
Created on Apr 1, 2013

@author: Spencer Graffe
'''
import sys
import os
from PyQt4.QtGui import QApplication

# Because we have local stuff, we need to append this local directory
# to the Python path
sys.path.append(os.path.abspath('..'))

from src.script_test_environment.gui.main_window import MainWindow

def main():
    
    print 'Running script testing environment...'
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
