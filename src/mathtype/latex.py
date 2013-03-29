'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
from lxml import etree
import cStringIO

mathml_NS = 'http://www.w3.org/1998/Math/MathML'
NS_MAP = {None : mathml_NS}

def convertToMathML(latexString):
    '''
    Converts the LaTeX in the string to MathML.
    '''
    
    root = etree.Element('math', nsmap=NS_MAP)
    
    latexBuffer = cStringIO.StringIO(latexString)
    
    # Because LaTeX equations are typically done infix, and MathML represents
    # data in a sort of prefix way, I have to store the previous element
    prevElement = None
    
    # Start the whole reading procedure by reading it as a math
    _handleMath(prevElement, latexBuffer, root)
    
    return etree.tostring(root, pretty_print=True)


def _handleMath(prevElement, latexBuffer, root):
    '''
    Reads everything inside as if it were a part of the <math> element.
    '''
    
    c = latexBuffer.read(1)
    
    if c != None:
        if c == '{':
            # Start of a row
            prevElement = _handleRow(prevElement, latexBuffer, root)
            

def _handleRow(prevElement, latexBuffer, root):
    '''
    Reads everything inside it, treating it like a row
    '''
    
    row = etree.SubElement(root, 'mrow')
    
    while True:
        c = latexBuffer.read(1)
        if c == '}':
            # End of this row
            return row
        
    

# ------------------------------------------------------------------------------
# BACKSLASH DICTIONARY
#
# This dictionary stores all of the data concerning each of the elements that
# are backslashed in LaTeX. It has information on the element's type as well
# as how to represent it in MathML (which I will figure out in due time).
#
# ------------------------------------------------------------------------------
backslashDict = {

# Greek letters
'alpha' : '&#x03B1',
'beta' : '&#x03B2',
'gamma' : '&#x03B3',
'delta' : '&#x03B4',
'epsilon' : '&#x03B5',
'varepsilon' : '&#x025B',
'zeta' : '&#x03B6',
'eta' : '&#x03B7',
'theta' : '&#x03B8',
'iota' : '&#x03B9',
'kappa' : '&#x03BA',
'lambda' : '&#x03BB',
'mu' : '&#x03BC',
'nu' : '&#x03BD',
'xi' : '&#x03BE',
'pi' : '&#x03C0',
'varpi' : '&#x03D6',
'rho' : '&#x03C1',
'varrho' : '&#x03F1',
'varsigma' : '&#x03C2',
'sigma' : '&#x03C3',
'tau' : '&#x03C4',
'upsilon' : '&#x03C5',
'phi' : '&#x03C6',
'varphi' : '&#x03D5',
'chi' : '&#x03C7',
'psi' : '&#x03C8',
'omega' : '&#x03C9',
'Gamma' : '&#x0393',
'Delta' : '&#x0394',
'Theta' : '&#x0398',
'Lambda' : '&#x039B',
'Xi' : '&#x039E',
'Pi' : '&#x03A0',
'Sigma' : '&#x03A3',
'Upsilon' : '&#x03A5',
'Phi' : '&#x03A6',
'Psi' : '&#x03A8',
'Omega' : '&#x03A9'
}