'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''

import xml.etree.ElementTree as ET
import database
import replacer
from replacer import ReplaceTree
import re

class MathTTS():
    
    def __init__(self, initialDatabaseFile):
        
        # Load and generate the pattern trees
        databaseFile = open(initialDatabaseFile)
        contents = databaseFile.read()
        databaseFile.close()
        
        self.parserTree = database.parse(contents)
        
    def parse(self, mathmlString, stageSink=None):
        # Convert the MathML string to an XML DOM that I can parse
        root = ET.fromstring(mathmlString)
    
        speechTree = replacer.run(root, self.parserTree, stageSink=stageSink)
    
        print 'Generating speech...'
        speechList = self._generateSpeechFromTree(speechTree)
    
        myString = ''
        for s in speechList:
            myString += s
            myString += ' '
        
        return myString
    
    def setPatternDatabase(self, filePath):
        databaseFile = open(filePath)
        contents = databaseFile.read()
        databaseFile.close()
        
        self.parserTree = database.parse(contents)
        
    def _generateSpeechFromTree(self, tree):
        '''
        Generates the speech from a ReplaceTree. The only condition is that the root
        node MUST have a type of ReplaceTree.SPEECH. Returns a list containing each
        part of the speech.
        '''
        myString = []
        
        if isinstance(tree, ReplaceTree):
            
            if tree.type == ReplaceTree.SPEECH:
                # Divide up the components of its output
                components = re.split(r'(\{[0-9]+\})', tree.output)
                
                # Remove the empty ones
                i = 0
                while i < len(components):
                    if components[i] == '':
                        components.remove('')
                        i = 0
                    else:
                        i += 1
                        
                # Now let's do this!
                for c in components:
                    if c.find(r'{') != -1:
                        # Must generate speech from child object number refers to
                        num = int(c.replace('{', '').replace('}', '').strip()) - 1
                        myString.extend(self._generateSpeechFromTree(tree.expressions[num]))
                    else:
                        myString.append(c)
            else:
                myString.append('[ERROR]')
        
        else:
            # This would be a list of ReplaceTree's
            for t in tree:
                myString.extend(self._generateSpeechFromTree(t))
        
        return myString