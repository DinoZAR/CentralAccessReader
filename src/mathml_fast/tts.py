'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''

import xml.etree.ElementTree as ET
import database_parser
import database
from parser import transform
from pattern_tree import convertDOMToPatternTree
import re
from src.profilehooks import profile

class MathTTS():
    
    def __init__(self, initialDatabaseFile):
        
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
        
        print 'My math string:', myString
        
        return myString
    
    def setPatternDatabase(self, filePath):
        databaseFile = open(filePath)
        contents = databaseFile.read()
        databaseFile.close()
        
        self.parserTree = database.parse(contents, filePath)