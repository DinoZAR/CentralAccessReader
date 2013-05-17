# -*- mode: python -*-

a = Analysis(['src/main.py'],
             pathex=['W:\\Nifty Prose Articulator\\workspace2\\another'],
             hiddenimports=[],
             hookspath=None)
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\Nifty Prose Articulator', 'Nifty Prose Articulator.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
			   Tree(os.path.abspath('src/forms/icons')),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'Nifty Prose Articulator'))
app = BUNDLE(coll,
             name=os.path.join('dist', 'Nifty Prose Articulator.app'))
