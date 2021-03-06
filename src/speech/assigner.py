'''
Created on Feb 20, 2013

@author: Spencer Graffe
'''
import traceback
from HTMLParser import HTMLParser
from lxml import etree, html
from PyQt4.QtCore import QMutex, QThread, pyqtSignal
try:
    from mathml_fast.tts import MathTTS
except ImportError:
    from mathml.tts import MathTTS

from speech.math_parser_thread import MathParserThread
import time

# Namespace for XHTML
html_NS = '{http://www.w3.org/1999/xhtml}'

class PrepareSpeechThread(QThread):
    '''
    This thread prepares the HTML given to it into an output list that should
    be queued into the TTS engine. It will report progress and say when it is
    finished.
    '''
    reportProgress = pyqtSignal(int)
    
    def __init__(self, assigner, configuration, htmlToConvert, speechSignals):
        QThread.__init__(self)
        self._assigner = assigner
        self._config = configuration
        self._html = html.fromstring(htmlToConvert)
        self._stop = False
        self._startQueuing = speechSignals['startQueuing']
        self._addToQueue = speechSignals['addToQueue']
        self._doneQueuing = speechSignals['doneQueuing']
        
    def run(self):
        print 'preparer: started queuing'
        self._startQueuing.emit()
        for speech in self._assigner.generateSpeech(self._html, self._config):
            print 'preparer: Queuing some speech'
            self._addToQueue.emit(speech[0], speech[1])
            if self._stop:
                break
            QThread.yieldCurrentThread()
        self._doneQueuing.emit()
        print 'preparer: done!'
        
    def stop(self):
        print 'Stopping preparer...'
        self._stop = True
            
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
        
    def generateSpeech(self, element, configuration):
        '''
        Creates a generator that gets the speech output for the HTML element and
        configuration.
        '''
        
        if element.text != None:
            yield [element.text, 'text']
        
        if element.tag == 'img':
            altText = element.get('alt')
            if altText == None:
                altText = ' '
            
            if configuration.tag_image:
                    yield ['Image. ' + altText + '. End image.', 'image']
            else:
                if len(altText.strip()) > 0:
                    yield [altText, 'image']
                else:
                    yield ['Image.', 'image']
                    
            if element.tail != None:
                yield [element.tail, 'text']
        
        for child in element:
            testTag = child.tag.split('}')[-1]
            if (testTag == 'span') and (child.get('class') is not None):
                if 'MathJax' in child.get('class'):
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
                        yield ['Math. ' + mathOutput + '. End math.', 'math']
                    else:
                        yield [mathOutput, 'math']
                else:
                    for speech in self.generateSpeech(child, configuration):
                        yield speech
                        
            elif testTag == 'img':
                altText = child.get('alt')
                if altText == None:
                    altText = ' '
                    
                if configuration.tag_image:
                    yield ['Image. ' + altText + '. End image.', 'image']
                else:
                    if len(altText.strip()) > 0:
                        yield [altText, 'image']
                    else:
                        yield ['Image.', 'image']
                if child.tail != None:
                    yield [child.tail, 'text']
                    
            elif testTag == 'script':
                # Don't do anything
                pass
            
            else:
                for speech in self.generateSpeech(child, configuration):
                    yield speech
                
        if element.tail != None:
            yield [element.tail, 'text']
