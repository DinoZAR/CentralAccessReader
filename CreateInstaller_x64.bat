@echo off

:: Add Inno Setup and Python to my path
set PATH=%PATH%;C:\Program Files (x86)\Inno Setup 5;C:\Python27

:: Deleting
echo Deleting previous distribution folder...
RMDIR dist /S /Q

:: Generating the spec for the PyInstaller
echo Creating spec...
python generate_spec.py

:: Creating the executable
echo Creating executable...
python ../../pyinstaller-2.0/utils/Build.py "Central Access Reader.spec"

:: Importing my external JavaScript libraries

:: MathJax
echo Copying MathJax...
XCOPY mathjax "dist\Central Access Reader\mathjax\" /S /D /Y /I /Q

:: JQuery
echo Copying JQuery...
XCOPY jquery-1.9.1.min.js "dist\Central Access Reader\" /D /Y /Q

:: JQuery UI
echo Copying JQuery UI...
XCOPY jquery-ui "dist\Central Access Reader\jquery-ui\" /S /D /Y /I /Q

:: JQuery Scroll-To
echo Copying JQuery Scroll-to...
XCOPY jquery.scrollTo-1.4.3.1-min.js "dist\Central Access Reader\" /D /Y /Q

:: Other Files

:: Copy the pattern databases
echo Copying the MathML pattern databases...
XCOPY src\math_patterns "dist\Central Access Reader\src\math_patterns\" /S /D /Y /I /Q

:: Grabbing the LAME encoder executable
echo Copying LAME MP3 encoder...
XCOPY src\lame_64.exe "dist\Central Access Reader\src\" /D /Y /Q

:: Grabbing JavaScript functions
echo Copying JavaScript functions and configurations
XCOPY src\docx\mathjax_config.js "dist\Central Access Reader\src\docx\" /D /Y /Q
XCOPY src\docx\my_functions.js "dist\Central Access Reader\src\docx\" /D /Y /Q

:: Get the OMML to MathML XSLT
echo Copying OMML to MathML XSLT...
XCOPY src\docx\OMMLToMathML.xsl "dist\Central Access Reader\src\docx\" /D /Y /Q

:: Also getting Tutorial
echo Copying tutorial...
XCOPY Tutorial.docx "dist\Central Access Reader\" /D /Y /Q

:: Get the version file
echo Copying version file...
XCOPY version.txt "dist\Central Access Reader\" /D /Y /Q

:: Create the Inno Setup script
echo Creating Inno Setup script...
python generate_inno_setup_script.py 64

:: Compile Inno Setup script
echo Compiling Inno Setup script into installer...
iscc CAR_Setup.iss

:: Copy the setup file to the top of the Central Access Reader directory
echo Moving setup file to top...
move /Y CAR_Setup_64.exe ../../

echo ----------------------------------
echo Done!
echo Your file can be found as CAR_Setup_64.exe.
echo ----------------------------------