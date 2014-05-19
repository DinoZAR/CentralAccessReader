'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''

import xml.etree.ElementTree as ET
from math_to_prose_fast import database_parser
from math_to_prose_fast import database
from math_to_prose_fast.parser import transform
from math_to_prose_fast.pattern_tree import convertDOMToPatternTree

class MathTTS():
    
    def __init__(self, initialDatabaseFile=None):
        
        if initialDatabaseFile is not None:
            # Load and generate the pattern trees
            databaseFile = open(initialDatabaseFile)
            contents = databaseFile.read()
            databaseFile.close()
            
            self.parserTree = database_parser.parse(contents, initialDatabaseFile)
        
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
    
    def setPatternDatabase(self, filePath):
        databaseFile = open(filePath)
        contents = databaseFile.read()
        databaseFile.close()
        
        self.parserTree = database_parser.parse(contents, filePath)