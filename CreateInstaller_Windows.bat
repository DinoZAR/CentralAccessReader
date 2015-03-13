:: Creates an installer for Windows. Here is how the command should be run:
:: CreateInstaller_Windows {debug | release}

@echo off

:: Get the SDK path in order to sign executables
setlocal EnableDelayedExpansion
CALL "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd" /x64 /release

:: Add Inno Setup and Python to my path
set PATH=%PATH%;C:\Program Files (x86)\Inno Setup 5;C:\Python27

:: Deleting
echo Deleting previous distribution folder...
RMDIR dist /S /Q

:: Generating the spec for the PyInstaller
echo Creating spec...
python generate_spec.py %1

:: Creating the executable
echo Creating executable...
python ../../pyinstaller-2.0/utils/Build.py "Central Access Reader.spec"

:: Get code signing password (now set as %password%)]
echo Enter password for PFX:
set /p "password=>"

:: Sign the executable
SignTool sign /f CARCert.pfx /p %password% "dist\Central Access Reader\Central Access Reader.exe"

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

:: JQuery NextInDOM plugin...
echo Copying JQuery NextInDOM plugin...
XCOPY nextindom.jquery.js "dist\Central Access Reader\" /D /Y /Q

:: Other Files

:: Grabbing the headless renderer
echo Copying the headless renderer...
XCOPY car\headless\phantomjs.exe "dist\Central Access Reader\car\headless\" /D /Y /Q
XCOPY car\headless\render.js "dist\Central Access Reader\car\headless\" /D /Y /Q

:: Copy the built-in math library
echo Copying the built-in math library...
XCOPY car\math_library\CAR.mathlib "dist\Central Access Reader\car\math_library\" /D /Y /Q

:: Grabbing the LAME encoder executable
echo Copying LAME MP3 encoder...
XCOPY car\lame_64.exe "dist\Central Access Reader\car\" /D /Y /Q

:: Grabbing JavaScript functions
echo Copying JavaScript functions and configurations...
XCOPY car\javascript "dist\Central Access Reader\car\javascript\" /D /Y /Q

:: Get the OMML to MathML XSLT
echo Copying OMML to MathML XSLT...
XCOPY car\document\docx\OMMLToMathML.xsl "dist\Central Access Reader\car\document\docx\" /D /Y /Q

:: Get all of the layout and themes for my GUI
echo Copying theming files...
XCOPY car\forms\theme "dist\Central Access Reader\car\forms\theme\" /S /D /Y /I /Q
XCOPY car\forms\resource_rc.py "dist\Central Access Reader\car\forms\" /D /Y /Q

:: Also getting Tutorial
echo Copying tutorial...
XCOPY Tutorial.docx "dist\Central Access Reader\" /D /Y /Q

:: Get the version file
echo Copying version file...
XCOPY version.txt "dist\Central Access Reader\" /D /Y /Q

:: Get the batch file to run CAR
echo Copying CAR runner...
XCOPY RunCARFromUpdate.bat "dist\Central Access Reader\" /D /Y /Q

:: Create the Inno Setup script
echo Creating Inno Setup script...
python generate_inno_setup_script.py 64

:: Compile Inno Setup script
echo Compiling Inno Setup script into installer...
iscc CAR_Setup.iss

:: Sign this executable too
SignTool sign /f CARCert.pfx /p %password% CAR_Setup_64.exe

:: Copy the setup file to the top of the Central Access Reader directory
echo Moving setup file to top...
move /Y CAR_Setup_64.exe ..\..\

:: Also copy the version text file to put up there too
XCOPY version.txt "..\..\" /D /Y /Q

echo ----------------------------------
echo Done!
echo Your file can be found as CAR_Setup_64.exe.
echo The version file is called version.txt
echo ----------------------------------