; The name of this installer
Name "The Nifty Prose Articulator Installer"

; The output file to write
OutFile 'nifty_prose_articulator_installer.exe'

; Installation directory (like in Program Files)
InstallDir $DESKTOP\Nifty Prose Articulator

; Don't have the stupid security thing pop up by only requesting user access
RequestExecutionLevel user

; ------------------------------------------
; Sections

Section

File /r "dist\Nifty Prose Articulator"

SectionEnd

; ------------------------------------------

; The stuff to install
