'''
Created on Jun 11, 2013

@author: Spencer Graffe
'''
import copy
from pattern_tree import DepthFirstIterator, PatternTree

def markMatches(tree, pattern):
    '''
    Marks all of the matches it finds in the tree based on the pattern given.
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
        currNode = treeIterator.next()
        
        if patternIterator.hasNext():
            currExpr = patternIterator.next()
        else:
            # Match! I can say this because there is nothing left from the
            # pattern editor to match with
            matchesList.append((nodeAccum, expressionAccum))
            nodeAccum = []
            expressionAccum = []
            patternIterator = DepthFirstIterator(pattern)
            patternIterator.next()  # Skip the top element
            currExpr = patternIterator.next()
        
        if not gotRoot:
            
            # Search for the first instance of the pattern. Once I got
            # something, go accumulate the stuff
            
            if currNode[0].isMatch(currExpr[0]):
                gotRoot = True
                relativeDepth = currNode[1] - currExpr[1]
                nodeAccum.append(currNode[0])
                _accumulateVariable(treeIterator, currExpr, currNode, nodeAccum, expressionAccum)
            
            # Restart pattern
            else:
                patternIterator = DepthFirstIterator(pattern)
                patternIterator.next()
                gotRoot = False
                
        else:
            
            if currNode[0].isMatch(currExpr[0]) and ((currNode[1] - currExpr[1]) == relativeDepth):
                nodeAccum.append(currNode[0])
                _accumulateVariable(treeIterator, currExpr, currNode, nodeAccum, expressionAccum)
                
            # Restart pattern
            else:
                gotRoot = False
                nodeAccum = []
                expressionAccum = []
                patternIterator = DepthFirstIterator(pattern)
                patternIterator.next()
        
        # If both of my iterators have nothing next, and I'm currently resolving
        # a match, then indeed I have a match
        if not treeIterator.hasNext() and not patternIterator.hasNext() and gotRoot:
            matchesList.append((nodeAccum, expressionAccum))
            
    # Mark all of my nodes for replacement and removal
    _markNodes(matchesList, pattern)
    
    return len(matchesList) > 0
                
def _accumulateVariable(treeIterator, expression, node, nodeAccum, expressionAccum):
    if expression[0].type == PatternTree.VARIABLE:
        expressionAccum.append(('variable', copy.copy(node)))
    elif expression[0].type == PatternTree.CATEGORY:
        expressionAccum.append(('category', copy.copy(node)))
    elif expression[0].type == PatternTree.XML:
        pass
    elif expression[0].type == PatternTree.TEXT:
        pass
    elif expression[0].type == PatternTree.COLLECTOR:
        if expression[0].value == '?':
            expressionAccum.append(('?', copy.copy(node)))
            _accumulateToNextSibling(treeIterator, expression, nodeAccum)
        elif expression[0].value == '+':
            _accumulateToParent(treeIterator, expression[0].value, nodeAccum, expressionAccum)
        elif expression[0].value == '#':
            _accumulateToParent(treeIterator, expression[0].value, nodeAccum, expressionAccum)

def _accumulateToNextSibling(iterator, node, nodeAccum):
    # Add the first one for removal purposes, and then progress iterator until
    # it reaches right before the next sibling
    nodeAccum.append(node[0])
    
    siblingLevel = node[1]
    while iterator.hasNext():
        if iterator.peek()[1] > siblingLevel:
            iterator.next()
        else:
            break

def _accumulateToParent(iterator, value, node, nodeAccum, expressionAccum):
    # Accumulate each sibling as part of the expression. Then, each sibling also
    # gets accumulated in the nodes accumulator
    exprs = []
    exprs.append(node[0])
    
    sibling = node
    parentLevel = node[1] - 1
    while iterator.hasNext():
        _accumulateToNextSibling(iterator, sibling, nodeAccum)
        if iterator.peek()[1] > parentLevel:
            sibling = iterator.next()
            exprs.append(sibling[0])
        else:
            break
    
    expressionAccum.append((value, exprs))

def _markNodes(matchesList, pattern):
    for match in matchesList:
        nodeAccum = match[0]
        for i in range(len(nodeAccum)):
            if i == 0:
                nodeAccum[i].markReplace()
                nodeAccum[i].expressions = match[1]
                nodeAccum[i].categories = pattern.categories
                nodeAccum[i].output = pattern.output
            else:
                nodeAccum[i].markRemove()
                