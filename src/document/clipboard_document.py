'''
Created on Dec 16, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QApplication
from lxml import etree, html
from document import Document, html_cleaner
from document.docx.paragraph import convertOMMLToMathML

class ClipboardDocument(Document):
    '''
    This document will display the contents of the clipboard.
    '''

    def __init__(self, filePath, progressHook, cancelHook):
        Document.__init__(self, filePath, progressHook, cancelHook)
        self._name = 'Clipboard'
        
        self._progressHook(0, 'Reading from clipboard...')
        
        mime = QApplication.clipboard().mimeData()
        
        if mime.hasHtml():
            myHtml = html_cleaner.clean(html.fromstring(unicode(mime.html())), progressHook=self._progressHook, cancelHook=self._cancelHook)
            self._contentDOM.append(myHtml)
            
        elif mime.hasText():
            self._contentDOM.text = unicode(QApplication.clipboard().text())
        
        else:
            self._contentDOM.text = 'Did not recognize content in clipboard.'
        
        # Post-processing stuff
        self.extractOMMLFromComments()
        self.surroundMathInSpan()
            
        self._mapMathEquations()
    
    def extractOMMLFromComments(self):
        '''
        Goes through the content DOM and checks the comments to see if they have
        OMML embedded in them. If they do, extract it, run my XSLT through it
        to convert to MathML and insert that.
        '''
        #convertOMMLToMathML(ommlNode)
        # Go through all of the comment tags and find some OMML.
        # If I find it, convert to MathML and insert it before comment
        comments = self._contentDOM.xpath('.//comment()')
        
        START_TAG = '<m:oMath>'
        END_TAG = '</m:oMath>'
        
        for c in comments:
            
            firstTag = c.text.find(START_TAG)
            if firstTag >= 0:
                secondTag = c.text.find(END_TAG, firstTag)
                if secondTag >= 0:
                    
                    secondTag += len(END_TAG)
                    baseOmml = c.text[firstTag:secondTag]
                    namespace = 'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"'
                    baseOmml = ' '.join(iter([baseOmml[:len(START_TAG) - 1], namespace, baseOmml[len(START_TAG) - 1:]]))                    
                    
                    omml = etree.fromstring(baseOmml)
                    
                    # For all of the <m:r>'s in it, surround the text with a
                    # <m:t>, since that what it looks like in Word
                    ommlRows = omml.xpath('.//m:r', namespaces={'m' : 'http://schemas.openxmlformats.org/officeDocument/2006/math'})
                    for r in ommlRows:
                        
                        # Get the text content, add to a <m:t>, and clear out
                        # rest of formatting garbage
                        myText = ''
                        for s in r.itertext():
                            myText += s
                        r.clear()
                        
                        ommlT = etree.SubElement(r, '{0}t'.format('{http://schemas.openxmlformats.org/officeDocument/2006/math}'))
                        ommlT.text = myText
                    
                    mathml = convertOMMLToMathML(omml)
                    
                    c.addnext(mathml)
                    
                    print etree.tostring(c.getparent(), pretty_print=True)
                    
                    # Delete the image after it if there is one. That is just an
                    # image of the equation.
                    current = mathml.getnext()
                    while current is not None:
                        if current.tag == 'img':
                            self.removeElement(current)
                            current = None
                        else:
                            current = current.getnext()
                    
            # Remove comment
            self.removeElement(c)
    
    def surroundMathInSpan(self):
        '''
        Finds all of the MathML and surrounds it in a math span to make it
        selectable, if it isn't already.
        '''
        m_NS = 'http://www.w3.org/1998/Math/MathML'
        for math in self._contentDOM.xpath('.//math | .//m:math', namespaces={'m' : m_NS}):
            
            # Wrap a span around the math
            mathSpan = etree.Element('span')
            mathSpan.set('class', 'mathmlEquation')
            math.addprevious(mathSpan)
            mathSpan.append(math)
            
            # Get the tail and append it to the span if necessary
            if math.tail is not None:
                mathSpan.tail = math.tail
                math.tail = ''
            
    def removeElement(self, elem):
        '''
        This removes an element while preserving the tail text.
        '''
        if elem.tail is not None:
            
            # Try the previous sibling
            if elem.getprevious() is not None:
                if elem.getprevious().tail is not None:
                    elem.getprevious().tail += elem.tail
                else:
                    elem.getprevious().tail = elem.tail
                    
            # Try the parent
            elif elem.getparent() is not None:
                if elem.getparent().text is not None:
                    elem.getparent().text += elem.tail
                else:
                    elem.getparent().text = elem.tail
                
        elem.getparent().remove(elem)
        
        