'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''
import zipfile
from lxml import etree
from lxml import html as HTML
import os
import urllib
from multiprocessing import Process, Pool
from src.gui.bookmarks import BookmarkNode
from src.misc import program_path, temp_path
from src.docx.paragraph import parseParagraph, parseTable, heirarchyStyles

ROOT_PATH = program_path('src/docx')

w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'

def convert_paragraph_to_html(paraId, elem, otherData):
    '''
    WARNING: Should only be called by the thread pools that are in the
    DocxDocument class. There is a reason why this is removed and isolated.
    
    Converts a Docx <p> XML element into a HTML element. Returns the tuple
    (id, htmlElement) when done.
    '''
    if elem.tag == '{0}p'.format(w_NS):
        return (paraId, parseParagraph(elem, otherData))
    elif elem.tag == '{0}tbl'.format(w_NS):
        return (paraId, parseTable(elem, otherData))
    
#         if len(newPara['data']) > 0:
#             self.paragraphData.append(newPara)
    

class DocxDocument(object):
    '''
    Imports a .docx and transforms it to meet my needs.
    
    The progressCallback expects a function that will handle the following
    arguments:
    
    progressCallback(percentageOutOf100)
    
    The checkCancelFunction is a function that returns True when we should the
    import process and False otherwise.
    '''
    
    def __init__(self, docxFilePath, progressCallback=None, checkCancelFunction=None):
        '''
        Generates the document structure from the .docx file.
        '''
        
        self.docxFilePath = docxFilePath
        self.importFolder = temp_path('import')
        
        if progressCallback:
            progressCallback(0)
        
        # Start saving images to my import folder in the background
        saveImagesThread = Process(target=self._saveImages)
        saveImagesThread.start()
        
        # Start a thread pool to parse all of the paragraphs in there
        threadPool = Pool()
        
        # .docx is just a zip file
        self.zip = zipfile.ZipFile(docxFilePath, 'r')
        
        # Get the other random data I will need to parse my paragraphs
        otherData = {}
        otherData['rels'] = self._getRels(self.zip)
        otherData['styles'] = self._getStyles(self.zip)
        otherData['paraStyles'] = self._getParaStyles(self.otherData['styles'])
        #otherData['numbering'] = self._getNumberingDict(self.zip)
        
        # Open my main document file
        document = self.zip.open('word/document.xml', 'r')
        tree = etree.parse(document)
        document.close()
        root = tree.getroot()
        
        # Get all of the paragraphs elements in my docx
        paragraphs = root.findall('./{0}body/*'.format(w_NS))
        self.paragraphData = {}
        
        # Keep track of my progress
        self.numParagraphs = len(paragraphs)
        self.numCompleted = 0
        
        # Queue up all of my paragraphs to my thread pool
        idCounter = 0
        for p in paragraphs:
            if checkCancelFunction:
                if checkCancelFunction():
                    break
                
            threadPool.apply_async(convert_paragraph_to_html, (idCounter, p, otherData), callback=self._appendParagraphResult)
            idCounter += 1
            
        print 'All paragraphs queued! Waiting for them to finish...'
        threadPool.close()
        threadPool.join()
        
        print 'Putting together HTML...'
        html = HTML.Element('html')
        head = HTML.Element('head')
        body = HTML.Element('body')
        html.append(head)
        html.append(body)
        
        self._prepareHead(head)
        self._prepareBody(body)
        
        self._html = etree.tostring(html)
        
        print 'Waiting for image saving thread to finish...'
        saveImagesThread.join()
        
        print 'Import done!'
        
    def _appendParagraphResult(self, result):
        '''
        Callback used by thread pool to post results of their computation into
        the paragraph data structure.
        '''
        id = result[0]
        data = result[1]
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
        sortedParas = sorted(self.paragraphData.iteritems(), key=lambda x: x[0])
        for p in sortedParas:
            pass

    def _saveImages(self):
         
        # Open a zip file of my docx file
        zip = zipfile.ZipFile(self.docxFilePath, 'r')
         
        # Delete images directory, if there is one
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
     
        for f in zip.namelist():
            if f.find('word/media/') == 0:
                # Extract it to my import folder
                imageFile = open(self.importFolder + '/images/' + f.replace('word/media/', ''), 'wb')
                imageFile.write(zip.read(f))
                imageFile.close()
         
        zip.close()
             
    def getMainPage(self):
        return self._html
    
    def getHeadings(self):
        '''
        Returns the BookmarkNodes for this document.
        '''
        # State data for creating the bookmarks
        parentStack = [(BookmarkNode(None, 'Docx'), 0)]
        lastNode = parentStack[0]
        currLevel = -1
        anchorCount = 1
         
        # The paragraphs are just a bunch of dictionaries
        for p in self.paragraphData:
             
            if 'style' in p:
                if p['style'] in heirarchyStyles:
                    currLevel = heirarchyStyles[p['style']]
                else:
                    currLevel = -1
            else:
                currLevel = -1
         
            # Create a bookmark if it is an actual hierarchical piece of content  
            if currLevel > 0:
                 
                # Add last node inserted as parent if it is logical to do so
                if lastNode[1] < currLevel:
                    parentStack.append(lastNode)
                     
                # Pop off unsuitable parents
                while True:
                    if parentStack[-1][1] >= currLevel:
                        parentStack.pop()
                    else:
                        break
                     
                # Make my BookmarkNode and stuff
                if len(parentStack) > 0:
                    myNode = BookmarkNode(parentStack[-1][0], self._generateParagraphHTMLNode(p, 0)[0].text_content(), anchorId=str(anchorCount))
                    lastNode = (myNode, currLevel)
                else:
                    myNode = BookmarkNode(lastNode[0], self._generateParagraphHTMLNode(p, 0)[0].text_content(), anchorId=str(anchorCount))
                    lastNode = (myNode, currLevel)
                     
                anchorCount += 1
                 
        # Return my root bookmark
        return parentStack[0][0]
    
    def getPages(self):
        '''
        Returns the PageNodes for this document.
        '''
        myPages = []
         
        for p in self.paragraphData:
            if 'pageNumber' in p:
                myPages.append(self._generateParagraphHTMLNode(p, 0)[0].text_content())
         
        return myPages
    
