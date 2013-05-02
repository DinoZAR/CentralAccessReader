# -*- mode: python -*-
a = Analysis(['src/main.py'],
             pathex=['W:\\Nifty Prose Articulator\\workspace2\\another'],
             hiddenimports=[],
             hookspath=None)
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\main', 'main.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'main'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'main.app'))
