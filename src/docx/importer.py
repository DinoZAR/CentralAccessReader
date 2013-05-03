'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''

import zipfile
from lxml import etree
from lxml import html as HTML
import os
import sys
import inspect
from src.gui.bookmarks import BookmarkNode
from src.misc import resource_path

# The path to this particular module
#rootPath = os.path.dirname(inspect.getfile(inspect.currentframe()))
rootPath = 'docx'

# Get my OMML to MathML stylesheet compiled
ommlXSLTPath = resource_path(os.path.join(rootPath, 'OMMLToMathML.xsl'))

print 'Opening the OMML File:'
print '----------------------------'
print ommlXSLTPath
print '----------------------------'

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

class DocxDocument(object):
    '''
    Imports a .docx and transforms it to meet my needs. Although it has not been 
    implemented yet, it will eventually support streaming, especially if we are
    dealing with very large books.
    '''
    
    def __init__(self, docxFilePath):
        '''
        Generates the document structure from the .docx file.
        '''
        
        self.docxFilePath = docxFilePath
        
        # .docx is just a zip file
        zip = zipfile.ZipFile(docxFilePath, 'r')
        
        # First, grab the relationships file. This has the id's and pointers to 
        # different bits of data, most importantly images.
        relFile = zip.open('word/_rels/document.xml.rels', 'r')
        
        self.rels = etree.parse(relFile)
        self.rels = self.rels.findall('./{0}Relationship'.format(r_NS))
        
        relFile.close()
        
        # Grab the styles too to match up the headings and other parts.
        stylesFile = zip.open('word/styles.xml', 'r')
        
        self.styles = etree.parse(stylesFile)
        self.styles = self.styles.findall('./{0}style'.format(w_NS))
        
        stylesFile.close()
        
        # Set the import folder to put all of my images and stuff
        self.importFolder = 'import'
        
        # Now generate a dictionary that can look up the name of the style depending
        # on the id of the style
        self.stylesDict = {}
        for s in self.styles:
            query = s.find('./{0}name'.format(w_NS))
            if query != None:
                key = s.get('{0}styleId'.format(w_NS))
                value = query.get('{0}val'.format(w_NS))
                self.stylesDict[key] = value
        
        # Open my main document file
        document = zip.open('word/document.xml', 'r')
        tree = etree.parse(document)
        document.close()
        root = tree.getroot()
        
        # Parse every paragraph in this document into a form I can convert later
        paragraphs = root.findall('./{0}body/*'.format(w_NS))
        self.paragraphData = []
        for p in paragraphs:
            if p.tag == '{0}p'.format(w_NS):
                newPara = self._parseParagraph(p)
                if len(newPara['data']) > 0:
                    self.paragraphData.append(newPara)
            elif p.tag == '{0}tbl'.format(w_NS):
                self.paragraphData.append(self._parseTable(p))
                
        zip.close()
        
    def _parseParagraph(self, elem):
        parseData = {'type' : 'paragraph'}
        parseData['data'] = []
        
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
                
        return parseData
    
    def _parseOMMLPara(self, elem, parentData):
        mathRoot = elem[0]  # Get the first child
        self._parseOMML(mathRoot, parentData)
    
    def _parseOMML(self, elem, parentData):
        data = {'type' : 'math'}
        data['data'] = self._convertOMMLToMathML(elem)
        parentData['data'].append(data)
    
    def _parseParagraphStyle(self, elem, parentData):
        query = elem.find('./{0}pStyle'.format(w_NS))
        if query != None:
            style = query.get('{0}val'.format(w_NS))
            if style in self.stylesDict:
                parentData['style'] = self.stylesDict[style]
    
    def _parseRow(self, elem, parentData):
        data = {'type' : 'row'}
        for child in elem:
            # Text
            if child.tag == '{0}t'.format(w_NS):
                data['text'] = child.text.encode('utf-8', errors='ignore')
            
            # Image or some drawing
            if child.tag == '{0}drawing'.format(w_NS):
                self._parseImage(child, data)
                
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
                    data['filename'] = filename
                    break
                
            # Get the description text for the image
            query = elem.find('.//{0}docPr'.format(wp_NS))
            if query != None:
                altText = query.get('descr')
                data['altText'] = altText
                
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
        scriptFile = open(resource_path(os.path.join(rootPath, 'mathjax_config.js')))
        contents = scriptFile.read()
        scriptFile.close()
        mathjaxConfig.text = contents
        
        mathjaxScript = HTML.Element('script')
        mathjaxScript.attrib['type'] = 'text/javascript'
        
        # This has to change depending on whether we have built this as .exe or
        # not
        if getattr(sys, 'frozen', None):
            mathjaxScript.attrib['src'] = r'mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML.js'
        else:
            mathjaxScript.attrib['src'] = r'../mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML.js'
        
        jqueryScript = HTML.Element('script')
        jqueryScript.attrib['type'] = 'text/javascript'
        if getattr(sys, 'frozen', None):
            jqueryScript.attrib['src'] = r'jquery-1.9.1.min.js'
        else:
            jqueryScript.attrib['src'] = r'../jquery-1.9.1.min.js'
            
        jqueryUIScript = HTML.Element('script')
        jqueryUIScript.attrib['type'] = 'text/javascript'
        if getattr(sys, 'frozen', None):
            jqueryUIScript.attrib['src'] = r'jquery-ui/js/jquery-ui-1.9.2.custom.js'
        else:
            jqueryUIScript.attrib['src'] = r'../jquery-ui/js/jquery-ui-1.9.2.custom.js'
            
            
        
        jqueryScrollTo = HTML.Element('script')
        jqueryScrollTo.attrib['type'] = 'text/javascript'
        if getattr(sys, 'frozen', None):
            jqueryScrollTo.attrib['src'] = r'jquery.scrollTo-1.4.3.1-min.js'
        else:
            jqueryScrollTo.attrib['src'] = r'../jquery.scrollTo-1.4.3.1-min.js'
        
        myScripts = HTML.Element('script')
        myScripts.set('language', 'javascript')
        myScripts.set('type', 'text/javascript')
        
        scriptFile = open(resource_path(os.path.join(rootPath, 'my_functions.js')), 'r')
        contents = scriptFile.read()
        scriptFile.close()
        myScripts.text = contents
        
        css = HTML.Element('link')
        css.attrib['rel'] = 'stylesheet'
        css.attrib['type'] = 'text/css'
        css.attrib['href'] = 'import/defaultStyle.css'
        
        head.append(mathjaxConfig)
        head.append(mathjaxScript)
        head.append(jqueryScript)
        head.append(jqueryUIScript)
        head.append(jqueryScrollTo)
        head.append(myScripts)
        head.append(css)
        
    def _prepareBody(self, body):
        anchorCount = 1
        for p in self.paragraphData:
            if p['type'] == 'paragraph':
                data = self._generateParagraphHTMLNode(p, anchorCount)
                if data[1]:
                    anchorCount += 1
                body.append(data[0])
            elif p['type'] == 'table':
                body.append(self._generateTableHTMLNode(p))
                
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
                    onRoot = True
                    
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
            
            elif c['type'] == 'math':
                mathSpan = etree.SubElement(pRoot, 'span')
                mathSpan.set('class', 'mathmlEquation')
                mathSpan.append(c['data'])
                currTextNode = mathSpan
                currTextNode.tail = ''
                onRoot = False
        
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
        '''
        Returns the HTML of the main landing page. This page will have the
        scripts for highlighting as well as content streaming (when available).
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
        
        return HTML.tostring(html, pretty_print=True)
    
    def getBookmarks(self):
        '''
        Returns the BookmarkNodes for this particular document.
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
            
        