'''
Created on May 30, 2013

@author: Spencer Graffe
'''
from lxml import etree

# Constants
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

def embellishElement(mathmlElem, embellishValue):
    
    mathml = etree.Element('mo')
    mathml.text = '?'
    
    if embellishValue == EMB_1DOT:
        pass
    elif embellishValue == EMB_2DOT:
        pass
    elif embellishValue == EMB_3DOT:
        pass
    elif embellishValue == EMB_1PRIME:
        mathml = etree.Element('msup')
        emb = etree.SubElement(mathml, 'mo')
        emb.text = unichr(8242)
        mathml.append(mathmlElem)
    
    elif embellishValue == EMB_2PRIME:
        mathml = etree.Element('msup')
        emb = etree.SubElement(mathml, 'mo')
        emb.text = unichr(8243)
        mathml.append(mathmlElem)
    
    elif embellishValue == EMB_BPRIME:
        pass
    
    elif embellishValue == EMB_TILDE:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(732)
        mathml.append(emb)
        
    elif embellishValue == EMB_HAT:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(710)
        mathml.append(emb)
        
    elif embellishValue == EMB_NOT:
        pass
    
    elif embellishValue == EMB_RARROW:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(8594)
        mathml.append(emb)
        
    elif embellishValue == EMB_LARROW:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(8592)
        mathml.append(emb)
        
    elif embellishValue == EMB_BARROW:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(10231)
        mathml.append(emb)
        
    elif embellishValue == EMB_R1ARROW:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(8640)
        mathml.append(emb)
        
    elif embellishValue == EMB_L1ARROW:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(8636)
        mathml.append(emb)
        
    elif embellishValue == EMB_MBAR:
        pass
    
    elif embellishValue == EMB_OBAR:
        mathml = etree.Element('mover')
        mathml.append(mathmlElem)
        emb = etree.Element('mo')
        emb.text = unichr(175)
        mathml.append(emb)
    
    elif embellishValue == EMB_3PRIME:
        mathml = etree.Element('msup')
        emb = etree.SubElement(mathml, 'mo')
        emb.text = unichr(8244)
        mathml.append(mathmlElem)
        
    elif embellishValue == EMB_FROWN:
        pass
    elif embellishValue == EMB_SMILE:
        pass
    elif embellishValue == EMB_X_BARS:
        pass
    elif embellishValue == EMB_UP_BAR:
        pass
    elif embellishValue == EMB_DOWN_BAR:
        pass
    elif embellishValue == EMB_4DOT:
        pass
    elif embellishValue == EMB_U_1DOT:
        pass
    elif embellishValue == EMB_U_2DOT:
        pass
    elif embellishValue == EMB_U_3DOT:
        pass
    elif embellishValue == EMB_U_4DOT:
        pass
    elif embellishValue == EMB_U_BAR:
        mathml = etree.Element('munder')
        emb = etree.SubElement(mathml, 'mo')
        emb.text = '&#x332;'
        mathml.append(mathmlElem)
        
    elif embellishValue == EMB_U_TILDE:
        mathml = etree.Element('munder')
        emb = etree.SubElement(mathml, 'mo')
        emb.text = '~'
        mathml.append(mathmlElem)
        
    elif embellishValue == EMB_U_FROWN:
        pass
    elif embellishValue == EMB_U_SMILE:
        pass
    elif embellishValue == EMB_U_RARROW:
        pass
    elif embellishValue == EMB_U_LARROW:
        pass
    elif embellishValue == EMB_U_BARROW:
        pass
    elif embellishValue == EMB_U_R1ARROW:
        pass
    elif embellishValue == EMB_U_L1ARROW:
        pass
    
    return mathml