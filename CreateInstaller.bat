@echo off

:: Creating the executable
echo Creating executable...
python ../../pyinstaller-2.0/utils/Build.py "Nifty Prose Articulator.spec"

:: Importing my external JavaScript libraries

:: MathJax
echo Copying MathJax...
XCOPY mathjax "dist\Nifty Prose Articulator\mathjax\" /S /D /Y /I

:: JQuery
echo Copying JQuery...
XCOPY jquery-1.9.1.min.js "dist\Nifty Prose Articulator\" /D /Y