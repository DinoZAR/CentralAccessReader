
# -*- mode: python -*-

a = Analysis(['src/main.py'],
             pathex=['W:\\Nifty Prose Articulator\\workspace\\nifty-prose-articulator'],
             hiddenimports=[],
             hookspath=None)
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\pyi.win32\Central Access Reader', 'Central Access Reader.exe'),
          debug=False,
          console=False,
          strip=None,
          upx=False,
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
