'''
Created on Mar 2, 2013

@author: Spencer Graffe
'''
import struct
from lxml import etree

MATHML_OPERATORS = ['+', 
                    '-',
                    '\u8722',
                    '*', 
                    '/', 
                    '=', 
                    '(', 
                    ')',
                    '[',
                    ']',
                    '{',
                    '}', 
                    '!']

R_END = 0
R_LINE = 1
R_CHAR = 2
R_TMPL = 3
R_PILE = 4
R_MATRIX = 5
R_EMBELL = 6
R_RULER = 7
R_FONT_STYLE_DEF = 8
R_SIZE = 9
R_FULL = 10
R_SUB = 11
R_SUB2 = 12
R_SYM = 13
R_SUBSYM = 14
R_COLOR = 15
R_COLOR_DEF = 16
R_FONT_DEF = 17
R_EQN_PREFS = 18
R_ENCODING_DEF = 19

# Future implementations (pretty experimental stuff that I found)
R_TEX_INPUT = 0x66

# Embellishments
EMB_1DOT = 2
EMB_2DOT = 3
EMB_3DOT = 4
EMB_1PRIME = 5
EMB_2PRIME = 6
EMB_BPRIME = 7
EMB_TILDE = 8
EMB_HAT = 9
EMB_NOT = 10
EMB_RARROW = 11
EMB_LARROW = 12
EMB_BARROW = 13
EMB_R1ARROW = 14
EMB_L1ARROW = 15
EMB_MBAR = 16
EMB_OBAR = 17
EMB_3PRIME = 18
EMB_FROWN = 19
EMB_SMILE = 20
EMB_X_BARS = 21
EMB_UP_BAR = 22
EMB_DOWN_BAR = 23
EMB_4DOT = 24
EMB_U_1DOT = 25
EMB_U_2DOT = 26
EMB_U_3DOT = 27
EMB_U_4DOT = 28
EMB_U_BAR = 29
EMB_U_TILDE = 30
EMB_U_FROWN = 31
EMB_U_SMILE = 32
EMB_U_RARROW = 33
EMB_U_LARROW = 34
EMB_U_BARROW = 35
EMB_U_R1ARROW = 36
EMB_U_L1ARROW = 37

def createRecord(type, fileHandle):
    '''
    Based on the type (just a byte), it will create the record corresponding
    to it.
    '''
    if type == R_END:
        return EndRecord(fileHandle)
    elif type == R_LINE:
        return LineRecord(fileHandle)
    elif type == R_CHAR:
        return CharRecord(fileHandle)
    elif type == R_TMPL:
        return TemplateRecord(fileHandle)
    elif type == R_PILE:
        print 'Error: Record type not implemented yet:', type
        return None
    elif type == R_MATRIX:
        print 'Error: Record type not implemented yet:', type
        return None
    elif type == R_EMBELL:
        return EmbellishmentRecord(fileHandle)
    elif type == R_RULER:
        _handleRuler(fileHandle)
        return None
    elif type == R_FONT_STYLE_DEF:
        print 'Error: Record type not implemented yet:', type
        return None
    elif type == R_SIZE:
        print 'Error: Record type not implemented yet:', type
        return None
    elif type == R_FULL:
        FullRecord(fileHandle)
        return None
    elif type == R_SUB:
        SubscriptRecord(fileHandle)
        return None
    elif type == R_SUB2:
        Subscript2Record(fileHandle)
        return None
    elif type == R_SYM:
        print 'Error: Record type not implemented yet:', type
        return None
    elif type == R_SUBSYM:
        print 'Error: Record type not implemented yet:', type
        return None
    elif type == R_COLOR:
        ColorRecord(fileHandle)
        return None
    elif type == R_COLOR_DEF:
        ColorDefinitionRecord(fileHandle)
        return None
    elif type == R_FONT_DEF:
        FontDefinitionRecord(fileHandle)
        return None
    elif type == R_EQN_PREFS:
        EquationPreferencesRecord(fileHandle)
        return None
    elif type == R_ENCODING_DEF:
        EncodingDefinitionRecord(fileHandle)
        return None
    elif type == R_TEX_INPUT:
        TexInputRecord(fileHandle)
        return None
    else:
        print 'Future implemented record! Skipping for now...'
        count = struct.unpack('<B', fileHandle.read(1))[0]
        fileHandle.read(count)
        return None
    
