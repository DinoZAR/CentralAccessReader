'''
Created on Feb 20, 2013

@author: Spencer Graffe
'''
import traceback
from HTMLParser import HTMLParser
from lxml import etree, html
from PyQt4.QtCore import QMutex, QThread, pyqtSignal
from src.mathml.tts import MathTTS
from src.speech.math_parser_thread import MathParserThread

# Namespace for XHTML
html_NS = '{http://www.w3.org/1999/xhtml}'

class PrepareSpeechThread(QThread):
    '''
    This thread prepares the HTML given to it into an output list that should
    be queued into the TTS engine. It will report progress and say when it is
    finished.
    '''
    reportProgress = pyqtSignal(int)
    
    def __init__(self, assigner, configuration, htmlToConvert, maxPercent):
        QThread.__init__(self)
        self._assigner = assigner
        self._config = configuration
        self._html = htmlToConvert
        self._outputList = []
        self._stop = False
        self._max = maxPercent
        
    def run(self):
        def myProgressCallback(percent):
            self.reportProgress.emit(int(percent / 100.0 * self._max))
            
        def myCheckCancel():
            return self._stop
        
        self._outputList = self._assigner.getSpeech(self._html, self._config, myProgressCallback, myCheckCancel)
        
    def stop(self):
        print 'Stopping preparer...'
        self._stop = True
        
    def isSuccessful(self):
        return not self._stop
    
    def getOutputList(self):
        return self._outputList
            
class Assigner(object):
    '''
    Used to assign parts of the content (represented as HTML) to specific
    speech handlers that handle saying that specific content.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._maths = {}
        self._mathsLock = QMutex()
        self._mathTTS = None
        
        # Start my math parsing thread, which will constantly parse math into
        # prose
        self.mathThread = MathParserThread(self._mathTTS)
        self.mathThread.mathParsed.connect(self._setMathData)
        self.mathThread.start()
        
    def prepare(self, content):
        '''
        Caches certain aspects of the content so that it can properly assign
        the content (like MathML)
        '''
        
        print 'Assigner preparing document...'
        
        self.mathThread.clearQueue()
        self._maths = {}
        
        contentDom = html.fromstring(content)
        
        # Find every <math> tag and store its corresponding data into my math
        # dictionary
        m_NS = '{http://www.w3.org/1998/Math/MathML}'
        i = 1
        for math in contentDom.findall('.//math'):
            mathContent = etree.tostring(math, method='xml')
            key = 'MathJax-Element-' + str(i) + '-Frame'
            
            data = {'mathml' : mathContent, 'parsed' : False, 'prose' : '', 'index' : i}
            self._maths[key] = data
            
            # Send it to my math parser thread
            self.mathThread.addToQueue((key, data))
            
            i += 1
    
    def getSpeech(self, htmlContent, configuration, progressCallback=None, checkCancelFunction=None):
        '''
        Returns a list of utterances to say the HTML content in the following 
        format:
        
        [[text, label], [text, label], ...]
        '''
        if progressCallback:
            progressCallback(0)
        
        htmlDom = html.fromstring(htmlContent)
        
        if progressCallback:
            progressCallback(3)
            
        return self._recursiveGetSpeech(htmlDom, configuration, progressCallback, checkCancelFunction)
    
    def setMathDatabase(self, filePath):
        '''
        Sets the math database it uses to parse the MathML to the one specified
        by the file path.
        '''
        print ' --> ! Changing math to:', filePath
        try:
            self.mathTTS = MathTTS(str(filePath))
            self.mathThread.setMathDatabase(self.mathTTS)
        except Exception:
            traceback.print_exc()
            self.mathTTS = None
            pass
        
    def _setMathData(self, mathData):
        '''
        Used by the math parsing thread to save the prose into my math 
        dictionary.
        '''
        self._mathsLock.lock()
        self._maths[mathData[0]] = mathData[1]
        self._mathsLock.unlock()
        
    def _recursiveGetSpeech(self, element, configuration, progressCallback=None, checkCancelFunction=None):
        
        # Use recursion to handle it.
        myList = []
        
        if element.text != None:
            myList.append([element.text, 'text'])
        
        if element.tag == 'img':
            
            altText = element.get('alt')
            if altText == None:
                altText = ' '
            
            if configuration.tag_image:
                    myList.append(['Image. ' + altText + '. End image.', 'image'])
            else:
                if len(altText.strip()) > 0:
                    myList.append([altText, 'image'])
                else:
                    myList.append(['Image.', 'image'])
            if element.tail != None:
                myList.append([element.tail, 'text'])
        
        
        # Make up my own progress callback function, which I will transform
        # into the actual progress I will report
        i = 0
        def myProgressCallback(percent):
            if progressCallback:
                p = (float(i) / len(element)) * 100.0
                p += (1.0 / len(element)) * percent
                progressCallback(int(p))
        
        for child in element:
            
            # Check to see if I need to stop abruptly
            if checkCancelFunction:
                print ' '
                if checkCancelFunction():
                    break
            
            i += 1
            
            testTag = child.tag.split('}')[-1]
            
            if testTag == 'span':
                if child.get('class') == 'MathJax':
                    # See if the MathML already got parsed. Otherwise, generate
                    # the speech on demand and save that.
                    key = child.get('id')
                    mathOutput = ''
                    if self._maths[key]['parsed']:
                        mathOutput = self._maths[key]['prose']
                    else:
                        mathOutput = self.mathTTS.parse(self._maths[key]['mathml'])
                        self._mathsLock.lock()
                        self._maths[key]['parsed'] = True
                        self._maths[key]['prose'] = mathOutput
                        self._mathsLock.unlock()
                    
                    if configuration.tag_math:
                        myList.append(['Math. ' + mathOutput + '. End math.', 'math'])
                    else:
                        myList.append([mathOutput, 'math'])
                else:
                    myList.extend(self._recursiveGetSpeech(child, configuration, myProgressCallback, checkCancelFunction))
                        
            elif testTag == 'img':
                
                altText = child.get('alt')
                if altText == None:
                    altText = ' '
                    
                if configuration.tag_image:
                    myList.append(['Image. ' + altText + '. End image.', 'image'])
                else:
                    if len(altText.strip()) > 0:
                        myList.append([altText, 'image'])
                    else:
                        myList.append(['Image.', 'image'])
                if child.tail != None:
                    myList.append([child.tail, 'text'])
                    
            elif testTag == 'script':
                # Don't do anything
                pass
            
            else:
                myList.extend(self._recursiveGetSpeech(child, configuration, myProgressCallback, checkCancelFunction))
                
        if element.tail != None:
            myList.append([element.tail, 'text'])
        
        if progressCallback:
            progressCallback(100)
            
        return myList