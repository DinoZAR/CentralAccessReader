'''
Created on Feb 20, 2013

@author: Spencer Graffe
'''
from lxml import etree, html
from HTMLParser import HTMLParser
from src.mathml.tts import MathTTS
from src.misc import resource_path, clean_XML_input

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
        self.mathTTS = MathTTS(resource_path('mathml/parser_pattern_database.txt'))
        
        
    def prepare(self, content):
        '''
        Caches certain aspects of the content so that it can properly assign
        the content (like in the case of MathJax)
        '''
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
    
    def getSpeech(self, htmlContent):
        '''
        Returns a list of utterances to say the HTML content in the following format:
        
        [[text, label], [text, label], ...]
        '''
        print 'HTML Content:', htmlContent
        htmlDom = html.fromstring(htmlContent)
        return self._recursiveGetSpeech(htmlDom)
        
    def _recursiveGetSpeech(self, element):
        
        # Use recursion to handle it.
        myList = []
        
        if element.text != None:
            myList.append([clean_XML_input(element.text.encode('utf8')), 'text'])
        
        for child in element:
            testTag = child.tag.split('}')[-1]
            
            if testTag == 'span':
                if child.get('class') == 'MathJax':
                    # Parse MathML and get output!
                    mathOutput = self.mathTTS.parse(self._maths[child.get('id')])
                    myList.append([mathOutput, 'math'])
                else:
                    myList.extend(self._recursiveGetSpeech(child))
                        
            elif testTag == 'img':
                myList.append(['Image. ' + child.get('alt'), 'image'])
                if child.tail != None:
                    myList.append([clean_XML_input(child.tail.encode('utf8')), 'text'])
            
            else:
                myList.extend(self._recursiveGetSpeech(child))
        
        if element.tail != None:
            myList.append([clean_XML_input(element.tail.encode('utf8')), 'text'])
            
        return myList
            
            