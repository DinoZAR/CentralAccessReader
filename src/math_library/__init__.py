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
            lib = MathLibrary(os.path.join(BUILTIN_DIR, f))
            lib.builtIn = True
            libraries.append(lib)

    for f in os.listdir(CUSTOM_DIR):
        ext = os.path.splitext(f)[1]
        if ext == '.mathlib':
            lib = MathLibrary(os.path.join(CUSTOM_DIR, f))
            libraries.append(lib)

    return libraries

def getLibraryFromPath(path):
    '''
    Returns a (MathLibrary, MathPattern) tuple with the given path. The path
    should be a list of strings defining the path to a particular pattern.

    Note: For now, the list should only have 2 items, the first the name of
    the math library, the second the name of the pattern.
    '''
    libs = getLibraries()

    libName = path.pop(0)
    myLib = None
    for l in libs:
        if libName == l.name:
            myLib = l
            break

    patternName = path.pop(0)
    myPattern = None
    for p in myLib.patterns:
        if patternName == p.name:
            myPattern = p
            break

    return (myLib, myPattern)

def saveCustomLibrary(mathLibFilePath, replace=False):
    '''
    Saves the custom library to the user's private collection. If the name of
    the library exists in the collection, it will return the offending
    MathLibrary. If replace is set, then it will replace it.

    Returns None if replace was successful.
    '''

    fileName = os.path.basename(mathLibFilePath)

    if not os.path.exists(CUSTOM_DIR):
        os.makedirs(CUSTOM_DIR)

    # Check to see if the library with the same name already exists
    myLib = MathLibrary(mathLibFilePath)
    for lib in getLibraries():
        if myLib.name == lib.name:
            if lib.builtIn:
                raise ValueError('{0} is the name of a built-in library, which cannot be replaced.'.format(lib.name))
            if not replace:
                return lib
            else:
                os.remove(lib.filePath)

    with open(mathLibFilePath, 'rb') as f1:
        with open(os.path.join(CUSTOM_DIR, fileName), 'wb') as f2:
            f2.write(f1.read())

    return None

def removeLibrary(mathLibName):
    '''
    Removes the library from the user's custom library list.
    '''

    if not os.path.exists(CUSTOM_DIR):
        os.makedirs(CUSTOM_DIR)

    for lib in getLibraries():
        if lib.name == mathLibName:
            if lib.builtIn:
                raise ValueError('{0} is a built-in library that can\'t be removed.'.format(lib.name))
            os.remove(lib.filePath)
            break