def convertRecords(i, records, parentStack):
    while i < len(records):
        if isinstance(records[i], LineRecord):
            newElem = etree.SubElement(parentStack[-1], 'mrow')
            parentStack.append(newElem)
            convertRecords(0, records[i].childRecords, parentStack)
            parentStack.pop()
        if isinstance(records[i], CharRecord):
            character = unichr(records[i].mtCode)
            if len(records[i].embellishments) > 0:
                pass
            if character in MATHML_OPERATORS:
                elem = etree.SubElement(parentStack[-1], 'mo')
                elem.text = character
            else:
                elem = etree.SubElement(parentStack[-1], 'mi')
                elem.text = character
                
        if isinstance(records[i], TemplateRecord):
            import templates
            data = templates.getMathMLFromTemplate(records[i], i, records)
            while data[1] > 0:
                parentStack[-1].remove(parentStack[-1][-1])
                data = (data[0], data[1] - 1)
            if len(data[0]) > 0:
                for d in data[0]:
                    parentStack[-1].append(d)
            
        i += 1
        
# 
# Functions that help skip over parts of the data I don't want 
# ------------------------------------------------------------------------------

def _handleRuler(f):
    '''
    Handles a Ruler record. It's useless to me right now, so I'm going to
    cleanly skip over it.
    '''
    print 'Ruler!'
    f.read(1)
    n_stops = struct.unpack('<H', f.read(2))[0]
    for i in range(n_stops):
        f.read(3)
    
def _handleNudge(f): 
    '''
    For now, read enough of it just to discard it.
    '''
    print 'Nudge!'
    # Nudge can have 2 or six bytes, depending on whether the first 2
    # bytes are at +128 or not
    first2 = struct.unpack('<bb', f.read(2))
    
    if (first2[0] == 128) and (first2[1] == 128):
        # Skip through the next 4 bytes
        f.read(4)
            
# Utility Functions
# ------------------------------------------------------------------------------

def getNullTermString(fileHandle):
    '''
    Gets the Python string from a null-terminated string in a file. This
    function assumes that the file has already been seeked to the first position
    of the requested string to convert.
    '''
    
    myString = ''
    
    try:
        while True:
            nextChar = fileHandle.read(1)
            if nextChar == '\x00':
                break
            else:
                myString += nextChar
    except EOFError:
        print 'ERROR: Could not get null-terminated string because of EOF'
        
    return myString


# Classes of my records
# ------------------------------------------------------------------------------

class Record():
    '''
    Class used to store a record found in a MathType equation. This is just an
    abstract class that shouldn't be directly used by anything.
    '''
    
    # Options flags
    O_NUDGE = 8
    O_CHAR_EMBELL = 1
    O_CHAR_FUNC_START = 2
    O_CHAR_ENC_CHAR_8 = 4
    O_CHAR_ENC_CHAR_16 = 16
    O_CHAR_ENC_NO_MTCODE = 32
    O_LINE_NULL = 1
    O_LINE_LSPACE = 4
    O_LP_RULER = 2
    O_COLOR_CMYK = 1
    O_COLOR_SPOT = 2
    O_COLOR_NAME = 4
    
    def __init__(self):
        self.childRecords = []
        
    def _checkFlag(self, flags, flag):
        return (flags & flag) > 0

class FullRecord(Record):
    def __init__(self, f):
        Record.__init__(self)
        print 'Full!'

class SubscriptRecord(Record):
    def __init__(self, f):
        Record.__init__(self)
        print 'Subscript!'
        
class Subscript2Record(Record):
    def __init__(self, f):
        Record.__init__(self)
        print 'Subscript 2!'
        
class EndRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        print 'End!'
        
class LineRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Line!'
        
        # Get the options
        options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge. If so, get the nudge
        if self._checkFlag(options, Record.O_NUDGE):
            _handleNudge(f)
            
        # Check for line spacing
        if self._checkFlag(options, Record.O_LINE_LSPACE):
            f.read(2)   # Skip it
            
        # Check for ruler
        if self._checkFlag(options, Record.O_LP_RULER):
            _handleRuler(f)
          
        # The rest are objects in the line record, which should be added to
        # the children
        if not self._checkFlag(options, Record.O_LINE_NULL):
            while True:
                type = struct.unpack('<B', f.read(1))[0]
                record = createRecord(type, f)
                if isinstance(record, EndRecord):
                    break
                else:
                    if record != None:
                        self.childRecords.append(record)
                        
class EmbellishmentRecord(Record):
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Embellishment!'
        
        self.options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge
        if self._checkFlag(self.options, Record.O_NUDGE):
            _handleNudge(f)
            
        self.type = struct.unpack('<B', f.read(1))[0]
                    
