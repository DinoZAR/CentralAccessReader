'''
Created on Mar 2, 2013

@author: Spencer Graffe
'''
import struct
from records import createRecord, getNullTermString


def parseWMF(wmfFile):
    '''
    Parses the WMF file to find the embedded MathType data. Then, it will get
    a MathType object from it.
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
        pass
    
    if found:
        print 'Found AppsMFCC tag!'
        print
        
        # Grab all of the other data in the comment header (even most I won't need)
        commentHeader = struct.unpack('<HII', wmfFile.read(10))
        print 'Comment Header:', commentHeader
        
        signature = getNullTermString(wmfFile)
        print 'Signature:', signature
        
        # Store the seek position of the file at this point. We now need to
        # keep track of how much data we are reading.
        startPos = wmfFile.tell()
        
        print
        print '--------------------------------------------------------'
        print
        
        # The rest shall be the MTEF equation
        mtefHeader = struct.unpack('<BBBBB', wmfFile.read(5))
        print 'MTEF Header:', mtefHeader
        
        applicationKey = getNullTermString(wmfFile)
        print 'Application Key:', applicationKey
        
        equationOptions = struct.unpack('<B', wmfFile.read(1))[0]
        print 'Equation Options:', equationOptions
        
        print
        print 'Starting reading math content...'
        print '----------------------------------------------------'
        print
        
        while wmfFile.tell() < (startPos + commentHeader[2]):            
            # Get record type
            recordType = struct.unpack('<B', wmfFile.read(1))[0]
            
            # Let the Record object handle how to read this record
            record = createRecord(recordType, wmfFile)
        
        print 'Final positions:', hex(wmfFile.tell()), '=', hex((startPos + commentHeader[2]))