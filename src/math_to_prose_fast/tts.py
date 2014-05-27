'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''

import xml.etree.ElementTree as ET
from src.math_to_prose_fast import database_parser
from src.math_to_prose_fast import database
from src.math_to_prose_fast.parser import transform
from src.math_to_prose_fast.pattern_tree import convertDOMToPatternTree

class MathTTS():
    
    def __init__(self, mathLibrary=None):
        
        if mathLibrary is not None:
            # Load and generate the pattern trees
            databaseFile = open(mathLibrary)
            contents = databaseFile.read()
            databaseFile.close()
            
            self.parserTree = database_parser.parse(contents, mathLibrary)
        
    def parse(self, mathmlString, stageSink=None):
        root = ET.fromstring(mathmlString)
        mathTree = convertDOMToPatternTree(root)
                
        i = 0
        for p in self.parserTree['patterns']:
            i += 1
            pattern = database.convertToPatternTree(p)
            mathTree = transform(mathTree, pattern)
        
        myString = ' '.join(mathTree.getOutput())
        
        return myString
    
    def setMathLibrary(self, mathLib, patternName):
        self.parserTree = database_parser.parseMathLibrary(mathLib, patternName)