#     def _getNumberingDict(self, zip):
#         '''
#         Returns a nested dictionary that looks like the following:
#         
#         {numId : {levelId : {"format" : "decimal|bullet", "start" : 0}, levelId : {...}, ...}}
#         '''
#         myDict = {}
#         
#         if 'word/numbering.xml' in zip.namelist():
#             # Get the numbering XML
#             numberingFile = zip.open('word/numbering.xml', 'r')
#             numXML = etree.parse(numberingFile)
#             numberingFile.close()
#             
#             # Get all numberings and get the abstract element they refer to
#             # (pointless indirection in my opinion)
#             nums = numXML.findall('./{0}num'.format(w_NS))
#             for e in nums:
#                 abstractId = e.find('./{0}abstractNumId'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                 abstractNum = numXML.find('./{0}abstractNum[@{0}abstractNumId=\''.format(w_NS) + abstractId + '\']')
#                 
#                 # Get list of levels in that particular element
#                 levels = abstractNum.findall('./{0}lvl'.format(w_NS))
#                 levelDicts = {}
#                 for l in levels:
#                     key = l.attrib['{0}ilvl'.format(w_NS)]
#                     levelDicts[key] = {}
#                     format = l.find('./{0}numFmt'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                     
#                     if l.find('./{0}start'.format(w_NS)):
#                         levelDicts[key]['start'] = l.find('./{0}start'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                     else:
#                         levelDicts[key]['start'] = 1
#                     
#                     #start = l.find('./{0}start'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                     levelDicts[key]['format'] = format
#                 
#                 key = e.attrib['{0}numId'.format(w_NS)]
#                 myDict[key] = levelDicts
#                 
#         return myDict