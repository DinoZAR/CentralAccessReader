'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''
import re

import xml.etree.ElementTree as ET

import database
from parser import transform
from pattern_tree import convertDOMToPatternTree
from src import misc

class MathTTS():
    
    def __init__(self, mathLibrary=None):

        if mathLibrary is not None:
            # Load and generate the pattern trees
            databaseFile = open(mathLibrary)
            contents = databaseFile.read()
            databaseFile.close()

            self.parserTree = database.parse(contents, mathLibrary)

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
        self.parserTree = database.parseMathLibrary(mathLib, patternName)