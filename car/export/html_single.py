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

try:
    from PyQt4.QtCore import QThread
except ImportError:
    from PyQt5.QtCore import QThread
from lxml import etree
from lxml import html
from car import cairosvg

from car.export import ExportThread
from car.gui import configuration
from car.headless.renderer import HeadlessRendererThread
from car import misc


class PNGHTMLSingleExportThread(ExportThread):
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
        super(PNGHTMLSingleExportThread, self).__init__(document, htmlContent, tempDirectory)
        self._lastProgress = -1

    @staticmethod
    def description():
        return '[HTML] PNG: JAWS 15/NVDA/Windows Eyes'

    @staticmethod
    def getDefaultPath(inputFilePath):
        '''
        Returns a possible default path for the given input file.
        '''
        return os.path.splitext(inputFilePath)[0] + '.html'

    def run(self):
        super(PNGHTMLSingleExportThread, self).run()

        mainHtml = html.fromstring(self._document.getMainPage(mathOutput='svg'))

        if configuration.getBool('AddTOC', True):
            self._createTableOfContents(mainHtml)

        # Regenerate the content to use SVGs. They render better and more
        # consistently.
        headlessRender = HeadlessRendererThread(html.tostring(mainHtml))
        headlessRender.progress.connect(self._myOnProgress)
        headlessRender.start()
        while headlessRender.isRunning():
            if not self._running:
                headlessRender.stop()
            QThread.yieldCurrentThread()

        self._htmlContent = html.fromstring(unicode(headlessRender.getRenderedHTML(), encoding='utf-8'))

        if self._running:
            self._convertPageNumbersToH6(self._htmlContent)
            self._removeAltTextIfIgnored(self._htmlContent)
            self._removeHighlighter(self._htmlContent)
            self._removeScripts(self._htmlContent)
            self._embedImages(self._htmlContent)
            self._embedFonts(self._htmlContent)
            self._embedCSS(self._htmlContent)
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


    def _createTableOfContents(self, myHtml):
        '''
        Create a table of contents.
        '''
        # Generate a table of contents from the headings
        headingMap = {'h1': 1,
                      'h2': 2,
                      'h3': 3,
                      'h4': 4,
                      'h5': 5}
        headings = []
        leastHeadingLevel = 500000
        for ev, elem in etree.iterwalk(myHtml, events=('end',)):
            if elem.tag in headingMap:
                headings.append((headingMap[elem.tag], self._getTextInsideElement(elem), elem))
                if headingMap[elem.tag] < leastHeadingLevel:
                    leastHeadingLevel = headingMap[elem.tag]

        navRoot = html.Element('nav')
        navRoot.set('role', 'navigation')
        navRoot.set('class', 'table-of-contents')

        # Check if need warning about page number conversion
        elem1 = html.Element('p')
        elem1.text = 'Screen Reader Users: This document has been optimized for use with JAWS 15 and older, ' \
                        'NVDA, and Windows Eyes. Equations are formatted as images with equation information saved ' \
                        'as alt-text.'
        navRoot.append(elem1)

        query = myHtml.find(".//p[@class='pageNumber']")
        if query is not None:
            elem2 = html.Element('p')
            elem2.text = 'Page numbers have been converted to heading 6.'
            navRoot.append(elem2)

        elem = html.Element('h1')
        elem.text = 'Contents:'
        navRoot.append(elem)

        elem = html.Element('ul')
        navRoot.append(elem)

        currentLevel = 1
        headingId = 0
        parent = elem
        for h in headings:

            # Indent/deindent to right level
            while h[0] != currentLevel:
                if currentLevel < h[0]:
                    elem = html.Element('ul')
                    parent.append(elem)
                    parent = elem
                    currentLevel += 1

                if currentLevel > h[0]:
                    parent = parent.getparent()
                    currentLevel -= 1


            # Make element for the thing
            elem = html.Element('li')
            link = html.Element('a')
            link.set('href', '#heading' + str(headingId))
            elem.append(link)
            link.text = h[1]

            # Set the link
            link.set('href', '#heading' + str(headingId))
            h[2].set('id', 'heading' + str(headingId))
            headingId += 1

            parent.append(elem)

        # Insert TOC into document
        myHtml.insert(0, navRoot)

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

    def _removeAltTextIfIgnored(self, myHtml):
        '''
        Removes the alt text from images if the settings say to remove it.
        '''
        if configuration.getBool('IgnoreAltText', False):
            imgs = myHtml.xpath('//img')
            for i in imgs:
                i.attrib.pop('alt', None)
                i.attrib.pop('title', None)

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
                punctuationToRemove = ['"', ',', ';', ':', "'"]
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
                if ':' in attr:
                    myAttr = attr[attr.find(':') + 1:]
                    myMath.set(myAttr, svg.get(attr))
                else:
                    myMath.set(attr, svg.get(attr))

            except Exception as ex:
                print 'Could not copy SVG attribute:', ex

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

            try:
                p = images[i].get('src')
                images[i].set('src', self._createEmbeddedImageDataURL(p))
            except urllib2.URLError as e:
                # The URL may already be embedded, so don't do it twice.
                pass

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


    def _embedCSS(self, myHtml):
        '''
        Embeds the CSS into the HTML.
        '''
        cssLinks = myHtml.findall(".//link[@rel='stylesheet']")
        head = myHtml.find(".//head")

        for css in cssLinks:
            print

            # Download the stylesheet
            f = urllib2.urlopen(css.get('href'))
            contents = f.read()

            # Create a new element to save the style in
            newCss = html.Element('style')
            newCss.set('type', 'text/css')
            newCss.text = contents
            head.append(newCss)

            # Remove the link
            css.getparent().remove(css)

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
        data URL should be placed in the car attribute of an <img> tag.
        '''
        ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
        dataString = 'data:image/' + ext + ';base64,'

        # Read the image
        f = urllib2.urlopen(imageURL)
        contents = base64.b64encode(f.read())
        dataString += contents

        return dataString

    def _getTextInsideElement(self, elem):
        myText = ''
        if elem.text is not None:
            myText += elem.text

        for c in elem:
            myText += self._getTextInsideElement(c)
            if c.tail is not None:
                myText += c.tail

        return myText

class FlexHTMLSingleExportThread(ExportThread):
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
        super(FlexHTMLSingleExportThread, self).__init__(document, htmlContent, tempDirectory)
        self._lastProgress = -1

    @staticmethod
    def description():
        return '[HTML] Flex'

    @staticmethod
    def getDefaultPath(inputFilePath):
        '''
        Returns a possible default path for the given input file.
        '''
        return os.path.splitext(inputFilePath)[0] + '.html'

    def run(self):
        super(FlexHTMLSingleExportThread, self).run()

        mainHtml = html.fromstring(self._document.getMainPage(mathOutput='svg'))

        if configuration.getBool('AddTOC', True):
            self._createTableOfContents(mainHtml)

        # Regenerate the content to use SVGs. They render better and more
        # consistently.
        keepMathML = True
        if not keepMathML:
            headlessRender = HeadlessRendererThread(html.tostring(mainHtml))
            headlessRender.progress.connect(self._myOnProgress)
            headlessRender.start()
            while headlessRender.isRunning():
                if not self._running:
                    headlessRender.stop()
                QThread.yieldCurrentThread()

        #self._htmlContent = html.fromstring(unicode(headlessRender.getRenderedHTML(), encoding='utf-8'))
        self._htmlContent = mainHtml
        if self._running:
            self._convertPageNumbersToH6(self._htmlContent)
            self._removeAltTextIfIgnored(self._htmlContent)
            self._removeHighlighter(self._htmlContent)
            self._removeScripts(self._htmlContent)
            self._embedImages(self._htmlContent)
            self._embedCSS(self._htmlContent)
            self._embedOptions(self._htmlContent)
            self._convertMathEquations(self._htmlContent,keepMathML)

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

    def _createTableOfContents(self, myHtml):
        '''
        Create a table of contents.
        '''
        # Generate a table of contents from the headings
        headingMap = {'h1': 1,
                      'h2': 2,
                      'h3': 3,
                      'h4': 4,
                      'h5': 5}
        headings = []
        leastHeadingLevel = 500000
        for ev, elem in etree.iterwalk(myHtml, events=('end',)):
            if elem.tag in headingMap:
                headings.append((headingMap[elem.tag], self._getTextInsideElement(elem), elem))
                if headingMap[elem.tag] < leastHeadingLevel:
                    leastHeadingLevel = headingMap[elem.tag]

        navRoot = html.Element('nav')
        navRoot.set('role', 'navigation')
        navRoot.set('class', 'table-of-contents')

        # Check if need warning about page number conversion
        elem1 = html.Element('p')
        elem1.text = 'Screen Reader Users: HTML Flex has been optimized for IE + JAWS 16 and iOS and Mac + VoiceOver. ' \
                        'An internet connection is required.'
        navRoot.append(elem1)

        query = myHtml.find(".//p[@class='pageNumber']")
        if query is not None:
            elem2 = html.Element('p')
            elem2.text = 'Page numbers have been converted to heading 6.'
            navRoot.append(elem2)

        elem = html.Element('h1')
        elem.text = 'Contents:'
        navRoot.append(elem)

        elem = html.Element('ul')
        navRoot.append(elem)

        currentLevel = 1
        headingId = 0
        parent = elem
        for h in headings:

            # Indent/deindent to right level
            while h[0] != currentLevel:
                if currentLevel < h[0]:
                    elem = html.Element('ul')
                    parent.append(elem)
                    parent = elem
                    currentLevel += 1

                if currentLevel > h[0]:
                    parent = parent.getparent()
                    currentLevel -= 1


            # Make element for the thing
            elem = html.Element('li')
            link = html.Element('a')
            link.set('href', '#heading' + str(headingId))
            elem.append(link)
            link.text = h[1]

            # Set the link
            link.set('href', '#heading' + str(headingId))
            h[2].set('id', 'heading' + str(headingId))
            headingId += 1

            parent.append(elem)

        # Insert TOC into document
        myHtml.insert(0, navRoot)

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

    def _removeAltTextIfIgnored(self, myHtml):
        '''
        Removes the alt text from images if the settings say to remove it.
        '''
        if configuration.getBool('IgnoreAltText', False):
            imgs = myHtml.xpath('//img')
            for i in imgs:
                i.attrib.pop('alt', None)
                i.attrib.pop('title', None)

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

    def _convertMathEquations(self, myHtml, keepMathML=False):
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

                if keepMathML:
                    pass

                else:

                    # Get the prose for the math equation
                    prose = ''
                    for speech in self._document.generateSpeech(equations[i]):
                        prose += speech[0]
                        break

                    # Remove all of the quotes from the math equation. JAWS reads
                    # all of the quotes aloud, so it can get annoying
                    punctuationToRemove = ['"', ',', ';', ':', "'"]
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
                if ':' in attr:
                    myAttr = attr[attr.find(':') + 1:]
                    myMath.set(myAttr, svg.get(attr))
                else:
                    myMath.set(attr, svg.get(attr))

            except Exception as ex:
                print 'Could not copy SVG attribute:', ex

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

            try:
                p = images[i].get('src')
                images[i].set('src', self._createEmbeddedImageDataURL(p))
            except urllib2.URLError as e:
                # The URL may already be embedded, so don't do it twice.
                pass

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

    def _embedOptions(self, myHtml):
        '''
        :param myHtml:
        embeds color and font options pickers into HTML, as well as the MathJax script
        '''
        head = myHtml.find(".//head")

        accordionScript = html.Element('script')
        accordionScript.set('type','text/javascript')
        accordionScript.text = '''    var accordionItems = new Array();

    function init() {

      // Grab the accordion items from the page
      var divs = document.getElementsByTagName( 'div' );
      for ( var i = 0; i < divs.length; i++ ) {
        if ( divs[i].className == 'accordionItem' ) accordionItems.push( divs[i] );
      }

      // Assign onclick events to the accordion item headings
      for ( var i = 0; i < accordionItems.length; i++ ) {
        var h2 = getFirstChildWithTagName( accordionItems[i], 'H2' );
        h2.onclick = toggleItem;
      }

      // Hide all accordion item bodies except the first
      for ( var i = 1; i < accordionItems.length; i++ ) {
        accordionItems[i].className = 'accordionItem hide';
      }
    }

    //toggles visibility of item
    function toggleItem() {
      var itemClass = this.parentNode.className;

      // Hide all items
      for ( var i = 0; i < accordionItems.length; i++ ) {
        accordionItems[i].className = 'accordionItem hide';
      }

      // Show this item if it was previously hidden
      if ( itemClass == 'accordionItem hide' ) {
        this.parentNode.className = 'accordionItem';
      }
    }

    function getFirstChildWithTagName( element, tagName ) {
      for ( var i = 0; i < element.childNodes.length; i++ ) {
        if ( element.childNodes[i].nodeName == tagName ) return element.childNodes[i];
      }
    }
