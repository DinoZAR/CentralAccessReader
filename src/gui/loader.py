'''
Created on Nov 29, 2013

Contains functions for loading the GUI for different themes and layout styles.

@author: Spencer Graffe
'''
import os
import sys
from PyQt4 import uic
from misc import program_path

# Add the resource_rc to the Python path
sys.path.append(program_path('src/forms/'))

# Used when one could pick multiple layout types. We have settled on the New
# layout since then.
#
# def get_layouts():
#     '''
#     Gets a list of all of the possible layout names. The names in this list are
#     used directly in the load_ui() function.
#     '''
#     return [name for name in os.listdir(program_path('src/forms/layout'))
#             if os.path.isdir(os.path.join(program_path('src/forms/layout'), name))]

# def load_ui(uiFile, layoutType):
#     '''
#     Loads the correct UI object for the layout. The UI object can then be used
#     to setup the UI for the window.
#     '''
#     p = program_path('src/forms/layout/' + layoutType + '/' + uiFile)
#     return uic.loadUiType(p)[0]()

def get_themes():
    '''
    Gets a list of all the possible list themes. The list returned is used
    directly with load_theme() to load the right theme at startup.
    '''
    return [os.path.splitext(name)[0] for name in os.listdir(program_path('src/forms/theme'))
            if os.path.isfile(os.path.join(program_path('src/forms/theme'), name))]

def load_theme(app, themeName):
    '''
    Loads the theme into the application. 
    '''
    with open(program_path('src/forms/theme/' + themeName + '.css'), 'r') as f:
        app.setStyleSheet(f.read())