'''
Created on May 29, 2013

Has the code necessary to successfully interpret the templates that are in
MathType.

@author: Spencer Graffe
'''

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

def getMathMLFromTemplate(templateRecord, i, records):
    
    if templateRecord.selector == TM_ANGLE:
        pass
    elif templateRecord.selector == TM_PAREN:
        pass
    elif templateRecord.selector == TM_BRACE:
        pass
    elif templateRecord.selector == TM_BRACK:
        pass
    elif templateRecord.selector == TM_BAR:
        pass
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
        pass
    elif templateRecord.selector == TM_FRACT:
        pass
    elif templateRecord.selector == TM_UBAR:
        pass
    elif templateRecord.selector == TM_OBAR:
        pass
    elif templateRecord.selector == TM_ARROW:
        pass
    elif templateRecord.selector == TM_INTEG:
        pass
    elif templateRecord.selector == TM_SUM:
        pass
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
        pass
    elif templateRecord.selector == TM_SUP:
        pass
    elif templateRecord.selector == TM_SUBSUP:
        pass
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

class ArroBoxClass():
    pass

class BigOpBoxClass():
    pass

class DiracBoxClass():
    pass

class FracBoxClass():
    pass

class HFenceBoxClass():
    pass

class LDivBoxClass():
    pass

class LimBoxClass():
    pass

class ParBoxClass():
    pass

class RootBoxClass():
    pass

class ScrBoxClass():
    pass

class SlashBoxClass():
    pass