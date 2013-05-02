# -*- mode: python -*-

a = Analysis(['src/main.py'],
             pathex=['W:\\Nifty Prose Articulator\\workspace2\\another'],
             hiddenimports=[],
             hookspath=None)

# Find all of my icons
print '-------------------------------------------------------------'
print 'STARTING MY OWN NIFTY STUFF!'

import os
from glob import glob

extra_files = []
    
# Get my icons
#iconPath = os.path.abspath('src/forms/icons')
#print 'Icons folder:', iconPath
#iconFiles = glob(os.path.join(iconPath, '*.png'))
#print iconFiles
    
#extra_files.extend(iconFiles)
    
# Get my MathML pattern database
#mathDatabasePath = os.path.abspath('src/mathml/parser_pattern_database.txt')
#print 'MathML database:', mathDatabasePath
    
#extra_files.append(mathDatabasePath)
    
# Get OMML to MathML stylesheet
#ommlStylesheet = os.path.abspath('src/docx/OMMLToMathML.xsl')

#extra_files.append(ommlStylesheet)
    
# Get the JavaScript responsible for handling my views
#javascriptsPath = os.path.abspath('src/docx')
#jsFiles = glob(os.path.join(javascriptsPath, '*.js'))
#print 'JavaScript path:', javascriptsPath
#print jsFiles
    
#extra_files.extend(jsFiles)
    
# get JQuery
#jqueryPath = os.path.abspath('jquery-1.9.1.min.js')
#print 'JQuery:', jqueryPath
    
#extra_files.append(jqueryPath)
    
# Get the MathJax library
#mathjaxRoot = os.path.abspath('mathjax')
#mathjaxFiles = []
#print 'MathJax:', mathjaxRoot
#for root, dirs, files in os.walk(mathjaxRoot):
#    if len(files) > 0:
#        for f in files:
#            mathjaxFiles.append(os.path.join(root, f))

#extra_files.extend(mathjaxFiles)

#print 'Converting to installer tuples...'
#installerTuples = []
#for f in extra_files:
#    installerTuples.append((f, f, 'DATA'))

print 'END OF MY NIFTY STUFF!'
print '-------------------------------------------------------------'
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\Nifty Prose Articulator', 'Nifty Prose Articulator.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
			   Tree(os.path.abspath('src/forms/icons')),
			   Tree(os.path.abspath('src/docx')),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'Nifty Prose Articulator'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'Nifty Prose Articulator.app'))
