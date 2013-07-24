'''
Created on Jul 11, 2013

@author: Spencer Graffe
'''
import os
import traceback
from lxml import etree
from lxml import html as HTML
from src.mathtype.parser import parseWMF, MathTypeParseError
from src.misc import program_path, temp_path, REPORT_BUG_URL
from cStringIO import StringIO

# The path to this particular module
ROOT_PATH = program_path('src/docx')
IMPORT_FOLDER = temp_path('import')

# This dictionary holds image file extensions that must be converted to another
# image type because the WebView doesn't support displaying it
IMAGE_TRANSLATION = {'.emf' : '.png'}

# Get my OMML to MathML stylesheet compiled
ommlXSLTPath = os.path.join(ROOT_PATH, 'OMMLToMathML.xsl')

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

# def clean_XML_input(input):  
#       
#     if input:  
#         import re
#         # unicode invalid characters  
#         RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + u'|' + u'([{0}-{1}][^{2}-{3}])|([^{4}-{5}][{6}-{7}])|([{8}-{9}]$)|(^[{10}-{11}])'.format(
#                         unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))
#         input = re.sub(RE_XML_ILLEGAL, '', input)  
#                           
#         # ascii control characters  
#         input = re.sub(r'[\x01-\x1F\x7F]', '', input)  
#               
#     return input.decode('utf8')

def parseParagraph(elem, otherData):
    parseData = {'type' : 'paragraph'}
    parseData['data'] = []
    
    # Add bullet or numbered list information if any
#         if _isList(elem):
#             numId = elem.find('./{0}pPr/{0}numPr/{0}numId'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#             levelId = elem.find('./{0}pPr/{0}numPr/{0}ilvl'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#             myNumDict = numberingDict[numId][levelId]
#             parseData['list'] = True
#             parseData['format'] = myNumDict['format']
#             parseData['start'] = int(myNumDict['start'])
#             parseData['level'] = int(levelId)
    
    for child in elem:
        
        # Paragraph style
        if child.tag == '{0}pPr'.format(w_NS):
            _parseParagraphStyle(child, parseData, otherData)
        
        # OMML equation as separate paragraph
        elif child.tag == '{0}oMathPara'.format(m_NS):
            _parseOMMLPara(child, parseData)
        
        # Inline OMML equation
        elif child.tag == '{0}oMath'.format(m_NS):
            _parseOMML(child, parseData)
            
        # A row object, which usually has text but may have other inline
        # content, like images
        elif child.tag == '{0}r'.format(w_NS):
            _parseRow(child, parseData, otherData)
            
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
            for r in otherData['rels']:
                if r.get('Id') == myId:
                    hyperlinkData['value'] = r.get('Target')
                        
            # Add the http:// in the beginning if not present
            if 'http://' in hyperlinkData['value']:
                pass
            else:
                hyperlinkData['value'] = 'http://' + hyperlinkData['value']
                
            parseData['data'].append(hyperlinkData)
    
    # Generate the HTML from the parse data
    htmlContent = _generateParagraphHTMLNode(parseData)
                
    return htmlContent

def parseTable(elem, otherData):
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
                rowData['columns'].append(parseParagraph(myP, otherData))
                
        parseData['rows'].append(rowData)
        
    # Generate the HTML content from it
    htmlContent = _generateTableHTMLNode(parseData)
                
    return htmlContent

def _parseOMMLPara(elem, parentData):
    mathRoot = elem[0]  # Get the first child
    _parseOMML(mathRoot, parentData)

def _parseOMML(elem, parentData):
    data = {'type' : 'math'}
    data['data'] = _convertOMMLToMathML(elem)
    parentData['data'].append(data)

def _parseObject(elem, parentData, otherData):
    # Only do something to it if the object is MathType
    query = elem.find('{0}OLEObject[@ProgID="Equation.DSMT4"]'.format(o_NS))
    if query != None:
        data = {'type' : 'math'}
        
        # Get the image data for it
        query = elem.find('{0}shape/{0}imagedata'.format(v_NS))
        id = query.attrib['{0}id'.format(rel_NS)]
        
        # See which filename it refers to and create a valid one
        filename = ''
        for rel in otherData['rels']:
            if rel.get('Id') == id:
                filename = os.path.split(rel.get('Target'))[1]
                break
        
        # Stall until the image is available for me to read. I got to trust
        # that another function is moving the image over there
        imagePath = os.path.join(IMPORT_FOLDER, os.path.normpath('images/' + filename))
        imageType = os.path.splitext(imagePath)[1].lower()
#         try:
#             # Try to get the image already exported
#             imageFile = open(imagePath, 'r')
#             stuff = imageFile.read(1)
#             imageFile.seek(0)
#             if len(stuff) == 1:
#                 # Don't bother with that one. Use the other instead
#                 imageFile = otherData['zip'].open('word/media/' + filename, 'r')
#         except Exception:
        with otherData['zip'].open('word/media/' + filename, 'r') as imageFile:
            imageBuffer = StringIO(imageFile.read())
        
        try:
            if imageType == '.wmf':
                data['data'] = parseWMF(imageBuffer, debug=False)
                parentData['math'] = data
                
        except Exception as ex:
            # Print out the exception, then create a dummy MathML that says
            # "Couldn't read MathType"
            traceback.print_exc()
            print ex.message
                
            root = etree.Element('a')
            root.set('href', REPORT_BUG_URL)
            elem = etree.SubElement(root, 'math', nsmap={None: 'http://www.w3.org/1998/Math/MathML'})
            elem = etree.SubElement(elem, 'mrow')
            elem = etree.SubElement(elem, 'mtext')
            elem.text = '[MathType Error. Click Here to Tell Central Access!' + str(ex) +']'
            data['data'] = root
            parentData['math'] = data
            
            print 'Encountered error in reading MathType!'
            
        imageFile.close()

