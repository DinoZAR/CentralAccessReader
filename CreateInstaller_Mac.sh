cd src

# Cleanup what we had before
echo "Cleaning up previous build..."
rm -rf build dist

echo "Building the app..."
python setup_mac.py py2app

mkdir -p "./dist/Central Access Reader.app/Contents/Resources"

echo "Copying application icon file..."
cp ./icons.icns "./dist/Central Access Reader.app/Contents/Resources"

# JavaScript files

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

# Other files
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

# Package it all up using the created "dist" folder
#echo "Creating package..."
#pkgbuild --identifier com.cwu.centralaccessreader --version 1.02 --root ./dist "Central Access Reader.pkg"

#echo "Moving app and version file to top level..."
#cp ../version.txt ../../../
#mv "./dist/Central Access Reader.app" "../../../Central Access Reader.app"

cd ..

echo "----------------------------------"
echo "Done!"
echo "Your file can be found as Central Access Reader.pkg."
echo "The version file is called version.txt"
echo "----------------------------------"