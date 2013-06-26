'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''

import zipfile
from lxml import etree
from lxml import html as HTML
import os
import urllib
from src.gui.bookmarks import BookmarkNode
from src.misc import program_path, app_data_path, temp_path
from src.mathtype.parser import parseWMF

# The path to this particular module
rootPath = 'src/docx'

# Get my OMML to MathML stylesheet compiled
ommlXSLTPath = program_path(os.path.join(rootPath, 'OMMLToMathML.xsl'))

f = open(ommlXSLTPath, 'r')
xslRoot = etree.parse(f)
ommlTransform = etree.XSLT(xslRoot)
f.close()

# Namespaces inside .docx xml
w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
wp_NS = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
m_NS = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
pic_NS = '{http://schemas.openxmlformats.org/drawingml/2006/picture}'
r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'
rel_NS = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
a_NS = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
o_NS = '{urn:schemas-microsoft-com:office:office}'
v_NS = '{urn:schemas-microsoft-com:vml}'

# Heirarchical levels of each of the styles
heirarchyStyles = {'Title' : 1,
                  'Heading 1': 2,
                  'heading 1' : 2,
                  'Heading 2': 3,
                  'heading 2': 3,
                  'Heading 3': 4,
                  'heading 3': 4,
                  'Heading 4': 5,
                  'heading 4': 5}

# HTML elements for each level
htmlLevels = {1 : 'h1',
              2 : 'h2',
              3 : 'h3',
              4 : 'h4',
              5 : 'h5',
              -1 : 'p'} # Default

def clean_XML_input(input):  
      
    if input:  
        import re
        # unicode invalid characters  
        RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + u'|' + u'([{0}-{1}][^{2}-{3}])|([^{4}-{5}][{6}-{7}])|([{8}-{9}]$)|(^[{10}-{11}])'.format(
                        unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))
        input = re.sub(RE_XML_ILLEGAL, "", input)  
                          
        # ascii control characters  
        input = re.sub(r"[\x01-\x1F\x7F]", "", input)  
              
    return input.decode('utf8')

class DocxDocument(object):
    '''
    Imports a .docx and transforms it to meet my needs. Although it has not been 
    implemented yet, it will eventually support streaming, especially if we are
    dealing with very large books.
    
    The progressCallback expects a function that will handle the following
    arguments:
    
    progressCallback(percentageOutOf100)
    '''
    
    def __init__(self, docxFilePath, progressCallback=None, checkCancelFunction=None):
        '''
        Generates the document structure from the .docx file.
        '''
        
        self.docxFilePath = docxFilePath
        
        self.importFolder = temp_path('import')
        
        if progressCallback:
            progressCallback(0)
        
        # .docx is just a zip file
        self.zip = zipfile.ZipFile(docxFilePath, 'r')
        
        self.rels = self._getRels(self.zip)
        self.styles = self._getStyles(self.zip)
        self.paraStylesDict = self._getParaStylesDict(self.styles)
        #self.numberingDict = self._getNumberingDict(self.zip)
        
        # Open my main document file
        document = self.zip.open('word/document.xml', 'r')
        tree = etree.parse(document)
        document.close()
        root = tree.getroot()
        
        # Parse every paragraph in this document into a form I can convert later
        paragraphs = root.findall('./{0}body/*'.format(w_NS))
        self.paragraphData = []
        i = 0
        for p in paragraphs:
            
            if checkCancelFunction:
                if checkCancelFunction():
                    break
            
            if progressCallback:
                progressCallback(int(float(i) / len(paragraphs) * 100))
                
            i += 1 
            if p.tag == '{0}p'.format(w_NS):
                newPara = self._parseParagraph(p)
                if len(newPara['data']) > 0:
                    self.paragraphData.append(newPara)
            elif p.tag == '{0}tbl'.format(w_NS):
                self.paragraphData.append(self._parseTable(p))
                
        self.zip.close()
        
        # Finally, create the HTML for the thing
        self._createHTML()
        
    def _getRels(self, zip):
        relFile = zip.open('word/_rels/document.xml.rels', 'r')
        myRels = etree.parse(relFile)
        myRels = myRels.findall('./{0}Relationship'.format(r_NS))
        relFile.close()
        return myRels
    
    def _getStyles(self, zip):
        stylesFile = zip.open('word/styles.xml', 'r')
        myStyles = etree.parse(stylesFile)
        myStyles = myStyles.findall('./{0}style'.format(w_NS))
        stylesFile.close()
        return myStyles
    
    def _getParaStylesDict(self, styles):
        '''
        Returns a dictionary where the key is the style id and the value is the
        name of that style.
        '''
        myDict = {}
        for s in styles:
            query = s.find('./{0}name'.format(w_NS))
            if query != None:
                key = s.get('{0}styleId'.format(w_NS))
                value = query.get('{0}val'.format(w_NS))
                myDict[key] = value
        return myDict
    
    def _getNumberingDict(self, zip):
        '''
        Returns a nested dictionary that looks like the following:
        
        {numId : {levelId : {"format" : "decimal|bullet", "start" : 0}, levelId : {...}, ...}}
        '''
        myDict = {}
        
        if 'word/numbering.xml' in zip.namelist():
            # Get the numbering XML
            numberingFile = zip.open('word/numbering.xml', 'r')
            numXML = etree.parse(numberingFile)
            numberingFile.close()
            
            # Get all numberings and get the abstract element they refer to
            # (pointless indirection in my opinion)
            nums = numXML.findall('./{0}num'.format(w_NS))
            for e in nums:
                abstractId = e.find('./{0}abstractNumId'.format(w_NS)).attrib['{0}val'.format(w_NS)]
                abstractNum = numXML.find('./{0}abstractNum[@{0}abstractNumId=\''.format(w_NS) + abstractId + '\']')
                
                # Get list of levels in that particular element
                levels = abstractNum.findall('./{0}lvl'.format(w_NS))
                levelDicts = {}
                for l in levels:
                    key = l.attrib['{0}ilvl'.format(w_NS)]
                    levelDicts[key] = {}
                    format = l.find('./{0}numFmt'.format(w_NS)).attrib['{0}val'.format(w_NS)]
                    
                    if l.find('./{0}start'.format(w_NS)):
                        levelDicts[key]['start'] = l.find('./{0}start'.format(w_NS)).attrib['{0}val'.format(w_NS)]
                    else:
                        levelDicts[key]['start'] = 1
                    
                    #start = l.find('./{0}start'.format(w_NS)).attrib['{0}val'.format(w_NS)]
                    levelDicts[key]['format'] = format
                
                key = e.attrib['{0}numId'.format(w_NS)]
                myDict[key] = levelDicts
                
        return myDict
    
    def _isList(self, elem):
        '''
        Returns whether the element is numbered, or in other words, a part of an
        ordered list or unordered list
        '''
        return elem.find('./{0}pPr/{0}numPr'.format(w_NS)) != None
        
    def _parseParagraph(self, elem):
        parseData = {'type' : 'paragraph'}
        parseData['data'] = []
        
        # Add bullet or numbered list information if any
