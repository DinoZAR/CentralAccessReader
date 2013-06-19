import copy
from pattern_tree import PatternTree

def transform(tree, pattern):
    '''
    Transforms the tree with the pattern, converting all matched nodes to
    Variable objects representing that match.
    '''
    start = tree

    while start != None:
        
        if _testMatch(start, pattern):
            print 'Got a match!'
            _transformNode(start, pattern)
            
        # If it has expressions in it, go and transform those too
#         if start.expressions != None:
#             for i in range(len(start.expressions)):
#                 for j in range(len(start.expressions[i][1])):
#                     if start.expressions[i][1][j].type == PatternTree.XML or start.expressions[i][1][j].type == PatternTree.TEXT:
#                         transform(start.expressions[i][1][j], pattern)

        start = start.getNext()

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
        next = pat.gather(curr)
        nodes.append(curr)
        curr.disconnect()
        curr = next

    # Create Variable node
    newNode = PatternTree(pattern.name)
    newNode.type = PatternTree.VARIABLE
    newNode.categories = pattern.categories
    newNode.output = pattern.output
    newNode.attributes = None
    newNode.children = []
    
    # Serialize my expressions found in the nodes
    expressions = []
    for n in nodes:
        expressions.extend(n.getExpressions())
    
    # Move the new children under the mutated node
    for ex in expressions:
        c = copy.deepcopy(ex) 
        c.disconnect()
        start.addChild(c)
