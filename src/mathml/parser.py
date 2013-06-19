import copy
from pattern_tree import PatternTree

def transform(tree, pattern):
    '''
    Transforms the tree with the pattern, converting all matched nodes to
    Variable objects representing that match.
    '''
    
    returnNode = tree
    start = tree
    
    while start != None:
        
        
        if _testMatch(start, pattern):
            print 'Got a match!'
            alreadyVisited = True
            start = _transformNode(start, pattern)
            if start.parent == None:
                # Update reference tree reference to the new, replaced node
                returnNode = start
        else:
            alreadyVisited = False
            
        start = start.getNext()
        
        # If it has expressions in it, go and transform those too
#         if start.expressions != None:
#             for i in range(len(start.expressions)):
#                 for j in range(len(start.expressions[i][1])):
#                     if start.expressions[i][1][j].type == PatternTree.XML or start.expressions[i][1][j].type == PatternTree.TEXT:
#                         transform(start.expressions[i][1][j], pattern)

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
        if not data[0]:
            return False
        else:
            curr = data[1]

    return True
    
def _transformNode(start, pattern):
    '''
    Transforms the start node into a Variable that conveys the pattern. The
    other elements that were a part of the match are serialized as an expression
    list that is put into the new Variable
    '''
    curr = start
    nodes = []
    
    for pat in pattern.getChildren():
        data = pat.gather(curr)
        nodes.extend(data[1])
        curr = data[0]

    # Create Variable node
    newNode = PatternTree(pattern.name)
    newNode.type = PatternTree.VARIABLE
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
        
    return newNode
