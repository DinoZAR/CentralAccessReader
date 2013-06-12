'''
Created on Jun 11, 2013

@author: Spencer Graffe
'''
from pattern_tree import DepthFirstIterator, PatternTree

def markMatches(tree, pattern):
    '''
    Marks all of the matches it finds in the tree based on the pattern given. It
    will then 
    '''
    matchesList = []
    nodeAccum = []
    expressionAccum = []
    
    relativeDepth = 0
    gotRoot = False
    
    patternIterator = DepthFirstIterator(pattern)
    patternIterator.next()
    
    treeIterator = DepthFirstIterator(tree)
    
    currNode = None
    currExpr = None
    
    while treeIterator.hasNext():
        
        if patternIterator.hasNext():
            currExpr = patternIterator.next()
        else:
            # Match! I can say this because there is nothing left from the
            # pattern editor
            matchesList.append((nodeAccum, expressionAccum))
            nodeAccum = []
            expressionAccum = []
            patternIterator = DepthFirstIterator(pattern)
            patternIterator.next()  # Skip the top element
            currExpr = patternIterator.next()
        
        if not gotRoot:
            
            # Search for the first instance of the pattern. Once I got
            # something, go accumulate the stuff
            pass