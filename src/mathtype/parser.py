'''
Created on Mar 2, 2013

@author: Spencer Graffe
'''
import os
import struct
import StringIO
import traceback
from lxml import etree
from records import *
from src.misc import temp_path

def parseMTEF(mtefString):
    '''
    Parses an MTEF data string and gets the MathType object for it or something.
    '''
    mtefFile = StringIO.StringIO(mtefString)
        
    mtefHeader = struct.unpack('<BBBBB', mtefFile.read(5))
    print 'MTEF Header:', mtefHeader
            
    applicationKey = getNullTermString(mtefFile)
    print 'Application Key:', applicationKey
            
    equationOptions = struct.unpack('<B', mtefFile.read(1))[0]
    print 'Equation Options:', equationOptions
        
    print 'Math ---------------------------------------'
        
    records = []
        
    while True:
        # Get record type
        recordType = mtefFile.read(1)
        if len(recordType) == 0:
            break
        recordType = struct.unpack('<B', recordType)[0]
        
        # Let the Record object handle how to read this record
        newRecord = createRecord(recordType, mtefFile)
        if newRecord != None:
            records.append(newRecord)
            
    mtefFile.close()
    
    # Get the MathML from the said records
    mathmlRoot = etree.Element('math', nsmap={None : 'http://www.w3.org/1998/Math/MathML'})
    i = 0
    parentStack = []
    parentStack.append(mathmlRoot)
    convertRecords(i, records, parentStack)
    
    # Do some post-processing
    _combineNumbers(mathmlRoot)
        
    return mathmlRoot

def parseWMF(wmfFile):
    '''
    Parses the WMF file to find the embedded MathType data. Then, it will get
    the MathML interpreted from the MTEF data.
    
    The file should already be opened for binary reading.
    '''
    wmfString = wmfFile.read()
    wmfString = StringIO.StringIO(wmfString)
    try:
        # Keep reading until I find the first instance of the AppsMFCC tag. This is
        # the embedded comment tag that holds my MathType stuff
        testString = ''
        
        done = False
        found = False
        try:
            while not done:
                nextByte = wmfString.read(1)
                testString += nextByte
                if len(nextByte) == 0:
                    found = False
                    break
                if len(testString) > 8:
                    testString = testString[1:]
                    if testString == 'AppsMFCC':
                        done = True
                        found = True              
                    
        except EOFError:
            return None
        
        if found:
            print 'Found AppsMFCC tag!'
            print
            
            # Grab all of the other data in the comment header (even most I won't need)
            commentHeader = struct.unpack('<HII', wmfString.read(10))
            print 'Comment Header:', commentHeader
            
            signature = getNullTermString(wmfString)
            print 'Signature:', signature
            
            # If the signature is something like "Design Science, Inc.", then it is MTEF
            if signature == 'Design Science, Inc.':
                return parseMTEF(wmfString.read(commentHeader[2]))
        
        else:
            
            # Make some MathML that says it cannot read this particular math
            root = etree.Element('math', nsmap={None: 'http://www.w3.org/1998/Math/MathML'})
            
            elem = etree.SubElement(root, 'mrow')
            elem = etree.SubElement(elem, 'mtext')
            elem.text = 'Couldn\'t read MathType.'
            
            return root
            
    except Exception as ex:
        # Write the problem file to my temp
        savePath = temp_path(os.path.join('mathtype', os.path.basename(wmfFile.name)))
        if not os.path.exists(os.path.dirname(savePath)):
            os.makedirs(os.path.dirname(savePath))
        saveFile = open(savePath, 'wb')
        wmfString.seek(0)
        saveFile.write(wmfString.read())
        saveFile.close()
            
        raise MathTypeParseError(savePath, traceback.format_exc())
    
def _combineNumbers(mathml):
    '''
    Combines continuous digit elements into a single digit element. This is a
    post-processing function.
    '''
    
    if _isNumber(mathml):
        # Keep grabbing nodes after this and putting them in here if they are
        # also numbers
        while True:
            n = mathml.getnext()
            if n == None:
                break
            
            # If the next element is a number, combine its text content into
            # my current node
            if _isNumber(n):
                mathml.text += n.text
                if n.getparent() != None:
                    n.getparent().remove(n)
            else:
                
                # If there is a number that is inside of a superscript or
                # subscript that is directly after this, then move this node
                # under that sibling
                if _isSuperscriptOrSubscript(n):
                    if len(n) > 0:
                        if _isNumber(n[0]):
                            if mathml.getparent() != None:
                                mathml.getparent().remove(mathml)
                            n.insert(0, mathml)
                            mathml = n
                break
    
    # Check the children and make sure those are all good too
    if len(mathml) > 0:
        # The function will handle all of the siblings too
        _combineNumbers(mathml[0])
    
    # Do it for this element's sibling
    if mathml.getnext() != None:
        _combineNumbers(mathml.getnext())

def _isNumber(mathml):
    testTag = mathml.tag.rsplit('}', 1)[-1].lower()
    if testTag == 'mn':
        try:
            float(mathml.text)
            return True
        except ValueError:
            return False
    else:
        return False
    
def _isSuperscriptOrSubscript(mathml):
    testTag = mathml.tag.rsplit('}', 1)[-1].lower()
    if testTag == 'msup':
        return True
    elif testTag == 'msub':
        return True
    
    return False
    
            
class MathTypeParseError(Exception):
    def __init__(self, savePath, traceback):
        self.savePath = savePath
        self.message = 'Couldn\'t parse MathType: Saved to ' + self.savePath + '\n'
        self.message += '\nTraceback:\n' + traceback