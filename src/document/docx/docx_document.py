'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
import zipfile
from cStringIO import StringIO
import os
import sys
from threading import Thread

from lxml import etree
from PIL import Image

from src.misc import program_path
from src.document import Document
from src.document.docx.paragraph import parseParagraph, parseTable, addToBody, IMAGE_TRANSLATION

ROOT_PATH = program_path('src/docx')

w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'

class DocxDocument(Document):
    '''
    Imports a .docx and transforms it to meet my needs.
    
    The progressCallback expects a function that will handle the following
    arguments:
    
    progressCallback(percentageOutOf100)
    
    The checkCancelFunction is a function that returns True when we should stop
    the import process and False otherwise.
    '''
    
    def __init__(self, docxFilePath, progressHook, cancelHook):
        '''
        Generates the document structure from the .docx file.
        '''
        Document.__init__(self, docxFilePath, progressHook, cancelHook)
        
        self._name = os.path.splitext(os.path.basename(docxFilePath))[0]
        
        self._progressHook(0, 'Starting up...')
            
        # Make my images directory
        if not os.path.isdir(self._tempFolder + '/images'):
            os.makedirs(self._tempFolder + '/images')
        
        # Start saving images to my import folder in the background
        self._imageProgress = 0
        def myImageProgressHook(percent):
            self._imageProgress = percent / 2.0
        
        saveImagesThread = Thread(target=save_images, args=(docxFilePath, self._tempFolder, self._cancelHook, myImageProgressHook))
        saveImagesThread.start()
        
        # .docx is just a zip file
        docxZip = None
        with open(docxFilePath, 'rb') as docx:
            docxZip = zipfile.ZipFile(StringIO(docx.read()), 'r')
        
        # Get the other random data I will need to parse my paragraphs
        otherData = {}
        otherData['zip'] = docxZip
        otherData['rels'] = self._getRels(docxZip)
        otherData['styles'] = self._getStyles(docxZip)
        otherData['paraStyles'] = self._getParaStyles(otherData['styles'])
        otherData['numbering'] = self._getNumberingDict(docxZip)
        
        # Open my main document file
        with docxZip.open('word/document.xml', 'r') as document:
            tree = etree.parse(document)
        root = tree.getroot()
        
        # Get all of the paragraphs elements in my docx
        paragraphs = root.findall('./{0}body/*'.format(w_NS))
        paragraphData = []
        
        # Keep track of my progress while I convert all of the said paragraphs
        # Also, only report whole number changes, just in case if the progress
        # hook is expensive
        interrupted = False
        lastProgress = -1
        i = 0
        for p in paragraphs:
            if self._cancelHook():
                interrupted = True
                break
            paragraphData.append(self._convert_paragraph_to_html(p, otherData))
            i += 1
            
            progress = int(float(i) / len(paragraphs) * 50.0) + int(self._imageProgress)
            if progress != lastProgress:
                self._progressHook(progress, 'Reading in paragraphs...')
                lastProgress = progress
        
        # Put together the content HTML for the document if I wasn't interrupted
        if not interrupted:
            addToBody(self._contentDOM, paragraphData)
        
        while saveImagesThread.isAlive() and not self._cancelHook():
            progress = 50 + int(self._imageProgress)
            if progress != lastProgress:
                self._progressHook(progress, 'Saving rest of images...')
                lastProgress = progress
        
        self._mapMathEquations()
    
    def _convert_paragraph_to_html(self, elem, otherData):
        '''
        WARNING: Should only be called by the thread pools that are in the
        DocxDocument class. There is a reason why this is removed and isolated.
        
        Converts a Docx <p> XML element string into a HTML element. Returns the 
        tuple (id, htmlElementString) when done.
        ''' 
        if elem.tag == '{0}p'.format(w_NS):
            return parseParagraph(elem, otherData, self._tempFolder)
        elif elem.tag == '{0}tbl'.format(w_NS):
            return parseTable(elem, otherData, self._tempFolder)
        
        return None
         
    def _getRels(self, zip):
        relFile = zip.open('word/_rels/document.xml.rels', 'r')
        myRels = etree.parse(relFile)
        myRels = myRels.findall('./{0}Relationship'.format(r_NS))
        relFile.close()
        return myRels
     
    def _getStyles(self, zip):
        stylesFile = zip.open('word/styles.xml', 'r')
        myStyles = etree.parse(stylesFile)
        myStyles = myStyles.findall('./{0}style'.format(w_NS))
        stylesFile.close()
        return myStyles
     
    def _getParaStyles(self, styles):
        '''
        Returns a dictionary where the key is the style id and the value is the
        name of that style.
        '''
        myDict = {}
        for s in styles:
            query = s.find('./{0}name'.format(w_NS))
            if query != None:
                key = s.get('{0}styleId'.format(w_NS))
                value = query.get('{0}val'.format(w_NS))
                myDict[key] = value
        return myDict
    
    def _getNumberingDict(self, docxZip):
        '''
        Returns a dictionary of the numbering styles present in the document.
        '''        
        if 'word/numbering.xml' in docxZip.namelist():
            numberingFile = docxZip.open('word/numbering.xml', 'r')
            numberingXML = etree.parse(numberingFile)
            
            # Get all of the numbers used in the document and their references
            # to the abstract numbers.
            nums = numberingXML.findall('{0}num'.format(w_NS))
            
            # Map all of the num's to the abstract numbers
            numMapping = {}
            for n in nums:
                numId = n.get('{0}numId'.format(w_NS))
                abstractNumId = n.find('./{0}abstractNumId'.format(w_NS)).get('{0}val'.format(w_NS))
                numMapping[numId] = abstractNumId
                
            # Now, get the relevant data for the numbering from the abstract
            # numbers
            for k in numMapping.keys():
                abstractNum = numberingXML.find('./{0}abstractNum[@{0}abstractNumId=\''.format(w_NS) + numMapping[k] + '\']')
                
                levels = {}
                for level in abstractNum.findall('./{0}lvl'.format(w_NS)):
                    levelKey = level.get('{0}ilvl'.format(w_NS))
                    data = {}
                    if level.find('./{0}start'.format(w_NS)) is not None:
                        data['start'] = level.find('./{0}start'.format(w_NS)).get('{0}val'.format(w_NS))
                    else:
                        data['start'] = '1'
                    data['format'] = level.find('./{0}numFmt'.format(w_NS)).get('{0}val'.format(w_NS))
                    levels[levelKey] = data
                    
                # Save all of that data to the big numbering dictionary
                numMapping[k] = levels
            
            return numMapping
        
        else:
            return None

