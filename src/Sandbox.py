'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
print 'Starting!'
import os
import zipfile
from lxml import etree
from lxml import html as HTML
from threading import Thread
from src.threadpool import Pool
from src.misc import program_path, temp_path
from src.docx.paragraph import parseParagraph, parseTable


def run_test(numThreads):
    
    # Load in the paragraphs from docx file, like the Tutorial
    docxFilePath = r'W:\Nifty Prose Articulator\test_files\Chs 6-11.docx'
    htmlSavePath = r'C:\Users\GraffeS\Desktop\doc.html'
    
    # Other things
    importFolder = temp_path('import')
    w_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    r_NS = '{http://schemas.openxmlformats.org/package/2006/relationships}'
    
    # Functions that I will need
    def _getRels(zip):
        relFile = zip.open('word/_rels/document.xml.rels', 'r')
        myRels = etree.parse(relFile)
        myRels = myRels.findall('./{0}Relationship'.format(r_NS))
        relFile.close()
        return myRels
     
    def _getStyles(zip):
        stylesFile = zip.open('word/styles.xml', 'r')
        myStyles = etree.parse(stylesFile)
        myStyles = myStyles.findall('./{0}style'.format(w_NS))
        stylesFile.close()
        return myStyles
     
    def _getParaStyles(styles):
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
    
    def _saveImages():         
        # Open a zip file of my docx file
        zip = zipfile.ZipFile(docxFilePath, 'r')
         
        # Delete images directory, if there is one
        if os.path.isdir(importFolder + '/images'):
            for the_file in os.listdir(importFolder + '/images'):
                file_path = os.path.join(importFolder + '/images', the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    print e
        else:
            os.makedirs(importFolder + '/images')
     
        for f in zip.namelist():
            if f.find('word/media/') == 0:
                # Extract it to my import folder
                imageFile = open(importFolder + '/images/' + f.replace('word/media/', ''), 'wb')
                imageFile.write(zip.read(f))
                imageFile.close()
         
        zip.close()
    
    # Actually load the document
    zip = zipfile.ZipFile(docxFilePath, 'r')
    
    # Start saving images to my import folder in the background
    saveImagesThread = Thread(target=_saveImages)
    saveImagesThread.start()
            
    # Get the other random data I will need to parse my paragraphs
    otherData = {}
    otherData['rels'] = _getRels(zip)
    otherData['styles'] = _getStyles(zip)
    otherData['paraStyles'] = _getParaStyles(otherData['styles'])
    #otherData['numbering'] = _getNumberingDict(zip)
    
    # Open my main document file
    document = zip.open('word/document.xml', 'r')
    tree = etree.parse(document)
    document.close()
    root = tree.getroot()
    
    # Get all of the paragraphs elements in my docx
    paragraphs = root.findall('./{0}body/*'.format(w_NS))
    paragraphData = {}
    
    h = HTML.Element('html')
    body = HTML.Element('body')
    h.append(body)
    
    # Use a process pool to parse all of my paragraphs.
    # Also define the functions that the thread pool will use.
    pool = Pool(numThreads)
    
    def processParagraphElement(id, elem, otherData):
        elem = None
        if p.tag == '{0}p'.format(w_NS):
            elem = parseParagraph(p, otherData)
        elif p.tag == '{0}tbl'.format(w_NS):
            elem = parseTable(p, otherData)
        
        return (id, elem)
    
    def updateParagraph(result):
        id = result[0]
        elem = result[1]
        paragraphData[id] = elem
    
    print 'Doing the paragraphs...'
    idCounter = 0
    for p in paragraphs:
        args = (idCounter, p, otherData)
        #updateParagraph(processParagraphElement(*args))
        pool.addTask(processParagraphElement, updateParagraph, args=(idCounter, p, otherData))
        idCounter += 1
    
    print 'All paragraphs queued. Waiting for them to finish processing...'
    
    pool.join()
    
    saveImagesThread.join()
    
    zip.close()
    
    # print 'Saving HTML...'
    # 
    # f = open(htmlSavePath, 'w')
    # f.write(HTML.tostring(h))
    # f.close()
    
    print 'Done!'


# Just to protect this module when using the process pool
if __name__ == '__main__':
    pass