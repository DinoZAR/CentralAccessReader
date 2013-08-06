# Cleanup what we had before
rm -rf build dist

#echo "Creating spec…"
#python generate_spec.py release

#echo "Creating the executable…"
#python ../../pyinstaller-2.0/utils/Build.py "Central Access Reader.spec"

# JavaScript files
echo "Copying MathJax…"
cp -R ./mathjax "./dist/Central Access Reader/mathjax/"

echo "Copying JQuery…"
cp ./jquery-1.9.1.min.js "./dist/Central Access Reader/"

echo "Copying JQuery UI…"
cp -R ./jquery-ui "./dist/Central Access Reader/jquery-ui/"

echo "Copying JQuery Scroll-to…"
cp ./jquery.scrollTo-1.4.3.1-min.js "./dist/Central Access Reader/"

echo "Copying JavaScript functions and configurations…"
cp -R ./src/javascript "./dist/Central Access Reader/src/javascript/"

# Other files
echo "Copying the MathML pattern databases…"
cp -R ./src/math_patterns "./dist/Central Access Reader/src/math_patterns/"

echo "Copying LAME MP3 encoder…"
cp ./src/lame_mac "./dist/Central Access Reader/src/"

echo "Copying OMML to MathML XSLT…"
cpy ./src/docx/OMMLToMathML.xsl "./dist/Central Access Reader/src/docx/"

echo "Copying tutorial…"
cp ./Tutorial.docx "./dist/Central Access Reader/"

echo "Copying version file…"
cp ./version.txt "./dist/Central Access Reader/"

# Package it all up using the created "dist" folder
pkgbuild --identifier com.cwu.centralaccessreader --version 1.02 --root ./dist "Central Access Reader.pkg"

echo "----------------------------------"
echo "Done!"
echo "Your file can be found as Central Access Reader.pkg."
echo "The version file is called version.txt"
echo "----------------------------------"