'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
import zipfile
from lxml import etree
from lxml import html as HTML
import os
import urllib
import re
from cStringIO import StringIO
from threading import Thread
from src.gui.bookmarks import BookmarkNode
from src.misc import program_path, temp_path
from src.docx.paragraph import parseParagraph, parseTable

ROOT_PATH = program_path('src/docx')

w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'

def save_images(docxPath, importPath):
     
    # Open a zip file of my docx file
    z = zipfile.ZipFile(docxPath, 'r')
 
    for f in z.namelist():
        if f.find('word/media/') == 0:
            # Extract it to my import folder
            with open(importPath + '/images/' + f.replace('word/media/', ''), 'wb') as imageFile:
                imageFile.write(z.read(f))
     
    z.close()

class DocxDocument(object):
    '''
    Imports a .docx and transforms it to meet my needs.
    
    The progressCallback expects a function that will handle the following
    arguments:
    
    progressCallback(percentageOutOf100)
    
    The checkCancelFunction is a function that returns True when we should stop
    the import process and False otherwise.
    '''
    
    def __init__(self, docxFilePath, progressHook=None, cancelHook=None):
        '''
        Generates the document structure from the .docx file.
        '''
        self.importFolder = temp_path('import')
        
        if progressHook is not None:
            progressHook(0)
            
        print 'Cleaning up things...'
            
        # Delete all of the images in my import directory, if any
        if os.path.isdir(self.importFolder + '/images'):
            for the_file in os.listdir(self.importFolder + '/images'):
                file_path = os.path.join(self.importFolder + '/images', the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    print e
        else:
            os.makedirs(self.importFolder + '/images')
            
        print 'Starting the save images thread...'
        
        # Start saving images to my import folder in the background
        saveImagesThread = Thread(target=save_images, args=(docxFilePath, self.importFolder))
        saveImagesThread.start()
        
        # .docx is just a zip file
        docxZip = None
        with open(docxFilePath, 'rb') as docx:
            docxZip = zipfile.ZipFile(StringIO(docx.read()), 'r')
        
        print 'Getting my other data...'
        
        # Get the other random data I will need to parse my paragraphs
        otherData = {}
        otherData['zip'] = docxZip
        otherData['rels'] = self._getRels(docxZip)
        otherData['styles'] = self._getStyles(docxZip)
        otherData['paraStyles'] = self._getParaStyles(otherData['styles'])
        #otherData['numbering'] = self._getNumberingDict(docxZip)
        
        print 'Opening my document file...'
        
        # Open my main document file
        with docxZip.open('word/document.xml', 'r') as document:
            tree = etree.parse(document)
        root = tree.getroot()
        
        # Get all of the paragraphs elements in my docx
        paragraphs = root.findall('./{0}body/*'.format(w_NS))
        self.paragraphData = []
        
        print 'Converting paragraphs...'
        
        # Keep track of my progress while I convert all of the said paragraphs
        # Also, only report whole number changes, just in case if the progress
        # hook is expensive
        interrupted = False
        lastProgress = -1
        i = 0
        for p in paragraphs:
            if cancelHook is not None:
                if cancelHook():
                    interrupted = True
                    break
            self.paragraphData.append(self._convert_paragraph_to_html(p, otherData))
            i += 1
            if progressHook is not None:
                progress = int(float(i) / len(paragraphs) * 100.0)
                if progress != lastProgress:
                    progressHook(progress)
                    lastProgress = progress
        
        # Put together the HTML for the document if I wasn't interrupted
        if not interrupted:
            print 'Putting together HTML...'
            self._html = HTML.Element('html')
            head = HTML.Element('head')
            body = HTML.Element('body')
            self._html.append(head)
            self._html.append(body)
            
            self._prepareHead(head)
            self._prepareBody(body)
        
        else:
            print 'I was interrupted'
        
        print 'Waiting for image saving thread to finish...'
        saveImagesThread.join()
        
        print 'Import done!'
        
    def getMainPage(self):
        return HTML.tostring(self._html)
    
    def getHeadings(self):
        '''
        Returns the BookmarkNodes for this document.
        '''
        # State data for creating the bookmarks
        parentStack = [(BookmarkNode(None, 'Docx'), 0)]
        lastNode = parentStack[0]
        currLevel = -1
        anchorCount = 1
        
        # Get every heading element in the document
        headingElements = self._html.xpath(r'//h1 | //h2 | //h3 | //h4 | //h5') 
        
        for heading in headingElements:
            currLevel = int(re.search('[0-9]+', heading.tag).group(0))
            
            # Add last node inserted as parent if it is logical to do so
            if lastNode[1] < currLevel:
                parentStack.append(lastNode)
            
            # Pop off unsuitable parents
            while True:
                if parentStack[-1][1] >= currLevel:
                    parentStack.pop()
                else:
                    break
            
            # Make my bookmark and stuff
            if len(parentStack) > 0:
                myNode = BookmarkNode(parentStack[-1][0], heading.text_content(), anchorId=str(anchorCount))
                lastNode = (myNode, currLevel)
            else:
                myNode = BookmarkNode(lastNode[0], heading.text_content(), anchorId=str(anchorCount))
                lastNode = (myNode, currLevel)
                
            anchorCount += 1
        
        return parentStack[0][0]
    
    def getPages(self):
        '''
        Returns the PageNodes for this document.
        '''
        myPages = []
        
        pages = self._html.xpath("//*[@class='pageNumber']")
        if pages is not None:
            for p in pages:
                myPages.append(p.text_content())
         
        return myPages
    
    def _convert_paragraph_to_html(self, elem, otherData):
        '''
        WARNING: Should only be called by the thread pools that are in the
        DocxDocument class. There is a reason why this is removed and isolated.
        
        Converts a Docx <p> XML element string into a HTML element. Returns the 
        tuple (id, htmlElementString) when done.
        ''' 
        if elem.tag == '{0}p'.format(w_NS):
            return parseParagraph(elem, otherData)
        elif elem.tag == '{0}tbl'.format(w_NS):
            return parseTable(elem, otherData)
        
        return None
        
    def _appendParagraphResult(self, result):
        '''
        Callback used by thread pool to post results of their computation into
        the paragraph data structure.
        '''
        if self.progressCallback is not None:
            self.numCompleted += 1
            self.progressCallback(int(float(self.numCompleted) / self.numParagraphs * 99.0))
        
        if result is not None:
            id = result[0]
            data = HTML.fromstring(result[1])
            if len(data) > 0 or len(data.text_content()) > 0:
                self.paragraphData[id] = data
         
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
    
    def _prepareHead(self, head):
         
        mathjaxConfig = HTML.Element('script')
        mathjaxConfig.set('type', 'text/x-mathjax-config')
        scriptFile = open(program_path('src/mathjax_config.js'), 'r')
        contents = scriptFile.read()
        scriptFile.close()
        mathjaxConfig.text = contents
         
        mathjaxScript = HTML.Element('script')
        mathjaxScript.attrib['type'] = 'text/javascript'
        mathjaxScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('mathjax/MathJax.js')) + r'?config=TeX-AMS-MML_HTMLorMML.js'
         
        jqueryScript = HTML.Element('script')
        jqueryScript.attrib['type'] = 'text/javascript'
        jqueryScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery-1.9.1.min.js'))
             
        jqueryUIScript = HTML.Element('script')
        jqueryUIScript.attrib['type'] = 'text/javascript'
        jqueryUIScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery-ui/js/jquery-ui-1.9.2.custom.js'))
         
        jqueryScrollTo = HTML.Element('script')
        jqueryScrollTo.attrib['type'] = 'text/javascript'
        jqueryScrollTo.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery.scrollTo-1.4.3.1-min.js'))
         
        highlighterNormalScript = HTML.Element('script')
        highlighterNormalScript.set('language', 'javascript')
        highlighterNormalScript.set('type', 'text/javascript')
        scriptFile = open(program_path('src/highlighter_normal.js'), 'r')
        contents = scriptFile.read()
        scriptFile.close()
        highlighterNormalScript.text = contents
        
        highlighterStreamScript = HTML.Element('script')
        highlighterStreamScript.set('language', 'javascript')
        highlighterStreamScript.set('type', 'text/javascript')
        scriptFile = open(program_path('src/highlighter_stream.js'), 'r')
        contents = scriptFile.read()
        scriptFile.close()
        highlighterStreamScript.text = contents
        
        css = HTML.Element('link')
        css.attrib['rel'] = 'stylesheet'
        css.attrib['type'] = 'text/css'
        css.attrib['href'] = 'file:' + urllib.pathname2url(temp_path('import/defaultStyle.css'))
         
        head.append(mathjaxConfig)
        head.append(mathjaxScript)
        head.append(jqueryScript)
        head.append(jqueryUIScript)
        head.append(jqueryScrollTo)
        head.append(highlighterNormalScript)
        head.append(highlighterStreamScript)
        head.append(css)
        
    def _prepareBody(self, body):
        #sortedParas = sorted(self.paragraphData.iteritems(), key=lambda x: x[0])
        for p in self.paragraphData:
            if p is not None:
                body.append(p)
                
        # Get all of the headings and add anchor ids to them
        headings = body.xpath('//h1 | //h2 | //h3 | //h4 | //h5 | //h6')
        anchorCount = 1
        for h in headings:
            h.set('id', str(anchorCount))
            anchorCount += 1


if __name__ == '__main__':
    pass