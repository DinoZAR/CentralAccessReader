'''
Created on May 19, 2014

@author: Spencer Graffe
'''
import zipfile
from lxml import etree

class MathLibrary(object):
    '''
    Math library used for the math-to-prose engine. This will be used for both
    the built-in libraries and for custom libraries that one can import.
    '''

    def __init__(self, title):
        self.title = ''
        self.author = ''
        self.patterns = []
    
    def read(self, f):
        '''
        Reads in a math library from file object.
        '''
        zipFile = zipfile.ZipFile(f, 'r')
        self._read_manifest(zipFile)
        self._read_patterns(zipFile)
        
    def write(self, f):
        '''
        Writes out this library to file object.
        '''
        zipFile = zipfile.ZipFile(f, 'w')
        self._write_manifest(zipFile)
        self._write_patterns(zipFile)
    
    def _read_manifest(self, zipFile):
        '''
        Reads the manifest from the zip file.
        '''
        root = etree.fromstring(zipFile.read('manifest.xml'))
        
        elem = root.findelem('.//title')
        self.title = elem.text
        
        elem = root.findelem('.//author')
        self.author = elem.text
    
    def _write_manifest(self, zipFile):
        '''
        Writes the manifest to the zip file
        '''
        root = etree.Element('manifest')
        
        elem = etree.SubElement(root, 'title')
        elem.text = self.title
        
        elem = etree.SubElement(root, 'author')
        elem.text = self.author
        
        zipFile.write('manifest.xml', etree.tostring(root, pretty_print=True, encoding='UTF-8', xml_declaration=True))
    
    def _read_patterns(self, zipFile):
        pass
    
    def _write_patterns(self, zipFile):
        pass