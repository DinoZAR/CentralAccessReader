'''
Created on Jun 11, 2013

@author: Spencer Graffe
'''
from pattern_tree import PatternTree, DepthFirstIterator

def replaceAndRemove(tree, variableValue, output):
    '''
    Searches through the whole tree and replaces the nodes marked for
    replacement and deletes the nodes marked for removal. It will also do this
    inside of the expressions for the speech objects.
    '''
    
    # Do main tree first
    _searchAndReplace(tree, variableValue, output)
    
    # Do all of the expressions for the variable objects
    iter = DepthFirstIterator(tree)
     
    while iter.hasNext():
        elem = iter.next()[0]
        if elem.isVariable():
            replaceAndRemove(elem, variableValue, output)
            

def _searchAndReplace(tree, variableValue, output):
    '''
    Searches and replaces or removes nodes in the current tree that have been
    previously marked as such.
    '''
    
    iter = DepthFirstIterator(tree)
    
    while iter.hasNext():
        data = iter.next()
        node = data[0]
        level = data[1]
        
        if node.isMarkedReplace():
            
            # Get parent
            iter.jumpToParent()
            parent = iter.next()[0]
            
            # Do replacement
            for i in range(len(parent.children)):
                if parent.children[i].isMarkedReplace():
                    
                    # Make new node to insert in its place
                    newNode = PatternTree()
                    newNode.type = PatternTree.VARIABLE
                    newNode.value = variableValue
                    newNode.output = output
                    newNode.expressions = parent.children[i].expressions
                    
                    # Replace
                    parent.children.pop(i)
                    parent.children.insert(i, newNode)
                    
            # Restart iterator
            iter = DepthFirstIterator(tree)
        
        elif node.isMarkedRemove():
            
            # Get parent
            iter.jumpToParent()
            parent = iter.next()[0]
            
            # Remove element
            for i in range(len(parent.children)):
                if parent.children[i].isMarkedRemove():
                    parent.children.pop(i)
                    break
            
            # Start iterator over from parent
            iter = DepthFirstIterator(tree)