'''

        head.append(accordionScript)

        mathjaxScript = html.Element('script')
        mathjaxScript.set('type','text/javascript')
        mathjaxScript.text = '''
//converts MathML to MathJax if necessary, along with any other browser-specific considerations
function automathjax()
{

//determine which browser is being used
var isOpera = !!window.opera || navigator.userAgent.indexOf(' OPR/') >= 0;
    // Opera 8.0+ (UA detection to detect Blink/v8-powered Opera)
var isFirefox = typeof InstallTrigger !== 'undefined';   // Firefox 1.0+
var isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0;
    // At least Safari 3+: "[object HTMLElementConstructor]"
var isChrome = !!window.chrome && !isOpera;              // Chrome 1+
var isIE = /*@cc_on!@*/false || !!document.documentMode; // At least IE6


//decide if math needs to be set in block format and if MathJax needs to be run
	if (isIE || isFirefox || isChrome || isOpera) {

		RunMathJax();

	} else if (isSafari) {

    //nothing needs to be done, Safari properly reads/displays MathML

	} else {

		RunMathJax();

	}
}

function RunMathJax()
{
	var sr = document.createElement('script');
	var scr = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML';
	var t = 'text/javascript'
	sr.src = scr;
	sr.type = t
	var hh = document.getElementsByTagName('head')[0];
	hh.appendChild(sr);
}

'''
        head.append(mathjaxScript)

        accordionContents = ''' <div class="accordionItem">
      <h2>+ Visibility Options</h2>
      <div>

        <!-- background color selection -->
        <form name="bgcolorForm">Background Color:
          <select onChange="if(this.selectedIndex!=0)
            document.bgColor=this.options[this.selectedIndex].value">
            <option value="choose">set background color
            <option class="bla" value="000000">black
            <option class="wht" value="FFFFFF">white
            <option class="brn" value="884900">brown
            <option class="red" value="B60000">red
            <option class="pnk" value="A11C80">pink
            <option class="ppl" value="6C2ADB">purple
            <option class="blu" value="0045E7">blue
            <option class="cyn" value="00617B">cyan
            <option class="grn" value="0F6800">green
            <option class="gry" value="595959">grey
            </select></form>

        <!-- text color selection -->
        <form name="textcolorForm">Text Color:
          <select onChange="if(this.selectedIndex!=0)
            document.body.text=this.options[this.selectedIndex].value">
            <option value="choose">set text color
            <option class="bla" value="000000">black
            <option class="wht" value="FFFFFF">white
            <option class="brn" value="884900">brown
            <option class="red" value="B60000">red
            <option class="pnk" value="A11C80">pink
            <option class="ppl" value="6C2ADB">purple
            <option class="blu" value="0045E7">blue
            <option class="cyn" value="00617B">cyan
            <option class="grn" value="0F6800">green
            <option class="gry" value="595959">grey
          </select></form>

        <!-- text size selection -->
        <form name="textSizeForm">Text Size:
          <select onChange="if(this.selectedIndex!=0)
          document.body.style.fontSize=this.options[this.selectedIndex].value">
            <option value="choose">set text size
            <option value="75%">small
            <option value="100%">medium (default size)
            <option value="150%">large
            <option value="200%">extra large
          </select></form>

        <!-- font selection -->
        <form name="fontForm">Font:
          <select onChange="if(this.selectedIndex!=0)
          document.body.style.fontFamily=this.options[this.selectedIndex].value">
            <option value="choose">set font
            <option class="ar" value="Arial">Arial
            <option class="ba" value="Book Antiqua">Book Antiqua
            <option class="ga" value="Georgia">Georgia
            <option class="ta" value="Tahoma">Tahoma
            <option class="ti" value="Times New Roman">Times New Roman
            <option class="tr" value="Trebuchet MS">Trebuchet MS
            <option class="ve" value="Verdana">Verdana
          </select></form>
      </div>
    </div>
'''

        accordion = html.fromstring(accordionContents)
        head.append(accordion)

        body = myHtml.find(".//body")
        body.set('onload','automathjax();init()')

    def _embedCSS(self, myHtml):
        '''
        Embeds the CSS into the HTML.
        '''
        cssLinks = myHtml.findall(".//link[@rel='stylesheet']")
        head = myHtml.find(".//head")

        #gets rid of css links in myHtml
        for css in cssLinks:
            print

            # Download the stylesheet
            f = urllib2.urlopen(css.get('href'))

            # Remove the link
            css.getparent().remove(css)

        #insert Flex export styles
        contentStyle = html.Element('style')
        contentStyle.set('type','text/css')
        contentStyle.text = '''h1
{
text-align: center;
font-size: 300%;
}

h2
{
border-style: dashed;
border-width: 0px 0px 1px 0px;
padding: 15px;
font-size: 200%;
}

h3
{
padding: 10px;
font-size: 175%;
}

h4
{
font-size: 150%;
}

a.button {
text-decoration: none;
padding: 10px 15px;
margin: 10px;
background: rgb(0,0,0);
-webkit-border-radius: 4px;
-moz-border-radius: 4px;
border-radius: 4px;
border: solid 1px rgb(255,255,255);
text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.4);
-webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
-moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
-webkit-transition-duration: 0.2s;
-moz-transition-duration: 0.2s;
transition-duration: 0.2s;
-webkit-user-select:none;
-moz-user-select:none;
-ms-user-select:none;
user-select:none;
}

a.button:hover {
background: rgb(255,255,0);
border: solid 1px #2A4E77;
}

a.button:active {
-webkit-box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
-moz-box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
background: rgb(0,255,0);
box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
border: solid 1px
}

img
{
max-width: 1024px;
max-height: 900px
}

table, th, td
{
margin-top: 2em;
margin-bottom: 2em;
border-collapse: collapse;
border: 1px solid rgb(255,255,255);
padding: 15px;
}

.mathmlEquation
{
}

.pageNumber
{
border-style:solid;
border-width: 1px 0px 0px 0px;
padding: 5px 0px 0px 25px;
font-size: 150%;
}

h6
{
border-style:solid;
border-width: 1px 0px 0px 0px;
padding: 5px 0px 0px 25px;
font-size: 150%;
}

.ui-tooltip
{
background: rgb(0,0,0);
border: 2px solid rgb(255,255,255);
padding: 10px 20px;
margin-left: 10px;
border-radius: 20px;
box-shadow: 0 0 7px rgb(255,255,255);
-webkit-user-select: none;
-moz-user-select: -moz-none;
}

#npaHighlightLine
{
background-color: rgb(0,255,0);
-webkit-border-radius: 5px;
}

#npaHighlight
{
background-color: rgb(255,255,0);
-webkit-border-radius: 3px;
display: inline-block;
z-index: 2;
}

#npaHighlightSelection
{
background-color: rgb(255,255,0);
-webkit-border-radius: 3px;
display: inline-block;
z-index: 2;
}

.table-of-contents
{
border: 1px dashed;
padding: 1em;
}

.table-of-contents h1
{
text-align: left;
font-size: 1.5em;
}

'''
        head.append(contentStyle)

        optionStyle = html.Element('style')
        optionStyle.set('type','text/css')
        optionStyle.text = '''
.accordionItem { color: white; background-color: black;}
.accordionItem h2 { margin: 0; font-size: 1.1em; padding: 0.4em; border-bottom: 1px solid }
.accordionItem h2:hover { cursor: pointer; }
.accordionItem div { margin: 0; padding: 1em 0.4em; border-bottom: 1px solid;}
.accordionItem.hide h2 { }
.accordionItem.hide div { display: none; }

