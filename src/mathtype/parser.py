'''
Created on Mar 2, 2013

@author: Spencer Graffe
'''
import StringIO
import traceback

from src import OleFileIO_PL as OLE
from src.misc import REPORT_BUG_URL
from records import *

def parseMTEF(mtefString, debug=False):
    '''
    Parses an MTEF data string and gets the MathType object for it or something.
    '''
    mtefFile = StringIO.StringIO(mtefString)
        
    mtefHeader = struct.unpack('<BBBBB', mtefFile.read(5))
    if debug: print 'MTEF Header:', mtefHeader
            
    applicationKey = getNullTermString(mtefFile, debug)
    if debug: print 'Application Key:', applicationKey
            
    equationOptions = struct.unpack('<B', mtefFile.read(1))[0]
    if debug: print 'Equation Options:', equationOptions
        
    if debug: print 'Math ---------------------------------------'
        
    records = []
        
    while True:
        # Get record type
        recordType = mtefFile.read(1)
        if len(recordType) == 0:
            break
        recordType = struct.unpack('<B', recordType)[0]
        
        # Let the Record object handle how to read this record
        newRecord = createRecord(recordType, mtefFile, debug)
        if newRecord != None:
            records.append(newRecord)
            
    mtefFile.close()
    
    # Get the MathML from the said records
    mathmlRoot = etree.Element('math', nsmap={None : 'http://www.w3.org/1998/Math/MathML'})
    i = 0
    parentStack = []
    parentStack.append(mathmlRoot)
    convertRecords(i, records, parentStack, debug)
    
    # Do some post-processing
    _combineNumbers(mathmlRoot)
        
    return mathmlRoot

def parseWMF(wmfFile, debug=False):
    '''
    Parses the WMF file to find the embedded MathType data. Then, it will get
    the MathML interpreted from the MTEF data.
    
    The file should already be opened for binary reading.
    '''
    if debug: print '!>------------------------------------------------------------------<!'
    
    try:
        # Keep reading until I find the first instance of the AppsMFCC tag. This is
        # the embedded comment tag that holds my MathType stuff
        testString = ''
        
        done = False
        found = False
        try:
            while not done:
                nextByte = wmfFile.read(1)
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
            if debug: print 'Found AppsMFCC tag!'
            if debug: print
            
            # Grab all of the other data in the comment header (even most I won't need)
            commentHeader = struct.unpack('<HII', wmfFile.read(10))
            if debug: print 'Comment Header:', commentHeader
            
            signature = getNullTermString(wmfFile, debug)
            if debug: print 'Signature:', signature
            
            # If the signature is something like "Design Science, Inc.", then it is MTEF
            if signature == 'Design Science, Inc.':
                if debug: print 'Math size:', commentHeader[2]
                return parseMTEF(wmfFile.read(commentHeader[2]), debug)
        
        else:
            
            # Make some MathML that says it cannot read this particular math
            root = etree.Element('a')
            root.set('href', REPORT_BUG_URL)
            elem = etree.SubElement(root, 'math', nsmap={None: 'http://www.w3.org/1998/Math/MathML'})
            elem = etree.SubElement(elem, 'mrow')
            elem = etree.SubElement(elem, 'mtext')
            elem.text = '[MathType Error. Click Here to Tell Central Access!]'
            
            return root
            
    except Exception as ex:
        raise MathTypeParseError('', traceback.format_exc())
    
def parseOLE(oleFile, debug=False):
    '''
    Parses a MathType object from an OLE compound file. Returns the MathML
    associated with it.
    '''
    
    OLE_OBJECT_NAME = 'Equation Native'
    OLE_HEADER_LENGTH = 28
    
    ole = OLE.OleFileIO(oleFile)
    
    if ole.exists(OLE_OBJECT_NAME):
        if debug: print 'Math size:', ole.get_size(OLE_OBJECT_NAME)
        mathStream = ole.openstream(OLE_OBJECT_NAME)
        mathData = mathStream.read()[OLE_HEADER_LENGTH:]
        if debug: print 'Math data:', mathData
        ole.close()
        return parseMTEF(mathData, debug)
        
    else:
        ole.close()
        # Make some MathML that says it cannot read this particular math
        root = etree.Element('a')
        root.set('href', REPORT_BUG_URL)
        elem = etree.SubElement(root, 'math', nsmap={None: 'http://www.w3.org/1998/Math/MathML'})
        elem = etree.SubElement(elem, 'mrow')
        elem = etree.SubElement(elem, 'mtext')
        elem.text = '[MathType Error. Click Here to Tell Central Access!]'
        
        return root
    
def _combineNumbers(mathml):
    '''
    Combines continuous digit elements into a single digit element. This is a
    post-processing function.
    '''
    
    if _isNumber(mathml):
        gotDecimal = False
        
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
            
            # Check if it is a decimal
            elif _isDecimal(n):
                if not gotDecimal:
                    gotDecimal = True
                    mathml.text += n.text
                    if n.getparent() != None:
                        n.getparent().remove(n)
                else:
                    break
                
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
            
    elif _isDecimal(mathml):
        
        # Mutate the node to turn it into a <mn>
        if '}' in mathml.tag:
            namespace = mathml.tag.rsplit('}')[0] + '}'
            print 'Setting MathML tag to:', namespace + 'mn'
            mathml.tag = namespace + 'mn'
        else:
            mathml.tag = 'mn'
        
        # Same procedure as the normal number.
        while True:
            n = mathml.getnext()
            if n == None:
                break
            
            if _isNumber(n):
                mathml.text += n.text
                if n.getparent() != None:
                    n.getparent().remove(n)
                
            else:
                break
    
    # Check the children and make sure those are all good too
    if len(mathml) > 0:
        # The function will handle all of the siblings too
        _combineNumbers(mathml[0])
    
    # Do it for this element's sibling
    if mathml.getnext() != None:
        _combineNumbers(mathml.getnext())

def _isNumber(mathml):
    '''
    Checks whether the MathML element is a number, or more specifically, a <mn>
    element. Returns True if it is.
    '''
    testTag = mathml.tag.rsplit('}', 1)[-1].lower()
    if testTag == 'mn':
        try:
            float(mathml.text)
            return True
        except ValueError:
            return False
    else:
        return False
    
def _isDecimal(mathml):
    '''
    Checks whether the MathML element has a decimal in it and there is a digit
    to the right of it. Returns True if it is.
    '''
    if mathml.text == '.':
        n = mathml.getnext()    
        if n != None:
            return _isNumber(n)
            
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
