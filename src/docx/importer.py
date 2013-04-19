'''
Created on Apr 18, 2013

@author: Spencer Graffe
'''

import zipfile
from lxml import etree
from lxml import html as HTML
from lxml.builder import E
import copy
import os
import platform
import inspect
from src.gui.bookmarks import BookmarkNode

rootPath = os.path.dirname(inspect.getfile(inspect.currentframe()))

# Get my OMML to MathML stylesheet compiled
ommlXSLTPath = os.path.normpath(rootPath + '/OMMLToMathML.xsl')
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
        self.imageFolder = 'import/images'
        
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
        
        # When we are done with them, close them up
        document.close()
        
        root = tree.getroot()
        
        # Parse every paragraph in this document into a form I can convert later
        paragraphs = root.findall('./{0}body/*'.format(w_NS))
        self.paragraphData = []
        for p in paragraphs:
            if p.tag == '{0}p'.format(w_NS):
                self.paragraphData.append(self._parseParagraph(p))
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
        self._parseOMML(elem, parentData)
    
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
                data['text'] = child.text
            
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
        scriptFile = open(os.path.normpath(rootPath + '/mathjax_config.js'))
        contents = scriptFile.read()
        scriptFile.close()
        mathjaxConfig.text = contents
        
        mathjaxScript = HTML.Element('script')
        mathjaxScript.attrib['type'] = 'text/javascript'
        mathjaxScript.attrib['src'] = r'../mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML.js'
        
        jqueryScript = HTML.Element('script')
        jqueryScript.attrib['type'] = 'text/javascript'
        jqueryScript.attrib['src'] = r'../jquery-1.9.1.min.js'
        
        myScripts = HTML.Element('script')
        myScripts.set('language', 'javascript')
        myScripts.set('type', 'text/javascript')
        
        scriptFile = open(os.path.normpath(rootPath + '/my_functions.js'), 'r')
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
        head.append(myScripts)
        head.append(css)
            
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
        
        return HTML.tostring(html, pretty_print=True)
        