.bla:hover{ background: #000000; color: #FFFFFF; }
.wht:hover{ background: #FFFFFF; }
.brn:hover{ background: #884900; }
.red:hover{ background: #B60000; color: #FFFFFF; }
.pnk:hover{ background: #A11C80; color: #FFFFFF; }
.ppl:hover{ background: #6C2ADB; color: #FFFFFF; }
.blu:hover{ background: #0045E7; color: #FFFFFF; }
.cyn:hover{ background: #00617B; color: #FFFFFF; }
.grn:hover{ background: #0F6800; color: #FFFFFF; }
.gry:hover{ background: #595959; color: #FFFFFF; }

.ar:hover{ font-family: Arial; }
.ba:hover{ font-family: "Book Antiqua"; }
.ga:hover{ font-family: Georgia; }
.ta:hover{ font-family: Tahoma; }
.ti:hover{ font-family: "Times New Roman"; }
.tr:hover{ font-family: "Trebuchet MS"; }
.ve:hover{ font-family: Verdana; }
'''
        head.append(optionStyle)

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
        data URL should be placed in the car attribute of an <img> tag.
        '''
        ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
        dataString = 'data:image/' + ext + ';base64,'

        # Read the image
        f = urllib2.urlopen(imageURL)
        contents = base64.b64encode(f.read())
        dataString += contents

        return dataString

    def _getTextInsideElement(self, elem):
        myText = ''
        if elem.text is not None:
            myText += elem.text

        for c in elem:
            myText += self._getTextInsideElement(c)
            if c.tail is not None:
                myText += c.tail

        return myText

class MathPlayerHTMLSingleExportThread(ExportThread):
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
        super(MathPlayerHTMLSingleExportThread, self).__init__(document, htmlContent, tempDirectory)
        self._lastProgress = -1

    @staticmethod
    def description():
        return '[HTML] +Mathplayer 4.0'

    @staticmethod
    def getDefaultPath(inputFilePath):
        '''
        Returns a possible default path for the given input file.
        '''
        return os.path.splitext(inputFilePath)[0] + '.html'

    def run(self):
        super(MathPlayerHTMLSingleExportThread, self).run()

        mainHtml = html.fromstring(self._document.getMainPage(mathOutput='svg'))

        if configuration.getBool('AddTOC', True):
            self._createTableOfContents(mainHtml)

        # Regenerate the content to use SVGs. They render better and more
        # consistently.
        keepMathML = True
        if not keepMathML:
            headlessRender = HeadlessRendererThread(html.tostring(mainHtml))
            headlessRender.progress.connect(self._myOnProgress)
            headlessRender.start()
            while headlessRender.isRunning():
                if not self._running:
                    headlessRender.stop()
                QThread.yieldCurrentThread()

        #self._htmlContent = html.fromstring(unicode(headlessRender.getRenderedHTML(), encoding='utf-8'))
        self._htmlContent = mainHtml
        if self._running:
            self._convertPageNumbersToH6(self._htmlContent)
            self._removeAltTextIfIgnored(self._htmlContent)
            self._removeHighlighter(self._htmlContent)
            self._removeScripts(self._htmlContent)
            self._embedImages(self._htmlContent)
            self._embedCSS(self._htmlContent)
            self._embedOptions(self._htmlContent)
            self._convertMathEquations(self._htmlContent,keepMathML)

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

    def _createTableOfContents(self, myHtml):
        '''
        Create a table of contents.
        '''
        # Generate a table of contents from the headings
        headingMap = {'h1': 1,
                      'h2': 2,
                      'h3': 3,
                      'h4': 4,
                      'h5': 5}
        headings = []
        leastHeadingLevel = 500000
        for ev, elem in etree.iterwalk(myHtml, events=('end',)):
            if elem.tag in headingMap:
                headings.append((headingMap[elem.tag], self._getTextInsideElement(elem), elem))
                if headingMap[elem.tag] < leastHeadingLevel:
                    leastHeadingLevel = headingMap[elem.tag]

        navRoot = html.Element('nav')
        navRoot.set('role', 'navigation')
        navRoot.set('class', 'table-of-contents')

        # Check if need warning about page number conversion
        query = myHtml.find(".//p[@class='pageNumber']")
        elem1 = html.Element('p')
        elem1.text  = 'Screen Reader Users: This document has been optimized for use with MathPlayer 4.0. ' \
                        'Ensure you have downloaded MathPlayer and you have enabled Active Content upon opening.'
        navRoot.append(elem1)
        if query is not None:
            elem = html.Element('p')
            elem.text = 'Page numbers have been converted to heading 6.'
            navRoot.append(elem)

        elem = html.Element('h1')
        elem.text = 'Contents:'
        navRoot.append(elem)

        elem = html.Element('ul')
        navRoot.append(elem)

        currentLevel = 1
        headingId = 0
        parent = elem
        for h in headings:

            # Indent/deindent to right level
            while h[0] != currentLevel:
                if currentLevel < h[0]:
                    elem = html.Element('ul')
                    parent.append(elem)
                    parent = elem
                    currentLevel += 1

                if currentLevel > h[0]:
                    parent = parent.getparent()
                    currentLevel -= 1


            # Make element for the thing
            elem = html.Element('li')
            link = html.Element('a')
            link.set('href', '#heading' + str(headingId))
            elem.append(link)
            link.text = h[1]

            # Set the link
            link.set('href', '#heading' + str(headingId))
            h[2].set('id', 'heading' + str(headingId))
            headingId += 1

            parent.append(elem)

        # Insert TOC into document
        myHtml.insert(0, navRoot)

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

    def _removeAltTextIfIgnored(self, myHtml):
        '''
        Removes the alt text from images if the settings say to remove it.
        '''
        if configuration.getBool('IgnoreAltText', False):
            imgs = myHtml.xpath('//img')
            for i in imgs:
                i.attrib.pop('alt', None)
                i.attrib.pop('title', None)

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

    def _convertMathEquations(self, myHtml, keepMathML=False):
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

                if keepMathML:
                    pass

                else:

                    # Get the prose for the math equation
                    prose = ''
                    for speech in self._document.generateSpeech(equations[i]):
                        prose += speech[0]
                        break

                    # Remove all of the quotes from the math equation. JAWS reads
                    # all of the quotes aloud, so it can get annoying
                    punctuationToRemove = ['"', ',', ';', ':', "'"]
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
                if ':' in attr:
                    myAttr = attr[attr.find(':') + 1:]
                    myMath.set(myAttr, svg.get(attr))
                else:
                    myMath.set(attr, svg.get(attr))

            except Exception as ex:
                print 'Could not copy SVG attribute:', ex

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

            try:
                p = images[i].get('src')
                images[i].set('src', self._createEmbeddedImageDataURL(p))
            except urllib2.URLError as e:
                # The URL may already be embedded, so don't do it twice.
                pass

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

    def _embedOptions(self, myHtml):
        '''
        :param myHtml:
        embeds color and font options pickers into HTML, as well as the MathJax script
        '''
        head = myHtml.find(".//head")

        mathplayerScript = html.Element('meta')
        mathplayerScript.set('http-equiv','X-UA-Compatible')
        mathplayerScript.set('content','IE=EmulateIE8')
        head.append(mathplayerScript)


        mathplayercheckScript = html.Element('script')
        mathplayercheckScript.set('language','javascript')
        mathplayercheckScript.text = '''

    function IsMPInstalled()
        {
          try {
            var oMP = new ActiveXObject("MathPlayer.Factory.1");
            return true;
          }
          catch(e) {
            return false;
          }
        }
        function IsIE6LaterWindows()
        {
          var pos=navigator.appVersion.indexOf("MSIE ")+5;
          return( navigator.appName=="Microsoft Internet Explorer" && navigator.platform=="Win32" && parseFloat(navigator.appVersion.substr(pos))>="6.0");
        }
        if( IsIE6LaterWindows() ) {
          if( ! IsMPInstalled() ) {
            if( confirm("This page requires Design Science's MathPlayer to display equations and symbols. MathPlayer is not currently installed, so equations and symbols will not display properly. Would you like to download and install MathPlayer now?") )
              window.open("http://www.dessci.com/webmath/mathplayer", "MPDownload");
          }
        }
        else {
          alert("This page uses Design Science's MathPlayer to display equations and symbols,and requires Microsoft Internet Explorer 6.0 or later on Windows.As you are using a different browser, equations and symbols will not display properly. Download at www.dessci.com/webmath/mathplayer.");
        }
        -->
        </script>
        '''

        head.append(mathplayercheckScript)

        accordionScript = html.Element('script')
        accordionScript.set('type','text/javascript')
        accordionScript.text = '''    var accordionItems = new Array();

    function init() {

      // Grab the accordion items from the page
      var divs = document.getElementsByTagName( 'div' );
      for ( var i = 0; i < divs.length; i++ ) {
        if ( divs[i].className == 'accordionItem' ) accordionItems.push( divs[i] );
      }

      // Assign onclick events to the accordion item headings
      for ( var i = 0; i < accordionItems.length; i++ ) {
        var h2 = getFirstChildWithTagName( accordionItems[i], 'H2' );
        h2.onclick = toggleItem;
      }

      // Hide all accordion item bodies except the first
      for ( var i = 1; i < accordionItems.length; i++ ) {
        accordionItems[i].className = 'accordionItem hide';
      }
    }

    //toggles visibility of item
    function toggleItem() {
      var itemClass = this.parentNode.className;

      // Hide all items
      for ( var i = 0; i < accordionItems.length; i++ ) {
        accordionItems[i].className = 'accordionItem hide';
      }

      // Show this item if it was previously hidden
      if ( itemClass == 'accordionItem hide' ) {
        this.parentNode.className = 'accordionItem';
      }
    }

    function getFirstChildWithTagName( element, tagName ) {
      for ( var i = 0; i < element.childNodes.length; i++ ) {
        if ( element.childNodes[i].nodeName == tagName ) return element.childNodes[i];
      }
    }
'''

        head.append(accordionScript)


        accordionContents = ''' <div class="accordionItem">
      <h2>+ Visibility Options</h2>
      <div>

        <!-- background color selection -->
        <form name="bgcolorForm">Background Color:
          <select onChange="if(this.selectedIndex!=0)
            document.bgColor=this.options[this.selectedIndex].value">
            <option value="choose">set background color
            <option class="bla" value="000000">black
            <option class="wht" value="FFFFFF">white
            <option class="brn" value="884900">brown
            <option class="red" value="B60000">red
            <option class="pnk" value="A11C80">pink
            <option class="ppl" value="6C2ADB">purple
            <option class="blu" value="0045E7">blue
            <option class="cyn" value="00617B">cyan
            <option class="grn" value="0F6800">green
            <option class="gry" value="595959">grey
            </select></form>

        <!-- text color selection -->
        <form name="textcolorForm">Text Color:
          <select onChange="if(this.selectedIndex!=0)
            document.body.text=this.options[this.selectedIndex].value">
            <option value="choose">set text color
            <option class="bla" value="000000">black
            <option class="wht" value="FFFFFF">white
            <option class="brn" value="884900">brown
            <option class="red" value="B60000">red
            <option class="pnk" value="A11C80">pink
            <option class="ppl" value="6C2ADB">purple
            <option class="blu" value="0045E7">blue
            <option class="cyn" value="00617B">cyan
            <option class="grn" value="0F6800">green
            <option class="gry" value="595959">grey
          </select></form>

        <!-- text size selection -->
        <form name="textSizeForm">Text Size:
          <select onChange="if(this.selectedIndex!=0)
          document.body.style.fontSize=this.options[this.selectedIndex].value">
            <option value="choose">set text size
            <option value="75%">small
            <option value="100%">medium (default size)
            <option value="150%">large
            <option value="200%">extra large
          </select></form>

        <!-- font selection -->
        <form name="fontForm">Font:
          <select onChange="if(this.selectedIndex!=0)
          document.body.style.fontFamily=this.options[this.selectedIndex].value">
            <option value="choose">set font
            <option class="ar" value="Arial">Arial
            <option class="ba" value="Book Antiqua">Book Antiqua
            <option class="ga" value="Georgia">Georgia
            <option class="ta" value="Tahoma">Tahoma
            <option class="ti" value="Times New Roman">Times New Roman
            <option class="tr" value="Trebuchet MS">Trebuchet MS
            <option class="ve" value="Verdana">Verdana
          </select></form>
      </div>
    </div>
'''

        accordion = html.fromstring(accordionContents)
        head.append(accordion)

        body = myHtml.find(".//body")
        body.set('onload','init()')

    def _embedCSS(self, myHtml):
        '''
        Embeds meta tag to enable IE8 mode.
        '''

        head = myHtml.find(".//head")

        mathplayerScript = html.Element('meta')
        mathplayerScript.set('http-equiv','X-UA-Compatible')
        mathplayerScript.set('content','IE=EmulateIE8')
        head.append(mathplayerScript)

        '''
        Embeds the CSS into the HTML.
        '''

        cssLinks = myHtml.findall(".//link[@rel='stylesheet']")
        head = myHtml.find(".//head")

        #gets rid of css links in myHtml
        for css in cssLinks:
            print

            # Download the stylesheet
            f = urllib2.urlopen(css.get('href'))

            # Remove the link
            css.getparent().remove(css)

        #insert Flex export styles
        contentStyle = html.Element('style')
        contentStyle.set('type','text/css')
        contentStyle.text = '''h1
{
text-align: center;
font-size: 300%;
}

h2
{
border-style: dashed;
border-width: 0px 0px 1px 0px;
padding: 15px;
font-size: 200%;
}

h3
{
padding: 10px;
font-size: 175%;
}

h4
{
font-size: 150%;
}

a.button {
text-decoration: none;
padding: 10px 15px;
margin: 10px;
background: rgb(0,0,0);
-webkit-border-radius: 4px;
-moz-border-radius: 4px;
border-radius: 4px;
border: solid 1px rgb(255,255,255);
text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.4);
-webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
-moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
-webkit-transition-duration: 0.2s;
-moz-transition-duration: 0.2s;
transition-duration: 0.2s;
-webkit-user-select:none;
-moz-user-select:none;
-ms-user-select:none;
user-select:none;
}

a.button:hover {
background: rgb(255,255,0);
border: solid 1px #2A4E77;
}

a.button:active {
-webkit-box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
-moz-box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
background: rgb(0,255,0);
box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
border: solid 1px
}

img
{
max-width: 1024px;
max-height: 900px
}

table, th, td
{
margin-top: 2em;
margin-bottom: 2em;
border-collapse: collapse;
border: 1px solid rgb(255,255,255);
padding: 15px;
}

.mathmlEquation
{
}

.pageNumber
{
border-style:solid;
border-width: 1px 0px 0px 0px;
padding: 5px 0px 0px 25px;
font-size: 150%;
}

h6
{
border-style:solid;
border-width: 1px 0px 0px 0px;
padding: 5px 0px 0px 25px;
font-size: 150%;
}

.ui-tooltip
{
background: rgb(0,0,0);
border: 2px solid rgb(255,255,255);
padding: 10px 20px;
margin-left: 10px;
border-radius: 20px;
box-shadow: 0 0 7px rgb(255,255,255);
-webkit-user-select: none;
-moz-user-select: -moz-none;
}

#npaHighlightLine
{
background-color: rgb(0,255,0);
-webkit-border-radius: 5px;
}

#npaHighlight
{
background-color: rgb(255,255,0);
-webkit-border-radius: 3px;
display: inline-block;
z-index: 2;
}

#npaHighlightSelection
{
background-color: rgb(255,255,0);
-webkit-border-radius: 3px;
display: inline-block;
z-index: 2;
}

.table-of-contents
{
border: 1px dashed;
padding: 1em;
}

.table-of-contents h1
{
text-align: left;
font-size: 1.5em;
}

'''
        head.append(contentStyle)

        optionStyle = html.Element('style')
        optionStyle.set('type','text/css')
        optionStyle.text = '''
.accordionItem { color: white; background-color: black;}
.accordionItem h2 { margin: 0; font-size: 1.1em; padding: 0.4em; border-bottom: 1px solid }
.accordionItem h2:hover { cursor: pointer; }
.accordionItem div { margin: 0; padding: 1em 0.4em; border-bottom: 1px solid;}
.accordionItem.hide h2 { }
.accordionItem.hide div { display: none; }

.bla:hover{ background: #000000; color: #FFFFFF; }
.wht:hover{ background: #FFFFFF; }
.brn:hover{ background: #884900; }
.red:hover{ background: #B60000; color: #FFFFFF; }
.pnk:hover{ background: #A11C80; color: #FFFFFF; }
.ppl:hover{ background: #6C2ADB; color: #FFFFFF; }
.blu:hover{ background: #0045E7; color: #FFFFFF; }
.cyn:hover{ background: #00617B; color: #FFFFFF; }
.grn:hover{ background: #0F6800; color: #FFFFFF; }
.gry:hover{ background: #595959; color: #FFFFFF; }

.ar:hover{ font-family: Arial; }
.ba:hover{ font-family: "Book Antiqua"; }
.ga:hover{ font-family: Georgia; }
.ta:hover{ font-family: Tahoma; }
.ti:hover{ font-family: "Times New Roman"; }
.tr:hover{ font-family: "Trebuchet MS"; }
.ve:hover{ font-family: Verdana; }
'''
        head.append(optionStyle)

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
        data URL should be placed in the car attribute of an <img> tag.
        '''
        ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
        dataString = 'data:image/' + ext + ';base64,'

        # Read the image
        f = urllib2.urlopen(imageURL)
        contents = base64.b64encode(f.read())
        dataString += contents

        return dataString

    def _getTextInsideElement(self, elem):
        myText = ''
        if elem.text is not None:
            myText += elem.text

        for c in elem:
            myText += self._getTextInsideElement(c)
            if c.tail is not None:
                myText += c.tail

        return myText

# class MathJaxHTMLSingleExportThread(ExportThread):
#     '''
#     Exports the content to a single HTML page with embedded images and math
#     descriptions.
#     '''
#
#     # Arbitrary portions of the progress bar that the different stages take up
#     PERCENT_CONVERTING_MATH = (0.0, 75.0)
#     PERCENT_EMBED_IMAGES = (PERCENT_CONVERTING_MATH[1], 100.0)
#
#     # Set the label for each of the states
#     DESCRIPTION_CONVERTING_MATH = 'Converting equation '
#     DESCRIPTION_EMBED_IMAGES = 'Embedding image '
#
#     def __init__(self, document, htmlContent, tempDirectory):
#         super(MathJaxHTMLSingleExportThread, self).__init__(document, htmlContent, tempDirectory)
#         self._lastProgress = -1
#
#     @staticmethod
#     def description():
#         return '[HTML] MathJax: JAWS 16'
#
#     @staticmethod
#     def getDefaultPath(inputFilePath):
#         '''
#         Returns a possible default path for the given input file.
#         '''
#         return os.path.splitext(inputFilePath)[0] + '.html'
#
#     def run(self):
#         super(MathJaxHTMLSingleExportThread, self).run()
#
#         mainHtml = html.fromstring(self._document.getMainPage(mathOutput='svg'))
#
#         if configuration.getBool('AddTOC', True):
#             self._createTableOfContents(mainHtml)
#
#         # Regenerate the content to use SVGs. They render better and more
#         # consistently.
#         keepMathML = True
#         if not keepMathML:
#             headlessRender = HeadlessRendererThread(html.tostring(mainHtml))
#             headlessRender.progress.connect(self._myOnProgress)
#             headlessRender.start()
#             while headlessRender.isRunning():
#                 if not self._running:
#                     headlessRender.stop()
#                 QThread.yieldCurrentThread()
#
#         #self._htmlContent = html.fromstring(unicode(headlessRender.getRenderedHTML(), encoding='utf-8'))
#         self._htmlContent = mainHtml
#         if self._running:
#             self._convertPageNumbersToH6(self._htmlContent)
#             self._removeAltTextIfIgnored(self._htmlContent)
#             self._removeHighlighter(self._htmlContent)
#             self._removeScripts(self._htmlContent)
#             self._embedImages(self._htmlContent)
#             #self._embedFonts(self._htmlContent)
#             self._embedCSS(self._htmlContent)
#             self._convertMathEquations(self._htmlContent,keepMathML)
#             self._mathmltoblock(self._htmlContent)
#
#             if self._running:
#
#                 with open(self._filePath, 'wb') as f:
#                     f.write(html.tostring(self._htmlContent))
#
#                 # Say that this export finished successfully
#                 self.success.emit()
#                 self.isSuccess = True
#
#     def _myOnProgress(self, percent, label):
#         self._reportProgress(percent, label)
#
#     def _reportProgress(self, percent, label, alwaysUpdate=False):
#         myPercent = int(percent)
#         if (myPercent != self._lastProgress) or alwaysUpdate:
#             self._lastProgress = myPercent
#             self.progress.emit(myPercent, label)
#
#     def _createTableOfContents(self, myHtml):
#         '''
#         Create a table of contents.
#         '''
#         # Generate a table of contents from the headings
#         headingMap = {'h1': 1,
#                       'h2': 2,
#                       'h3': 3,
#                       'h4': 4,
#                       'h5': 5}
#         headings = []
#         leastHeadingLevel = 500000
#         for ev, elem in etree.iterwalk(myHtml, events=('end',)):
#             if elem.tag in headingMap:
#                 headings.append((headingMap[elem.tag], self._getTextInsideElement(elem), elem))
#                 if headingMap[elem.tag] < leastHeadingLevel:
#                     leastHeadingLevel = headingMap[elem.tag]
#
#         navRoot = html.Element('nav')
#         navRoot.set('role', 'navigation')
#         navRoot.set('class', 'table-of-contents')
#
#         # Check if need warning about page number conversion
#         query = myHtml.find(".//p[@class='pageNumber']")
#         if query is not None:
#             elem = html.Element('p')
#             elem.text = 'Screen Reader Users: Math content has been optimized for use with JAWS 16 with ' \
#                         'Internet Explorer; an internet connection is required to access math content. ' \
#                         'Page numbers have been converted to heading 6.'
#             navRoot.append(elem)
#
#         elem = html.Element('h1')
#         elem.text = 'Contents:'
#         navRoot.append(elem)
#
#         elem = html.Element('ul')
#         navRoot.append(elem)
#
#         currentLevel = 1
#         headingId = 0
#         parent = elem
#         for h in headings:
#
#             # Indent/deindent to right level
#             while h[0] != currentLevel:
#                 if currentLevel < h[0]:
#                     elem = html.Element('ul')
#                     parent.append(elem)
#                     parent = elem
#                     currentLevel += 1
#
#                 if currentLevel > h[0]:
#                     parent = parent.getparent()
#                     currentLevel -= 1
#
#
#             # Make element for the thing
#             elem = html.Element('li')
#             link = html.Element('a')
#             link.set('href', '#heading' + str(headingId))
#             elem.append(link)
#             link.text = h[1]
#
#             # Set the link
#             link.set('href', '#heading' + str(headingId))
#             h[2].set('id', 'heading' + str(headingId))
#             headingId += 1
#
#             parent.append(elem)
#
#         # Insert TOC into document
#         myHtml.insert(0, navRoot)
#
#     def _convertPageNumbersToH6(self, myHtml):
#         '''
#         Converts all of the page numbers into H6 headings so that they are
#         easily navigable by JAWS and other screen-reading software.
#         '''
#         # Get all of the page numbers
#         pageNumbers = myHtml.xpath("//p[@class='pageNumber']")
#
#         # Convert each page number to an h6 element
#         for p in pageNumbers:
#             if not self._running:
#                 break
#             p.tag = 'h6'
#             p.attrib.pop('class')
#
#     def _removeAltTextIfIgnored(self, myHtml):
#         '''
#         Removes the alt text from images if the settings say to remove it.
#         '''
#         if configuration.getBool('IgnoreAltText', False):
#             imgs = myHtml.xpath('//img')
#             for i in imgs:
#                 i.attrib.pop('alt', None)
#                 i.attrib.pop('title', None)
#
#     def _removeHighlighter(self, myHtml):
#         '''
#         Removes the highlighter from the document, if any.
#         '''
#         highlights = myHtml.xpath("//span[@id='npaHighlight']")
#         highlightLines = myHtml.xpath("//span[@id='npaHighlightLine']")
#         highlightSelections = myHtml.xpath("//span[@id='npaHighlightSelection']")
#
#         for h in highlights:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#         for h in highlightLines:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#         for h in highlightSelections:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#     def _replaceWithChildren(self, elem):
#         '''
#         Replaces the element with its own children.
#         '''
#         p = elem.getparent()
#         i = p.index(elem)
#
#         # Mess with the text
#         if elem.text is not None:
#             firstHalf = p[:i]
#             if len(firstHalf) > 0:
#                 if firstHalf[-1].tail is not None:
#                     firstHalf[-1].tail += elem.text
#                 else:
#                     firstHalf[-1].tail = elem.text
#             else:
#                 if p.text is not None:
#                     p.text += elem.text
#                 else:
#                     p.text = elem.text
#
#         # Mess with the tail
#         if elem.tail is not None:
#             if len(elem) > 0:
#                 if elem[-1].tail is not None:
#                     elem[-1].tail += elem.tail
#                 else:
#                     elem[-1].tail = elem.tail
#             else:
#                 if elem.text is not None:
#                     p.text += elem.tail
#                 else:
#                     p.text = elem.tail
#
#         # Get all of the children of element and insert
#         # them in the parent, in correct order
#         childs = []
#         for c in elem:
#             childs.append(c)
#         childs.reverse()
#         for c in childs:
#             p.insert(i, c)
#
#         # Remove the element
#         p.remove(elem)
#
#     def _removeScripts(self, myHtml):
#         '''
#         Removes all the <script> elements from the document. No need for
#         showing everyone the JavaScript.
#         '''
#         for e in myHtml.xpath('.//script'):
#             e.getparent().remove(e)
#
#     def _convertMathEquations(self, myHtml, keepMathML=False):
#         '''
#         Converts the Math equations inside (presumed to be SVGs generated by
#         MathJax) into embedded PNGs with the math prose as alternate text.
#         '''
#         equations = myHtml.xpath("//script[@class='math/mml']")
#
#         # Get the <defs> in the hidden SVGs (wherever they may be)
#         defs = myHtml.xpath('//svg/defs')
#         defXMLs = []
#         for d in defs:
#             if not self._running:
#                 break
#             defXMLs.append(etree.fromstring(html.tostring(d)))
#
#         for i in range(len(equations)):
#             QThread.yieldCurrentThread()
#             try:
#                 if not self._running:
#                     break
#                 myProgress = float(i) / float(len(equations))
#                 myProgress = myProgress * (self.PERCENT_CONVERTING_MATH[1] - self.PERCENT_CONVERTING_MATH[0]) + self.PERCENT_CONVERTING_MATH[0]
#                 myLabel = self.DESCRIPTION_CONVERTING_MATH + str(i + 1) + ' of ' + str(len(equations)) + '...'
#                 self._reportProgress(myProgress, myLabel, alwaysUpdate=True)
#
#                 if keepMathML:
#                     pass
#                     # mathml = equations[i].xpath('//script')[0].text
#                     #
#                     # # Copy the children over
#                     # for child in equations[i]:
#                     #     child.drop_tree()
#                     #
#                     # equations[i].text = mathml
#                     # # Morph equation span into MathML
#                     # #equations[i].tag = 'math'
#                     # # for key in equations[i].attrib:
#                     # #     equations[i].attrib.pop(key)
#                     # # for key in mathml.attrib.keys():
#                     # #     equations[i].attrib[key] = mathml.attrib[key]
#
#
#
#                 else:
#
#                     # Get the prose for the math equation
#                     prose = ''
#                     for speech in self._document.generateSpeech(equations[i]):
#                         prose += speech[0]
#                         break
#
#                     # Remove all of the quotes from the math equation. JAWS reads
#                     # all of the quotes aloud, so it can get annoying
#                     punctuationToRemove = ['"', ',', ';', ':', "'"]
#                     for p in punctuationToRemove:
#                         prose = prose.replace(p, '')
#
#                     # Replace the span with an image representing the equation
#                     svgElem = equations[i].xpath('.//svg')[0]
#                     pngData = self._renderMathSVGToPNG(svgElem, defXMLs)
#                     dataString = 'data:image/png;base64,' + base64.b64encode(pngData)
#                     equations[i].tag = 'img'
#
#                     # Clear out all children and attributes from node
#                     for k in equations[i].attrib.keys():
#                         del equations[i].attrib[k]
#                     for c in equations[i]:
#                         c.getparent().remove(c)
#
#                     # Set the image attributes
#                     equations[i].set('src', dataString)
#                     equations[i].set('alt', prose)
#                     equations[i].set('title', prose)
#
#
#             except Exception as e:
#                 print 'Equation', i, 'did not parse correctly!', e
#                 traceback.print_exc()
#
#     def _mathmltoblock(self, myHtml):
#
#         equations = myHtml.xpath("//math")
#
#         for math in equations:
#             math.attrib['display'] = 'block'
#
#         print etree.tostring(myHtml)
#
#         # f = myHtml
#         # for r in f.xpath('//math'):
#         #     r = 'xmlns="http://www.w3.org/1998/Math/MathML" display="block"'
#         # print etree.tostring(f)
#
#         #mathml.replace('xmlns="http://www.w3.org/1998/Math/MathML"','xmlns="http://www.w3.org/1998/Math/MathML" display="block"')
#
#         #for e in myHtml.find('xmlns="http://www.w3.org/1998/Math/MathML"'):
#             #myHtml = myHtml.replace(e, 'xmlns="http://www.w3.org/1998/Math/MathML" display="block"')
#
#
#         #query = myHtml.find('xmlns="http://www.w3.org/1998/Math/MathML"')
#         #if query is not None:
#            # equation = html
#            # equation.text = 'xmlns="http://www.w3.org/1998/Math/MathML" display="block"'
#
#
#         #for e in myHtml.find('.//xmlns'):
#            # e.append(' display="block"')
#
#         #for b in myHtml('xmlns="http://www.w3.org/1998/Math/MathML"'):
#             #b.append(' display="block"')
#
#
#
#
#        # b = 'xmlns="http://www.w3.org/1998/Math/MathML"'
#        # b.replace('xmlns="http://www.w3.org/1998/Math/MathML"','xmlns="http://www.w3.org/1998/Math/MathML" display="block"');
#
#
#
#     def _renderMathSVGToPNG(self, svg, defXMLs):
#         '''
#         Renders the Math SVG (an lxml Element) into a PNG. Returns the
#         bytestring containing the PNG data.
#         '''
#         # Create my own SVG with valid namespaces
#         SVG_NS = '{http://www.w3.org/2000/svg}'
#         XLINK_NS = '{http://www.w3.org/1999/xlink}'
#         NS_MAP = {None : SVG_NS[1:-1], 'xlink' : XLINK_NS[1:-1]}
#         myMath = etree.Element('{0}svg'.format(SVG_NS), nsmap=NS_MAP)
#
#         # Copy all attributes
#         for attr in svg.attrib.keys():
#             try:
#                 if ':' in attr:
#                     myAttr = attr[attr.find(':') + 1:]
#                     myMath.set(myAttr, svg.get(attr))
#                 else:
#                     myMath.set(attr, svg.get(attr))
#
#             except Exception as ex:
#                 print 'Could not copy SVG attribute:', ex
#
#         # Copy all elements
#         for m in svg:
#             myMath.append(m)
#
#         # Change the viewbox attribute of <svg> to viewBox
#         if 'viewbox' in myMath.attrib:
#             data = myMath.get('viewbox')
#             myMath.attrib.pop('viewbox')
#             myMath.set('viewBox', data)
#
#         # Insert the defs into my math equation
#         myDef = etree.SubElement(myMath, 'defs')
#         for d in defXMLs:
#             for p in d:
#                 myDef.append(etree.fromstring(etree.tostring(p)))
#
#         # In my math equation, every <use href> must be changed to
#         # <use xlink:href>
#         uses = myMath.xpath('.//use[@href]')
#         for u in uses:
#             data = u.get('href')
#             u.attrib.pop('href')
#             u.set('{0}href'.format(XLINK_NS), data)
#
#         # Change the color of every element in the svg to the text color defined
#         # in user preferences
#         strokes = myMath.xpath(".//*[@stroke]")
#         fills = myMath.xpath(".//*[@fill]")
#         for s in strokes:
#             if not ('none' in s.get('stroke')):
#                 s.set('stroke', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
#         for f in fills:
#             if not ('none' in f.get('fill')):
#                 f.set('fill', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
#
#         # Write to temp file, run CairoSVG through it, then push it out
#         svgTemp = os.path.join(self._tempDirectory, 'tmp.svg')
#         with open(svgTemp, 'wb') as f:
#             f.write(etree.tostring(myMath, pretty_print=True))
#
#         tmpURL = urlparse.urljoin('file:', urllib.pathname2url(svgTemp))
#
#         return cairosvg.svg2png(url=tmpURL)
#
#     def _embedImages(self, myHtml):
#         '''
#         It goes through all of the image tags, reads the original image it is
#         referencing, and embeds the image data into the tag so that the document
#         is portable.
#         '''
#         images = myHtml.xpath("//img")
#
#         for i in range(len(images)):
#             if not self._running:
#                 break
#
#             myProgress = float(i) / float(len(images))
#             myProgress = myProgress * (self.PERCENT_EMBED_IMAGES[1] - self.PERCENT_EMBED_IMAGES[0]) + self.PERCENT_EMBED_IMAGES[0]
#             myLabel = self.DESCRIPTION_EMBED_IMAGES + str(i + 1) + ' of ' + str(len(images)) + '...'
#             self._reportProgress(myProgress, myLabel)
#
#             try:
#                 p = images[i].get('src')
#                 images[i].set('src', self._createEmbeddedImageDataURL(p))
#             except urllib2.URLError as e:
#                 # The URL may already be embedded, so don't do it twice.
#                 pass
#
#     def _embedFonts(self, myHtml):
#         '''
#         For all of the @font-face directives in the CSS in the head, get all of
#         the urls, download the font, and embed it.
#         '''
#         styles = myHtml.xpath(r".//head/style[@type='text/css']")
#         fontPattern = r'@font-face[\s]*\{.*?\}'
#         urlPattern = r"url\('(?P<url>.*?)'\)"
#
#         for style in styles:
#             fontSplit = misc.SplitRegex(fontPattern, style.text)
#             for match in fontSplit:
#                 sub = match['value']
#                 urlSplit = misc.SplitRegex(urlPattern, sub)
#                 for u_match in urlSplit:
#                     url_sub = u_match['value']
#                     myUrl = self._createEmbeddedFontDataURL(u_match['matchObj'].group('url'))
#                     u_match['value'] = url_sub.replace(u_match['matchObj'].group('url'), myUrl).replace("'", '')
#                 match['value'] = str(urlSplit)
#
#             style.text = str(fontSplit)
#
#     def _embedCSS(self, myHtml):
#         '''
#         Embeds the CSS into the HTML.
#         '''
#         cssLinks = myHtml.findall(".//link[@rel='stylesheet']")
#         head = myHtml.find(".//head")
#
#         for css in cssLinks:
#             print
#
#             # Download the stylesheet
#             f = urllib2.urlopen(css.get('href'))
#             contents = f.read()
#
#             g = ''
#
#             # Create a new element to save the style in
#             newCss = html.Element('style')
#             newCss.set('type','text/css')
#             newCss.text = contents
#
#
#             head.append(newCss)
#
#             #Create link
#             linkMathJax = html.Element('script')
#             linkMathJax.set('type', 'text/javascript')
#             linkMathJax.set('src', 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML')
#
#             head.append(linkMathJax)
#
#             # Remove the link
#             css.getparent().remove(css)
#
#     def _createEmbeddedFontDataURL(self, fontURL):
#         '''
#         Reads in the font from fontURL and encodes to a data URI usable inside
#         a url() for a font-face.
#         '''
#         ext = os.path.splitext(fontURL)[-1].replace('.', '').lower()
#         dataString = 'data:application/x-font-' + ext + ';charset=utf-8;base64,'
#
#         # Read the font
#         f = urllib2.urlopen(fontURL)
#         contents = base64.b64encode(f.read())
#         dataString += contents
#
#         return dataString
#
#     def _createEmbeddedImageDataURL(self, imageURL):
#         '''
#         Reads the image from imageURL and creates a data URL using the data. The
#         data URL should be placed in the car attribute of an <img> tag.
#         '''
#         ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
#         dataString = 'data:image/' + ext + ';base64,'
#
#         # Read the image
#         f = urllib2.urlopen(imageURL)
#         contents = base64.b64encode(f.read())
#         dataString += contents
#
#         return dataString
#
#     def _getTextInsideElement(self, elem):
#         myText = ''
#         if elem.text is not None:
#             myText += elem.text
#
#         for c in elem:
#             myText += self._getTextInsideElement(c)
#             if c.tail is not None:
#                 myText += c.tail
#
#         return myText

# class AppleHTMLSingleExportThread(ExportThread):
#     '''
#     Exports the content to a single HTML page with embedded images and math
#     descriptions.
#     '''
#
#     # Arbitrary portions of the progress bar that the different stages take up
#     PERCENT_CONVERTING_MATH = (0.0, 75.0)
#     PERCENT_EMBED_IMAGES = (PERCENT_CONVERTING_MATH[1], 100.0)
#
#     # Set the label for each of the states
#     DESCRIPTION_CONVERTING_MATH = 'Converting equation '
#     DESCRIPTION_EMBED_IMAGES = 'Embedding image '
#
#     def __init__(self, document, htmlContent, tempDirectory):
#         super(AppleHTMLSingleExportThread, self).__init__(document, htmlContent, tempDirectory)
#         self._lastProgress = -1
#
#     @staticmethod
#     def description():
#         return '[HTML] MathML: Voiceover (iOS/Mac)'
#
#     @staticmethod
#     def getDefaultPath(inputFilePath):
#         '''
#         Returns a possible default path for the given input file.
#         '''
#         return os.path.splitext(inputFilePath)[0] + '.html'
#
#     def run(self):
#         super(AppleHTMLSingleExportThread, self).run()
#
#         mainHtml = html.fromstring(self._document.getMainPage(mathOutput='svg'))
#
#         if configuration.getBool('AddTOC', True):
#             self._createTableOfContents(mainHtml)
#
#         # Regenerate the content to use SVGs. They render better and more
#         # consistently.
#         keepMathML = True
#         if not keepMathML:
#             headlessRender = HeadlessRendererThread(html.tostring(mainHtml))
#             headlessRender.progress.connect(self._myOnProgress)
#             headlessRender.start()
#             while headlessRender.isRunning():
#                 if not self._running:
#                     headlessRender.stop()
#                 QThread.yieldCurrentThread()
#
#         #self._htmlContent = html.fromstring(unicode(headlessRender.getRenderedHTML(), encoding='utf-8'))
#         self._htmlContent = mainHtml
#         if self._running:
#             self._convertPageNumbersToH6(self._htmlContent)
#             self._removeAltTextIfIgnored(self._htmlContent)
#             self._removeHighlighter(self._htmlContent)
#             self._removeScripts(self._htmlContent)
#             self._embedImages(self._htmlContent)
#             #self._embedFonts(self._htmlContent)
#             self._embedCSS(self._htmlContent)
#             self._convertMathEquations(self._htmlContent,keepMathML)
#
#             if self._running:
#
#                 with open(self._filePath, 'wb') as f:
#                     f.write(html.tostring(self._htmlContent))
#
#                 # Say that this export finished successfully
#                 self.success.emit()
#                 self.isSuccess = True
#
#     def _myOnProgress(self, percent, label):
#         self._reportProgress(percent, label)
#
#     def _reportProgress(self, percent, label, alwaysUpdate=False):
#         myPercent = int(percent)
#         if (myPercent != self._lastProgress) or alwaysUpdate:
#             self._lastProgress = myPercent
#             self.progress.emit(myPercent, label)
#
#     def _createTableOfContents(self, myHtml):
#         '''
#         Create a table of contents.
#         '''
#         # Generate a table of contents from the headings
#         headingMap = {'h1': 1,
#                       'h2': 2,
#                       'h3': 3,
#                       'h4': 4,
#                       'h5': 5}
#         headings = []
#         leastHeadingLevel = 500000
#         for ev, elem in etree.iterwalk(myHtml, events=('end',)):
#             if elem.tag in headingMap:
#                 headings.append((headingMap[elem.tag], self._getTextInsideElement(elem), elem))
#                 if headingMap[elem.tag] < leastHeadingLevel:
#                     leastHeadingLevel = headingMap[elem.tag]
#
#         navRoot = html.Element('nav')
#         navRoot.set('role', 'navigation')
#         navRoot.set('class', 'table-of-contents')
#
#         # Check if need warning about page number conversion
#         query = myHtml.find(".//p[@class='pageNumber']")
#         if query is not None:
#             elem = html.Element('p')
#             elem.text = 'Screen Reader Users: This document has been optimized for use with Safari on iOS and Mac ' \
#                         'devices using VoiceOver. Page numbers have been converted to heading 6.'
#             navRoot.append(elem)
#
#         elem = html.Element('h1')
#         elem.text = 'Contents:'
#         navRoot.append(elem)
#
#         elem = html.Element('ul')
#         navRoot.append(elem)
#
#         currentLevel = 1
#         headingId = 0
#         parent = elem
#         for h in headings:
#
#             # Indent/deindent to right level
#             while h[0] != currentLevel:
#                 if currentLevel < h[0]:
#                     elem = html.Element('ul')
#                     parent.append(elem)
#                     parent = elem
#                     currentLevel += 1
#
#                 if currentLevel > h[0]:
#                     parent = parent.getparent()
#                     currentLevel -= 1
#
#
#             # Make element for the thing
#             elem = html.Element('li')
#             link = html.Element('a')
#             link.set('href', '#heading' + str(headingId))
#             elem.append(link)
#             link.text = h[1]
#
#             # Set the link
#             link.set('href', '#heading' + str(headingId))
#             h[2].set('id', 'heading' + str(headingId))
#             headingId += 1
#
#             parent.append(elem)
#
#         # Insert TOC into document
#         myHtml.insert(0, navRoot)
#
#     def _convertPageNumbersToH6(self, myHtml):
#         '''
#         Converts all of the page numbers into H6 headings so that they are
#         easily navigable by JAWS and other screen-reading software.
#         '''
#         # Get all of the page numbers
#         pageNumbers = myHtml.xpath("//p[@class='pageNumber']")
#
#         # Convert each page number to an h6 element
#         for p in pageNumbers:
#             if not self._running:
#                 break
#             p.tag = 'h6'
#             p.attrib.pop('class')
#
#     def _removeAltTextIfIgnored(self, myHtml):
#         '''
#         Removes the alt text from images if the settings say to remove it.
#         '''
#         if configuration.getBool('IgnoreAltText', False):
#             imgs = myHtml.xpath('//img')
#             for i in imgs:
#                 i.attrib.pop('alt', None)
#                 i.attrib.pop('title', None)
#
#     def _removeHighlighter(self, myHtml):
#         '''
#         Removes the highlighter from the document, if any.
#         '''
#         highlights = myHtml.xpath("//span[@id='npaHighlight']")
#         highlightLines = myHtml.xpath("//span[@id='npaHighlightLine']")
#         highlightSelections = myHtml.xpath("//span[@id='npaHighlightSelection']")
#
#         for h in highlights:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#         for h in highlightLines:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#         for h in highlightSelections:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#     def _replaceWithChildren(self, elem):
#         '''
#         Replaces the element with its own children.
#         '''
#         p = elem.getparent()
#         i = p.index(elem)
#
#         # Mess with the text
#         if elem.text is not None:
#             firstHalf = p[:i]
#             if len(firstHalf) > 0:
#                 if firstHalf[-1].tail is not None:
#                     firstHalf[-1].tail += elem.text
#                 else:
#                     firstHalf[-1].tail = elem.text
#             else:
#                 if p.text is not None:
#                     p.text += elem.text
#                 else:
#                     p.text = elem.text
#
#         # Mess with the tail
#         if elem.tail is not None:
#             if len(elem) > 0:
#                 if elem[-1].tail is not None:
#                     elem[-1].tail += elem.tail
#                 else:
#                     elem[-1].tail = elem.tail
#             else:
#                 if elem.text is not None:
#                     p.text += elem.tail
#                 else:
#                     p.text = elem.tail
#
#         # Get all of the children of element and insert
#         # them in the parent, in correct order
#         childs = []
#         for c in elem:
#             childs.append(c)
#         childs.reverse()
#         for c in childs:
#             p.insert(i, c)
#
#         # Remove the element
#         p.remove(elem)
#
#     def _removeScripts(self, myHtml):
#         '''
#         Removes all the <script> elements from the document. No need for
#         showing everyone the JavaScript.
#         '''
#         for e in myHtml.xpath('.//script'):
#             e.getparent().remove(e)
#
#     def _convertMathEquations(self, myHtml, keepMathML=False):
#         '''
#         Converts the Math equations inside (presumed to be SVGs generated by
#         MathJax) into embedded PNGs with the math prose as alternate text.
#         '''
#         equations = myHtml.xpath("//span[@class='mathmlEquation']")
#
#         # Get the <defs> in the hidden SVGs (wherever they may be)
#         defs = myHtml.xpath('//svg/defs')
#         defXMLs = []
#         for d in defs:
#             if not self._running:
#                 break
#             defXMLs.append(etree.fromstring(html.tostring(d)))
#
#         for i in range(len(equations)):
#             QThread.yieldCurrentThread()
#             try:
#                 if not self._running:
#                     break
#                 myProgress = float(i) / float(len(equations))
#                 myProgress = myProgress * (self.PERCENT_CONVERTING_MATH[1] - self.PERCENT_CONVERTING_MATH[0]) + self.PERCENT_CONVERTING_MATH[0]
#                 myLabel = self.DESCRIPTION_CONVERTING_MATH + str(i + 1) + ' of ' + str(len(equations)) + '...'
#                 self._reportProgress(myProgress, myLabel, alwaysUpdate=True)
#
#                 if keepMathML:
#                     pass
#                     # mathml = equations[i].xpath('//script')[0].text
#                     #
#                     # # Copy the children over
#                     # for child in equations[i]:
#                     #     child.drop_tree()
#                     #
#                     # equations[i].text = mathml
#                     # # Morph equation span into MathML
#                     # #equations[i].tag = 'math'
#                     # # for key in equations[i].attrib:
#                     # #     equations[i].attrib.pop(key)
#                     # # for key in mathml.attrib.keys():
#                     # #     equations[i].attrib[key] = mathml.attrib[key]
#
#
#
#                 else:
#
#                     # Get the prose for the math equation
#                     prose = ''
#                     for speech in self._document.generateSpeech(equations[i]):
#                         prose += speech[0]
#                         break
#
#                     # Remove all of the quotes from the math equation. JAWS reads
#                     # all of the quotes aloud, so it can get annoying
#                     punctuationToRemove = ['"', ',', ';', ':', "'"]
#                     for p in punctuationToRemove:
#                         prose = prose.replace(p, '')
#
#                     # Replace the span with an image representing the equation
#                     svgElem = equations[i].xpath('.//svg')[0]
#                     pngData = self._renderMathSVGToPNG(svgElem, defXMLs)
#                     dataString = 'data:image/png;base64,' + base64.b64encode(pngData)
#                     equations[i].tag = 'img'
#
#                     # Clear out all children and attributes from node
#                     for k in equations[i].attrib.keys():
#                         del equations[i].attrib[k]
#                     for c in equations[i]:
#                         c.getparent().remove(c)
#
#                     # Set the image attributes
#                     equations[i].set('src', dataString)
#                     equations[i].set('alt', prose)
#                     equations[i].set('title', prose)
#
#             except Exception as e:
#                 print 'Equation', i, 'did not parse correctly!', e
#                 traceback.print_exc()
#
#     def _renderMathSVGToPNG(self, svg, defXMLs):
#         '''
#         Renders the Math SVG (an lxml Element) into a PNG. Returns the
#         bytestring containing the PNG data.
#         '''
#         # Create my own SVG with valid namespaces
#         SVG_NS = '{http://www.w3.org/2000/svg}'
#         XLINK_NS = '{http://www.w3.org/1999/xlink}'
#         NS_MAP = {None : SVG_NS[1:-1], 'xlink' : XLINK_NS[1:-1]}
#         myMath = etree.Element('{0}svg'.format(SVG_NS), nsmap=NS_MAP)
#
#         # Copy all attributes
#         for attr in svg.attrib.keys():
#             try:
#                 if ':' in attr:
#                     myAttr = attr[attr.find(':') + 1:]
#                     myMath.set(myAttr, svg.get(attr))
#                 else:
#                     myMath.set(attr, svg.get(attr))
#
#             except Exception as ex:
#                 print 'Could not copy SVG attribute:', ex
#
#         # Copy all elements
#         for m in svg:
#             myMath.append(m)
#
#         # Change the viewbox attribute of <svg> to viewBox
#         if 'viewbox' in myMath.attrib:
#             data = myMath.get('viewbox')
#             myMath.attrib.pop('viewbox')
#             myMath.set('viewBox', data)
#
#         # Insert the defs into my math equation
#         myDef = etree.SubElement(myMath, 'defs')
#         for d in defXMLs:
#             for p in d:
#                 myDef.append(etree.fromstring(etree.tostring(p)))
#
#         # In my math equation, every <use href> must be changed to
#         # <use xlink:href>
#         uses = myMath.xpath('.//use[@href]')
#         for u in uses:
#             data = u.get('href')
#             u.attrib.pop('href')
#             u.set('{0}href'.format(XLINK_NS), data)
#
#         # Change the color of every element in the svg to the text color defined
#         # in user preferences
#         strokes = myMath.xpath(".//*[@stroke]")
#         fills = myMath.xpath(".//*[@fill]")
#         for s in strokes:
#             if not ('none' in s.get('stroke')):
#                 s.set('stroke', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
#         for f in fills:
#             if not ('none' in f.get('fill')):
#                 f.set('fill', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
#
#         # Write to temp file, run CairoSVG through it, then push it out
#         svgTemp = os.path.join(self._tempDirectory, 'tmp.svg')
#         with open(svgTemp, 'wb') as f:
#             f.write(etree.tostring(myMath, pretty_print=True))
#
#         tmpURL = urlparse.urljoin('file:', urllib.pathname2url(svgTemp))
#
#         return cairosvg.svg2png(url=tmpURL)
#
#     def _embedImages(self, myHtml):
#         '''
#         It goes through all of the image tags, reads the original image it is
#         referencing, and embeds the image data into the tag so that the document
#         is portable.
#         '''
#         images = myHtml.xpath("//img")
#
#         for i in range(len(images)):
#             if not self._running:
#                 break
#
#             myProgress = float(i) / float(len(images))
#             myProgress = myProgress * (self.PERCENT_EMBED_IMAGES[1] - self.PERCENT_EMBED_IMAGES[0]) + self.PERCENT_EMBED_IMAGES[0]
#             myLabel = self.DESCRIPTION_EMBED_IMAGES + str(i + 1) + ' of ' + str(len(images)) + '...'
#             self._reportProgress(myProgress, myLabel)
#
#             try:
#                 p = images[i].get('src')
#                 images[i].set('src', self._createEmbeddedImageDataURL(p))
#             except urllib2.URLError as e:
#                 # The URL may already be embedded, so don't do it twice.
#                 pass
#
#     def _embedFonts(self, myHtml):
#         '''
#         For all of the @font-face directives in the CSS in the head, get all of
#         the urls, download the font, and embed it.
#         '''
#         styles = myHtml.xpath(r".//head/style[@type='text/css']")
#         fontPattern = r'@font-face[\s]*\{.*?\}'
#         urlPattern = r"url\('(?P<url>.*?)'\)"
#
#         for style in styles:
#             fontSplit = misc.SplitRegex(fontPattern, style.text)
#             for match in fontSplit:
#                 sub = match['value']
#                 urlSplit = misc.SplitRegex(urlPattern, sub)
#                 for u_match in urlSplit:
#                     url_sub = u_match['value']
#                     myUrl = self._createEmbeddedFontDataURL(u_match['matchObj'].group('url'))
#                     u_match['value'] = url_sub.replace(u_match['matchObj'].group('url'), myUrl).replace("'", '')
#                 match['value'] = str(urlSplit)
#
#             style.text = str(fontSplit)
#
#     def _embedCSS(self, myHtml):
#         '''
#         Embeds the CSS into the HTML.
#         '''
#         cssLinks = myHtml.findall(".//link[@rel='stylesheet']")
#         head = myHtml.find(".//head")
#
#
#         for css in cssLinks:
#             print
#
#             # Download the stylesheet
#             f = urllib2.urlopen(css.get('href'))
#             contents = f.read()
#
#             # Create a new element to save the style in
#             newCss = html.Element('style')
#             newCss.set('type', 'text/css')
#             newCss.text = contents
#             head.append(newCss)
#
#             # Remove the link
#             css.getparent().remove(css)
#
#
#     def _createEmbeddedFontDataURL(self, fontURL):
#         '''
#         Reads in the font from fontURL and encodes to a data URI usable inside
#         a url() for a font-face.
#         '''
#         ext = os.path.splitext(fontURL)[-1].replace('.', '').lower()
#         dataString = 'data:application/x-font-' + ext + ';charset=utf-8;base64,'
#
#         # Read the font
#         f = urllib2.urlopen(fontURL)
#         contents = base64.b64encode(f.read())
#         dataString += contents
#
#         return dataString
#
#     def _createEmbeddedImageDataURL(self, imageURL):
#         '''
#         Reads the image from imageURL and creates a data URL using the data. The
#         data URL should be placed in the car attribute of an <img> tag.
#         '''
#         ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
#         dataString = 'data:image/' + ext + ';base64,'
#
#         # Read the image
#         f = urllib2.urlopen(imageURL)
#         contents = base64.b64encode(f.read())
#         dataString += contents
#
#         return dataString
#
#     def _getTextInsideElement(self, elem):
#         myText = ''
#         if elem.text is not None:
#             myText += elem.text
#
#         for c in elem:
#             myText += self._getTextInsideElement(c)
#             if c.tail is not None:
#                 myText += c.tail
#
#         return myText

# class MathJaxHTMLSingleExportThread_old(ExportThread):
#     '''
#     Exports the content to a single HTML page with embedded images and math
#     descriptions.
#     '''
#
#     # Arbitrary portions of the progress bar that the different stages take up
#     PERCENT_CONVERTING_MATH = (0.0, 75.0)
#     PERCENT_EMBED_IMAGES = (PERCENT_CONVERTING_MATH[1], 100.0)
#
#     # Set the label for each of the states
#     DESCRIPTION_CONVERTING_MATH = 'Converting equation '
#     DESCRIPTION_EMBED_IMAGES = 'Embedding image '
#
#     def __init__2(self, document, htmlContent, tempDirectory):
#         super(MathJaxHTMLSingleExportThread, self).__init__2(document, htmlContent, tempDirectory)
#         self._lastProgress = -1
#
#     @staticmethod
#     def description():
#         return 'HTML'
#
#     @staticmethod
#     def getDefaultPath(inputFilePath):
#         '''
#         Returns a possible default path for the given input file.
#         '''
#         return os.path.splitext(inputFilePath)[0] + '.html'
#
#     def run(self):
#         super(MathJaxHTMLSingleExportThread, self).run()
#
#         mainHtml = html.fromstring(self._document.getMainPage(mathOutput='svg'))
#
#         if configuration.getBool('AddTOC', True):
#             self._createTableOfContents(mainHtml)
#
#         # Regenerate the content to use SVGs. They render better and more
#         # consistently.
#         headlessRender = HeadlessRendererThread(html.tostring(mainHtml))
#         headlessRender.progress.connect(self._myOnProgress)
#         headlessRender.start()
#         while headlessRender.isRunning():
#             if not self._running:
#                 headlessRender.stop()
#             QThread.yieldCurrentThread()
#
#         self._htmlContent = html.fromstring(unicode(headlessRender.getRenderedHTML(), encoding='utf-8'))
#
#         if self._running:
#             self._convertPageNumbersToH6(self._htmlContent)
#             self._removeAltTextIfIgnored(self._htmlContent)
#             self._removeHighlighter(self._htmlContent)
#             self._removeScripts(self._htmlContent)
#             self._embedImages(self._htmlContent)
#             #self._embedFonts(self._htmlContent)
#             self._embedCSS(self._htmlContent)
#             #self._convertMathEquations(self._htmlContent)
#
#             if self._running:
#
#                 with open(self._filePath, 'wb') as f:
#                     f.write(html.tostring(self._htmlContent))
#
#                 # Say that this export finished successfully
#                 self.success.emit()
#                 self.isSuccess = True
#
#     def _myOnProgress(self, percent, label):
#         self._reportProgress(percent, label)
#
#     def _reportProgress(self, percent, label, alwaysUpdate=False):
#         myPercent = int(percent)
#         if (myPercent != self._lastProgress) or alwaysUpdate:
#             self._lastProgress = myPercent
#             self.progress.emit(myPercent, label)
#
#     def _createTableOfContents(self, myHtml):
#         '''
#         Create a table of contents.
#         '''
#         # Generate a table of contents from the headings
#         headingMap = {'h1': 1,
#                       'h2': 2,
#                       'h3': 3,
#                       'h4': 4,
#                       'h5': 5}
#         headings = []
#         leastHeadingLevel = 500000
#         for ev, elem in etree.iterwalk(myHtml, events=('end',)):
#             if elem.tag in headingMap:
#                 headings.append((headingMap[elem.tag], self._getTextInsideElement(elem), elem))
#                 if headingMap[elem.tag] < leastHeadingLevel:
#                     leastHeadingLevel = headingMap[elem.tag]
#
#         navRoot = html.Element('nav')
#         navRoot.set('role', 'navigation')
#         navRoot.set('class', 'table-of-contents')
#
#         # Check if need warning about page number conversion
#         query = myHtml.find(".//p[@class='pageNumber']")
#         if query is not None:
#             elem = html.Element('p')
#             elem.text = 'NOTE: Page numbers have been converted to heading 6'
#             navRoot.append(elem)
#
#         elem = html.Element('h1')
#         elem.text = 'Contents:'
#         navRoot.append(elem)
#
#         elem = html.Element('ul')
#         navRoot.append(elem)
#
#         currentLevel = 1
#         headingId = 0
#         parent = elem
#         for h in headings:
#
#             # Indent/deindent to right level
#             while h[0] != currentLevel:
#                 if currentLevel < h[0]:
#                     elem = html.Element('ul')
#                     parent.append(elem)
#                     parent = elem
#                     currentLevel += 1
#
#                 if currentLevel > h[0]:
#                     parent = parent.getparent()
#                     currentLevel -= 1
#
#
#             # Make element for the thing
#             elem = html.Element('li')
#             link = html.Element('a')
#             link.set('href', '#heading' + str(headingId))
#             elem.append(link)
#             link.text = h[1]
#
#             # Set the link
#             link.set('href', '#heading' + str(headingId))
#             h[2].set('id', 'heading' + str(headingId))
#             headingId += 1
#
#             parent.append(elem)
#
#         # Insert TOC into document
#         myHtml.insert(0, navRoot)
#
#     def _convertPageNumbersToH6(self, myHtml):
#         '''
#         Converts all of the page numbers into H6 headings so that they are
#         easily navigable by JAWS and other screen-reading software.
#         '''
#         # Get all of the page numbers
#         pageNumbers = myHtml.xpath("//p[@class='pageNumber']")
#
#         # Convert each page number to an h6 element
#         for p in pageNumbers:
#             if not self._running:
#                 break
#             p.tag = 'h6'
#             p.attrib.pop('class')
#
#     def _removeAltTextIfIgnored(self, myHtml):
#         '''
#         Removes the alt text from images if the settings say to remove it.
#         '''
#         if configuration.getBool('IgnoreAltText', False):
#             imgs = myHtml.xpath('//img')
#             for i in imgs:
#                 i.attrib.pop('alt', None)
#                 i.attrib.pop('title', None)
#
#     def _removeHighlighter(self, myHtml):
#         '''
#         Removes the highlighter from the document, if any.
#         '''
#         highlights = myHtml.xpath("//span[@id='npaHighlight']")
#         highlightLines = myHtml.xpath("//span[@id='npaHighlightLine']")
#         highlightSelections = myHtml.xpath("//span[@id='npaHighlightSelection']")
#
#         for h in highlights:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#         for h in highlightLines:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#         for h in highlightSelections:
#             if not self._running:
#                 break
#             self._replaceWithChildren(h)
#
#     def _replaceWithChildren(self, elem):
#         '''
#         Replaces the element with its own children.
#         '''
#         p = elem.getparent()
#         i = p.index(elem)
#
#         # Mess with the text
#         if elem.text is not None:
#             firstHalf = p[:i]
#             if len(firstHalf) > 0:
#                 if firstHalf[-1].tail is not None:
#                     firstHalf[-1].tail += elem.text
#                 else:
#                     firstHalf[-1].tail = elem.text
#             else:
#                 if p.text is not None:
#                     p.text += elem.text
#                 else:
#                     p.text = elem.text
#
#         # Mess with the tail
#         if elem.tail is not None:
#             if len(elem) > 0:
#                 if elem[-1].tail is not None:
#                     elem[-1].tail += elem.tail
#                 else:
#                     elem[-1].tail = elem.tail
#             else:
#                 if elem.text is not None:
#                     p.text += elem.tail
#                 else:
#                     p.text = elem.tail
#
#         # Get all of the children of element and insert
#         # them in the parent, in correct order
#         childs = []
#         for c in elem:
#             childs.append(c)
#         childs.reverse()
#         for c in childs:
#             p.insert(i, c)
#
#         # Remove the element
#         p.remove(elem)
#
#     def _removeScripts(self, myHtml):
#         '''
#         Removes all the <script> elements from the document. No need for
#         showing everyone the JavaScript.
#         '''
#         for e in myHtml.xpath('.//script'):
#             e.getparent().remove(e)
#
#     def _convertMathEquations(self, myHtml):
#         '''
#         Converts the Math equations inside (presumed to be SVGs generated by
#         MathJax) into embedded PNGs with the math prose as alternate text.
#         '''
#         equations = myHtml.xpath("//span[@class='mathmlEquation']")
#
#         # Get the <defs> in the hidden SVGs (wherever they may be)
#         defs = myHtml.xpath('//svg/defs')
#         defXMLs = []
#         for d in defs:
#             if not self._running:
#                 break
#             defXMLs.append(etree.fromstring(html.tostring(d)))
#
#         for i in range(len(equations)):
#             QThread.yieldCurrentThread()
#             try:
#                 if not self._running:
#                     break
#                 myProgress = float(i) / float(len(equations))
#                 myProgress = myProgress * (self.PERCENT_CONVERTING_MATH[1] - self.PERCENT_CONVERTING_MATH[0]) + self.PERCENT_CONVERTING_MATH[0]
#                 myLabel = self.DESCRIPTION_CONVERTING_MATH + str(i + 1) + ' of ' + str(len(equations)) + '...'
#                 self._reportProgress(myProgress, myLabel, alwaysUpdate=True)
#
#                 # Get the prose for the math equation
#                 prose = ''
#                 for speech in self._document.generateSpeech(equations[i]):
#                     prose += speech[0]
#                     break
#
#                 # Remove all of the quotes from the math equation. JAWS reads
#                 # all of the quotes aloud, so it can get annoying
#                 punctuationToRemove = ['"', ',', ';', ':', "'"]
#                 for p in punctuationToRemove:
#                     prose = prose.replace(p, '')
#
#                 # Replace the span with an image representing the equation
#                 svgElem = equations[i].xpath('.//svg')[0]
#                 pngData = self._renderMathSVGToPNG(svgElem, defXMLs)
#                 dataString = 'data:image/png;base64,' + base64.b64encode(pngData)
#                 equations[i].tag = 'img'
#
#                 # Clear out all children and attributes from node
#                 for k in equations[i].attrib.keys():
#                     del equations[i].attrib[k]
#                 for c in equations[i]:
#                     c.getparent().remove(c)
#
#                 # Set the image attributes
#                 equations[i].set('src', dataString)
#                 equations[i].set('alt', prose)
#                 equations[i].set('title', prose)
#
#             except Exception as e:
#                 print 'Equation', i, 'did not parse correctly!', e
#                 traceback.print_exc()
#
#     def _renderMathSVGToPNG(self, svg, defXMLs):
#         '''
#         Renders the Math SVG (an lxml Element) into a PNG. Returns the
#         bytestring containing the PNG data.
#         '''
#         # Create my own SVG with valid namespaces
#         SVG_NS = '{http://www.w3.org/2000/svg}'
#         XLINK_NS = '{http://www.w3.org/1999/xlink}'
#         NS_MAP = {None : SVG_NS[1:-1], 'xlink' : XLINK_NS[1:-1]}
#         myMath = etree.Element('{0}svg'.format(SVG_NS), nsmap=NS_MAP)
#
#         # Copy all attributes
#         for attr in svg.attrib.keys():
#             try:
#                 if ':' in attr:
#                     myAttr = attr[attr.find(':') + 1:]
#                     myMath.set(myAttr, svg.get(attr))
#                 else:
#                     myMath.set(attr, svg.get(attr))
#
#             except Exception as ex:
#                 print 'Could not copy SVG attribute:', ex
#
#         # Copy all elements
#         for m in svg:
#             myMath.append(m)
#
#         # Change the viewbox attribute of <svg> to viewBox
#         if 'viewbox' in myMath.attrib:
#             data = myMath.get('viewbox')
#             myMath.attrib.pop('viewbox')
#             myMath.set('viewBox', data)
#
#         # Insert the defs into my math equation
#         myDef = etree.SubElement(myMath, 'defs')
#         for d in defXMLs:
#             for p in d:
#                 myDef.append(etree.fromstring(etree.tostring(p)))
#
#         # In my math equation, every <use href> must be changed to
#         # <use xlink:href>
#         uses = myMath.xpath('.//use[@href]')
#         for u in uses:
#             data = u.get('href')
#             u.attrib.pop('href')
#             u.set('{0}href'.format(XLINK_NS), data)
#
#         # Change the color of every element in the svg to the text color defined
#         # in user preferences
#         strokes = myMath.xpath(".//*[@stroke]")
#         fills = myMath.xpath(".//*[@fill]")
#         for s in strokes:
#             if not ('none' in s.get('stroke')):
#                 s.set('stroke', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
#         for f in fills:
#             if not ('none' in f.get('fill')):
#                 f.set('fill', configuration.getRGBStringFromQColor(configuration.getColor('ContentTextColor')))
#
#         # Write to temp file, run CairoSVG through it, then push it out
#         svgTemp = os.path.join(self._tempDirectory, 'tmp.svg')
#         with open(svgTemp, 'wb') as f:
#             f.write(etree.tostring(myMath, pretty_print=True))
#
#         tmpURL = urlparse.urljoin('file:', urllib.pathname2url(svgTemp))
#
#         return cairosvg.svg2png(url=tmpURL)
#
#     def _embedImages(self, myHtml):
#         '''
#         It goes through all of the image tags, reads the original image it is
#         referencing, and embeds the image data into the tag so that the document
#         is portable.
#         '''
#         images = myHtml.xpath("//img")
#
#         for i in range(len(images)):
#             if not self._running:
#                 break
#
#             myProgress = float(i) / float(len(images))
#             myProgress = myProgress * (self.PERCENT_EMBED_IMAGES[1] - self.PERCENT_EMBED_IMAGES[0]) + self.PERCENT_EMBED_IMAGES[0]
#             myLabel = self.DESCRIPTION_EMBED_IMAGES + str(i + 1) + ' of ' + str(len(images)) + '...'
#             self._reportProgress(myProgress, myLabel)
#
#             try:
#                 p = images[i].get('src')
#                 images[i].set('src', self._createEmbeddedImageDataURL(p))
#             except urllib2.URLError as e:
#                 # The URL may already be embedded, so don't do it twice.
#                 pass
#
#     def _embedFonts(self, myHtml):
#         '''
#         For all of the @font-face directives in the CSS in the head, get all of
#         the urls, download the font, and embed it.
#         '''
#         styles = myHtml.xpath(r".//head/style[@type='text/css']")
#         fontPattern = r'@font-face[\s]*\{.*?\}'
#         urlPattern = r"url\('(?P<url>.*?)'\)"
#
#         for style in styles:
#             fontSplit = misc.SplitRegex(fontPattern, style.text)
#             for match in fontSplit:
#                 sub = match['value']
#                 urlSplit = misc.SplitRegex(urlPattern, sub)
#                 for u_match in urlSplit:
#                     url_sub = u_match['value']
#                     myUrl = self._createEmbeddedFontDataURL(u_match['matchObj'].group('url'))
#                     u_match['value'] = url_sub.replace(u_match['matchObj'].group('url'), myUrl).replace("'", '')
#                 match['value'] = str(urlSplit)
#
#             style.text = str(fontSplit)
#
#
#     def _embedCSS(self, myHtml):
#         '''
#         Embeds the CSS into the HTML.
#         '''
#         cssLinks = myHtml.findall(".//link[@rel='stylesheet']")
#         head = myHtml.find(".//head")
#
#         for css in cssLinks:
#             print
#
#             # Download the stylesheet
#             f = urllib2.urlopen(css.get('href'))
#             contents = f.read()
#
#             # Create a new element to save the style in
#             newCss = html.Element('style')
#             newCss.set('type', 'text/css')
#             newCss.text = contents
#             head.append(newCss)
#
#             # Remove the link
#             css.getparent().remove(css)
#
#     def _createEmbeddedFontDataURL(self, fontURL):
#         '''
#         Reads in the font from fontURL and encodes to a data URI usable inside
#         a url() for a font-face.
#         '''
#         ext = os.path.splitext(fontURL)[-1].replace('.', '').lower()
#         dataString = 'data:application/x-font-' + ext + ';charset=utf-8;base64,'
#
#         # Read the font
#         f = urllib2.urlopen(fontURL)
#         contents = base64.b64encode(f.read())
#         dataString += contents
#
#         return dataString
#
#     def _createEmbeddedImageDataURL(self, imageURL):
#         '''
#         Reads the image from imageURL and creates a data URL using the data. The
#         data URL should be placed in the car attribute of an <img> tag.
#         '''
#         ext = os.path.splitext(imageURL)[-1].replace('.', '').lower()
#         dataString = 'data:image/' + ext + ';base64,'
#
#         # Read the image
#         f = urllib2.urlopen(imageURL)
#         contents = base64.b64encode(f.read())
#         dataString += contents
#
#         return dataString
#
#     def _getTextInsideElement(self, elem):
#         myText = ''
#         if elem.text is not None:
#             myText += elem.text
#
#         for c in elem:
#             myText += self._getTextInsideElement(c)
#             if c.tail is not None:
#                 myText += c.tail
#
#         return myText