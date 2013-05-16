@echo off

:: Add NSIS and Python to my path
set PATH=%PATH%;C:\Program Files (x86)\NSIS;C:\Python27

:: Deleting temp files and configuration files
echo Deleting temporary files and configurations...
DEL src\configuration.xml
echo import folder...
RMDIR src\import /S /Q
DEL src\tmp.wav
DEL src\ttsSettings.txt

:: Delete previous distribution folder
echo dist folder...
RMDIR dist /S /Q

:: Creating the executable
echo Creating executable...
python ../../pyinstaller-2.0/utils/Build.py "Nifty Prose Articulator.spec"

:: Importing my external JavaScript libraries

:: MathJax
echo Copying MathJax...
XCOPY mathjax "dist\Nifty Prose Articulator\mathjax\" /S /D /Y /I /Q

:: JQuery
echo Copying JQuery...
XCOPY jquery-1.9.1.min.js "dist\Nifty Prose Articulator\" /D /Y /Q

:: JQuery UI
echo Copying JQuery UI...
XCOPY jquery-ui "dist\Nifty Prose Articulator\jquery-ui\" /S /D /Y /I /Q

:: JQuery Scroll-To
echo Copying JQuery Scroll-to...
XCOPY jquery.scrollTo-1.4.3.1-min.js "dist\Nifty Prose Articulator\" /D /Y /Q

:: Other Files

:: Grabbing the LAME encoder executable
echo Copying LAME MP3 encoder...
XCOPY src\lame.exe "dist\Nifty Prose Articulator\" /D /Y /Q

:: Also getting Tutorial
echo Copying tutorial...
XCOPY src\Tutorial.docx "dist\Nifty Prose Articulator\" /D /Y /Q

:: Create the NSIS script
echo Creating NSIS script...
python generate_nsis_script.py

:: Compile NSIS script
echo Compiling NSIS script into installer...
makensis /V4 NSIS_installer_script.nsi

:: Copy the setup file to the top of the Nifty Prose Articulator directory
echo Moving setup file to top...
move /Y NPA_Setup.exe ../../

echo ----------------------------------
echo Done!
echo Your file can be found as NPA_Setup.exe.
echo ----------------------------------