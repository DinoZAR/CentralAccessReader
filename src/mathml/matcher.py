'''
Created on Feb 10, 2013

@author: Spencer Graffe
'''
from mathml.replacer import DepthFirstIterator, ReplaceTree
import copy

def matchAndPrepare(tree, pattern, output):
    '''
    Finds matches in the tree based on the pattern and then prepares it for
    the replacer by injecting information into the replaced object of what it
    should have. Then, it will mark other elements that were part of the pattern
    for removal.
    
    Returns true or false depending on whether we have found matches.
    '''
    matchesList = []
    
    patternAccum = []
    variableAccum = []
    
    relativeDepth = 0
    gotRoot = False
    
    patternIterator = DepthFirstIterator(pattern)
    patternIterator.next()
    treeIterator = DepthFirstIterator(tree)
    
    currNode = None
    currExpr = None
    
    while treeIterator.hasNext():
        currNode = treeIterator.next()
        
        # Check if we have another expression to match. If we don't, then we
        # have matched the pattern.
        if patternIterator.hasNext():
            currExpr = patternIterator.next()
        else:
            # Matched the pattern
            matchesList.append((patternAccum, variableAccum))
            patternAccum = []
            variableAccum = []
            gotRoot = False
            patternIterator = _restartPattern(pattern)
            currExpr = patternIterator.next()
            
        if not gotRoot:
            # Look for the first instance of the pattern. If not found, then
            # restart the pattern iterator again.
            if currNode[0].isMatch(currExpr[0]):
                gotRoot = True
                relativeDepth = currNode[1] - currExpr[1]
                patternAccum.append(currNode[0])
                
                # When you accumulate to a variable, always create copy of first
                # one to prevent infinite recursion.
                if currExpr[0].type == ReplaceTree.SPEECH:
                    variableAccum.append(copy.copy(currNode[0]))
                elif currExpr[0].type == ReplaceTree.ANY:
                    variableAccum.append(copy.copy(currNode[0]))
                    treeIterator = _accumToNextSibling(treeIterator, patternAccum, currNode)[1]
                elif currExpr[0].type == ReplaceTree.ANY_PLUS:
                    treeIterator = _accumToParent(treeIterator, patternAccum, variableAccum, currNode)[1]
                elif currExpr[0].type == ReplaceTree.CATEGORY:
                    variableAccum.append(copy.copy(currNode[0]))
            else:
                patternIterator = _restartPattern(pattern)
                
        else:
            if currNode[0].isMatch(currExpr[0]) and ((currNode[1] - currExpr[1]) == relativeDepth):
                patternAccum.append(currNode[0])
                if currExpr[0].type == ReplaceTree.SPEECH:
                    variableAccum.append(currNode[0])
                elif currExpr[0].type == ReplaceTree.ANY:
                    variableAccum.append(currNode[0])
                    treeIterator = _accumToNextSibling(treeIterator, patternAccum, currNode)[1]
                elif currExpr[0].type == ReplaceTree.ANY_PLUS:
                    treeIterator = _accumToParent(treeIterator, patternAccum, variableAccum, currNode)[1]
                elif currExpr[0].type == ReplaceTree.CATEGORY:
                    variableAccum.append(currNode[0])
                
            else:
                gotRoot = False
                patternAccum = []
                variableAccum = []
                patternIterator = _restartPattern(pattern)
        
        # If neither of my iterators have anything next, and I am currently
        # trying to match something, say that I have got a match
        if not treeIterator.hasNext() and not patternIterator.hasNext() and gotRoot:
            matchesList.append((patternAccum, variableAccum))
                
    # Now that we have found all instances of the pattern, mark nodes for
    # replacement and removal
    for match in matchesList:
        pAccum = match[0]
        for i in range(len(pAccum)):
            # If we are at the first node, mark for replacement
            if i == 0:
                pAccum[i].mark = ReplaceTree.REPLACE
                pAccum[i].expressions = match[1]
                pAccum[i].replaceVariable = pattern.value
                pAccum[i].categories = pattern.categories
                pAccum[i].output = output
            else:
                pAccum[i].mark = ReplaceTree.REMOVE
                
    
    # Return whether we found matches or not
    return len(matchesList) > 0

def _restartPattern(parentNode):
    '''
    Restarts the pattern iterator back to the first position (directly after
    root)
    '''
    iterator = DepthFirstIterator(parentNode)
    iterator.next()
    return iterator

def _accumToNextSibling(iterator, pAccum, node):
    '''
    Accumulates and moves the iterator until it points to the next sibling.
    Returns the node that is right before this next sibling.
    '''
    level = node[1]
    prevNode = None
    nextNode = node

    while iterator.hasNext():
        prevNode = nextNode
        nextNode = iterator.next()
        if nextNode[1] <= level:
            iterator = DepthFirstIterator(prevNode[0], level=prevNode[1], rootResume=True)
            iterator.next()
            return (prevNode, iterator)
        else:
            pAccum.append(nextNode[0])
            
    return (prevNode, iterator)
        

def _accumToParent(iterator, pAccum, vAccum, node):
    '''
    Snags all of the current node's siblings and then 
    '''
    level = node[1] - 1
    
    # Add current node to accumulator and variables before I forget
    pAccum.append(node[0])
    
    myVAccum = []
    myVAccum.append(node[0])
    
    prevNode = node
    otherNode = prevNode
    while iterator.hasNext():
        prevNode = otherNode
        data = _accumToNextSibling(iterator, pAccum, otherNode)
        iterator = data[1]
        otherNode = data[0]
        
        if iterator.hasNext():
            otherNode = iterator.next()
            if otherNode[1] > level:
                pAccum.append(otherNode[0])
                myVAccum.append(otherNode[0])
            else:
                # Restart this iterator 
                iterator = DepthFirstIterator(prevNode[0], level=prevNode[1], rootResume=True)
                iterator.next()
                vAccum.append(myVAccum)
                return (prevNode, iterator)
    
    
    # Append to variable accumulator using my list of stuff
    vAccum.append(myVAccum)
    
    return (prevNode, iterator)
            