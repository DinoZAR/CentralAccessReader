import os

SPEC_DIRECTORY = os.path.abspath('./Central Access Reader.spec')
PATH_EXTENSION = os.path.abspath('./')

if __name__ == '__main__':

    print 'Saving spec to:', SPEC_DIRECTORY
    print 'Path extension:', PATH_EXTENSION

    outString = r'''
# -*- mode: python -*-

a = Analysis(['src/main.py'],
             pathex=[''' + '\'' + PATH_EXTENSION.replace('\\', '\\\\') + '\'' + '''],
             hiddenimports=[],
             hookspath=None)
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\Central Access Reader', 'Central Access Reader.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon=os.path.normpath('src/forms/icons/CAR_Logo.ico') )
coll = COLLECT(exe,
			   Tree(os.path.abspath('src/forms/icons')),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'Central Access Reader'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'Central Access Reader.app'))
'''

    f = open(SPEC_DIRECTORY, 'w')
    f.write(outString)
    f.close()