class CharRecord(Record):
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Char!'
        
        self.options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge
        if self._checkFlag(self.options, Record.O_NUDGE):
            _handleNudge(f)
        
        # Get typeface (signed integer)
        val = struct.unpack('<b', f.read(1))[0]
        if (val >= -128) and (val < 127):
            self.typeface = val + 128
        else:
            self.typeface = struct.unpack('<h', f.read(2))[0] + 32768
            
        print 'Typeface:', self.typeface
        
        # Check for MTCode
        if not self._checkFlag(self.options, Record.O_CHAR_ENC_NO_MTCODE):
            self.mtCode = struct.unpack('<H', f.read(2))[0]
            print 'MTCode:', self.mtCode
        
        # Check for 8-bit font position
        if self._checkFlag(self.options, Record.O_CHAR_ENC_CHAR_8):
            print '8-bit Position:', struct.unpack('<B', f.read(1))[0]
        
        # Check for 16-bit font position (mutually exclusive)
        if self._checkFlag(self.options, Record.O_CHAR_ENC_CHAR_16):
            print '16-bit Position:', struct.unpack('<H', f.read(2))[0]
            
        # Check for embellishments
        self.embellishments = []
        if self._checkFlag(self.options, Record.O_CHAR_EMBELL):
            while True:
                type = struct.unpack('<B', f.read(1))[0]
                record = createRecord(type, f)
                if isinstance(record, EndRecord):
                    break
                else:
                    if record != None:
                        self.embellishments.append(record)
            
                         
class TemplateRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Template!'
        
        self.options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge
        if self._checkFlag(self.options, Record.O_NUDGE):
            _handleNudge(f)
        
        # Get the template selector code
        self.selector = struct.unpack('<B', f.read(1))[0]
        print 'Selector Code:', self.selector
        
        # Get the variation byte, or bytes
        val = struct.unpack('<B', f.read(1))[0]
        if self._checkFlag(val, 0x80):
            self.variation = (val & 0x7F) | struct.unpack('<B', f.read(1))[0]
        else:
            self.variation = val
        print 'Variation:', self.variation
        
        # Get template-specific options
        self.templateOptions = struct.unpack('<B', f.read(1))[0]
        print 'Template Options:', self.templateOptions
        
        # Get all of the children for this template
        self.childRecords = []
        while True:
            type = struct.unpack('<B', f.read(1))[0]
            record = createRecord(type, f)
            if isinstance(record, EndRecord):
                break
            else:
                if record != None:
                    self.childRecords.append(record)
        
class ColorRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Color!'
        
        val = struct.unpack('<B', f.read(1))[0]
        if val < 255:
            self.defIndex = val
        else:
            self.defIndex = struct.unpack('<H', f.read(2))[0]
            
        print 'Definition Index:', self.defIndex
                    
class ColorDefinitionRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Color Definition!'
        
        self.options = struct.unpack('<B', f.read(1))[0]
        
        # If RGB, do one thing. If CMYK, do another
        if self._checkFlag(self.options, Record.O_COLOR_CMYK):
            print 'Color Type: CMYK'
            f.read(8)
        else:
            print 'Color Type: RGB'
            f.read(6)
        
        # Check if we got a color name. If we do, get it
        if self._checkFlag(self.options, Record.O_COLOR_NAME):
            self.name = getNullTermString(f)
            print 'Color Name: ' + self.name
                    
class FontDefinitionRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Font Definition!'
        
        self.encodingIndex = struct.unpack('<B', f.read(1))[0]
        self.fontName = getNullTermString(f)
        
        print 'Encoding Index:', self.encodingIndex
        print 'Font Name:', self.fontName

class EquationPreferencesRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Equation Preferences!'
        
        # Grab byte for options flags that hasn't been implemented yet?
        f.read(1)
        
        # Completely ignore the next three arrays
        # (2 being dimensional arrays and the other just a weird one)
        for i in range(2):
            count = struct.unpack('<B', f.read(1))[0]
            print 'Dimensional Array', i, 'Count:', count
            while count > 0:
                nextVal = struct.unpack('<B', f.read(1))[0]
                if (nextVal & 0x0F) == 0x0F:
                    count -= 1
                if (nextVal & 0xF0) == 0xF0:
                    count -= 1
        
        # Handle the "weird" styles array
        count = struct.unpack('<B', f.read(1))[0]
        print 'Styles Array Count:', count
        while count > 0:
            nextVal = struct.unpack('<B', f.read(1))[0]
            if nextVal > 0:
                f.read(1)
            count -= 1
                    
class EncodingDefinitionRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Encoding Definition!'
        
        # Grab the encoding name, which is null-terminated
        self.encodingName = getNullTermString(f)
        
        print 'Encoding Name:', self.encodingName
        
class TexInputRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'LaTex Input! (I think)'
        
        self.options = struct.unpack('<B', f.read(1))
        self.description = getNullTermString(f)
        self.code = getNullTermString(f)
        
        print 'Description:', self.description
        print 'Code:', self.code