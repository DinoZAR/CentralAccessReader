'''
Created on Jan 21, 2013

@author: Spencer Graffe
'''

def main():
    print 'Starting Central Access Reader...'

    import sys
    import os
    
    # Because we have local stuff, we need to append this local directory
    # to the Python path
    #sys.path.append(os.path.abspath('..'))
    
    from PySide.QtGui import QApplication, QPixmap, QSplashScreen
    app = QApplication(sys.argv)
      
    # Create a splash screen
    from forms import resource_rc
    pixmap = QPixmap(':/icons/icons/CAR Splash.png')
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    
    # Check to see if my folders in my paths exist. If they don't, make them
    from misc import program_path, app_data_path, temp_path
    
    if not os.path.exists(os.path.dirname(program_path('test.txt'))):
        os.makedirs(os.path.dirname(program_path('test.txt')))
    if not os.path.exists(os.path.dirname(app_data_path('test.txt'))):
        os.makedirs(os.path.dirname(app_data_path('test.txt')))
    if not os.path.exists(os.path.dirname(temp_path('test.txt'))):
        os.makedirs(os.path.dirname(temp_path('test.txt')))
    
    from gui.main_window import MainWindow
    
    window = MainWindow(app)
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