def save_images(docxPath, importPath, cancelHook, progressHook):
     
    # Open a zip file of my docx file
    z = zipfile.ZipFile(docxPath, 'r')
    
    i = 0
    for f in z.namelist():
        i += 1
        
        # Check for cancel
        if cancelHook():
            break
            
        # Report progress
        progressHook(int(float(i) / len(z.namelist()) * 100.0))
        
        if f.find('word/media/') == 0:
            
            # Don't save any MathType equations, which are WMF's. Web browsers
            # don't know how to display them
            if os.path.splitext(f)[1].lower() != '.wmf':
                # Extract it to my import folder
                savePath = importPath + '/images/' + f.replace('word/media/', '')
                
                # Only do the image translation on Windows. PIL doesn't like to
                # be frozen on Macs
                # TODO: Make PIL work when frozen on Macs
                if (os.path.splitext(savePath)[1].lower() in IMAGE_TRANSLATION) and (sys.platform == 'win32'):
                    try:
                        contents = z.read(f)
                        myFile = StringIO(contents)
                        convertFile = Image.open(myFile)
                        outPath = os.path.splitext(savePath)[0] + IMAGE_TRANSLATION[os.path.splitext(savePath)[1].lower()]
                        convertFile.save(outPath)
                    except IOError as e:
                        # Don't try to do anything else with it. Just copy the
                        # file over
                        print 'Could not convert image', f, 'to', os.path.basename(savePath)
                        with open(savePath, 'wb') as imageFile:
                            imageFile.write(z.read(f))
                else:
                    with open(savePath, 'wb') as imageFile:
                        imageFile.write(z.read(f))
     
    z.close()
    
if __name__ == '__main__':
    pass
