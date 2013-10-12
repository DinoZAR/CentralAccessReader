'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
import zipfile
from lxml import etree
from lxml import html as HTML
from PIL import Image
from cStringIO import StringIO
import os
import urllib
import re
from cStringIO import StringIO
from threading import Thread
from gui.bookmarks import BookmarkNode
from misc import program_path, temp_path
from docx.paragraph import parseParagraph, parseTable, IMAGE_TRANSLATION

ROOT_PATH = program_path('src/docx')

w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'

def save_images(docxPath, importPath, cancelHook=None, progressHook=None):
     
    # Open a zip file of my docx file
    z = zipfile.ZipFile(docxPath, 'r')
    
    i = 0
    for f in z.namelist():
        i += 1
        
        # Check for cancel
        if cancelHook is not None:
            if cancelHook():
                break
            
        # Check the progress
        if progressHook is not None:
            progressHook(int(float(i) / len(z.namelist()) * 100.0))
        
        if f.find('word/media/') == 0:
            # Extract it to my import folder
            savePath = importPath + '/images/' + f.replace('word/media/', '')
            if os.path.splitext(savePath)[1].lower() in IMAGE_TRANSLATION:
                contents = z.read(f)
                myFile = StringIO(contents)
                convertFile = Image.open(myFile)
                outPath = os.path.splitext(savePath)[0] + IMAGE_TRANSLATION[os.path.splitext(savePath)[1].lower()]
                convertFile.save(outPath)
            else:
                with open(savePath, 'wb') as imageFile:
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
        self._imageProgress = 0
        def myImageProgressHook(percent):
            self._imageProgress = percent / 2.0
        
        saveImagesThread = Thread(target=save_images, args=(docxFilePath, self.importFolder, cancelHook, myImageProgressHook))
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
                progress = int(float(i) / len(paragraphs) * 50.0) + int(self._imageProgress)
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
        while saveImagesThread.isAlive():
            if progressHook is not None:
                progress = 50 + int(self._imageProgress)
                if progress != lastProgress:
                    progressHook(progress)
                    lastProgress = progress
        
        print 'Import done!'
        
    def getMainPage(self, mathOutput='html'):
        if mathOutput == 'svg':
            html = HTML.Element('html')
            head = HTML.Element('head')
            body = HTML.Element('body')
            html.append(head)
            html.append(body)
            self._prepareHead(head, mathOutput='svg')
            self._prepareBody(body)
            return HTML.tostring(html)
        else:
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
    
    def _prepareHead(self, head, mathOutput='html'):
        mathjaxConfig = HTML.Element('script')
        mathjaxConfig.set('type', 'text/x-mathjax-config')
        mathjaxConfigFile = ''
        if mathOutput == 'svg':
            mathjaxConfigFile = program_path('src/javascript/mathjax_config_svg.jsconfig')
        else:
            mathjaxConfigFile = program_path('src/javascript/mathjax_config.jsconfig')
        scriptFile = open(mathjaxConfigFile, 'r')
        contents = scriptFile.read()
        scriptFile.close()
        mathjaxConfig.text = contents
         
        mathjaxScript = HTML.Element('script')
        mathjaxScript.attrib['type'] = 'text/javascript'
        mathjaxScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('mathjax/MathJax.js'))
         
        jqueryScript = HTML.Element('script')
        jqueryScript.attrib['type'] = 'text/javascript'
        jqueryScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery-1.9.1.min.js'))
             
        jqueryUIScript = HTML.Element('script')
        jqueryUIScript.attrib['type'] = 'text/javascript'
        jqueryUIScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery-ui/js/jquery-ui-1.9.2.custom.js'))
         
        jqueryScrollTo = HTML.Element('script')
        jqueryScrollTo.attrib['type'] = 'text/javascript'
        jqueryScrollTo.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery.scrollTo-1.4.3.1-min.js'))
        
        # Get all of my own JavaScripts into the document
        javascriptFiles = [f for f in os.listdir(program_path('src/javascript/')) 
                           if os.path.isfile(os.path.join(program_path('src/javascript/'), f)) and
                           os.path.splitext(os.path.join(program_path('src/javascript/'), f))[1] == '.js']
        javascriptElements = []
        for f in javascriptFiles:
            elem = HTML.Element('script')
            elem.set('language', 'javascript')
            elem.set('type', 'text/javascript')
            with open(os.path.join(program_path('src/javascript/'), f), 'r') as jsFile:
                elem.text = jsFile.read()
            javascriptElements.append(elem)
        
        css = HTML.Element('link')
        css.attrib['rel'] = 'stylesheet'
        css.attrib['type'] = 'text/css'
        css.attrib['href'] = 'file:' + urllib.pathname2url(temp_path('import/defaultStyle.css'))
         
        head.append(mathjaxConfig)
        head.append(mathjaxScript)
        head.append(jqueryScript)
        head.append(jqueryUIScript)
        head.append(jqueryScrollTo)
        for elem in javascriptElements:
            head.append(elem)
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
