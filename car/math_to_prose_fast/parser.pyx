'''
Created on Jul 17, 2013

@author: Spencer Graffe
'''
import copy
from car.math_to_prose_fast cimport pattern_tree

def transform(tree, pattern, gotMatchFlag=None):
    '''
    Transforms the tree with the pattern, converting all matched nodes to
    Variable objects representing that match.
    '''
    
    returnNode = tree
    start = tree
    
    while start != None:
        if _testMatch(start, pattern):
            
            # Report that a match was found
            if gotMatchFlag != None:
                gotMatchFlag[:] = [True]
            
            alreadyVisited = True
            
            start = _transformNode(start, pattern)
            if start.parent == None:
                # Update reference tree reference to the new, replaced node
                returnNode = start
        else:
            alreadyVisited = False
        
        start = start.getNext()
        
    return returnNode

def _testMatch(startNode, pattern):
    '''
    Tests to see whether we got a match or not.
    '''
    curr = startNode
    
    for pat in pattern.getChildren():
        
        # If there are no more nodes and we still have more things in pattern,
        # then it is not a match
        if curr == None:
            return False
        
        # Test the node and get the next element from the node
        data = pat.isMatch(curr)
        if not data.match:
            return False
        else:
            curr = data.next

    return True
    
cpdef pattern_tree.PatternTree _transformNode(pattern_tree.PatternTree start, pattern_tree.PatternTree pattern):
    '''
    Transforms the start node into a Variable that conveys the pattern. The
    other elements that were a part of the match are serialized as an expression
    list that is put into the new Variable
    '''
    cdef pattern_tree.GatherResult gatherData
    cdef pattern_tree.PatternTree newNode
    cdef pattern_tree.PatternTree curr
    
    curr = start
    nodes = []
    removes = []
    
    for pat in pattern.getChildren():
        gatherData = pat.gather(curr)
        nodes.extend(gatherData.extends)
        removes.extend(gatherData.removes)
        curr = gatherData.next
        
    # Create Variable node
    newNode = pattern_tree.PatternTree(pattern.name)
    newNode.type = pattern_tree.VARIABLE
    newNode.categories = pattern.categories
    newNode.output = pattern.output
    newNode.attributes = None
    newNode.children = []
    
    # Move the new children under the new node
    if start.parent != None:
        start.parent.insertBefore(newNode, start)
    start.disconnect()
    for n in nodes:
        newNode.addChild(n)
        
    # Remove the other nodes that were left over
    for r in removes:
        r.disconnect()
        
    return newNode