'''
Created on Apr 1, 2013

@author: Spencer Graffe
'''
import sys
import os
from PyQt4.QtGui import QApplication

from script_test_environment.gui.main_window import MainWindow

def main():
    
    print 'Running script testing environment...'
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