def _parseParagraphStyle(elem, parentData, otherData):
    query = elem.find('./{0}pStyle'.format(w_NS))
    if query != None:
        style = query.get('{0}val'.format(w_NS))
        if style in otherData['paraStyles']:
            parentData['style'] = otherData['paraStyles'][style]
        
    rowQuery = elem.find('./{0}rPr/{0}rStyle'.format(w_NS))
    if rowQuery != None:
        if 'pagenumber' in rowQuery.attrib['{0}val'.format(w_NS)].lower():
            parentData['pageNumber'] = True

def _parseRow(elem, parentData, otherData):
    data = {'type' : 'row'}
    for child in elem:
        # Text
        if child.tag == '{0}t'.format(w_NS):
            data['text'] = unicode(child.text)
        
        # Image or some drawing
        if child.tag == '{0}drawing'.format(w_NS):
            _parseImage(child, data, otherData)
            
        if child.tag == '{0}object'.format(w_NS):
            _parseObject(child, data, otherData)
            
    parentData['data'].append(data)
            
def _parseImage(elem, parentData, otherData):
    
    # Check to see if there is an image. If yes, create an image node that
    # has the correct filename reference to it
    query = elem.find('.//{0}pic'.format(pic_NS))
    if query != None:
        
        data = {'type' : 'image'}
        
        query = query.find('.//{0}blip'.format(a_NS))
        
        # Grab the ID from it
        id = query.get('{0}embed'.format(rel_NS))
                    
        # See which filename it refers to and create a valid one
        for rel in otherData['rels']:
            if rel.get('Id') == id:
                filename = os.path.split(rel.get('Target'))[1]
                
                # Check to see if this is an image I need to convert later. If 
                # so, change the file extension to match the converted file
                if os.path.splitext(filename)[1] in IMAGE_TRANSLATION:
                    filename = os.path.splitext(filename)[0] + IMAGE_TRANSLATION[os.path.splitext(filename)[1]]
                    
                data['filename'] = unicode(filename)
                break
            
        # Get the description text for the image
        query = elem.find('.//{0}docPr'.format(wp_NS))
        if query != None:
            altText = query.get('descr')
            if altText != None:
                data['altText'] = unicode(altText)
            
        # Append this to the parent data
        parentData['image'] = data

def _convertOMMLToMathML(ommlNode):
    '''
    Converts an oMath lxml node into a MathML node.
    '''
    mathml = ommlTransform(ommlNode)
    
    # Convert the transformed XML into UTF-8 while removing a bunch of
    # prefix crap
    mathml = etree.fromstring(etree.tostring(mathml, encoding='utf-8', xml_declaration=False).replace('mml:', '').replace(':mml', ''))
    
    return mathml
 
def _generateParagraphHTMLNode(p):
    '''
    From a paragraph dictionary, create the HTML for it, and whether the
    anchorID needs to be increased:
    (htmlELement, boolean)
    '''
    pRoot = None
     
    # Figure out what my root HTML will be
    level = -1
    if 'style' in p:
        if p['style'] in heirarchyStyles:
            level = heirarchyStyles[p['style']]
             
    pRoot = HTML.Element(htmlLevels[level])
     
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
                imageTag.set('src', os.path.join(IMPORT_FOLDER, os.path.normpath('images/' + image['filename'])))
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
    return pRoot

def _generateTableHTMLNode(t):
    '''
    From a table dictionary, create the HTML for it.
    '''
    tRoot = HTML.Element('table')
     
    for r in t['rows']:
        rRoot = etree.SubElement(tRoot, 'tr')
         
        for c in r['columns']:
            cRoot = etree.SubElement(rRoot, 'td')
            cRoot.append(c)
             
    return tRoot
 
#     def _isList(self, elem):
#         '''
#         Returns whether the element is numbered, or in other words, a part of an
#         ordered list or unordered list
#         '''
#         return elem.find('./{0}pPr/{0}numPr'.format(w_NS)) != None

#     def _getNumberingDict(self, zip):
#         '''
#         Returns a nested dictionary that looks like the following:
#         
#         {numId : {levelId : {"format" : "decimal|bullet", "start" : 0}, levelId : {...}, ...}}
#         '''
#         myDict = {}
#         
#         if 'word/numbering.xml' in zip.namelist():
#             # Get the numbering XML
#             numberingFile = zip.open('word/numbering.xml', 'r')
#             numXML = etree.parse(numberingFile)
#             numberingFile.close()
#             
#             # Get all numberings and get the abstract element they refer to
#             # (pointless indirection in my opinion)
#             nums = numXML.findall('./{0}num'.format(w_NS))
#             for e in nums:
#                 abstractId = e.find('./{0}abstractNumId'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                 abstractNum = numXML.find('./{0}abstractNum[@{0}abstractNumId=\''.format(w_NS) + abstractId + '\']')
#                 
#                 # Get list of levels in that particular element
#                 levels = abstractNum.findall('./{0}lvl'.format(w_NS))
#                 levelDicts = {}
#                 for l in levels:
#                     key = l.attrib['{0}ilvl'.format(w_NS)]
#                     levelDicts[key] = {}
#                     format = l.find('./{0}numFmt'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                     
#                     if l.find('./{0}start'.format(w_NS)):
#                         levelDicts[key]['start'] = l.find('./{0}start'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                     else:
#                         levelDicts[key]['start'] = 1
#                     
#                     #start = l.find('./{0}start'.format(w_NS)).attrib['{0}val'.format(w_NS)]
#                     levelDicts[key]['format'] = format
#                 
#                 key = e.attrib['{0}numId'.format(w_NS)]
#                 myDict[key] = levelDicts
#                 
#         return myDict