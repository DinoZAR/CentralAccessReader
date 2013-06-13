'''
Created on Mar 2, 2013

@author: Spencer Graffe
'''
import os
import struct
import StringIO
from lxml import etree
from records import *
import templates
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
                testString += wmfString.read(1)
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
            
    except Exception as ex:
        # Write the problem file to my temp
        savePath = temp_path(os.path.join('mathtype', os.path.basename(wmfFile.name)))
        if not os.path.exists(os.path.dirname(savePath)):
            os.makedirs(os.path.dirname(savePath))
        saveFile = open(savePath, 'wb')
        wmfString.seek(0)
        saveFile.write(wmfString.read())
        saveFile.close()
            
        raise MathTypeParseError(savePath, ex)
            
class MathTypeParseError(Exception):
    def __init__(self, savePath, originalException):
        self.originalException = originalException
        self.savePath = savePath
        self.message = 'Couldn\'t parse MathType: Saved to ' + self.savePath + '\n'
        self.message += 'Original Exception:\n' + self.originalException.__class__.__name__ + ': ' + str(self.originalException)