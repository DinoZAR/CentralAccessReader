'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
from mathtype import parser, latex

if __name__ == '__main__':
    
    # Let's test out the Mathtype library
    testPath = 'mathtype/image40.wmf'
    test = open(testPath, 'rb')
    
    stuff = parser.parseWMF(test)
    
    test.close()
    
    print 'Done!'