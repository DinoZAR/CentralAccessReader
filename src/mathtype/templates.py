'''
Created on May 29, 2013

Has the code necessary to successfully interpret the templates that are in
MathType.

@author: Spencer Graffe
'''
from lxml import etree
from records import *
from parser import convertRecords

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
        pass
        
    elif templateRecord.selector == TM_FLOOR:
        pass
    elif templateRecord.selector == TM_CEILING:
        pass
    elif templateRecord.selector == TM_OBRACK:
        pass
    elif templateRecord.selector == TM_INTERVAL:
        pass
    
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
        pass
    elif templateRecord.selector == TM_INTEG:
        pass
    
    elif templateRecord.selector == TM_SUM:
        data = BigOpBoxClass(templateRecord)
        mathml = etree.Element('munderover')
        mathml.attrib['align'] = 'center'
        operator = etree.Element('mo')
        operator.text = data.operator
        mathml.append(operator)
        mathml.append(data.lower)
        mathml.append(data.upper)
        mathmlElements.append(mathml)
        mathmlElements.append(data.mainSlot)
    
    elif templateRecord.selector == TM_PROD:
        pass
    elif templateRecord.selector == TM_COPROD:
        pass
    elif templateRecord.selector == TM_UNION:
        pass
    elif templateRecord.selector == TM_INTER:
        pass
    elif templateRecord.selector == TM_INTOP:
        pass
    elif templateRecord.selector == TM_SUMOP:
        pass
    elif templateRecord.selector == TM_LIM:
        pass
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
        pass
    elif templateRecord.selector == TM_BOX:
        pass
    
    return (mathmlElements, removePrevious)

def _testVariation(variationBits, variationConstant):
    return (variationBits & variationConstant) > 0

class ArroBoxClass():
    def __init__(self):
        pass

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
    def __init__(self):
        pass

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
        
class SlashBoxClass():
    def __init__(self):
        pass