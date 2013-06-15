def transform(tree, pattern):
    '''
    Transforms the tree with the pattern, converting all matched nodes to
    Variable objects representing that match.
    '''
    start = tree.getFirstChild()

    while start != None:
        
        if _testMatch(start, pattern):
            _matchTransform(start, pattern)

        start = start.getNext()

def _testMatch(startNode, pattern):
    '''
    Tests to see whether we got a match or not.
    '''
    curr = startNode
    for pat in pattern.getChildren():
        data = pat.accumulate(curr)
        if data == None:
            return False
        else:
            curr = data.newNext
        if curr == None:
            return False

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
        expressions.extend(data.expressions)

    # Morph the start node into a Variable node
    start.type = PatternTree.VARIABLE
    start.name = pattern.name
    start.categories = pattern.categories
    start.expressions = expressions
    start.output = pattern.output

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