#         if self._isList(elem):
#             numId = elem.find('./{0}pPr/{0}numPr/{0}numId'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#             levelId = elem.find('./{0}pPr/{0}numPr/{0}ilvl'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#             myNumDict = self.numberingDict[numId][levelId]
#             parseData['list'] = True
#             parseData['format'] = myNumDict['format']
#             parseData['start'] = int(myNumDict['start'])
#             parseData['level'] = int(levelId)
        
        for child in elem:
            
            # Paragraph style
            if child.tag == '{0}pPr'.format(w_NS):
                self._parseParagraphStyle(child, parseData)
            
            # OMML equation as separate paragraph
            elif child.tag == '{0}oMathPara'.format(m_NS):
                self._parseOMMLPara(child, parseData)
            
            # Inline OMML equation
            elif child.tag == '{0}oMath'.format(m_NS):
                self._parseOMML(child, parseData)
                
            # A row object, which usually has text but may have other inline
            # content, like images
            elif child.tag == '{0}r'.format(w_NS):
                self._parseRow(child, parseData)
                
            # Hyperlink
            elif child.tag == '{0}hyperlink'.format(w_NS):
                
                hyperlinkData = {'type' : 'hyperlink'}
                
                # Get all of the text from all of the rows and put it all
                # together
                text = ''
                textNodes = child.xpath('w:r/w:t', namespaces={'w': w_NS[1:-1]})
                for t in textNodes:
                    text += t.text
                hyperlinkData['text'] = text
                    
                # Get the link URL from the rels
                myId = child.get('{0}id'.format(rel_NS))
                for r in self.rels:
                    if r.get('Id') == myId:
                        hyperlinkData['value'] = r.get('Target')
                            
                    
                print 'Before URL:', hyperlinkData['value']
                # Add the http:// in the beginning if not present
                if 'http://' in hyperlinkData['value']:
                    pass
                else:
                    hyperlinkData['value'] = 'http://' + hyperlinkData['value']
            
                print 'After URL:', hyperlinkData['value']
                    
                parseData['data'].append(hyperlinkData)
                
                
        return parseData
    
    def _parseOMMLPara(self, elem, parentData):
        mathRoot = elem[0]  # Get the first child
        self._parseOMML(mathRoot, parentData)
    
    def _parseOMML(self, elem, parentData):
        data = {'type' : 'math'}
        data['data'] = self._convertOMMLToMathML(elem)
        parentData['data'].append(data)
        
    def _parseObject(self, elem, parentData):
        # Only do something to it if the object is MathType
        query = elem.find('{0}OLEObject[@ProgID="Equation.DSMT4"]'.format(o_NS))
        if query != None:
            data = {'type' : 'math'}
            
            # Get the image data for it
            query = elem.find('{0}shape/{0}imagedata'.format(v_NS))
            id = query.attrib['{0}id'.format(rel_NS)]
            
            # See which filename it refers to and create a valid one
            filename = ''
            for rel in self.rels:
                if rel.get('Id') == id:
                    filename = os.path.split(rel.get('Target'))[1]
                    break
            
            # Figure out the image type to run correct parser through
            imageFile = self.zip.open('word/media/' + filename, 'r')
            imageType = os.path.splitext(filename)[1].lower()
            if imageType == '.wmf':
                data['data'] = parseWMF(imageFile)
                parentData['math'] = data
                
            imageFile.close()
    
    def _parseParagraphStyle(self, elem, parentData):
        query = elem.find('./{0}pStyle'.format(w_NS))
        if query != None:
            style = query.get('{0}val'.format(w_NS))
            if style in self.paraStylesDict:
                parentData['style'] = self.paraStylesDict[style]
            
        rowQuery = elem.find('./{0}rPr/{0}rStyle'.format(w_NS))
        if rowQuery != None:
            if 'pagenumber' in rowQuery.attrib['{0}val'.format(w_NS)].lower():
                parentData['pageNumber'] = True
    
    def _parseRow(self, elem, parentData):
        data = {'type' : 'row'}
        for child in elem:
            # Text
            if child.tag == '{0}t'.format(w_NS):
                data['text'] = clean_XML_input(child.text.encode('utf-8'))
            
            # Image or some drawing
            if child.tag == '{0}drawing'.format(w_NS):
                self._parseImage(child, data)
                
            if child.tag == '{0}object'.format(w_NS):
                self._parseObject(child, data)
                
        parentData['data'].append(data)
                
    def _parseImage(self, elem, parentData):
        
        # Check to see if there is an image. If yes, create an image node that
        # has the correct filename reference to it
        query = elem.find('.//{0}pic'.format(pic_NS))
        if query != None:
            
            data = {'type' : 'image'}
            
            query = query.find('.//{0}blip'.format(a_NS))
            
            # Grab the ID from it
            id = query.get('{0}embed'.format(rel_NS))
                        
            # See which filename it refers to and create a valid one
            filename = ''
            for rel in self.rels:
                if rel.get('Id') == id:
                    filename = os.path.split(rel.get('Target'))[1]
                    data['filename'] = clean_XML_input(filename)
                    break
                
            # Get the description text for the image
            query = elem.find('.//{0}docPr'.format(wp_NS))
            if query != None:
                altText = query.get('descr')
                if altText != None:
                    data['altText'] = clean_XML_input(altText)
                
            # Append this to the parent data
            parentData['image'] = data
                
    def _parseTable(self, elem):
        parseData = {'type' : 'table'}
        parseData['rows'] = []
        
        # Find all of my rows
        rowElems = elem.findall('./{0}tr'.format(w_NS))
        
        for row in rowElems:
            rowData = {'type' : 'row'}
            rowData['columns'] = []
            
            for child in row:
                
                # Column contents
                if child.tag == '{0}tc'.format(w_NS):
                    # Get the paragraph in there
                    myP = child.find('./{0}p'.format(w_NS))
                    rowData['columns'].append(self._parseParagraph(myP))
                    
            parseData['rows'].append(rowData)
                    
        return parseData
    
    def _convertOMMLToMathML(self, ommlNode):
        '''
        Converts an oMath lxml node into a MathML node.
        '''
        mathml = ommlTransform(ommlNode)
        
        # Convert the transformed XML into UTF-8 while removing a bunch of
        # prefix crap
        mathml = etree.fromstring(etree.tostring(mathml, encoding='utf-8', xml_declaration=False).replace('mml:', '').replace(':mml', ''))
        
        return mathml
    
    def _prepareHead(self, head):
        
        mathjaxConfig = HTML.Element('script')
        mathjaxConfig.set('type', 'text/x-mathjax-config')
        scriptFile = open(program_path(os.path.join(rootPath, 'mathjax_config.js')))
        contents = scriptFile.read()
        scriptFile.close()
        mathjaxConfig.text = contents
        
        mathjaxScript = HTML.Element('script')
        mathjaxScript.attrib['type'] = 'text/javascript'
        mathjaxScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('mathjax/MathJax.js')) + r'?config=TeX-AMS-MML_HTMLorMML.js'
        
        jqueryScript = HTML.Element('script')
        jqueryScript.attrib['type'] = 'text/javascript'
        jqueryScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery-1.9.1.min.js'))
            
        jqueryUIScript = HTML.Element('script')
        jqueryUIScript.attrib['type'] = 'text/javascript'
        jqueryUIScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery-ui/js/jquery-ui-1.9.2.custom.js'))
        
        jqueryScrollTo = HTML.Element('script')
        jqueryScrollTo.attrib['type'] = 'text/javascript'
        jqueryScrollTo.attrib['src'] = 'file:' + urllib.pathname2url(program_path('jquery.scrollTo-1.4.3.1-min.js'))
        
        myScripts = HTML.Element('script')
        myScripts.set('language', 'javascript')
        myScripts.set('type', 'text/javascript')
        
        scriptFile = open(program_path(os.path.join(rootPath, 'my_functions.js')), 'r')
        contents = scriptFile.read()
        scriptFile.close()
        myScripts.text = contents
        
        css = HTML.Element('link')
        css.attrib['rel'] = 'stylesheet'
        css.attrib['type'] = 'text/css'
        css.attrib['href'] = 'file:' + urllib.pathname2url(temp_path('import/defaultStyle.css'))
        
        head.append(mathjaxConfig)
        head.append(mathjaxScript)
        head.append(jqueryScript)
        head.append(jqueryUIScript)
        head.append(jqueryScrollTo)
        head.append(myScripts)
        head.append(css)
        
    def _prepareBody(self, body):
        anchorCount = 1
        i = 0
        while i < len(self.paragraphData):
            if self.paragraphData[i]['type'] == 'paragraph':
                
