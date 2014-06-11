'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''

from copy import deepcopy

import xml.etree.ElementTree as ET

from car.math_to_prose_fast import database_parser
from car.math_to_prose_fast import database
from car.math_to_prose_fast.parser import transform
from car.math_to_prose_fast.pattern_tree import convertDOMToPatternTree

class MathTTS():
    
    def __init__(self):
        self.parserTree = None
        
    def parse(self, mathmlString, stageSink=None):
        '''
        Parses the MathML into prose.

        stageSink is a list that can be appended to as the patterns are
        processed, providing a means to track and debug the algorithm. It will
        insert items of the following:
        [pattern, patternTree]

        pattern is set to None if it is the start
        '''
        root = ET.fromstring(mathmlString)
        mathTree = convertDOMToPatternTree(root)

        if stageSink is not None:
            stageSink.append([None, mathTree.copy()])

        i = 0
        for p in self.parserTree['patterns']:
            i += 1
            pattern = database.convertToPatternTree(p)
            gotMatch = [False]
            mathTree = transform(mathTree, pattern, gotMatchFlag=gotMatch)

            if stageSink is not None:
                if gotMatch[0]:
                    stageSink.append([pattern, mathTree.copy()])
        
        myString = ' '.join(mathTree.getOutput())
        
        return myString
    
    def setMathLibrary(self, mathLib, pattern):
        self.parserTree = database_parser.parseMathLibrary(mathLib, pattern.name)