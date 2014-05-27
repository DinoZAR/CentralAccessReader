'''
Created on Jan 21, 2013

@author: Spencer Graffe
'''

def main():
    print 'Starting Central Access Reader...'

    import sys
    import os
     
    # Append the parent of this file so that my paths are correct when running
    # it from command-line
    from PyQt4.QtGui import QApplication, QPixmap, QSplashScreen 
     
    QApplication.setGraphicsSystem('raster')
     
    app = QApplication(sys.argv)
     
    # Create a splash screen
    from forms import resource_rc
    pixmap = QPixmap(':/all/icons/CAR Splash.png')
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
      
    # Check to see if my folders in my paths exist. If they don't, make them
    from src.misc import program_path, app_data_path, temp_path
      
    if not os.path.exists(os.path.dirname(program_path('test.txt'))):
        os.makedirs(os.path.dirname(program_path('test.txt')))
    if not os.path.exists(os.path.dirname(app_data_path('test.txt'))): 
        os.makedirs(os.path.dirname(app_data_path('test.txt')))
    if not os.path.exists(os.path.dirname(temp_path('test.txt'))):
        os.makedirs(os.path.dirname(temp_path('test.txt')))
          
    # Clear out all items in temp folder
    for path, dirnames, filenames in os.walk(temp_path('')):
        for f in filenames:
            os.remove(os.path.join(path, f))
      
    # Load and set default values for the configuration
    from src.gui import configuration
    configuration.load(app_data_path('configuration.xml'))
      
    # Set the default math database. If it has already been set, this caches it.
    configuration.setMathDatabase('MathDatabase', configuration.getValue('MathDatabase', 'General'))
      
    # Write out the CSS that styles all of the documents
    if not os.path.exists(os.path.dirname(temp_path('import/test.css'))):
        os.makedirs(os.path.dirname(temp_path('import/test.css')))
    with open(temp_path('import/defaultStyle.css'), 'w') as f:
        f.write(configuration.getCSS())
      
    # Set the theme for CAR
    from src.gui import loader
    loader.load_theme(app, configuration.getValue('Theme', 'Crimson'))
      
    from src.gui.main_window import MainWindow
      
    window = MainWindow(app)
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
