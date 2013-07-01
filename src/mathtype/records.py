'''
Created on Mar 2, 2013

@author: Spencer Graffe
'''
import struct
import math
from lxml import etree
import embellishments

MATHML_OPERATORS = ['+', 
                    '-',
                    unichr(8722), # Math minus
                    '*',
                    unichr(215),  # times that looks like an "x"
                    '/',
                    unichr(247),  # divided by symbol
                    unichr(177), # Plus/minus
                    '=',
                    '(', 
                    ')',
                    '[',
                    ']',
                    '{',
                    '}',
                    unichr(8214), # double bar
                    unichr(8970), # left floor
                    unichr(8971), # right floor
                    unichr(8968), # left ceiling
                    unichr(8969), # right ceiling
                    unichr(9001), # left angle bracket
                    unichr(9002), # right angle bracket
                    unichr(12314), # left double-stroke bracket
                    unichr(12315), # right double-stroke bracket
                    '!',
                    unichr(8594), # right arrow
                    unichr(8592), # left arrow
                    unichr(8596), # double-sided arrow
                    unichr(8636), # left arrow barb up
                    unichr(8637), # left arrow barb down
                    unichr(8640), # right arrow barb up
                    unichr(8641), # right arrow barb down
                    unichr(8644), # top right arrow, bottom left arrow
                    unichr(10529),# diagonal arrow top left to bottom right
                    unichr(10530),# diagonal arrow bottom left to top right
                    unichr(10562),# right arrow over small left arrow
                    unichr(10564),# small right arrow over left arrow
                    unichr(10564),# 
                    unichr(8756), # 3 dot therefore
                    unichr(8757), # 3 dot because
                    unichr(8717), # such that
                    unichr(8707), # exists
                    unichr(8704), # for all
                    unichr(172), # not
                    unichr(8743), # logical and
                    unichr(8744), # logical or
                    unichr(8745), # intersection
                    unichr(8746), # union
                    unichr(8712), # membership
                    unichr(8713), # not in membership
                    unichr(8834), # proper subset open right
                    unichr(8835), # proper subset open left
                    unichr(8838), # subset open right
                    unichr(8839), # subset open left
                    unichr(8836) # not a subset
]

# Don't include actual numeral digits [0-9] here
MATHML_NUMBERS = [unichr(8734)]

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
        return PileRecord(fileHandle)
    elif type == R_MATRIX:
        return MatrixRecord(fileHandle)
    elif type == R_EMBELL:
        return EmbellishmentRecord(fileHandle)
    elif type == R_RULER:
        _handleRuler(fileHandle)
        return None
    elif type == R_FONT_STYLE_DEF:
        FontStyleDefinitionRecord(fileHandle)
        return None
    elif type == R_SIZE:
        SizeRecord(fileHandle)
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
        print 'Symbol!'
        return None
    elif type == R_SUBSYM:
        print 'Sub Symbol!'
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
            
        elif isinstance(records[i], PileRecord):
            newElem = etree.SubElement(parentStack[-1], 'mrow')
            parentStack.append(newElem)
            convertRecords(0, records[i].childRecords, parentStack)
            parentStack.pop()
            
        elif isinstance(records[i], CharRecord):
            character = unichr(records[i].mtCode)
            elem = None
            if character in MATHML_OPERATORS:
                elem = etree.Element('mo')
                elem.text = character
            elif _isNumber(character):
                elem = etree.Element('mn')
                elem.text = character
            else:
                elem = etree.Element('mi')
                
                set = False
                
                # Double-struck
#                 if records[i].typeface in CharRecord.DOUBLE_STRUCK:
                if records[i].mtCode in CharRecord.DOUBLE_STRUCK:
                    elem.set('mathvariant', 'double-struck')
                    elem.text = unichr(CharRecord.DOUBLE_STRUCK[records[i].mtCode])
                    set = True
                
                # Fraktur
