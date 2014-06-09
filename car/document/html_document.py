'''
Created on Feb 20, 2014

@author: Spencer Graffe
'''
from lxml import html

from car.document import Document

class HTMLDocument(Document):
    '''
    Allows HTML to be rendered and the interaction managed by CAR. It can accept
    a file path or an HTML string. If the file path is None, then it will try
    to read from the HTML string.
    '''
    
    def __init__(self, filePath, progressHook, cancelHook, htmlString=''):
        Document.__init__(self, filePath, progressHook, cancelHook)
        
        self._contentDOM = html.Element('body')
        
        if filePath is not None:
            with open(filePath, 'r') as f:
                htmlString = f.read()
                
        myDom = html.fromstring(htmlString)
        
        # Check if it already has a body. If so, grab all the children off of
        # that and put it on my body
        query = myDom.xpath('.//body')
        if len(query) > 0:
            for e in query[0]:
                self._contentDOM.append(e)
        else:
            self._contentDOM.append(myDom)
            
        # The name is the textual content of the title tag. If one is not there,
        # then it shall be called Untitled
        query = myDom.xpath('.//title')
        if len(query) > 0:
            self._name = query[0].text
        else:
            self._name = 'Untitled'
        
        # Do this at the end of everything
        self._mapMathEquations()