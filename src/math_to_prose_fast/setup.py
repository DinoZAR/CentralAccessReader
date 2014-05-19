'''
Created on Jul 10, 2013

@author: Spencer Graffe
'''
import os
import sys
from distutils.core import setup
from distutils.extension import Extension
import numpy as np

# we'd better have Cython installed, or it's a no-go
try:
    from Cython.Distutils import build_ext
except:
    print "You don't seem to have Cython installed. Please get a"
    print "copy from www.cython.org and install it"
    sys.exit(1)

# Scan the 'mathml_fast' directory for extension files. Returns a list of tuples
# of the following:
#
# (moduleName, moduleFilePath)
#
# The moduleName is the name given to the module on compilation. When you
# import the module, you use that specific name.
#
# For the moduleFilePath, that is the absolute path of where the actual file
# is at.
def scandir(directory, top_dir, files=[],):
    for f in os.listdir(directory):
        p = os.path.join(directory, f)
        if os.path.isfile(p) and p.endswith(".pyx"):
            
            # Create the name of the module using the path
            index = p.index(top_dir) + len(top_dir) + 1
            name = os.path.splitext(p[index:])[0]
            name = name.replace(os.sep, '.')
            
            files.append([name, p])
            
        elif os.path.isdir(p):
            scandir(p, top_dir, files)
            
    return files    

# Generate an Extension object from an extension tuple
def makeExtension(extTuple):
    return Extension(
        extTuple[0],
        [extTuple[1]],
        include_dirs = ['.'],   # adding the '.' to include_dirs is CRUCIAL!
        )
    
# Get a list of my extensions in my directory
topDir = os.path.basename(os.path.abspath('./'))
extTuples = scandir(os.path.abspath('./'), topDir)
print 'My extension tuples:', extTuples

# Make extension object from them
extensions= [makeExtension(t) for t in extTuples]
 
setup(
      name = 'Math to Prose Engine',
      packages=['math_to_prose_fast'],
      cmdclass = {'build_ext' : build_ext},
      include_dirs = [np.get_include()],
      ext_modules = extensions
      )