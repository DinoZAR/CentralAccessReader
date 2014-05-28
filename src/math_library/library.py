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

    PATTERN_FILE_FORMAT = 'pattern{0}.txt'

    def __init__(self):
        self.name = 'Untitled'
        self.author = 'Someone'
        self.languageCode = 'en'

        self.patterns = []
        self.builtIn = False
    
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

    def getPattern(self, name):
        '''
        Retrieves a pattern with the given name.
        '''
        for p in self.patterns:
            if name == p.name:
                return p
        raise ValueError('Pattern {0} does not exist in library {1}.'.format(name, self.name))
    
    def _read_manifest(self, zipFile):
        '''
        Reads the manifest from the zip file.
        '''
        root = etree.fromstring(zipFile.read('manifest.xml'))
        
        elem = root.find('.//name')
        self.name = elem.text
        
        elem = root.find('.//author')
        self.author = elem.text

        elem = root.find('.//language')
        self.languageCode = elem.text
    
    def _write_manifest(self, zipFile):
        '''
        Writes the manifest to the zip file
        '''
        root = etree.Element('manifest')
        
        elem = etree.SubElement(root, 'name')
        elem.text = self.name
        
        elem = etree.SubElement(root, 'author')
        elem.text = self.author

        elem = etree.SubElement(root, 'language')
        elem.text = self.languageCode

        # Pattern mappings (doing this so that the name is not limited by
        # file system naming restrictions)
        patterns = etree.SubElement(root, 'patterns')
        num = 0
        for p in self.patterns:
            elem = etree.SubElement(patterns, 'pattern')
            elem.set('name', p.name)
            elem.set('file', self.PATTERN_FILE_FORMAT.format(num))
            num += 1
        
        zipFile.writestr('manifest.xml', etree.tostring(root, pretty_print=True,
                                                        encoding='UTF-8',
                                                        xml_declaration=True))
    
    def _read_patterns(self, zipFile):
        '''
        Reads in the patterns from the zip file.
        '''
        # Get my manifest for the name mappings
        root = etree.fromstring(zipFile.read('manifest.xml'))
        patternMaps = root.findall('.//patterns/pattern')
        for p in patternMaps:
            self.patterns.append(MathPattern(p.get('name'), zipFile.read(p.get('file'))))
    
    def _write_patterns(self, zipFile):
        '''
        Writes the patterns out to zip file.
        '''
        num = 0
        for p in self.patterns:
            fileName = self.PATTERN_FILE_FORMAT.format(num)
            zipFile.writestr(fileName, p.data)
            num += 1
            
class MathPattern(object):
    '''
    A single pattern in a library.
    '''
    
    def __init__(self, name='Untitled', data=''):
        self.name = name
        self.data = data