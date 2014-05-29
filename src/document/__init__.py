'''
Created on Nov 18, 2013

@author: Spencer Graffe
'''
import os
import re
import urllib

from lxml import etree
from lxml import html as HTML

from src.gui.bookmarks import BookmarkNode
from src.gui import configuration
from src import misc

class Document(object):
    '''
    Base class of all documents imported into CAR. It will handle the positions
    of the TTS and cursor location while keeping track of the state of certain
    interactions. Finally, this class will handle supplying the temp folder for
    the underlying implementation. The only thing the underlying implementation
    will do is import and format the content.
    
    filePath - path to the input file. May be left blank, e.g. ""
    progressHook - function that's called for reporting the import progress
                 - args = (percentInteger, labelString)
    cancelHook - function called everytime it checks for cancel
               - must return True if wanting cancel, False otherwise
    '''
    TEMP_FOLDER_ID = 0
    
    def __init__(self, filePath, progressHook, cancelHook):
        
        # Dictionary mapping all of the math equations in the DOM to the MathML
        # the equation originally was
        self._maths = {}
#         self._mathParserThread = MathParserThread()
#         self._mathParserThread.mathProseGenerated.connect(self._setMathProse)
#         self._mathParserThread.start()
        
        # The name of the document
        self._name = ''
        
        # The content DOM the underlying implementation creates
        self._contentDOM = HTML.Element('body')
        
        # Hooks for the load progress
        self._progressHook = progressHook
        self._cancelHook = cancelHook
        
        # Temp folder for that particular document
        self._tempFolder = misc.temp_path('doc' + str(Document.TEMP_FOLDER_ID) + '/')
        Document.TEMP_FOLDER_ID += 1
        
        # File path
        self._filePath = filePath
        
        # Flag whether this document is exportable
        self._exportable = True
    
    def getName(self):
        '''
        Gets the name for this document.
        '''
        return self._name
    
    def getFilePath(self):
        '''
        Returns the path of the file when it was loaded.
        '''
        if len(self._filePath) > 0:
            return self._filePath
        else:
            return self._name
        
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
        headingElements = self._contentDOM.xpath(r'//h1 | //h2 | //h3 | //h4 | //h5') 
        
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
        
        pages = self._contentDOM.xpath("//*[@class='pageNumber']")
        if pages is not None:
            for p in pages:
                myPages.append(p.text_content())
         
        return myPages
    
    def getMainPage(self, mathOutput='svg'):
        html = HTML.Element('html')
        head = HTML.Element('head')
        html.append(head)
        html.append(self._contentDOM)
        self._prepareHead(head, mathOutput=mathOutput)
        self._prepareBody(self._contentDOM)
        return HTML.tostring(html)
    
    def getMathMLFromID(self, mathID):
        '''
        Returns the MathML for a given ID, as an lxml Element
        '''
        return etree.fromstring(self._maths[mathID]['mathml'])
    
    def stopThreads(self):
        '''
        Stops the threads running on this document. You would do this in
        preparation for removing or deleting it.
        '''
        self._mathParserThread.stop()
        
    def _prepareHead(self, head, mathOutput):
        mathjaxConfig = HTML.Element('script')
        mathjaxConfig.set('type', 'text/x-mathjax-config')
        mathjaxConfigFile = ''
        if mathOutput == 'svg':
            mathjaxConfigFile = misc.program_path('src/javascript/mathjax_config_svg.jsconfig')
        else:
            mathjaxConfigFile = misc.program_path('src/javascript/mathjax_config.jsconfig')
        scriptFile = open(mathjaxConfigFile, 'r')
        contents = scriptFile.read()
        scriptFile.close()
        mathjaxConfig.text = contents
         
        mathjaxScript = HTML.Element('script')
        mathjaxScript.set('type', 'text/javascript')
        mathjaxScript.set('src', 'file:' + urllib.pathname2url(misc.program_path('mathjax/MathJax.js')))
         
        jqueryScript = HTML.Element('script')
        jqueryScript.set('type', 'text/javascript')
        jqueryScript.set('src', 'file:' + urllib.pathname2url(misc.program_path('jquery-1.9.1.min.js')))        
             
        jqueryUIScript = HTML.Element('script')
        jqueryUIScript.set('type', 'text/javascript')
        jqueryUIScript.set('src', 'file:' + urllib.pathname2url(misc.program_path('jquery-ui/js/jquery-ui-1.9.2.custom.js')))        
         
        jqueryScrollTo = HTML.Element('script')
        jqueryScrollTo.set('type', 'text/javascript')
        jqueryScrollTo.set('src', 'file:' + urllib.pathname2url(misc.program_path('jquery.scrollTo-1.4.3.1-min.js')))
        
        jqueryNextInDom = HTML.Element('script')
        jqueryNextInDom.set('type', 'text/javascript')
        jqueryNextInDom.set('src', 'file:' + urllib.pathname2url(misc.program_path('nextindom.jquery.js')))
        
        # Get all of my own JavaScripts into the document
        javascriptFiles = [f for f in os.listdir(misc.program_path('src/javascript/')) 
                           if os.path.isfile(os.path.join(misc.program_path('src/javascript/'), f)) and
                           os.path.splitext(os.path.join(misc.program_path('src/javascript/'), f))[1] == '.js']
        javascriptElements = []
        for f in javascriptFiles:
            elem = HTML.Element('script')
            elem.set('language', 'javascript')
            elem.set('type', 'text/javascript')
            with open(os.path.join(misc.program_path('src/javascript/'), f), 'r') as jsFile:
                elem.text = jsFile.read()
            javascriptElements.append(elem)
        
        css = HTML.Element('link')
        css.set('rel', 'stylesheet')
        css.set('type', 'text/css')
        css.set('href', 'file:' + urllib.pathname2url(misc.temp_path('import/defaultStyle.css')))
        
        head.append(mathjaxConfig)
        head.append(mathjaxScript)
        head.append(jqueryScript)
        head.append(jqueryUIScript)
        head.append(jqueryScrollTo)
        head.append(jqueryNextInDom)
        for elem in javascriptElements:
            head.append(elem)
        head.append(css)
        
    def _prepareBody(self, body):
        
        # Get all of the headings and add anchor ids to them
        headings = body.xpath('//h1 | //h2 | //h3 | //h4 | //h5 | //h6')
        anchorCount = 1
        for h in headings:
            h.set('id', str(anchorCount))
            anchorCount += 1
        
    def _mapMathEquations(self):
        '''
        Maps the math equations to the converted equations in the document so
        that it can pass them to the math TTS engine correctly.
        '''
        self._maths = {}
        
        # Find every <math> tag and store its corresponding data into my math
        # dictionary
        m_NS = 'http://www.w3.org/1998/Math/MathML'
        i = 1
        for math in self._contentDOM.xpath('.//math | .//m:math', namespaces={'m' : m_NS}):
            mathContent = etree.tostring(math, method='xml')
            key = 'MathJax-Element-' + str(i) + '-Frame'
            data = {'mathml' : mathContent, 'parsed' : False, 'prose' : '', 'database' : '', 'index' : i}
            self._maths[key] = data
            
            i += 1
            
