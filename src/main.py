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

from src.gui.main_window import MainWindow

def main():
    
    print 'Starting Nifty Prose Articulator...'
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
