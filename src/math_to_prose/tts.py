'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''

import xml.etree.ElementTree as ET
import database
from parser import transform
from pattern_tree import convertDOMToPatternTree
import re
import misc

class MathTTS():
    
    def __init__(self, initialDatabaseFile=None):
        
        if initialDatabaseFile is not None:
            # Load and generate the pattern trees
            databaseFile = open(initialDatabaseFile, 'r')
            contents = databaseFile.read()
            databaseFile.close()
            
            self.parserTree = database.parse(contents, initialDatabaseFile)
        
    def parse(self, mathmlString):
        root = ET.fromstring(mathmlString)
        mathTree = convertDOMToPatternTree(root)
        
        for p in self.parserTree['patterns']:
            pattern = database.convertToPatternTree(p)
            mathTree = transform(mathTree, pattern)
        
        print 'Parsed math equation to:'
        misc.safeprint(mathTree.dump())
    
        myString = ' '.join(mathTree.getOutput())
        
        return myString
    
    def setPatternDatabase(self, filePath):
        databaseFile = open(filePath)
        contents = databaseFile.read()
        databaseFile.close()
        
        self.parserTree = database.parse(contents, filePath)