#         # Send the dictionary off to my thread
#         if len(self._maths.keys()) > 0:
#             self._mathParserThread.setMaths(self._maths)
#         else:
#             self._mathParserThread.stop()
            
#     def _setMathProse(self, key, prose, database):
#         '''
#         Sets the math prose from the math parser thread.
#         '''
#         self._maths[key]['parsed'] = True
#         self._maths[key]['prose'] = prose
#         self._maths[key]['database'] = database
        
    def generateSpeech(self, element):
        '''
        Returns a generator that gets the speech output for the HTML element.
        '''
        return self._generateSpeech(element)
    
    def _getNextMath(self, elem):
        '''
        Gets the next math equation. If elem is a math equation, it returns that
        element.
        '''
        xpathString = './/span[@class=\'MathJax_SVG\']'
        
        myElem = elem
        nextElem = elem.find(xpathString)
     
        while nextElem is None:
     
            if myElem.getnext() is not None:
                myElem = myElem.getnext()
                nextElem = myElem.find(xpathString)
     
            else:
                if myElem.getparent() is not None:
                    myElem = myElem.getparent()
                else:
                    break
     
        return nextElem
    
    def _generateSpeech(self, element):
        '''
        Creates a generator that gets the speech output for the HTML element.
        '''
        visitChildren = True
        
        if element.tag == 'img':
            
            altText = element.get('alt')
            if altText == None or configuration.getBool('IgnoreAltText', False):
                altText = ' '
            
            if configuration.getBool('TagImage', False):
                    yield ['Image. ' + altText + '. End image.', 'image']
            else:
                if len(altText.strip()) > 0:
                    yield [altText, 'image']
                else:
                    yield ['Image.', 'image']
                    
            if element.tail != None:
                yield [element.tail, 'text']
        
        elif (element.tag == 'span') and (element.get('class') is not None):
                if 'MathJax' in element.get('class'):
                    
                    visitChildren = False
                    
                    # See if the MathML already got parsed. Otherwise, generate
                    # the speech on demand and save that.
                    key = element.get('id')
                    mathOutput = ''
                    if self._maths[key]['parsed'] and self._maths[key]['database'] == configuration.getValue('MathTTS'):
                        mathOutput = self._maths[key]['prose']
                    else:
                        mathOutput = configuration.getMathTTS('MathTTS').parse(self._maths[key]['mathml'])
                        self._maths[key]['prose'] = mathOutput
                        self._maths[key]['parsed'] = True
                        self._maths[key]['database'] = configuration.getValue('MathTTS')
                    
                    if configuration.getBool('TagMath', False):
                        yield ['Math. ' + mathOutput + '. End math.', 'math']
                    else:
                        yield [mathOutput, 'math']
        
        elif element.tag == 'script':
            # Don't do anything at all
            visitChildren = False
            
        else:
            if element.text != None:
                yield [element.text, 'text']
        
        # Get all of the speech from child elements (if allowed to)
        if visitChildren:
            for child in element:
                for speech in self._generateSpeech(child):
                    yield speech
        
        # If I have trailing text off of this element, read that too
        if element.tail != None:
            yield [element.tail, 'text']
            
            
