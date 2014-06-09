#
# Setting up the environment
#
echo "Setting up the environment..."
export PATH=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/:/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/:$PATH
echo $PATH

#
# Cleanup what we had before
#
echo "Cleaning up previous build..."
rm -rf ./build
rm -rf ./dist
sleep 2

#
# Build the app
#
echo "Building the app..."
python setup_mac.py py2app

APP_DIR="./dist/Central Access Reader.app/Contents/Resources";

mkdir -p "$APP_DIR"

echo "Copying application icon file..."
cp ./icons.icns "$APP_DIR"

#
# JavaScript files
#
echo "Copying MathJax..."
mkdir -p "$APP_DIR/mathjax"
cp -R ./mathjax "$APP_DIR/"

echo "Copying JQuery..."
cp ./jquery-1.9.1.min.js "$APP_DIR/"

echo "Copying JQuery UI..."
mkdir -p "$APP_DIR/jquery-ui"
cp -R ./jquery-ui "$APP_DIR/"

echo "Copying JQuery Scroll-to..."
cp ./jquery.scrollTo-1.4.3.1-min.js "$APP_DIR/"

echo "Copying JQuery Next In DOM..."
cp ./nextindom.jquery.js "$APP_DIR/"

echo "Copying JavaScript functions and configurations..."
mkdir -p "$APP_DIR/car/javascript"
cp -R ./car/javascript "$APP_DIR/car/"

#
# GUI forms
#
echo "Copying themes..."
mkdir -p "$APP_DIR/car/forms/theme"
cp -R ./car/forms/theme "$APP_DIR/car/forms/"

echo "Copying resource file..."
cp ./car/forms/resource_rc.py "$APP_DIR/car/forms/"

#
# Other files
#
echo "Copying files for the headless renderer..."
mkdir -p "$APP_DIR/car/headless"
chmod +x ./car/headless/phantomjs_mac
cp ./car/headless/phantomjs_mac "$APP_DIR/car/headless/"
cp ./car/headless/render.js "$APP_DIR/car/headless/"

echo "Make small revision to the Qt image plugins folder..."
mv "$APP_DIR/qt_pluginst4/plugins" "$APP_DIR/qt_plugins"

echo "Copying the MathML built-in libraries..."
mkdir -p "$APP_DIR/car/math_library"
cp -R ./car/math_library "$APP_DIR/car/"

echo "Copying LAME MP3 encoder..."
chmod +x ./car/lame_mac
cp ./car/lame_mac "$APP_DIR/car/"

echo "Copying OMML to MathML XSLT..."
mkdir -p "$APP_DIR/car/document/docx"
cp ./car/document/docx/OMMLToMathML.xsl "$APP_DIR/car/document/docx/"

echo "Copying tutorial..."
cp ./Tutorial.docx "$APP_DIR/"

echo "Copying version file..."
cp ./version.txt "$APP_DIR/"

echo "Copying the DMG background..."
mkdir -p ./dist/.background
cp ./car/CAR_DMG_Background.png ./dist/.background

echo "Creating Application folder alias..."
ABS_DIR=`cd "$1"; pwd`
echo '
set the app_folder to POSIX file "/Applications" as alias
set the destination to the POSIX file ("'$ABS_DIR'" & "/dist") as alias
tell application "Finder"
	make new alias file at destination to app_folder
end tell
' | osascript

#
# Sign the app bundle
#

# Frameworks
for f in dist/Central\ Access\ Reader.app/Contents/Frameworks/*.framework
do
    codesign -s "Central Washington University" -v "$f"
done

# Executables
for f in dist/Central\ Access\ Reader.app/Contents/MacOS/*
do
    codesign -s "Central Washington University" -v "$f"
done

# App bundle
codesign -s "Central Washington University" -v "./dist/Central Access Reader.app"

#
# Package it all up using the created .app
#
APP_SIZE=$(du -sk "./dist/Central Access Reader.app" | cut -d'.' -f1 | tr -d ' ')
echo "App size: $APP_SIZE kB"

echo "Creating the temporary DMG..."
hdiutil create -ov -srcfolder "./dist" -volname "Central Access Reader" -format UDRW "./dist/tmp.dmg"

echo "Modifying DMG..."
hdiutil attach -readwrite -noverify -noautoopen "./dist/tmp.dmg"

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
		
		# Set the position and colors of the icons
		set position of file "Applications" to {500, 250}
		set position of file "Central Access Reader.app" to {200, 250}
		
		# Update and eject
		update without registering applications
		
		# Have to do this so that icon positions are correctly updated
		close
		open
		
		delay 5
		eject
	end tell
end tell
' | osascript

#
# Finalize the DMG by compressing and setting the correct permissions on it
#
sync
hdiutil convert "./dist/tmp.dmg" -format UDBZ -o "./dist/Central_Access_Reader.dmg"
rm -f "./dist/tmp.dmg"

#
# Sign the image
#
codesign -s "Central Washington University" -v "./dist/Central_Access_Reader.dmg"

echo "Moving the files to top level..."
mv "./dist/Central_Access_Reader.dmg" "../../Central_Access_Reader.dmg"
cp ./version.txt ../../version.txt

echo "----------------------------------"
echo "Done!"
echo "Your file can be found as Central_Access_Reader.dmg"
echo "The version file is called version.txt"
echo "----------------------------------"