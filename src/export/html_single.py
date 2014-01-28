'''
Created on Dec 18, 2013

@author: Spencer Graffe
'''
import os
import base64
import urllib
import urllib2
import urlparse
import traceback

from PyQt4.QtCore import QThread
from lxml import etree
from lxml import html
import cairosvg

from export import ExportThread
from gui import configuration
from headless.renderer import HeadlessRendererThread
import misc

class HTMLSingleExportThread(ExportThread):
    '''
    Exports the content to a single HTML page with embedded images and math
    descriptions.
    '''
    
    # Arbitrary portions of the progress bar that the different stages take up
    PERCENT_CONVERTING_MATH = (0.0, 75.0)
    PERCENT_EMBED_IMAGES = (PERCENT_CONVERTING_MATH[1], 100.0)
    
    # Set the label for each of the states
    DESCRIPTION_CONVERTING_MATH = 'Converting equation '
    DESCRIPTION_EMBED_IMAGES = 'Embedding image '
    
    def __init__(self, document, htmlContent, tempDirectory):
        super(HTMLSingleExportThread, self).__init__(document, htmlContent, tempDirectory)
        self._lastProgress = -1
    
    @staticmethod
    def description():
        return 'HTML'
    
    @staticmethod
    def getDefaultPath(inputFilePath):
        '''
        Returns a possible default path for the given input file.
        '''
        return os.path.splitext(inputFilePath)[0] + '.html'
        
    def run(self):
        super(HTMLSingleExportThread, self).run()
        
        # Regenerate the content to use SVGs. They render better and more
        # consistently.
        headlessRender = HeadlessRendererThread(self._document.getMainPage(mathOutput='svg'))
        headlessRender.progress.connect(self._myOnProgress)
        headlessRender.start()
        while headlessRender.isRunning():
            if not self._running:
                headlessRender.stop()
            QThread.yieldCurrentThread()
        
        self._htmlContent = html.fromstring(unicode(headlessRender.getRenderedHTML(), encoding='utf-8'))
        
        if self._running:
            self._convertPageNumbersToH6(self._htmlContent)
            self._removeHighlighter(self._htmlContent)
            self._removeScripts(self._htmlContent)
            self._embedImages(self._htmlContent)
            self._embedFonts(self._htmlContent)
            self._convertMathEquations(self._htmlContent)
            
            if self._running:
                
                with open(self._filePath, 'wb') as f:
                    f.write(html.tostring(self._htmlContent))
                
                # Say that this export finished successfully
                self.success.emit()
                self.isSuccess = True
    
    def _myOnProgress(self, percent, label):
        self._reportProgress(percent, label)
        
    def _reportProgress(self, percent, label, alwaysUpdate=False):
        myPercent = int(percent)
        if (myPercent != self._lastProgress) or alwaysUpdate:
            self._lastProgress = myPercent
            self.progress.emit(myPercent, label)
    
    def _convertPageNumbersToH6(self, myHtml):
        '''
        Converts all of the page numbers into H6 headings so that they are
        easily navigable by JAWS and other screen-reading software.
        '''
        # Get all of the page numbers
        pageNumbers = myHtml.xpath("//p[@class='pageNumber']")
        
        # Convert each page number to an h6 element
        for p in pageNumbers:
            if not self._running:
                break
            p.tag = 'h6'
            p.attrib.pop('class')
    
    def _removeHighlighter(self, myHtml):
        '''
        Removes the highlighter from the document, if any.
        '''
        highlights = myHtml.xpath("//span[@id='npaHighlight']")
        highlightLines = myHtml.xpath("//span[@id='npaHighlightLine']")
        highlightSelections = myHtml.xpath("//span[@id='npaHighlightSelection']")
        
        for h in highlights:
            if not self._running:
                break
            self._replaceWithChildren(h)
        
        for h in highlightLines:
            if not self._running:
                break
            self._replaceWithChildren(h)
        
        for h in highlightSelections:
            if not self._running:
                break
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
    
    def _removeScripts(self, myHtml):
        '''
        Removes all the <script> elements from the document. No need for
        showing everyone the JavaScript.
        '''
        for e in myHtml.xpath('.//script'):
            e.getparent().remove(e)
    
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
            if not self._running:
                break
            defXMLs.append(etree.fromstring(html.tostring(d)))
        
        for i in range(len(equations)):
            QThread.yieldCurrentThread()
            try:
                if not self._running:
                    break
                myProgress = float(i) / float(len(equations))
                myProgress = myProgress * (self.PERCENT_CONVERTING_MATH[1] - self.PERCENT_CONVERTING_MATH[0]) + self.PERCENT_CONVERTING_MATH[0]
                myLabel = self.DESCRIPTION_CONVERTING_MATH + str(i + 1) + ' of ' + str(len(equations)) + '...'
                self._reportProgress(myProgress, myLabel, alwaysUpdate=True)
                
                # Get the prose for the math equation
                prose = ''
                for speech in self._document.generateSpeech(equations[i]):
                    prose += speech[0]
                    break
                
                # Remove all of the quotes from the math equation. JAWS reads
                # all of the quotes aloud, so it can get annoying
                punctuationToRemove = ['"', '.', ',', ';', ':', "'"]
                for p in punctuationToRemove:
                    prose = prose.replace(p, '')
                
                # Replace the span with an image representing the equation
                svgElem = equations[i].xpath('.//svg')[0]
                pngData = self._renderMathSVGToPNG(svgElem, defXMLs)
                dataString = 'data:image/png;base64,' + base64.b64encode(pngData)
                equations[i].tag = 'img'
                
                # Clear out all children and attributes from node
                for k in equations[i].attrib.keys():
                    del equations[i].attrib[k]
                for c in equations[i]:
                    c.getparent().remove(c)
                    
                # Set the image attributes
                equations[i].set('src', dataString)
                equations[i].set('alt', prose)
                equations[i].set('title', prose)
                
            except Exception as e:
                print 'Equation', i, 'did not parse correctly!', e
                traceback.print_exc()
            
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
                s.set('stroke', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
        for f in fills:
            if not ('none' in f.get('fill')):
                f.set('fill', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
        
        # Write to temp file, run CairoSVG through it, then push it out
        svgTemp = os.path.join(self._tempDirectory, 'tmp.svg')
        with open(svgTemp, 'wb') as f:
            f.write(etree.tostring(myMath, pretty_print=True))
        
        tmpURL = urlparse.urljoin('file:', urllib.pathname2url(svgTemp))
        
        return cairosvg.svg2png(url=tmpURL)
        
    def _embedImages(self, myHtml):
        '''
        It goes through all of the image tags, reads the original image it is
        referencing, and embeds the image data into the tag so that the document
        is portable.
        '''
        images = myHtml.xpath("//img")
        
        for i in range(len(images)):
            if not self._running:
                break
            
            myProgress = float(i) / float(len(images))
            myProgress = myProgress * (self.PERCENT_EMBED_IMAGES[1] - self.PERCENT_EMBED_IMAGES[0]) + self.PERCENT_EMBED_IMAGES[0]
            myLabel = self.DESCRIPTION_EMBED_IMAGES + str(i + 1) + ' of ' + str(len(images)) + '...'
            self._reportProgress(myProgress, myLabel)
            
            p = images[i].get('src')
            images[i].set('src', self._createEmbeddedImageDataURL(p))
    
    def _embedFonts(self, myHtml):
        '''
        For all of the @font-face directives in the CSS in the head, get all of
        the urls, download the font, and embed it.
        '''
        styles = myHtml.xpath(r".//head/style[@type='text/css']")
        fontPattern = r'@font-face[\s]*\{.*?\}'
        urlPattern = r"url\('(?P<url>.*?)'\)"    
        
        for style in styles:
            fontSplit = misc.SplitRegex(fontPattern, style.text)
            for match in fontSplit:
                sub = match['value']
                urlSplit = misc.SplitRegex(urlPattern, sub)
                for u_match in urlSplit:
                    url_sub = u_match['value']
                    myUrl = self._createEmbeddedFontDataURL(u_match['matchObj'].group('url'))
                    u_match['value'] = url_sub.replace(u_match['matchObj'].group('url'), myUrl).replace("'", '')
                match['value'] = str(urlSplit)
            
            style.text = str(fontSplit)
            
            
    def _createEmbeddedFontDataURL(self, fontURL):
        '''
        Reads in the font from fontURL and encodes to a data URI usable inside
        a url() for a font-face.
        '''
        ext = os.path.splitext(fontURL)[-1].replace('.', '').lower()
        dataString = 'data:application/x-font-' + ext + ';charset=utf-8;base64,'
        
        # Read the font
        f = urllib2.urlopen(fontURL)
        contents = base64.b64encode(f.read())
        dataString += contents
        
        return dataString
                    
    def _createEmbeddedImageDataURL(self, imageURL):
        '''
        Reads the image from imageURL and creates a data URL using the data. The
        data URL should be placed in the src attribute of an <img> tag.
        '''
        ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
        dataString = 'data:image/' + ext + ';base64,'
        
        # Read the image
        f = urllib2.urlopen(imageURL)
        contents = base64.b64encode(f.read())
        dataString += contents
        
        return dataString