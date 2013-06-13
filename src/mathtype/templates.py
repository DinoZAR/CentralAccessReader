'''
Created on May 29, 2013

Has the code necessary to successfully interpret the templates that are in
MathType.

@author: Spencer Graffe
'''
from lxml import etree
from records import convertRecords

# Template Constants
TM_ANGLE = 0
TM_PAREN = 1
TM_BRACE = 2
TM_BRACK = 3
TM_BAR = 4
TM_DBAR = 5
TM_FLOOR = 6
TM_CEILING = 7
TM_OBRACK = 8
TM_INTERVAL = 9
TM_ROOT = 10
TM_FRACT = 11
TM_UBAR = 12
TM_OBAR = 13
TM_ARROW = 14
TM_INTEG = 15
TM_SUM = 16
TM_PROD = 17
TM_COPROD = 18
TM_UNION = 19
TM_INTER = 20
TM_INTOP = 21
TM_SUMOP = 22
TM_LIM = 23
TM_HBRACE = 24
TM_HBRACK = 25
TM_LDIV = 26
TM_SUB = 27
TM_SUP = 28
TM_SUBSUP = 29
TM_DIRAC = 30
TM_VEC = 31
TM_TILDE = 32
TM_HAT = 33
TM_ARC = 34
TM_JSTATUS = 35
TM_STRIKE = 36
TM_BOX = 37

