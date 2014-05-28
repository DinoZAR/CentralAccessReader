'''
@author: Spencer Graffe
'''
import os

from src.math_library.library import MathLibrary
from src.misc import program_path, app_data_path

BUILTIN_DIR = program_path('src/math_library/')
CUSTOM_DIR = app_data_path('math_libraries/')

def getLibraries():
    '''
    Returns a list of MathLibrary's, both from the built-in ones and the custom
    ones.
    '''

    libraries = []

    if not os.path.exists(CUSTOM_DIR):
        os.makedirs(CUSTOM_DIR)

    for f in os.listdir(BUILTIN_DIR):
        ext = os.path.splitext(f)[1]
        if ext == '.mathlib':
            lib = MathLibrary()
            lib.read(os.path.join(BUILTIN_DIR, f))
            lib.builtIn = True
            libraries.append(lib)

    for f in os.listdir(CUSTOM_DIR):
        ext = os.path.splitext(f)[1]
        if ext == '.mathlib':
            lib = MathLibrary()
            lib.read(os.path.join(CUSTOM_DIR, f))
            libraries.append(lib)

    return libraries

def saveCustomLibrary(mathLibFilePath):
    '''
    Saves the custom library to the user's private collection.
    '''

    fileName = os.path.basename(mathLibFilePath)

    if not os.path.exists(CUSTOM_DIR):
        os.makedirs(CUSTOM_DIR)

    with open(os.path.join(CUSTOM_DIR, fileName), 'w') as f:
        with open(mathLibFilePath, 'r') as f2:
            f.write(f2.read())