# NOTE: Not used anymore. Just kept around for documentation purposes         
# class MathParserThread(QThread):
#     '''
#     This thread parses math equations given to it and then reports its 
#     corresponding prose.
#     '''
#     
#     # Emitted whenever prose is generated for a math equation
#     # unicode - key for math equation
#     # unicode - prose generated
#     # unicode - math database used for generation
#     mathProseGenerated = pyqtSignal(unicode, unicode, unicode)
#     
#     def __init__(self):
#         super(MathParserThread, self).__init__()
#         self._myMaths = {}
#         self._orderedKeys = []
#         self._running = False
#         self._index = 0
#     
#     def setMaths(self, maths):
#         '''
#         Gives this thread a copy of the math equation dictionary.
#         '''
#         self._myMaths = maths
#         
#         # Create a list of keys ordered by index
#         self._orderedKeys = sorted(self._myMaths, key=lambda x: self._myMaths.get(x)['index'])
#         
#         
#     def setParseIndex(self, newIndex):
#         '''
#         Sets the parser location to a new index. This is useful for when the
#         reader starts reading after a passage well after the start of the
#         document, adjusting this parser to keep up with new demand.
#         '''
#         self._index = newIndex
#         
#     def run(self):
#         self._running = True
#         self.setPriority(QThread.HighPriority)
#         
#         while self._running:
#             QThread.yieldCurrentThread()
#             # Reset the index back to beginning if I approach end
#             if self._index >= len(self._orderedKeys):
#                 self._index = 0
#             
#             # If I have any math at all
#             if len(self._orderedKeys) > 0:
#                 
#                 # Only parse if the the prose has not been parsed or if the
#                 # math database used wasn't the same
#                 d = self._myMaths[self._orderedKeys[self._index]]
#                 myDatabase = configuration.getValue('MathTTS', 'General')
#                 shouldParse = not d['parsed']
#                 shouldParse = shouldParse or (d['database'] != myDatabase)
#                 
#                 if shouldParse:
#                     myKey = self._orderedKeys[self._index]
#                     
#                     self._myMaths[myKey]['parsed'] = True
#                     
#                     prose = configuration.getMathDatabase('MathTTS').parse(d['mathml'])
#                     self._myMaths[myKey]['prose'] = prose
#                     self._myMaths[myKey]['database'] = myDatabase
#                     
#                     self.mathProseGenerated.emit(myKey, prose, myDatabase)
#             
#             self._index += 1
#             
#     def stop(self):
#         self._running = False
# 
#         