def getMathMLFromTemplate(templateRecord, currentIndex, records):
    '''
    Obtains the MathML representation of the template. This may be more than
    one element.
    
    templateRecord - the TemplateRecord that has data about the template
    i - the index in the list of records directly after the template record
    records - the list of records
    
    Returns a tuple of the following:
    (mathMLElementList, new_i)
    '''
    mathmlElements = []
    
    # How many elements before this template to remove
    removePrevious = 0
    
    if templateRecord.selector == TM_ANGLE:
        data = ParBoxClass(templateRecord, defaultLeft='<', defaultRight='>')
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_PAREN:
        data = ParBoxClass(templateRecord, defaultLeft='(', defaultRight=')')
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_BRACE:
        data = ParBoxClass(templateRecord, defaultLeft='{', defaultRight='}')
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_BRACK:
        data = ParBoxClass(templateRecord, defaultLeft='[', defaultRight=']')
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_BAR:
        data = ParBoxClass(templateRecord, defaultLeft='|', defaultRight='|')
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_DBAR:
        data = ParBoxClass(templateRecord, defaultLeft=unichr(8214), defaultRight=unichr(8214))
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_FLOOR:
        data = ParBoxClass(templateRecord, defaultLeft=unichr(8970), defaultRight=unichr(8971))
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
    
    elif templateRecord.selector == TM_CEILING:
        data = ParBoxClass(templateRecord, defaultLeft=unichr(8968), defaultRight=unichr(8969))
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
    
    elif templateRecord.selector == TM_OBRACK:
        data = ParBoxClass(templateRecord, defaultLeft=unichr(9001), defaultRight=unichr(9002))
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
    
    elif templateRecord.selector == TM_INTERVAL:
        data = ParBoxClass(templateRecord, defaultLeft='[', defaultRight=']')
        mathml = etree.Element('mfenced')
        mathml.attrib['open'] = data.leftFence
        mathml.attrib['close'] = data.rightFence
        mathml.append(data.mainSlot)
        mathmlElements.append(mathml)
    
    elif templateRecord.selector == TM_ROOT:
        data = RootBoxClass(templateRecord)
        mathml = None
        if _testVariation(templateRecord.variation, TV_ROOT_NTH):
            mathml = etree.Element('mroot')
            mathml.append(data.mainSlot)
            mathml.append(data.radicand)
            
        else:
            mathml = etree.Element('msqrt')
            mathml.append(data.mainSlot)
            
        mathmlElements.append(mathml)
    
    elif templateRecord.selector == TM_FRACT:
        data = FracBoxClass(templateRecord)
        mathml = etree.Element('mfrac')
        mathml.append(data.numerator)
        mathml.append(data.denominator)
        mathmlElements.append(mathml)
    
    elif templateRecord.selector == TM_UBAR:
        pass
    
    elif templateRecord.selector == TM_OBAR:
        pass
    
    elif templateRecord.selector == TM_ARROW:
        data = ArrowBoxClass(templateRecord)
        
        if _testVariation(templateRecord.variation, TV_AR_TOP) and not _testVariation(templateRecord.variation, TV_AR_BOTTOM):
            mathml = etree.Element('mover')
            mathml.append(data.arrow)
            mathml.append(data.slot1)
            mathmlElements.append(mathml)
            
        if not _testVariation(templateRecord.variation, TV_AR_TOP) and _testVariation(templateRecord.variation, TV_AR_BOTTOM):
            mathml = etree.Element('munder')
            
            if _testVariation(templateRecord.variation, TV_AR_DOUBLE):
                pass
            
            mathml.append(data.arrow)
            mathml.append(data.slot2)
            mathmlElements.append(mathml)
        
        elif _testVariation(templateRecord.variation, TV_AR_TOP) and _testVariation(templateRecord.variation, TV_AR_BOTTOM):
            mathml = etree.Element('munderover')
            mathml.append(data.arrow)
            mathml.append(data.slot1)
            mathml.append(data.slot2)
            mathmlElements.append(mathml)
    
    elif templateRecord.selector == TM_INTEG:
        data = BigOpBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.attrib['align'] = 'center'
        operator = etree.Element('mo')
        operator.text = data.operator
        mathml.append(operator)
        mathml.append(data.upper)
        mathml.append(data.lower)
        mathmlElements.append(mathml)
        mathmlElements.append(data.mainSlot)
    
    elif templateRecord.selector == TM_SUM:
        data = BigOpBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.attrib['align'] = 'center'
        operator = etree.Element('mo')
        operator.text = data.operator
        mathml.append(operator)
        mathml.append(data.upper)
        mathml.append(data.lower)
        mathmlElements.append(mathml)
        mathmlElements.append(data.mainSlot)
    
    elif templateRecord.selector == TM_PROD:
        data = BigOpBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.attrib['align'] = 'center'
        operator = etree.Element('mo')
        operator.text = data.operator
        mathml.append(operator)
        mathml.append(data.upper)
        mathml.append(data.lower)
        mathmlElements.append(mathml)
        mathmlElements.append(data.mainSlot)
        
    elif templateRecord.selector == TM_COPROD:
        data = BigOpBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.attrib['align'] = 'center'
        operator = etree.Element('mo')
        operator.text = data.operator
        mathml.append(operator)
        mathml.append(data.upper)
        mathml.append(data.lower)
        mathmlElements.append(mathml)
        mathmlElements.append(data.mainSlot)
    
    elif templateRecord.selector == TM_UNION:
        data = BigOpBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.attrib['align'] = 'center'
        operator = etree.Element('mo')
        operator.text = data.operator
        mathml.append(operator)
        mathml.append(data.upper)
        mathml.append(data.lower)
        mathmlElements.append(mathml)
        mathmlElements.append(data.mainSlot)
    
    elif templateRecord.selector == TM_INTER:
        data = BigOpBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.attrib['align'] = 'center'
        operator = etree.Element('mo')
        operator.text = data.operator
        mathml.append(operator)
        mathml.append(data.upper)
        mathml.append(data.lower)
        mathmlElements.append(mathml)
        mathmlElements.append(data.mainSlot)
    
    elif templateRecord.selector == TM_INTOP:
        pass
    
    elif templateRecord.selector == TM_SUMOP:
        pass
    
    elif templateRecord.selector == TM_LIM:
        data = LimBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.append(data.mainSlot)
        mathml.append(data.lower)
        mathml.append(data.upper)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_HBRACE:
        pass
    
    elif templateRecord.selector == TM_HBRACK:
        pass
    
    elif templateRecord.selector == TM_LDIV:
        pass
    
    elif templateRecord.selector == TM_SUB:
        data = ScrBoxClass(templateRecord)
        mathml = etree.Element('msub')
        base = etree.Element('stuff')
        convertRecords(0, [records[currentIndex - 1]], [base])
        removePrevious = 1
        base = base[0]
        mathml.append(base)
        mathml.append(data.subscript)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_SUP:
        data = ScrBoxClass(templateRecord)
        mathml = etree.Element('msup')
        base = etree.Element('stuff')
        convertRecords(0, [records[currentIndex - 1]], [base])
        removePrevious = 1
        base = base[0]
        mathml.append(base)
        mathml.append(data.superscript)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_SUBSUP:
        data = ScrBoxClass(templateRecord)
        mathml = etree.Element('msubsup')
        base = etree.Element('stuff')
        convertRecords(0, [records[currentIndex - 1]], [base])
        removePrevious = 1
        base = base[0]
        mathml.append(base)
        mathml.append(data.subscript)
        mathml.append(data.superscript)
        mathmlElements.append(mathml)
        
    elif templateRecord.selector == TM_DIRAC:
        pass
    
    elif templateRecord.selector == TM_VEC:
        pass
    
    elif templateRecord.selector == TM_TILDE:
        pass
    
    elif templateRecord.selector == TM_HAT:
        pass
    
    elif templateRecord.selector == TM_ARC:
        pass
    
    elif templateRecord.selector == TM_JSTATUS:
        pass
    
    elif templateRecord.selector == TM_STRIKE:
        data = StrikeBoxClass(templateRecord)
        mathml = etree.Element('menclose')
        mathml.append(data.mainSlot)
        mathml.set('notation', '')
        if _testVariation(templateRecord.variation, TV_ST_HORIZ):
            mathml.set('notation', 'horizontalstrike')
        if _testVariation(templateRecord.variation, TV_ST_UP):
            orig = mathml.get('notation')
            mathml.set('notation', orig + ' updiagonalstrike')
        if _testVariation(templateRecord.variation, TV_ST_DOWN):
            orig = mathml.get('notation')
            mathml.set('notation', orig + ' downdiagonalstrike')
        mathml.set('notation', mathml.get('notation').strip())
        mathmlElements.append(mathml)
            
    elif templateRecord.selector == TM_BOX:
        data = BoxBoxClass(templateRecord)
        # If all sides are present, treat this equation a little differently
        if (_testVariation(templateRecord.variation, TV_BX_LEFT) and 
            _testVariation(templateRecord.variation, TV_BX_RIGHT) and
            _testVariation(templateRecord.variation, TV_BX_TOP) and
            _testVariation(templateRecord.variation, TV_BX_BOTTOM)):
            mathml = etree.Element('mtable')
            mathml.set('frame', 'solid')
            mathml.append(data.mainSlot)
            mathmlElements.append(mathml)
        else:
            mathml = etree.Element('menclose')
            
            if _testVariation(templateRecord.variation, TV_BX_TOP) and _testVariation(templateRecord.variation, TV_BX_LEFT):
                mathml.set('notation', 'top left')
            elif _testVariation(templateRecord.variation, TV_BX_TOP) and _testVariation(templateRecord.variation, TV_BX_RIGHT):
                mathml.set('notation', 'actuarial')
            elif _testVariation(templateRecord.variation, TV_BX_BOTTOM) and _testVariation(templateRecord.variation, TV_BX_LEFT):
                mathml.set('notation', 'bottom left')
            elif _testVariation(templateRecord.variation, TV_BX_BOTTOM) and _testVariation(templateRecord.variation, TV_BX_RIGHT):
                mathml.set('notation', 'bottom right') 
            
            mathml.append(data.mainSlot)
            mathmlElements.append(mathml)
    
    return (mathmlElements, removePrevious)

