'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
from src.docx.importer import DocxDocument
import pythoncom
import win32com.client
from glob import glob
import os

if __name__ == '__main__':
    
    # This is a simulation of what would happen in my installer
    
    extra_files = []
    
    # Get my icons
    iconPath = os.path.abspath('forms/icons')
    print 'Icons folder:', iconPath
    iconFiles = glob(os.path.join(iconPath, '*.png'))
    print iconFiles
    
    extra_files.extend(iconFiles)
    
    # Get my MathML pattern database
    mathDatabasePath = os.path.abspath('mathml/parser_pattern_database.txt')
    print 'MathML database:', mathDatabasePath
    
    extra_files.append(mathDatabasePath)
    
    # Get OMML to MathML stylesheet
    ommlStylesheet = os.path.abspath('docx/OMMLToMathML.xsl')
    
    extra_files.append(ommlStylesheet)
    
    # Get the JavaScript responsible for handling my views
    javascriptsPath = os.path.abspath('docx')
    jsFiles = glob(os.path.join(javascriptsPath, '*.js'))
    print 'JavaScript path:', javascriptsPath
    print jsFiles
    
    extra_files.extend(jsFiles)
    
    # get JQuery
    jqueryPath = os.path.abspath('../jquery-1.9.1.min.js')
    print 'JQuery:', jqueryPath
    
    extra_files.append(jqueryPath)
    
    # Get the MathJax library
    mathjaxRoot = os.path.abspath('../mathjax')
    mathjaxFiles = []
    print 'MathJax:', mathjaxRoot
    for root, dirs, files in os.walk(mathjaxRoot):
        if len(files) > 0:
            for f in files:
                mathjaxFiles.append(os.path.join(root, f))
    print mathjaxFiles
    
    extra_files.extend(mathjaxFiles)
        
    print 'Done!'