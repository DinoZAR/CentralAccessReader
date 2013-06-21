'''
Created on Feb 20, 2013

@author: Spencer Graffe
'''
from lxml import etree, html
from HTMLParser import HTMLParser
from src.mathml.tts import MathTTS
from src.misc import program_path

# Namespace for XHTML
html_NS = '{http://www.w3.org/1999/xhtml}'

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
        self.mathTTS = None
        
    def prepare(self, content):
        '''
        Caches certain aspects of the content so that it can properly assign
        the content (like in the case of MathJax)
        '''
        self._maths = {}
        
        contentDom = html.fromstring(content)
        
        # Find every <math> tag and store its corresponding data into my math
        # dictionary
        m_NS = '{http://www.w3.org/1998/Math/MathML}'
        i = 1
        for math in contentDom.findall('.//math'):
            mathContent = etree.tostring(math, method='xml')
            key = 'MathJax-Element-' + str(i) + '-Frame'
            self._maths[key] = mathContent
            i += 1
    
    def getSpeech(self, htmlContent, configuration):
        '''
        Returns a list of utterances to say the HTML content in the following format:
        
        [[text, label], [text, label], ...]
        '''
        htmlDom = html.fromstring(htmlContent)
        return self._recursiveGetSpeech(htmlDom, configuration)
    
    def setMathDatabase(self, filePath):
        '''
        Sets the math database it uses to parse the MathML to the one specified
        by the file path.
        '''
        print ' --> ! Changing math to:', filePath
        try:
            self.mathTTS = MathTTS(filePath)
        except Exception:
            self.mathTTS = None
            pass
        
    def _recursiveGetSpeech(self, element, configuration):
        
        # Use recursion to handle it.
        myList = []
        
        if element.text != None:
            myList.append([element.text, 'text'])
        
        if element.tag == 'img':
            if configuration.tag_image:
                    myList.append(['Image. ' + element.get('alt') + '. End image.', 'image'])
            else:
                myList.append([element.get('alt'), 'image'])
            if element.tail != None:
                myList.append([element.tail, 'text'])
        
        for child in element:
            testTag = child.tag.split('}')[-1]
            
            if testTag == 'span':
                if child.get('class') == 'MathJax':
                    # Parse MathML and get output!
                    mathOutput = self.mathTTS.parse(self._maths[child.get('id')])
                    if configuration.tag_math:
                        myList.append(['Math. ' + mathOutput + '. End math.', 'math'])
                    else:
                        myList.append([mathOutput, 'math'])
                else:
                    myList.extend(self._recursiveGetSpeech(child, configuration))
                        
            elif testTag == 'img':
                if configuration.tag_image:
                    myList.append(['Image. ' + child.get('alt') + '. End image.', 'image'])
                else:
                    myList.append([child.get('alt'), 'image'])
                if child.tail != None:
                    myList.append([child.tail, 'text'])
                    
            elif testTag == 'script':
                # Don't do anything
                pass
            
            else:
                myList.extend(self._recursiveGetSpeech(child, configuration))
        
        if element.tail != None:
            myList.append([element.tail, 'text'])
            
        return myList
            
            