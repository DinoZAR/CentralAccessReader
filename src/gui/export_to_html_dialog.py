'''
Created on Oct 7, 2013

@author: Spencer Graffe
'''
import os
import base64
import urllib
import urllib2
import urlparse

from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QDialog, qApp
from PyQt4.QtWebKit import QWebPage

from lxml import etree
from lxml import html
import cairosvg

import misc
from forms.export_to_html_ui import Ui_ExportToHtmlDialog

class ExportToHtmlDialog(QDialog):
    '''
    This dialog shows the status of the document being converted to an HTML
    file. It also has the code for the actual conversion.
    '''

    def __init__(self, document, filePath, assigner, configuration, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        
        self.ui = Ui_ExportToHtmlDialog()
        self.ui.setupUi(self)
        
        self._document = document
        self._filePath = filePath
        self._assigner = assigner
        self._configuration = configuration
        
        # States
        self._canceled = False
        self._loaded = False
        self._loadProgress = 0
        self._mathTypeset = False
        self._mathProgress = 0
        self._finished = False
        
        # Signals/slots
        self.ui.cancelButton.clicked.connect(self.cancelPressed)
        
    def start(self):
        '''
        Starts the conversion process.
        '''
        
        def myLoadProgress(progress):
            self._loadProgress = progress
        
        def myLoadFinished(isLoaded):
            self._loaded = True
        
        webpage = QWebPage()
        webpage.loadProgress.connect(myLoadProgress)
        webpage.loadFinished.connect(myLoadFinished)
        
        url = misc.temp_path('import')
        baseUrl = QUrl.fromLocalFile(url)
        webpage.mainFrame().setHtml(self._document.getMainPage(mathOutput='svg'), baseUrl)
        
        while not self._loaded and not self._canceled:
            qApp.processEvents()
        
        self.ui.label.setText('Typesetting math equations...')
        
        if not self._canceled:
            
            # Wait for the MathJax to typeset
            while not self._mathTypeset and not self._canceled:
                qApp.processEvents()
                progress = int(webpage.mainFrame().evaluateJavaScript(misc.js_command('GetMathTypesetProgress', [])).toInt()[0])
                self.ui.progressBar.setValue(progress)
                self._mathTypeset = webpage.mainFrame().evaluateJavaScript(misc.js_command('IsMathTypeset', [])).toBool()
                
            # If I haven't canceled yet, let's convert the document
            if not self._canceled:            
                # Get the document back from the page, altered by MathJax
                myHtml = html.fromstring(unicode(webpage.mainFrame().evaluateJavaScript(misc.js_command('GetBodyHTML', [])).toString()))
                self._convertPageNumbersToH6(myHtml)
                self._removeHighlighter(myHtml)
                self._embedImages(myHtml)
                self._convertMathEquations(myHtml)
                
                root = html.Element('html')
                head = html.Element('head')
                body = html.Element('body')
                body.append(myHtml)
                root.append(head)
                root.append(body)
                
                self._insertCSS(head)
                
                with open(self._filePath, 'wb') as f:
                    f.write(html.tostring(root))
                
        self._finished = True
        self.close()
        
    def isSuccessful(self):
        '''
        Returns true if the export ran successfully.
        '''
        return self._finished and not self._canceled
    
    def _convertPageNumbersToH6(self, myHtml):
        '''
        Converts all of the page numbers into H6 headings so that they are
        easily navigable by JAWS and other screen-reading software.
        '''
        # Get all of the page numbers
        pageNumbers = myHtml.xpath("//p[@class='pageNumber']")
        
        # Convert each page number to an h6 element
        for p in pageNumbers:
            p.tag = 'h6'
            p.attrib.pop('class')
    
    def _insertCSS(self, head):
        '''
        Embeds the CSS information for this user into the HTML document.
        '''
        style = html.Element('style')
        style.set('type', 'text/css')
        style.text = self._configuration._writeCSS()
        head.append(style)
    
    def _removeHighlighter(self, myHtml):
        '''
        Removes the highlighter from the document, if any.
        '''
        highlights = myHtml.xpath("//span[@id='npaHighlight']")
        highlightLines = myHtml.xpath("//span[@id='npaHighlightLine']")
        
        for h in highlights:
            self._replaceWithChildren(h)
        
        for h in highlightLines:
            self._replaceWithChildren(h)
            
    def _replaceWithChildren(self, elem):
        '''
        Replaces the element with its own children.
        '''
        p = elem.getparent()
        i = p.index(elem)
        
        # Mess with the text
        if elem.text is not None:
            firstHalf = p[:i]
            if len(firstHalf) > 0:
                if firstHalf[-1].tail is not None:
                    firstHalf[-1].tail += elem.text
                else:
                    firstHalf[-1].tail = elem.text
            else:
                if p.text is not None:
                    p.text += elem.text
                else:
                    p.text = elem.text
        
        # Mess with the tail
        if elem.tail is not None:
            if len(elem) > 0:
                if elem[-1].tail is not None:
                    elem[-1].tail += elem.tail
                else:
                    elem[-1].tail = elem.tail
            else:
                if elem.text is not None:
                    p.text += elem.tail
                else:
                    p.text = elem.tail
        
        # Get all of the children of element and insert
        # them in the parent, in correct order
        childs = []
        for c in elem:
            childs.append(c)
        childs.reverse()
        for c in childs:
            p.insert(i, c)
            
        # Remove the element
        p.remove(elem)
    
    def _convertMathEquations(self, myHtml):
        '''
        Converts the Math equations inside (presumed to be SVGs generated by
        MathJax) into embedded PNGs with the math prose as alternate text.
        '''
        equations = myHtml.xpath("//span[@class='mathmlEquation']")
        
        # Get the <defs> in the hidden SVGs (wherever they may be)
        defs = myHtml.xpath('//svg/defs')
        defXMLs = []
        for d in defs:
            defXMLs.append(etree.fromstring(html.tostring(d)))
        
        for i in range(len(equations)):
            self.ui.label.setText('Converting equation ' + str(i + 1) + ' of ' + str(len(equations)) + '...')
            self.ui.progressBar.setValue((float(i) / float(len(equations)) * 50.0) + 50.0)
            
            # Get the SVG graphic inside the span and convert to PNG
            svg = equations[i].xpath('.//svg')[0]
            pngContents = self._renderMathSVGToPNG(svg, defXMLs)
            dataString = 'data:image/png;base64,' + base64.b64encode(pngContents)
            
            # Get the prose for the math equation
            prose = ''
            for speech in self._assigner.generateSpeech(equations[i], self._configuration):
                prose += speech[0]
                break
            
            # Remove all children of the soon-to-be image
            for child in equations[i]:
                child.getparent().remove(child)
            
            # Transform math equation into an image with prose as alt text
            equations[i].tag = 'img'
            equations[i].set('src', dataString)
            equations[i].set('alt', prose)
            equations[i].set('title', prose)
            
    def _renderMathSVGToPNG(self, svg, defXMLs):
        '''
        Renders the Math SVG (an lxml Element) into a PNG. Returns the
        bytestring containing the PNG data.
        '''
        # Create my own SVG with valid namespaces
        SVG_NS = '{http://www.w3.org/2000/svg}'
        XLINK_NS = '{http://www.w3.org/1999/xlink}'
        NS_MAP = {None : SVG_NS[1:-1], 'xlink' : XLINK_NS[1:-1]}
        myMath = etree.Element('{0}svg'.format(SVG_NS), nsmap=NS_MAP)
        
        # Copy all attributes
        for attr in svg.attrib.keys():
            try:
                myMath.attrib[attr] = svg.attrib[attr]
            except:
                pass
            
        # Copy all elements
        for m in svg:
            myMath.append(m)
            
        # Change the viewbox attribute of <svg> to viewBox
        if 'viewbox' in myMath.attrib:
            data = myMath.get('viewbox')
            myMath.attrib.pop('viewbox')
            myMath.set('viewBox', data)
            
        # Insert the defs into my math equation
        myDef = etree.SubElement(myMath, 'defs')
        for d in defXMLs:
            for p in d:
                myDef.append(etree.fromstring(etree.tostring(p)))
        
        # In my math equation, every <use href> must be changed to 
        # <use xlink:href>
        uses = myMath.xpath('.//use[@href]')
        for u in uses:
            data = u.get('href')
            u.attrib.pop('href')
            u.set('{0}href'.format(XLINK_NS), data)
        
        # Change the color of every element in the svg to the text color defined
        # in user preferences
        strokes = myMath.xpath(".//*[@stroke]")
        fills = myMath.xpath(".//*[@fill]")
        for s in strokes:
            if not ('none' in s.get('stroke')):
                s.set('stroke', self._configuration._createRGBStringFromQColor(self._configuration.color_contentText))
        for f in fills:
            if not ('none' in f.get('fill')):
                f.set('fill', self._configuration._createRGBStringFromQColor(self._configuration.color_contentText))
        
        # Write to temp file, run CairoSVG through it, then push it out
        with open(misc.temp_path('tmp.svg'), 'wb') as f:
            f.write(etree.tostring(myMath, pretty_print=True))
        
        tmpURL = urlparse.urljoin('file:', urllib.pathname2url(misc.temp_path('tmp.svg')))
        
        return cairosvg.svg2png(url=tmpURL)
        
    def _embedImages(self, myHtml, progressHook=None, cancelHook=None):
        '''
        It goes through all of the image tags, reads the original image it is
        referencing, and embeds the image data into the tag so that the document
        is portable.
        '''
        images = myHtml.xpath("//img")
        
        for i in range(len(images)):
            self.ui.label.setText('Embedding image ' + str(i + 1) + ' of ' + str(len(images)) + '...')
            self.ui.progressBar.setValue((float(i) / float(len(images)) * 50.0))
            
            if cancelHook is not None:
                if cancelHook():
                    return
            
            if progressHook is not None:
                progressHook(int(float(i + 1) * float(len(images)) * 100.0))
            
            p = images[i].get('src')
            images[i].set('src', self._createEmbeddedDataURL(p))
    
    def _createEmbeddedDataURL(self, imageURL):
        '''
        Reads the image from imageURL and creates a data URL using the data. The
        data URL should be placed in the src attribute of an <img> tag.
        '''
        ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
        elem = html.Element('img')
    
        dataString = 'data:image/' + ext + ';base64,'
        
        # Read the image
        myPath = urllib2.unquote(imageURL)
        contents = ''
        with open(myPath, 'rb') as f:
            contents = f.read()
        contents = base64.b64encode(contents)
        dataString += contents
        
        return dataString

    def cancelPressed(self):
        self.close()