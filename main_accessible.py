'''

Starts up the more accessible version of the Central Access Reader,
specifically designed for screen reader/keyboard use.

@author: Spencer Graffe
'''

def main():
    print 'Starting Central Access Reader...'

    import sys
    import os

    from PyQt5.QtWidgets import QApplication

    # Necessary to make drawing fast enough on Macs
    #QApplication.setGraphicsSystem('raster')

    app = QApplication(sys.argv)

    # # Create a splash screen
    # from PyQt5.QtGui import QPixmap
    # from car.forms import resource_rc  # Needed to load image from resource file
    # pixmap = QPixmap(':/all/icons/CAR Splash.png')
    # splash = QSplashScreen(pixmap)
    # splash.show()
    # app.processEvents()

    # Check to see if my folders in my paths exist. If they don't, make them
    from car.misc import program_path, app_data_path, temp_path

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
    from car.gui import configuration
    configuration.load(app_data_path('configuration.xml'))

    # Write out the CSS that styles all of the documents
    stylePath = temp_path('import/defaultStyle.css')
    if not os.path.exists(os.path.dirname(stylePath)):
        os.makedirs(os.path.dirname(stylePath))
    with open(stylePath, 'w') as f:
        f.write(configuration.getCSS())

    # # Set the theme for CAR
    # from car.gui import loader
    # loader.load_theme(app, configuration.getValue('Theme', 'Crimson'))

    # Show the main window
    from car.gui_accessible.main_window import MainWindow

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    print 'Done!'

    # from car.gui.main_window import MainWindow
    #
    # window = MainWindow(app)
    # window.show()
    # splash.finish(window)
    # sys.exit(app.exec_())

if __name__ == '__main__':
    main()