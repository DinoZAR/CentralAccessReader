from pattern_tree import PatternTree

def transform(tree, pattern):
    '''
    Transforms the tree with the pattern, converting all matched nodes to
    Variable objects representing that match.
    '''
    start = tree

    while start != None:
        
        if _testMatch(start, pattern):
            _matchTransform(start, pattern)
            
        # If it has expressions in it, go and transform those too
        if start.expressions != None:
            for i in range(len(start.expressions)):
                for j in range(len(start.expressions[i][1])):
                    if start.expressions[i][1][j].type == PatternTree.XML or start.expressions[i][1][j].type == PatternTree.TEXT:
                        transform(start.expressions[i][1][j], pattern)

        start = start.getNext()

def _testMatch(startNode, pattern):
    '''
    Tests to see whether we got a match or not.
    '''
    curr = startNode
    
    for pat in pattern.getChildren():
        if curr == None:
            return False
        data = pat.accumulate(curr)
        if data == None:
            return False
        else:
            curr = data.newNext

    return True
    
def _matchTransform(start, pattern):
    '''
    Transforms the start node into a Variable that conveys the pattern. The
    other elements that were a part of the match are serialized as an expression
    list that is put into the new Variable
    '''
    curr = start
    expressions = []
    for pat in pattern.getChildren():
        data = pat.accumulate(curr, mark=True)
        curr = data.newNext
        expressions.append(data.expressions)

    # Morph the start node into a Variable node, keeping all
    # parent/sibling connections
    start.type = PatternTree.VARIABLE
    start.name = pattern.name
    start.categories = pattern.categories
    start.children = []
    start.expressions = expressions
    start.output = pattern.output
    start.attributes = None

    # Delete the nodes after it that were a part of the match
    # All of these have been marked, so it's just a matter of going through
    # and deleting them
    while True:
        node = start.getNext()
        if node == None:
            break
        if node.isMarked():
            node.disconnect()
        else:
            break
    
    return True
