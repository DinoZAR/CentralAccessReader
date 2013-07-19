'''
Created on Jul 10, 2013

@author: Spencer Graffe
'''
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

# Make sure these are in least-dependent order
ext_modules = [Extension('parser', ['parser.pyx']),
               Extension('pattern_tree', ['pattern_tree.pyx']),
               Extension('database', ['database.pyx'])]
setup(
      name = 'MathML Parser',
      cmdclass = {'build_ext' : build_ext},
      include_dirs = [np.get_include()],
      ext_modules = ext_modules
      )