#                 if 'list' in self.paragraphData[i]:
#                     
#                     # Make a list of bullets or numbered elements
#                     parent = None
#                     startFormat = self.paragraphData[i]['format']
#                     if startFormat == 'bullet':
#                         parent = etree.SubElement(body, 'ul')
#                     elif startFormat == 'decimal':
#                         parent = etree.SubElement(body, 'ol')
#                     else:
#                         parent = etree.SubElement(body, 'ul')
#                     while i < len(self.paragraphData) and 'list' in self.paragraphData[i]:
#                         if self.paragraphData[i]['format'] != startFormat:
#                             break
#                         data = self._generateParagraphHTMLNode(self.paragraphData[i], anchorCount)
#                         if data[1]:
#                             anchorCount += 1
#                         childElem = etree.SubElement(parent, 'li')
#                         childElem.append(data[0])
#                         i += 1
                data = self._generateParagraphHTMLNode(self.paragraphData[i], anchorCount)
                if data[1]:
                    anchorCount += 1
                    body.append(data[0])
                else:
                    body.append(data[0])
                i += 1
            elif self.paragraphData[i]['type'] == 'table':
                body.append(self._generateTableHTMLNode(self.paragraphData[i]))
                i += 1
                
    def _generateTableHTMLNode(self, t):
        '''
        From a table dictionary, create the HTML for it.
        '''
        tRoot = HTML.Element('table')
        
        for r in t['rows']:
            rRoot = etree.SubElement(tRoot, 'tr')
            
            for c in r['columns']:
                cRoot = etree.SubElement(rRoot, 'td')
                cRoot.append(self._generateParagraphHTMLNode(c, 0)[0])
                
        return tRoot
    
    def _generateParagraphHTMLNode(self, p, anchorId):
        '''
        From a paragraph dictionary, create the HTML for it, and whether the
        anchorID needs to be increased:
        (htmlELement, boolean)
        '''
        pRoot = None
        incrementAnchorId = False
        
        # Figure out what my root HTML will be
        level = -1
        if 'style' in p:
            if p['style'] in heirarchyStyles:
                level = heirarchyStyles[p['style']]
                incrementAnchorId = True
                
        pRoot = HTML.Element(htmlLevels[level])
        
        # Set the id for bookmark navigation
        if level >= 0:
            pRoot.set('id', str(anchorId))
        
        # Loop through the content in the paragraph
        currTextNode = pRoot
        currTextNode.text = ''
        currTextNode.tail = ''
        onRoot = True
        for c in p['data']:
            
            if c['type'] == 'row':
                if 'text' in c:
                    if onRoot:
                        currTextNode.text += c['text']
                    else:
                        currTextNode.tail += c['text']
                    
                elif 'image' in c:
                    image = c['image']
                    imageTag = etree.SubElement(pRoot, 'img')
                    imageTag.set('src', self.importFolder + '/images/' + image['filename'])
                    if 'altText' in image:
                        imageTag.set('alt', image['altText'])
                        imageTag.set('title', image['altText'])
                    currTextNode = imageTag
                    currTextNode.tail = ''
                    onRoot = False
                    
                elif 'math' in c:
                    mathSpan = etree.SubElement(pRoot, 'span')
                    mathSpan.set('class', 'mathmlEquation')
                    mathSpan.append(c['math']['data'])
                    currTextNode = mathSpan
                    currTextNode.tail = ''
                    onRoot = False
            
            elif c['type'] == 'math':
                mathSpan = etree.SubElement(pRoot, 'span')
                mathSpan.set('class', 'mathmlEquation')
                mathSpan.append(c['data'])
                currTextNode = mathSpan
                currTextNode.tail = ''
                onRoot = False
                
            elif c['type'] == 'hyperlink':
                hyperlink = etree.SubElement(pRoot, 'a')
                hyperlink.set('href', c['value'])
                hyperlink.text = c['text']
        
        # Check to see if it is a page number
        if 'pageNumber' in p:
            pRoot.set('id', 'page' + pRoot.text_content())
            pRoot.set('class', 'pageNumber')
        
        # Return what I got
        return (pRoot, incrementAnchorId)
    
    def _saveImages(self):
        
        # Open a zip file of my docx file
        zip = zipfile.ZipFile(self.docxFilePath, 'r')
        
        # Delete images directory, if there is one
        if os.path.isdir(self.importFolder + '/images'):
            for the_file in os.listdir(self.importFolder + '/images'):
                file_path = os.path.join(self.importFolder + '/images', the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    print e
        else:
            os.makedirs(self.importFolder + '/images')
    
        for f in zip.namelist():
            if f.find('word/media/') == 0:
                # Extract it to my import folder
                imageFile = open(self.importFolder + '/images/' + f.replace('word/media/', ''), 'wb')
                imageFile.write(zip.read(f))
                imageFile.close()
        
        zip.close()
            
    def getMainPage(self):
        return self._html
        
    
    def _createHTML(self):
        '''
        Generates the HTML for the page.
        '''
        # Start with the basics
        html = HTML.Element('html')
        head = HTML.Element('head')
        body = HTML.Element('body')
        html.append(head)
        html.append(body)
        
        # Create the scripts and other references here in the head
        self._prepareHead(head)
        self._prepareBody(body)
        
        # Write out the images to the import folder
        self._saveImages()
        
        self._html = HTML.tostring(html)
    
    def getPages(self):
        '''
        Returns the PageNodes for this document.
        '''
        myPages = []
        
        for p in self.paragraphData:
            if 'pageNumber' in p:
                myPages.append(self._generateParagraphHTMLNode(p, 0)[0].text_content())
        
        return myPages
    
    def getBookmarks(self):
        '''
        Returns the BookmarkNodes for this document.
        '''
        # State data for creating the bookmarks
        parentStack = [(BookmarkNode(None, 'Docx'), 0)]
        lastNode = parentStack[0]
        currLevel = -1
        anchorCount = 1
        
        # The paragraphs are just a bunch of dictionaries
        for p in self.paragraphData:
            
            if 'style' in p:
                if p['style'] in heirarchyStyles:
                    currLevel = heirarchyStyles[p['style']]
                else:
                    currLevel = -1
            else:
                currLevel = -1
        
            # Create a bookmark if it is an actual hierarchical piece of content  
            if currLevel > 0:
                
                # Add last node inserted as parent if it is logical to do so
                if lastNode[1] < currLevel:
                    parentStack.append(lastNode)
                    
                # Pop off unsuitable parents
                while True:
                    if parentStack[-1][1] >= currLevel:
                        parentStack.pop()
                    else:
                        break
                    
                # Make my BookmarkNode and stuff
                if len(parentStack) > 0:
                    myNode = BookmarkNode(parentStack[-1][0], self._generateParagraphHTMLNode(p, 0)[0].text_content(), anchorId=str(anchorCount))
                    lastNode = (myNode, currLevel)
                else:
                    myNode = BookmarkNode(lastNode[0], self._generateParagraphHTMLNode(p, 0)[0].text_content(), anchorId=str(anchorCount))
                    lastNode = (myNode, currLevel)
                    
                anchorCount += 1
                
        # Return my root bookmark
        return parentStack[0][0]
            
        