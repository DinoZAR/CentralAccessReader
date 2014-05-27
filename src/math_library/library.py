'''
Created on May 19, 2014

@author: Spencer Graffe
'''
import os
import zipfile

from lxml import etree

class MathLibrary(object):
    '''
    Math library used for the math-to-prose engine. This will be used for both
    the built-in libraries and for custom libraries that one can import.
    '''

    def __init__(self):
        self.name = 'Untitled'
        self.author = ''
        self.patterns = []
    
    def read(self, f):
        '''
        Reads in a math library from file object.
        '''
        zipFile = zipfile.ZipFile(f, 'r')
        self._read_manifest(zipFile)
        self._read_patterns(zipFile)
        zipFile.close()
        
    def write(self, f):
        '''
        Writes out this library to file object.
        '''
        zipFile = zipfile.ZipFile(f, 'w')
        self._write_manifest(zipFile)
        self._write_patterns(zipFile)
        zipFile.close()
    
    def _read_manifest(self, zipFile):
        '''
        Reads the manifest from the zip file.
        '''
        root = etree.fromstring(zipFile.read('manifest.xml'))
        
        elem = root.findelem('.//name')
        self.name = elem.text
        
        elem = root.findelem('.//author')
        self.author = elem.text
    
    def _write_manifest(self, zipFile):
        '''
        Writes the manifest to the zip file
        '''
        root = etree.Element('manifest')
        
        elem = etree.SubElement(root, 'name')
        elem.text = self.name
        
        elem = etree.SubElement(root, 'author')
        elem.text = self.author
        
        zipFile.writestr('manifest.xml', etree.tostring(root, pretty_print=True, encoding='UTF-8', xml_declaration=True))
    
    def _read_patterns(self, zipFile):
        '''
        Reads in the patterns from the zip file.
        '''
        for name in zipFile.namelist():
            myName = os.path.splitext(os.path.basename(name))[0]
            ext = os.path.splitext(name)[1]
            if ext == '.txt':
                self.patterns.append(MathPattern(myName, zipFile.read(name)))
    
    def _write_patterns(self, zipFile):
        '''
        Writes the patterns out to zip file.
        '''
        for p in self.patterns:
            fileName = p.name + '.txt'
            zipFile.writestr(fileName, p.data)
            
class MathPattern(object):
    '''
    A single pattern in a library.
    '''
    
    def __init__(self, name='Untitled', data=''):
        self.name = name
        self.data = data