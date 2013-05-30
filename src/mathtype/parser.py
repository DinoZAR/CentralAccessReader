'''
Created on Mar 2, 2013

@author: Spencer Graffe
'''
import struct
import StringIO
from lxml import etree
from records import *
import templates
from src.misc import program_path

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
    print
    print 'Converting records to MathML...'
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
    '''
    
    # Keep reading until I find the first instance of the AppsMFCC tag. This is
    # the embedded comment tag that holds my MathType stuff
    testString = ''
    
    done = False
    found = False
    try:
        while not done:
            testString += wmfFile.read(1)
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
        commentHeader = struct.unpack('<HII', wmfFile.read(10))
        print 'Comment Header:', commentHeader
        
        signature = getNullTermString(wmfFile)
        print 'Signature:', signature
        
        # If the signature is something like "Design Science, Inc.", then it is MTEF
        if signature == 'Design Science, Inc.':
            return parseMTEF(wmfFile.read(commentHeader[2]))