cd src

#
# Cleanup what we had before
#
echo "Cleaning up previous build..."
rm -rf build dist

#
# Build the app
#
echo "Building the app..."
python setup_mac.py py2app

mkdir -p "./dist/Central Access Reader.app/Contents/Resources"

echo "Copying application icon file..."
cp ./icons.icns "./dist/Central Access Reader.app/Contents/Resources"

#
# JavaScript files
#
echo "Copying MathJax..."
mkdir -p "./dist/Central Access Reader.app/Contents/Resources/mathjax"
cp -R ../mathjax "./dist/Central Access Reader.app/Contents/Resources/"

echo "Copying JQuery..."
cp ../jquery-1.9.1.min.js "./dist/Central Access Reader.app/Contents/Resources/"

echo "Copying JQuery UI..."
mkdir -p "./dist/Central Access Reader.app/Contents/Resources/jquery-ui"
cp -R ../jquery-ui "./dist/Central Access Reader.app/Contents/Resources/"

echo "Copying JQuery Scroll-to..."
cp ../jquery.scrollTo-1.4.3.1-min.js "./dist/Central Access Reader.app/Contents/Resources/"

echo "Copying JavaScript functions and configurations..."
mkdir -p "./dist/Central Access Reader.app/Contents/Resources/src/javascript"
cp -R ./javascript "./dist/Central Access Reader.app/Contents/Resources/src/"

#
# Other files
#
echo "Copying the MathML pattern databases..."
mkdir -p "./dist/Central Access Reader.app/Contents/Resources/src/math_patterns"
cp -R ./math_patterns "./dist/Central Access Reader.app/Contents/Resources/src/"

echo "Copying LAME MP3 encoder..."
cp ./lame_mac "./dist/Central Access Reader.app/Contents/Resources/src/"

echo "Copying OMML to MathML XSLT..."
mkdir -p "./dist/Central Access Reader.app/Contents/Resources/src/docx"
cp ./docx/OMMLToMathML.xsl "./dist/Central Access Reader.app/Contents/Resources/src/docx/"

echo "Copying tutorial..."
cp ../Tutorial.docx "./dist/Central Access Reader.app/Contents/Resources/"

echo "Copying version file..."
cp ../version.txt "./dist/Central Access Reader.app/Contents/Resources/"

echo "Copying the DMG background..."
mkdir -p ./dist/.background
cp ./CAR_DMG_Background.png ./dist/.background

echo "Creating Application folder alias..."
ABS_DIR=`cd "$1"; pwd`
echo "Absolute path here: $ABS_DIR"

echo '
set the app_folder to POSIX file "/Applications" as alias
set the destination to the POSIX file ("'$ABS_DIR'" & "/dist") as alias
tell application "Finder"
	make new alias file at destination to app_folder
end tell
' | osascript

#
# Package it all up using the created .app
#
APP_SIZE=$(du -sk "./dist/Central Access Reader.app" | cut -d'.' -f1 | tr -d ' ')
echo "App size: $APP_SIZE kB"

echo "Creating the temporary DMG..."
hdiutil create -ov -srcfolder "./dist" -volname "Central Access Reader" -fs HFS+ -fsargs "-c c=64,a=16,e=16" -format UDRW "./dist/tmp.dmg"

echo "Modifying DMG..."
device=$(hdiutil attach -readwrite -noverify -noautoopen "./dist/tmp.dmg" | egrep '^/dev/' | sed 1q | awk '{print $1}')
echo "Mounted image address: $device"

#
# Make the DMG look nice
#
echo '
set the app_folder to the POSIX file "/Applications" as alias

tell application "Finder"
	tell disk "Central Access Reader"
		open
		
		# Make it an icon view and turn off toolbars
		set current view of container window to icon view
		set toolbar visible of container window to false
		set statusbar visible of container window to false
		
		# Set the bounds of the container
		set the bounds of container window to {0, 0, 700, 400}
		set theViewOptions to the icon view options of container window
		set arrangement of theViewOptions to not arranged
		set icon size of theViewOptions to 128
		set text size of theViewOptions to 16
		set background picture of theViewOptions to file ".background:CAR_DMG_Background.png"
		
		delay 3
		
		# Set the position and colors of the icons
		set label index of item "Central Access Reader.app" of container window to 2
		set label index of item "Applications" of container window to 2
		
		set position of file "Applications" to {500, 250}
		
		delay 3
		
		set position of file "Central Access Reader.app" to {200, 250}
		
		# Update and close out
		update without registering applications
		delay 5
		eject
	end tell
end tell
' | osascript

#
# Finalize the DMG by compressing and setting the correct permissions on it
#
sync
hdiutil convert "./dist/tmp.dmg" -format UDZO -imagekey zlib-level=9 -o "./dist/Central Access Reader.dmg"
rm -f "./dist/tmp.dmg"

echo "Moving the files to top level..."
mv "./dist/Central Access Reader.dmg" "../../../Central Access Reader.dmg"
cp ../version.txt ../../../version.txt

cd ..

echo "----------------------------------"
echo "Done!"
echo "Your file can be found as Central Access Reader Release.dmg"
echo "The version file is called version.txt"
echo "----------------------------------"