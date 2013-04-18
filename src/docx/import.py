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
        
        # Now generate a dictionary that can look up the name of the style depending
        # on the id of the style
        self.stylesDict = {}
        for s in self.styles:
            query = s.find('./{0}name'.format(w_NS))
            if query != None:
                key = s.get('{0}styleId'.format(w_NS))
                value = query.get('{0}val'.format(w_NS))
                self.stylesDict[key] = value
        
        # Grab the paragraphs from the document. They're more like <div> tags in
        # HTML. I will obtain the style of the paragraph as a whole, and for each
        # "row" (more like a <span> really), grab the text, equation, image, or
        # something from it along with the styling pertaining to that "row".
        #
        # The resulting data structure will look like this:
        # ([(objectInRow, rowStyle), [row]...], paragraphStyleID)
        # for each paragraph
        document = zip.open('word/document.xml', 'r')
        
        tree = etree.parse(document)
        
        # When we are done with them, close them up
        document.close()
        
        root = tree.getroot()
        
        paras = root.findall('.{0}body/{0}p'.format(w_NS))
        
        paraData = []
        
        for p in paras:
            pStyle = None
            rows = []
            for element in p:
                if element.tag == '{0}pPr'.format(w_NS):
                    # Got a paragraph style.
                    query = element.find('./{0}pStyle'.format(w_NS))
                    if query != None:
                        pStyle = query.get('{0}val'.format(w_NS))
                
                elif element.tag == '{0}oMathPara'.format(m_NS):
                    # An OMML equation in its own paragraph
                    mathRoot = element[0]
                    rows.append((mathRoot, None))
                    
                elif element.tag == '{0}oMath'.format(m_NS):
                    # An inline OMML equation. Treat like others
                    rows.append((element, None))
                    
                elif element.tag == '{0}r'.format(w_NS):
                    # A row object. Usually has text, but can have inline content
                    rowStyle = None
                    rowObject = None
                    for child in element:
                        if child.tag == '{0}rPr'.format(w_NS):
                            rowStyle = child
                        else:
                            rowObject = child
                            
                    rows.append((rowObject, rowStyle))
            
            paraData.append((rows, pStyle))
            
        
        # Start generating my HTML tree. Start with da basics
        html = HTML.Element('html')
        head = HTML.Element('head')
        body = HTML.Element('body')
        html.append(head)
        html.append(body)
        
        importFolder = 'import/images'
        
        _prepareHead(head)
        bookmarkRoot = _prepareBody(body, paraData, rels, stylesDict, importFolder)
        
        _grabImages(zip, importFolder)
        
        zip.close()
        