#                 if records[i].typeface in CharRecord.FRAKTUR:
                if records[i].mtCode in CharRecord.FRAKTUR:
                    elem.set('mathvariant', 'fraktur')
                    elem.text = unichr(CharRecord.FRAKTUR[records[i].mtCode])
                    set = True
                        
                # Script
#                 if records[i].typeface in CharRecord.SCRIPT:
                if records[i].mtCode in CharRecord.SCRIPT:
                    elem.set('mathvariant', 'script')
                    elem.text = unichr(CharRecord.SCRIPT[records[i].mtCode])
                    set = True
                
                # Everything else
                if not set:
                    elem.text = character
                
            if len(records[i].embellishments) > 0:
                for emb in records[i].embellishments:
                    elem = embellishments.embellishElement(elem, emb.type)
            
            parentStack[-1].append(elem)
                
        elif isinstance(records[i], TemplateRecord):
            import templates
            data = None
            if len(parentStack[-1]) > 0:
                data = templates.getMathMLFromTemplate(records[i], i, records, parentStack[-1][-1])
            else:
                data = templates.getMathMLFromTemplate(records[i], i, records, None)
            while data[1] > 0:
                parentStack[-1].remove(parentStack[-1][-1])
                data = (data[0], data[1] - 1)
            if len(data[0]) > 0:
                for d in data[0]:
                    parentStack[-1].append(d)
        
        elif isinstance(records[i], MatrixRecord):
            root = etree.SubElement(parentStack[-1], 'mtable')
            for r in range(records[i].rows):
                rowElem = etree.SubElement(root, 'mtr')
                for c in range(records[i].columns):
                    colElem = etree.SubElement(rowElem, 'mtd')
                    parentStack.append(colElem)
                    convertRecords(0, [records[i].childRecords[(r * records[i].columns) + c]], parentStack)
                    parentStack.pop()
            
        i += 1

def _isNumber(character):
    '''
    Returns whether the character in question is a number or something that can
    be treated as a number.
    '''
    if character.isdigit():
        return True
    
    # Infinity
    elif character in MATHML_NUMBERS:
        return True
    else:
        return False

# 
# Functions that help skip over parts of the data I don't want 
# ------------------------------------------------------------------------------

def _handleRuler(f):
    '''
    Handles a Ruler record. It's useless to me right now, so I'm going to
    cleanly skip over it.
    '''
    print 'Ruler!'
    #f.read(1)
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
        
class PileRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Pile!'
        
        # Get the options
        options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge. If so, get the nudge
        if self._checkFlag(options, Record.O_NUDGE):
            print '- Nudge!'
            _handleNudge(f)
            
        self.halign = struct.unpack('<B', f.read(1))[0]
        self.valign = struct.unpack('<B', f.read(1))[0]
        
        # Check for ruler
        if self._checkFlag(options, Record.O_LP_RULER):
            print '- Ruler in pile!'
            _handleRuler(f)
            
        # Get object list as child records
        while True:
            type = struct.unpack('<B', f.read(1))[0]
            record = createRecord(type, f)
            if isinstance(record, EndRecord):
                break
            else:
                if record != None:
                    self.childRecords.append(record)
class LineRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Line!'
        
        # Get the options
        options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge. If so, get the nudge
        if self._checkFlag(options, Record.O_NUDGE):
            print '- Nudge!'
            _handleNudge(f)
            
        # Check for line spacing
        if self._checkFlag(options, Record.O_LINE_LSPACE):
            print '- Line Spacing!'
            f.read(2)   # Skip it
            
        # Check for ruler
        if self._checkFlag(options, Record.O_LP_RULER):
            print '- Ruler in line!'
            recordType = f.read(1)
            if recordType == R_RULER:
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
        
