'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''

import xml.etree.ElementTree as ET
import database
from parser import transform
from pattern_tree import convertDOMToPatternTree
import re

class MathTTS():
    
    def __init__(self, initialDatabaseFile):
        
        # Load and generate the pattern trees
        databaseFile = open(initialDatabaseFile)
        contents = databaseFile.read()
        databaseFile.close()
        
        self.parserTree = database.parse(contents, initialDatabaseFile)
        
    def parse(self, mathmlString, stageSink=None):
        root = ET.fromstring(mathmlString)
        mathTree = convertDOMToPatternTree(root)
        
        for p in self.parserTree['patterns']:
            pattern = database.convertToPatternTree(p)
            mathTree = transform(mathTree, pattern)
    
        print 'Math tree output:', mathTree.getOutput()
        myString = ' '.join(mathTree.getOutput())
        
        return myString
    
    def setPatternDatabase(self, filePath):
        databaseFile = open(filePath)
        contents = databaseFile.read()
        databaseFile.close()
        
        self.parserTree = database.parse(contents, filePath)