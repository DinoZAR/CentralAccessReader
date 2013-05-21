'''
Created on May 14, 2013

@author: Spencer Graffe
'''
import os
import argparse

NSIS_INSTALLER_FILE = 'NSIS_installer_script.nsi'
DIST_DIRECTORY = 'dist'

def remove_top_folders(path, num):
    '''
    Removes the top number of folders from a path.
    
    Ex. dist/import/stuff/test.txt would be stuff/test.txt with num=2
    '''
    folders = []
    while 1:
        path,folder=os.path.split(path)
    
        if folder != "":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)
            break
    folders.reverse()
    
    folders = folders[num:]
    
    myPath = ''
    for f in folders:
        myPath = os.path.join(myPath, f)
        
    return myPath

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates NSIS file for specific bit-ness', version='1.0')
    parser.add_argument('bit', type=int, default='64', help='either 32 or 64')
    args = parser.parse_args()
    
    outString = r'''
RequestExecutionLevel admin

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "Central Access Reader"
'''
    
    # Read in the version number from file
    versionFile = open('version.txt')
    outString += '!define PRODUCT_VERSION "' + versionFile.read() + '"\n'
    versionFile.close()
    
    outString += '''
!define PRODUCT_PUBLISHER "Central Washington University"
!define PRODUCT_WEB_SITE "http://www.cwu.edu"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\Central Access Reader.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
!define MUI_FINISHPAGE_SHOWREADME ""
!define MUI_FINISHPAGE_SHOWREADME_TEXT "Create Desktop Shortcut"
!define MUI_FINISHPAGE_SHOWREADME_FUNCTION finishpageaction

Function finishpageaction
CreateShortcut "$DESKTOP\Central Access Reader.lnk" "$INSTDIR\Central Access Reader.exe"
FunctionEnd

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!insertmacro MUI_PAGE_LICENSE "W:\Nifty Prose Articulator\workspace2\another\license.txt"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\Central Access Reader.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; Reserve files
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
'''
    if args.bit == 32:
        outString += r'''
OutFile "NPA_Setup_32.exe"
InstallDir "$PROGRAMFILES\Central Access Reader"
'''

    elif args.bit == 64:
	    outString += r'''
OutFile "NPA_Setup_64.exe"
InstallDir "$PROGRAMFILES64\Central Access Reader"
'''
    
    outString += r'''
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite try
'''
    
    # Create lines for everything in my dist folder
    # r'SetOutPath "$INSTDIR\include"'
    # r'File "W:\Nifty Prose Articulator\workspace2\another\dist\Nifty Prose Articulator\mathjax\LICENSE"'
    
    for path, dirs, files in os.walk(DIST_DIRECTORY):
        print 'Adding files from:', path
        outString += 'SetOutPath "' + os.path.join('$INSTDIR', remove_top_folders(path, 2)) + '"\n'
        for f in files:
            outString += 'File "' + os.path.join(os.path.abspath(path), f) + '"\n'
    
    # Add more stuff
    outString += r'''
    CreateShortcut "$SMPROGRAMS\Central Access Reader.lnk" "$INSTDIR\Central Access Reader.exe"
SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\Central Access Reader\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\Central Access Reader.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\Central Access Reader.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

Section Uninstall 

RMDir /r $INSTDIR
Delete "$SMPROGRAMS\Central Access Reader.lnk"
Delete "$SMPROGRAMS\Central Access Reader\Uninstall.lnk"
Delete "$DESKTOP\Central Access Reader.lnk"

DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd 
'''
    
    # Write out my stuff to NSIS file
    f = open(NSIS_INSTALLER_FILE, 'w')
    f.write(outString)
    f.close()