class FontStyleDefinitionRecord(Record):
    def __init__(self, f):
        
        # Get the font index. It is an unsigned integer, so it gets to be
        # treated weirdly
        val = struct.unpack('<B', f.read(1))[0]
        if val < 255:
            self.fontIndex = val
        else:
            self.fontIndex = struct.unpack('<H', f.read(2))[0]
            
        # Also get the character style bits
        self.characterStyle = struct.unpack('<B', f.read(1))[0]
                    
class CharRecord(Record):
    
    # A dictionary that has a lookup table to replace any character code that
    # is just too weird.
    # It is in the following format:
    # {mtCode : unicode}
    WEIRDNESS = {
                 209 : 8913,     # double superset
                 59791 : 183,    # dot operator
                 
                 60423 : 124,    # single bar
                 60424 : 124,    # single bar
                 60425 : 8214,   # double bar
                 60426 : 8214,   # double bar
                 60428 : 9141,   # under spanning bracket
                 60429 : 9140,   # over spanning bracket
                 
                 63726 : 8968,   # left ceiling
                 63728 : 8970,   # left floor
                 63737 : 8969,   # right ceiling
                 63739 : 8971,   # right floor
                 
                 60161 : 10562,  # right arrow over small left arrow
                 60162 : 10564,  # small right arrow over left arrow
                 60163 : 8636,   # NOT MATCH - right harpoon over small left harpoon
                 60164 : 8636,   # NOT MATCH - small right harpoon over left harpoon
                 60165 : 10530,  # diagonal arrow bottom left to top right
                 60166 : 10529,  # diagonal arrow top left to bottom right
                 
                 60928 : 8755,   # counter-clockwise loop integral
                 60929 : 8754,   # clockwise loop integral
                 60945 : 8750,   # contour integral
                 60946 : 8751,   # double contour integral
                 60947 : 8752,   # triple contour integral
                 
                 61185 : 8203,   # zero-width space (what's the point of that?)
                 61186 : 8198,   # thin space
                 61187 : 8196,   # thick space
                 61189 : 8195,   # em space
                 61190 : 8195,   # 2 em space
                 61191 : 8202,   # inner space
                 61192 : 8202,   # one-point space
                 
                 61312 : 8754,   # Clockwise contour integral (arrow left side)
                 
                 61824 : 7424,   # small cap A
                 61825 : 665,    # small cap B
                 61826 : 7428,   # small cap C
                 61827 : 7429,   # small cap D
                 61828 : 7431,   # small cap E
                 61829 : 42800,  # small cap F
                 61830 : 610,    # small cap G
                 61831 : 668,    # small cap H
                 61832 : 618,    # small cap I
                 61833 : 7434,   # small cap J
                 61834 : 7435,   # small cap K
                 61835 : 671,    # small cap L
                 61836 : 7437,   # small cap M
                 61837 : 628,    # small cap N
                 61838 : 7439,   # small cap O
                 61839 : 7448,   # small cap P
                 61841 : 640,    # small cap R
                 61842 : 42801,  # small cap S
                 61843 : 7451,   # small cap T
                 61844 : 7452,   # small cap U
                 61845 : 7456,   # small cap V
                 61846 : 7457,   # small cap W
                 61848 : 655,    # small cap Y
                 61849 : 7458,   # small cap Z
                 61850 : 7425,   # small cap ligature ae
                 61851 : 7838    # small cap sharp s (not small yet)
                 }
    
    # This dictionary identifies double-struck characters
    # It is in the following format:
    # {mtCode: characterNotDoubleStruck}
    DOUBLE_STRUCK = {61568 : 65,  # cap A
                     61569 : 66,  # cap B
                     61570 : 67,  # cap C
                     61571 : 68,  # cap D
                     61572 : 69,  # cap E
                     61573 : 70,  # cap F
                     61574 : 71,  # cap G
                     61575 : 72,  # cap H
                     61576 : 73,  # cap I
                     61577 : 74,  # cap J
                     61578 : 75,  # cap K
                     61579 : 76,  # cap L
                     61580 : 77,  # cap M
                     61581 : 78,  # cap N
                     61582 : 79,  # cap O
                     61583 : 80,  # cap P
                     61584 : 81,  # cap Q
                     61585 : 82,  # cap R
                     61586 : 83,  # cap S
                     61587 : 84,  # cap T
                     61588 : 85,  # cap U
                     61589 : 86,  # cap V
                     61590 : 87,  # cap W
                     61591 : 88,  # cap X
                     61592 : 89,  # cap Y
                     61593 : 90,  # cap Z
                     
                     61594 : 97,  # small A
                     61595 : 98,  # small B
                     61596 : 99,  # small C
                     61597 : 100, # small D
                     61598 : 101, # small E
                     61599 : 102, # small F
                     61600 : 103, # small G
                     61601 : 104, # small H
                     61602 : 105, # small I
                     61603 : 106, # small J
                     61604 : 107, # small K
                     61605 : 108, # small L
                     61606 : 109, # small M
                     61607 : 110, # small N
                     61608 : 111, # small O
                     61609 : 112, # small P
                     61610 : 113, # small Q
                     61611 : 114, # small R
                     61612 : 115, # small S
                     61613 : 116, # small T
                     61614 : 117, # small U
                     61615 : 118, # small V
                     61616 : 119, # small W
                     61617 : 120, # small X
                     61618 : 121, # small Y
                     61619 : 122  # small Z
                     }
    
    # This dictionary identifies fraktur characters
    # It is in the following format:
    # {mtCode: characterNotFraktur}
    FRAKTUR = {61440 : 65,  # cap A
               61441 : 66,  # cap B
               61442 : 67,  # cap C
               61443 : 68,  # cap D
               61444 : 69,  # cap E
               61445 : 70,  # cap F
               61446 : 71,  # cap G
               61447 : 72,  # cap H
               61448 : 73,  # cap I
               61449 : 74,  # cap J
               61450 : 75,  # cap K
               61451 : 76,  # cap L
               61452 : 77,  # cap M
               61453 : 78,  # cap N
               61454 : 79,  # cap O
               61455 : 80,  # cap P
               61456 : 81,  # cap Q
               61457 : 82,  # cap R
               61458 : 83,  # cap S
               61459 : 84,  # cap T
               61460 : 85,  # cap U
               61461 : 86,  # cap V
               61462 : 87,  # cap W
               61463 : 88,  # cap X
               61464 : 89,  # cap Y
               61465 : 90,  # cap Z
               
               61466 : 97,  # small A
               61467 : 98,  # small B
               61468 : 99,  # small C
               61469 : 100, # small D
               61470 : 101, # small E
               61471 : 102, # small F
               61472 : 103, # small G
               61473 : 104, # small H
               61474 : 105, # small I
               61475 : 106, # small J
               61476 : 107, # small K
               61477 : 108, # small L
               61478 : 109, # small M
               61479 : 110, # small N
               61480 : 111, # small O
               61481 : 112, # small P
               61482 : 113, # small Q
               61483 : 114, # small R
               61484 : 115, # small S
               61485 : 116, # small T
               61486 : 117, # small U
               61487 : 118, # small V
               61488 : 119, # small W
               61489 : 120, # small X
               61490 : 121, # small Y
               61491 : 122  # small Z
               }
    
    # This dictionary identifies script characters
    # It is in the following format:
    # {mtCode: characterNotScript}
    SCRIPT = {
              61696 : 65,   # cap A
              61697 : 66,   # cap B
              61698 : 67,   # cap C
              61699 : 68,   # cap D
              61700 : 69,   # cap E
              61701 : 70,   # cap F
              61702 : 71,   # cap G
              61703 : 72,   # cap H
              61704 : 73,   # cap I
              61705 : 74,   # cap J
              61706 : 75,   # cap K
              61707 : 76,   # cap L
              61708 : 77,   # cap M
              61709 : 78,   # cap N
              61710 : 79,   # cap O
              61711 : 80,   # cap P
              61712 : 81,   # cap Q
              61713 : 82,   # cap R
              61714 : 83,   # cap S
              61715 : 84,   # cap T
              61716 : 85,   # cap U
              61717 : 86,   # cap V
              61718 : 87,   # cap W
              61719 : 88,   # cap X
              61720 : 89,   # cap Y
              61721 : 90,   # cap Z
              
              61722 : 97,   # small A
              61723 : 98,   # small B
              61724 : 99,   # small C
              61725 : 100,  # small D
              61726 : 101,  # small E
              61727 : 102,  # small F
              61728 : 103,  # small G
              61729 : 104,  # small H
              61730 : 105,  # small I
              61731 : 106,  # small J
              61732 : 107,  # small K
              61733 : 108,  # small L
              61734 : 109,  # small M
              61735 : 110,  # small N
              61736 : 111,  # small O
              61737 : 112,  # small P
              61738 : 113,  # small Q
              61739 : 114,  # small R
              61740 : 115,  # small S
              61741 : 116,  # small T
              61742 : 117,  # small U
              61743 : 118,  # small V
              61744 : 119,  # small W
              61745 : 120,  # small X
              61746 : 121,  # small Y
              61747 : 122   # small Z
              }

    def __init__(self, f):
        Record.__init__(self)
        
        print 'Char!'
        
        self.options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge
        if self._checkFlag(self.options, Record.O_NUDGE):
            _handleNudge(f)
        
        # Get typeface (signed integer)
        val = struct.unpack('<b', f.read(1))[0]
        print 'Initial typeface:', val
        if (val >= -128) and (val <= 127):
            self.typeface = val + 128
        else:
            self.typeface = struct.unpack('<h', f.read(2))[0] + 32768
            
        print 'Typeface:', self.typeface
        
        # Check for MTCode
        if not self._checkFlag(self.options, Record.O_CHAR_ENC_NO_MTCODE):
            self.mtCode = struct.unpack('<H', f.read(2))[0]
            print 'MTCode:', self.mtCode
            
        # Clean it up if the code and typeface are from a weird place
        self._cleanup()
        
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
        
    def _cleanup(self):
        '''
        Searches through its database of weirdness and tries to fix up the
        character code.
        '''
        #if self.typeface in self.WEIRDNESS:
        #    codes = self.WEIRDNESS[self.typeface]
        if self.mtCode in self.WEIRDNESS:
            self.mtCode = self.WEIRDNESS[self.mtCode]
                         
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
                    
class SizeRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Size!'
        
        # Skip over it all
        f.read(2)

class MatrixRecord(Record):
    
    def __init__(self, f):
        Record.__init__(self)
        
        print 'Matrix!'
        
        self.options = struct.unpack('<B', f.read(1))[0]
        
        # Check for nudge
        if self._checkFlag(self.options, Record.O_NUDGE):
            _handleNudge(f)
        
        self.valign = struct.unpack('<B', f.read(1))[0]
        self.h_just = struct.unpack('<B', f.read(1))[0]
        self.v_just = struct.unpack('<B', f.read(1))[0]
        
        self.rows = struct.unpack('<B', f.read(1))[0]
        self.columns = struct.unpack('<B', f.read(1))[0]
        
        print 'Rows:', self.rows
        print 'Columns:', self.columns
        
        # Get row partition line types (ignore for now)
        f.read(1)
        for i in range(int(math.floor(self.rows / 4.0))):
            f.read(1)
            
        # Get column partition types (ignore for now)
        f.read(1)
        for i in range(int(math.floor(self.columns / 4.0))):
            f.read(1)
        
        # Get my list of lines that are for each entry in the matrix
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
        
        val = struct.unpack('<B', f.read(1))[0]
        if val < 255:
            self.encodingIndex = val
        else:
            self.encodingIndex = struct.unpack('<H', f.read(2))[0]
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