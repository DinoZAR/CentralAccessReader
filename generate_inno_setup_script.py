'''
Created on June 24, 2013

@author: Spencer Graffe
'''
import os

INNO_SETUP_SCRIPT = 'CAR_Setup.iss'
DIST_DIRECTORY = 'dist\\Central Access Reader\\'

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

    outString = r'''
#define MyAppName "Central Access Reader"
'''

    # Add my version number
    f = open(os.path.abspath('version.txt'), 'r')
    version = f.read()
    f.close()

    outString += r'#define MyAppVersion "' + version + '"'
    
    outString += '''
#define MyAppPublisher "Central Washington University"
#define MyAppURL "http://www.cwu.edu/"
#define MyAppExeName "Central Access Reader.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{AD36ACE8-D0F9-440B-B1EB-10509674E34B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DisableDirPage=yes
DefaultGroupName={#MyAppName}
'''

    # Get the path of my license file
    path = os.path.abspath('license.txt')
    outString += 'LicenseFile=' + path + '\n'

    outString += '''OutputBaseFilename=CAR_Setup_64
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
ArchitecturesAllowed=x64
OutputDir=.
SetupIconFile=''' + os.path.abspath(os.path.join(DIST_DIRECTORY, 'CAR_Logo.ico')) + '''
UninstallIconFile=''' + os.path.abspath(os.path.join(DIST_DIRECTORY, 'CAR_Logo.ico')) + '''

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
'''

    # Get my files and directories from my distribution folder
    files = []
    directories = []
    print 'Reading directories...'
    for path, dirs, fls in os.walk(DIST_DIRECTORY):
        directories.append(path)
        for f in fls:
            files.append((os.path.join(os.path.abspath(path), f), path))

    # Files, add the following
    # Source: "<full path>"; DestDir: "{app}\<some folder>"; Flags: ignoreversion
    print 'Adding files...'
    for t in files:
        f = t[0]
        d = t[1]
        outString += 'Source: "' + f + '"; DestDir: "' + d.replace(DIST_DIRECTORY, '{app}\\') + '"; Flags: ignoreversion'
        outString += '\n'

    outString += r'''
[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Dirs]
'''

    # Directories, add the following
    # Name: "{app}\src"
    print 'Adding directories...'
    for d in directories:
        outString += 'Name: "' + d.replace(DIST_DIRECTORY, '{app}\\') + '"'
        outString += '\n'

    # Write it out to file
    f = open(INNO_SETUP_SCRIPT, 'w')
    f.write(outString)
    f.close()
    
