# import zipfile
# from lxml import etree
# from lxml import html as HTML
# from lxml.builder import E
# import copy
# import os
# import platform
# import inspect
# from src.gui.bookmarks import BookmarkNode
# 
# rootPath = os.path.dirname(inspect.getfile(inspect.currentframe()))
# 
# # Get my OMML to MathML stylesheet compiled
# ommlXSLTPath = os.path.normpath(rootPath + '/OMMLToMathML.xsl')
# f = open(ommlXSLTPath, 'r')
# xslRoot = etree.parse(f)
# ommlTransform = etree.XSLT(xslRoot)
# f.close()
# 
# # Namespaces inside .docx xml
# w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
# wp_NS = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
# m_NS = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
# pic_NS = '{http://schemas.openxmlformats.org/drawingml/2006/picture}'
# r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'
# rel_NS = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
# a_NS = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
#         
# def getHtmlAndNavigation(docxFilePath):
#     '''
#     Returns the HTML for the .docx file and also a list of BookmarkNode's to add
#     to our view.
#     '''
#     
#     # .docx is just a zip file
#     zip = zipfile.ZipFile(docxFilePath, 'r')
#     
#     # First, grab the relationships file. This has the id's and pointers to 
#     # different bits of data, most importantly images.
#     relFile = zip.open('word/_rels/document.xml.rels', 'r')
#     rels = etree.parse(relFile)
#     rels = rels.findall('./{0}Relationship'.format(r_NS))
#     relFile.close()
#     
#     # Grab the styles too to match up the headings and other parts.
#     stylesFile = zip.open('word/styles.xml', 'r')
#     styles = etree.parse(stylesFile)
#     styles = styles.findall('./{0}style'.format(w_NS))
#     stylesFile.close()
#     
#     # Now generate a dictionary that can look up the name of the style depending
#     # on the id of the style
#     stylesDict = {}
#     for s in styles:
#         query = s.find('./{0}name'.format(w_NS))
#         if query != None:
#             key = s.get('{0}styleId'.format(w_NS))
#             value = query.get('{0}val'.format(w_NS))
#             stylesDict[key] = value
#     
#     # Grab the paragraphs from the document. They're more like <div> tags in
#     # HTML. I will obtain the style of the paragraph as a whole, and for each
#     # "row" (more like a <span> really), grab the text, equation, image, or
#     # something from it along with the styling pertaining to that "row".
#     #
#     # The resulting data structure will look like this:
#     # ([(objectInRow, rowStyle), [row]...], paragraphStyleID)
#     # for each paragraph
#     document = zip.open('word/document.xml', 'r')
#     
#     tree = etree.parse(document)
#     
#     # When we are done with them, close them up
#     document.close()
#     
#     root = tree.getroot()
#     
#     paras = root.findall('.{0}body/{0}p'.format(w_NS))
#     
#     paraData = []
#     
#     for p in paras:
#         pStyle = None
#         rows = []
#         for element in p:
#             if element.tag == '{0}pPr'.format(w_NS):
#                 # Got a paragraph style.
#                 query = element.find('./{0}pStyle'.format(w_NS))
#                 if query != None:
#                     pStyle = query.get('{0}val'.format(w_NS))
#             
#             elif element.tag == '{0}oMathPara'.format(m_NS):
#                 # An OMML equation in its own paragraph
#                 mathRoot = element[0]
#                 rows.append((mathRoot, None))
#                 
#             elif element.tag == '{0}oMath'.format(m_NS):
#                 # An inline OMML equation. Treat like others
#                 rows.append((element, None))
#                 
#             elif element.tag == '{0}r'.format(w_NS):
#                 # A row object. Usually has text, but can have inline content
#                 rowStyle = None
#                 rowObject = None
#                 for child in element:
#                     if child.tag == '{0}rPr'.format(w_NS):
#                         rowStyle = child
#                     else:
#                         rowObject = child
#                         
#                 rows.append((rowObject, rowStyle))
#         
#         paraData.append((rows, pStyle))
#         
#     
#     # Start generating my HTML tree. Start with da basics
#     html = HTML.Element('html')
#     head = HTML.Element('head')
#     body = HTML.Element('body')
#     html.append(head)
#     html.append(body)
#     
#     importFolder = 'import/images'
#     
#     _prepareHead(head)
#     bookmarkRoot = _prepareBody(body, paraData, rels, stylesDict, importFolder)
#     
#     _grabImages(zip, importFolder)
#     
#     zip.close()
#     
#     return (HTML.tostring(html), bookmarkRoot)
#     
# def _prepareHead(head):
#     
#     mathjaxConfig = HTML.Element('script')
#     mathjaxConfig.set('type', 'text/x-mathjax-config')
#     scriptFile = open(os.path.normpath(rootPath + '/mathjax_config.js'))
#     contents = scriptFile.read()
#     scriptFile.close()
#     mathjaxConfig.text = contents
#     
#     mathjaxScript = HTML.Element('script')
#     mathjaxScript.attrib['type'] = 'text/javascript'
#     mathjaxScript.attrib['src'] = r'../mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML.js'
#     
#     jqueryScript = HTML.Element('script')
#     jqueryScript.attrib['type'] = 'text/javascript'
#     jqueryScript.attrib['src'] = r'../jquery-1.9.1.min.js'
#     
#     myScripts = HTML.Element('script')
#     myScripts.set('language', 'javascript')
#     myScripts.set('type', 'text/javascript')
#     
#     scriptFile = open(os.path.normpath(rootPath + '/my_functions.js'), 'r')
#     contents = scriptFile.read()
#     scriptFile.close()
#     myScripts.text = contents
#     
#     css = HTML.Element('link')
#     css.attrib['rel'] = 'stylesheet'
#     css.attrib['type'] = 'text/css'
#     css.attrib['href'] = 'import/defaultStyle.css'
#     
#     head.append(mathjaxConfig)
#     head.append(mathjaxScript)
#     head.append(jqueryScript)
#     head.append(myScripts)
#     head.append(css)
#     
# def _prepareBody(body, paraData, rels, stylesDict, importFolder):
#     
#     # Store this counter for creating the anchor tags for page navigation
#     anchorCount = 0
#     parentStack = []
#     lastNode = (BookmarkNode(None, 'Docx'), 0)
#     currLevel = -1
#     
#     for p in paraData:
#         
#         # Check to see if it has a paragraph style. If it does, then use the
#         # correct HTML tag for it. Otherwise, assume it's a paragraph.
#         pRoot = None
#         
#         if p[1] != None:
#             # Check the ID and look it up in the styles dictionary. If the style
#             # text matches my own dictionary of what to substitute with it, then
#             # make the substitution.
#             if stylesDict[p[1]] == 'Title':
#                 pRoot = HTML.Element('h1')
#                 body.append(pRoot)
#                 anchorCount += 1
#                 pRoot.set('id', str(anchorCount))
#                 currLevel = 1
#             elif stylesDict[p[1]] == 'Heading 1':
#                 pRoot = HTML.Element('h2')
#                 body.append(pRoot)
#                 anchorCount += 1
#                 pRoot.set('id', str(anchorCount))
#                 currLevel = 2
#             elif stylesDict[p[1]] == 'Heading 2':
#                 pRoot = HTML.Element('h3')
#                 body.append(pRoot)
#                 anchorCount += 1
#                 pRoot.set('id', str(anchorCount))
#                 currLevel = 3
#             elif stylesDict[p[1]] == 'Heading 3':
#                 pRoot = HTML.Element('h4')
#                 body.append(pRoot)
#                 anchorCount += 1
#                 pRoot.set('id', str(anchorCount))
#                 currLevel = 4
#             else:
#                 pRoot = HTML.Element('p')
#                 body.append(pRoot)
#                 currLevel = -1
#         else:
#             pRoot = HTML.Element('p')
#             body.append(pRoot)
#             currLevel = -1
#         
#         # Loop through the content that is in that paragraph
#         currTextNode = pRoot
#         currTextNode.text = ''
#         currTextNode.tail = ''
#         onRoot = True
#         for content in p[0]:
#             if content[0] != None:
#                 if content[0].tag == '{0}oMath'.format(m_NS):
#                     # Grab OMML element inside it and transform it
#                     mathml = ommlTransform(content[0])
#                     
#                     # Convert the transformed XML into a UTF-8 version
#                     # (it was in UTF-16 before for some dumb reason)
#                     # Also strip the namespace prefix crap
#                     mathml = etree.fromstring(etree.tostring(mathml, encoding='utf-8', xml_declaration=False).replace('mml:', '').replace(':mml', ''))
#                     
#                     #print etree.tostring(mathml, pretty_print=True)
#                     
#                     mathSpan = etree.SubElement(pRoot, 'span')
#                     mathSpan.attrib['class'] = 'mathmlEquation'
#                     mathSpan.append(mathml)
#                     currTextNode = mathSpan
#                     currTextNode.tail = ''
#                     onRoot = False
#                 
#                 elif content[0].tag == '{0}t'.format(w_NS):
#                     # Do different things depending on whether the content is styled
#                     # or not
#                     if content[1] != None:
#                         # Recursively add child elements to match the styling in
#                         # the content. In the very bottommost child, add the text to
#                         # that.
#                         hasStyle = False
#                         for style in content[1]:
#                             if style.tag == '{0}b'.format(w_NS):
#                                 bold = etree.SubElement(pRoot, 'b')
#                                 bold.text = ''
#                                 bold.tail = ''
#                                 hasStyle = True
#                                 onRoot = True
#                                 currTextNode = bold
#                             elif style.tag == '{0}i'.format(w_NS):
#                                 italics = etree.SubElement(pRoot, 'i')
#                                 italics.text = ''
#                                 italics.tail = ''
#                                 hasStyle = True
#                                 onRoot = True
#                                 currTextNode = italics
#                         
#                         if content[0].text != None:
#                             if onRoot:
#                                 currTextNode.text += content[0].text
#                             else:
#                                 currTextNode.tail += content[0].text
#                             
#                             if hasStyle:
#                                 onRoot = False
#                             
#                     else:
#                         if content[0].text != None:
#                             if onRoot:
#                                 currTextNode.text += content[0].text
#                             else:
#                                 currTextNode.tail += content[0].text
#                                 
#                 elif content[0].tag == '{0}drawing'.format(w_NS):
#                     
#                     # Check to see if there is an image inside. If so, make an 
#                     # image tag linking to it
#                     query = content[0].find('.//{0}pic'.format(pic_NS))
#                     if query != None:
#                         
#                         query = query.find('.//{0}blip'.format(a_NS))
#                         
#                         # Grab the ID from it
#                         id = query.get('{0}embed'.format(rel_NS))
#                         
#                         # See which filename it refers to and create a valid one
#                         filename = ''
#                         for rel in rels:
#                             if rel.get('Id') == id:
#                                 filename = os.path.split(rel.get('Target'))[1]
#                                 break
#                         
#                         # Generate the image tag
#                         image = etree.SubElement(pRoot, 'img')
#                         image.set('src', importFolder + '/' + filename)
#                         
#                         # Get the description text for the image
#                         query = content[0].find('.//{0}docPr'.format(wp_NS))
#                         if query != None:
#                             altText = query.get('descr')
#                             image.set('alt', altText)
#                             
#         # END CONTENT LOOP
#         
#         # Now, create a bookmark if I need to
#         if currLevel > 0:
#             # Figure out my parent
#             while True:
#                 if len(parentStack) > 0:
#                     if currLevel > parentStack[-1][1]:
#                         parentStack.append(lastNode)
#                         break
#                     elif currLevel < (parentStack[-1][1] - 1):
#                         # Pop off the next parent on the stack
#                         lastNode = parentStack.pop()
#                     elif currLevel == parentStack[-1][1]:
#                         lastNode = parentStack.pop()
#                     else:
#                         break
#                 else:
#                     if currLevel > lastNode[1]:
#                         parentStack.append(lastNode)
#                     break
#                     
#             # Now make the bookmark node and all of the other things
#             if len(parentStack) > 0:
#                 myNode = BookmarkNode(parentStack[-1][0], pRoot.text_content(), anchorId=str(anchorCount))
#                 lastNode = (myNode, currLevel)
#             else:
#                 myNode = BookmarkNode(lastNode[0], pRoot.text_content(), anchorId=str(anchorCount))
#                 lastNode = (myNode, currLevel)
#                 
#                 
#     # Return my head bookmark
#     return parentStack[0][0]
#                             
# def _grabImages(zip, importFolder):
#     '''
#     Grabs the images from the word file and puts them in the specified folder.
#     '''
#     
#     # Delete images directory, if there is one
#     if os.path.isdir(importFolder + '/images'):
#         for the_file in os.listdir(importFolder + '/images'):
#             file_path = os.path.join(importFolder, the_file)
#             try:
#                 if os.path.isfile(file_path):
#                     os.unlink(file_path)
#             except Exception, e:
#                 print e
#     else:
#         os.makedirs(importFolder + '/images')
#     
#     for f in zip.namelist():
#         if f.find('word/media/') == 0:
#             # Extract it to my import folder
#             imageFile = open(importFolder + '/' + f.replace('word/media/', ''), 'wb')
#             imageFile.write(zip.read(f))
#             imageFile.close()    