def _testVariation(variationBits, variationConstant):
    return (variationBits & variationConstant) > 0

TV_AR_SINGLE = 0
TV_AR_DOUBLE = 1
TV_AR_HARPOON = 2
TV_AR_TOP = 4
TV_AR_BOTTOM = 8
TV_AR_LEFT = 16
TV_AR_RIGHT = 32
TV_AR_LOS = 16
TV_AR_SOL = 32
class ArrowBoxClass():
    def __init__(self, templateRecord):
        self.slot1 = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.slot1])
        self.slot1 = self.slot1[0]
        
        #i = 1
        
#         if _testVariation(templateRecord.variation, TV_AR_TOP) and _testVariation(templateRecord.variation, TV_AR_BOTTOM):
#             self.slot2 = etree.Element('mrow')
#             convertRecords(0, [templateRecord.childRecords[i]], [self.slot2])
#             self.slot2 = self.slot2[0]
#             i += 1
        self.slot2 = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[1]], [self.slot2])
        self.slot2 = self.slot2[0]
        
        self.arrow = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[2]], [self.arrow])
        self.arrow = self.arrow[0]

class BigOpBoxClass():
    def __init__(self, templateRecord):
        self.mainSlot = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.mainSlot])
        self.mainSlot = self.mainSlot[0]
        
        self.upper = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[1]], [self.upper])
        self.upper = self.upper[0]
        
        self.lower = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[2]], [self.lower])
        self.lower = self.lower[0]
        
        self.operator = unichr(templateRecord.childRecords[3].mtCode)

