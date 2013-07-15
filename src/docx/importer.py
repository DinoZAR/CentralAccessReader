'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
import zipfile
from lxml import etree
from lxml import objectify
from lxml import html as HTML
import os
import urllib
import re
from multiprocessing import Process
from Queue import Queue, Empty
#from src.threadpool import Pool
from src.threadmap import ThreadMapper
from src.gui.bookmarks import BookmarkNode
from src.misc import program_path, temp_path
from src.docx.paragraph import parseParagraph, parseTable, heirarchyStyles

ROOT_PATH = program_path('src/docx')

w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'

def convert_paragraph_to_html(elem, otherData):
    '''
    WARNING: Should only be called by the thread pools that are in the
    DocxDocument class. There is a reason why this is removed and isolated.
    
    Converts a Docx <p> XML element string into a HTML element. Returns the 
    tuple (id, htmlElementString) when done.
    ''' 
    print 'Parsing paragraph'
    if elem.tag == '{0}p'.format(w_NS):
        return HTML.tostring(parseParagraph(elem, otherData))
    elif elem.tag == '{0}tbl'.format(w_NS):
        return HTML.tostring(parseTable(elem, otherData))
    
    return None

def save_images(docxPath, importPath):
     
    # Open a zip file of my docx file
    z = zipfile.ZipFile(docxPath, 'r')
 
    for f in z.namelist():
        if f.find('word/media/') == 0:
            # Extract it to my import folder
            imageFile = open(importPath + '/images/' + f.replace('word/media/', ''), 'wb')
            imageFile.write(z.read(f))
            imageFile.close()
     
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
    
    def __init__(self, docxFilePath, progressCallback=None, checkCancelFunction=None):
        '''
        Generates the document structure from the .docx file.
        '''
        
        self.docxFilePath = docxFilePath
        self.importFolder = temp_path('import')
        self.progressCallback = progressCallback
        
        if self.progressCallback is not None:
            self.progressCallback(0)
            
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
        
        # Start saving images to my import folder in the background
        saveImagesThread = Process(target=save_images, args=(self.docxFilePath, self.importFolder))
        saveImagesThread.start()
        
        # .docx is just a zip file
        zip = zipfile.ZipFile(docxFilePath, 'r')
        
        # Get the other random data I will need to parse my paragraphs
        otherData = {}
        otherData['rels'] = self._getRels(zip)
        otherData['styles'] = self._getStyles(zip)
        otherData['paraStyles'] = self._getParaStyles(otherData['styles'])
        #otherData['numbering'] = self._getNumberingDict(zip)
        
        # Open my main document file
        document = zip.open('word/document.xml', 'r')
        tree = objectify.parse(document)
        document.close()
        root = tree.getroot()
        
        # Get all of the paragraphs elements in my docx
        paragraphs = root.findall('./{0}body/*'.format(w_NS))
        self.paragraphData = []
        
        # Keep track of my progress
        self.numParagraphs = len(paragraphs)
        self.numCompleted = 0
        
        # Get my multithreaded mapper on my paragraphs
        tm = ThreadMapper(paragraphs, convert_paragraph_to_html, args=(otherData,), progressHook=progressCallback, cancelHook=checkCancelFunction)
        tm.start()
        tm.join()
        
        self._error = None
        
        if tm.success():
            self.paragraphData = tm.results()
            print 'Paragraph results:', self.paragraphData
            
            
#         threadPool = Pool()
#         idCounter = 0
#         
#         for p in paragraphs:
#             
#             if checkCancelFunction is not None:
#                 if checkCancelFunction():
#                     break
#                 
#             threadPool.addTask(convert_paragraph_to_html, self._appendParagraphResult, args=(idCounter, etree.tostring(p), otherData)) 
#             idCounter += 1
#         
#         # After all paragraphs have been queued, just check for cancel
#         print 'All paragraphs queued! Waiting for them to finish...'
#         interrupted = False
#         while True:
#             if checkCancelFunction is not None:
#                 if checkCancelFunction():
#                     threadPool.stop()
#                     interrupted = True
#                     break
#             if not threadPool.hasTasks():
#                 break
#         
#         # Check that I didn't get any errors
#         self._error = threadPool.getErrors()
#         if self._error:
#             interrupted = True
#             self._error = self._error[0]
#         
#         # If I haven't been interrupted at this point, construct HTML
#         if not interrupted:
#             threadPool.join()
        
            print 'Putting together HTML...'
            self._html = HTML.Element('html')
            head = HTML.Element('head')
            body = HTML.Element('body')
            self._html.append(head)
            self._html.append(body)
            
            self._prepareHead(head)
            self._prepareBody(body)
        
        else:
            # Set the error as the first error I encountered
            self._error = tm.errors()
            if len(self._error) > 0:
                self._error = self._error[0]
            else:
                self._error = None
        
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
    
    def getError(self):
        '''
        Returns a DocxImportError object if the import process encountered an
        exception. Otherwise, it returns None.
        '''
        return self._error
        
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
        myRels = objectify.parse(relFile)
        myRels = myRels.findall('./{0}Relationship'.format(r_NS))
        relFile.close()
        return myRels
     
    def _getStyles(self, zip):
        stylesFile = zip.open('word/styles.xml', 'r')
        myStyles = objectify.parse(stylesFile)
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
        scriptFile = open(os.path.join(ROOT_PATH, 'mathjax_config.js'))
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
         
        myScripts = HTML.Element('script')
        myScripts.set('language', 'javascript')
        myScripts.set('type', 'text/javascript')
         
        scriptFile = open(os.path.join(ROOT_PATH, 'my_functions.js'), 'r')
        contents = scriptFile.read()
        scriptFile.close()
        myScripts.text = contents
         
        css = HTML.Element('link')
        css.attrib['rel'] = 'stylesheet'
        css.attrib['type'] = 'text/css'
        css.attrib['href'] = 'file:' + urllib.pathname2url(temp_path('import/defaultStyle.css'))
         
        head.append(mathjaxConfig)
        head.append(mathjaxScript)
        head.append(jqueryScript)
        head.append(jqueryUIScript)
        head.append(jqueryScrollTo)
        head.append(myScripts)
        head.append(css)
        
    def _prepareBody(self, body):
        #sortedParas = sorted(self.paragraphData.iteritems(), key=lambda x: x[0])
        for p in self.paragraphData:
            if p is not None:
                body.append(HTML.fromstring(p))
                
        # Get all of the headings and add anchor ids to them
        headings = body.xpath('//h1 | //h2 | //h3 | //h4 | //h5 | //h6')
        anchorCount = 1
        for h in headings:
            h.set('id', str(anchorCount))
            anchorCount += 1

class DocxImportError(Exception):
    
    def __init__(self, origEx, traceback):
        Exception.__init__(self)
        self.message = 'Docx import error:\n' + str(origEx) + '\n' + traceback
        
    def __repr__(self):
        return self.message
    
    def __str(self):
        return self.message


if __name__ == '__main__':
    pass