class DiracBoxClass():
    def __init__(self):
        pass

class FracBoxClass():
    def __init__(self, templateRecord):
        self.numerator = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.numerator])
        self.numerator = self.numerator[0]
        
        self.denominator = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[1]], [self.denominator])
        self.denominator = self.denominator[0] 

class HFenceBoxClass():
    def __init__(self):
        pass

class LDivBoxClass():
    def __init__(self):
        pass

class LimBoxClass():
    def __init__(self, templateRecord):
        self.mainSlot = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.mainSlot])
        self.mainSlot = self.mainSlot[0]
        
        self.lower = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[1]], [self.lower])
        self.lower = self.lower[0]
        
        self.upper = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[2]], [self.upper])
        self.upper = self.upper[0]

TV_FENCE_L = 1
TV_FENCE_R = 2
class ParBoxClass():
    def __init__(self, templateRecord, defaultLeft='(', defaultRight=')'):
        j = 0
        self.mainSlot = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[j]], [self.mainSlot])
        self.mainSlot = self.mainSlot[0]
        if _testVariation(templateRecord.variation, TV_FENCE_L):
            j += 1
            self.leftFence = unichr(templateRecord.childRecords[j].mtCode)
        else:
            self.leftFence = defaultLeft
            
        if _testVariation(templateRecord.variation, TV_FENCE_R):
            j += 1
            self.rightFence = unichr(templateRecord.childRecords[j].mtCode)
        else:
            self.rightFence = defaultRight

TV_ROOT_SQ = 0
TV_ROOT_NTH = 1
class RootBoxClass():
    def __init__(self, templateRecord):
        self.mainSlot = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.mainSlot])
        self.mainSlot = self.mainSlot[0]
        
        self.radicand = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[1]], [self.radicand])
        self.radicand = self.radicand[0]

TV_SU_PRECEDES = 1
class ScrBoxClass():
    def __init__(self, templateRecord):
        self.subscript = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.subscript])
        self.subscript = self.subscript[0]
        self.superscript = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[1]], [self.superscript])
        self.superscript = self.superscript[0]

TV_ST_HORIZ = 1
TV_ST_UP = 2
TV_ST_DOWN = 4
class StrikeBoxClass():
    def __init__(self, templateRecord):
        self.mainSlot = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.mainSlot])
        self.mainSlot = self.mainSlot[0]

TV_BX_ROUND = 1
TV_BX_LEFT = 2
TV_BX_RIGHT = 4
TV_BX_TOP = 8
TV_BX_BOTTOM = 16
class BoxBoxClass():
    def __init__(self, templateRecord):
        self.mainSlot = etree.Element('mrow')
        convertRecords(0, [templateRecord.childRecords[0]], [self.mainSlot])
        self.mainSlot = self.mainSlot[0]