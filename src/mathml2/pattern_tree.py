'''
Created on Jun 11, 2013

@author: Spencer Graffe
'''
import re

class DepthFirstIterator(object):
    
    def __init__(self, treeRoot, level=0):
        self._fringe = []
        self._fringe.append(_FringeRecord(treeRoot, level, None, 0))
        
        # Data to keep track of parent relationships
        self._last = None
        self._parents = []
        
    def next(self):
        '''
        Progresses the iterator forward, giving the following about it:
        (patternTreeNode, level)
        '''
        
        data = self._fringe.pop()
        self._last = data
        
        myTree = data.node
        level = data.level
        
        # Add that tree's children to the _fringe, reverse order
        if len(myTree.children) > 0:
            for i in range(len(myTree.children)):
                index = len(myTree.children) - 1 - i
                self._fringe.append(_FringeRecord(myTree.children[index], level + 1, data, index))
                
        return (data.node, data.level)
    
    def peek(self):
        '''
        Returns what next() would return, except that it does not progress the
        iterator. It returns the following:
        (patternTreeNode, level)
        
        It returns None if nothing is there.
        '''
        if len(self._fringe) > 0:
            stuff = self._fringe[-1]
            return (stuff.node, stuff.level)
        else:
            return None
    
    def jumpToParent(self):
        '''
        Moves the iterator up to the parent of the node that it returned last
        from next()
        '''
        # In order to do this, I have to somehow reconstruct the fringe and
        # states to make it look like I was starting from the parent I am
        # reporting next.
        parent = self._last.parentRecord
        if parent != None:
            grandparent = parent.parentRecord
            
            if grandparent != None:
                for i in range(len(grandparent.node.children)):
                    index = len(grandparent.node.children) - 1 - i
                    if index >= parent.childNumber:
                        self._fringe.append(_FringeRecord(grandparent.node.children[index], grandparent.level + 1, grandparent, index))
            
            self._fringe.append(parent)
        
#         level = self._last[1]
#         while level >= self._last[1]:
#             if len(self._fringe) > 0:
#                 level = self._fringe.pop()[1]
#             else:
#                 break
#         self._fringe.append(self._last)
        
                
    def hasNext(self):
        return len(self._fringe) > 0
    
class _FringeRecord(object):
    def __init__(self, node, level, parentRecord, childNumber):
        self.node = node
        self.level = level
        self.parentRecord = parentRecord
        self.childNumber = childNumber

class PatternTree(object):
    '''
    Used during the parsing process
    '''
    VARIABLE = 1
    CATEGORY = 2
    XML = 3
    TEXT = 4
    COLLECTOR = 5
    
    COLLECTOR_TOKENS = ['?', '+', '#']
    
    REPLACE = 2
    REMOVE = 4

    def __init__(self):
        '''
        Constructor
        '''
        self.value = ''
        self.type = PatternTree.TEXT
        self.categories = []
        self.children = []
        self.expressions = []
        
        # Info for replace/remove algorithm
        self._marks = 0
        self.output = ''
        
    def clearMarks(self):
        self._marks = 0
    
    def markReplace(self):
        self._marks = PatternTree.REPLACE
    
    def markRemove(self):
        self._marks = PatternTree.REMOVE
        
    def isMarkedReplace(self):
        return self._marks == PatternTree.REPLACE
        
    def isMarkedRemove(self):
        return self._marks == PatternTree.REMOVE
        
    def isVariable(self):
        return self.type == PatternTree.VARIABLE
        
    def isMatch(self, other):
        '''
        Returns true or false depending on whether this element matches the 
        other element.
        '''
        if self.type == PatternTree.VARIABLE:
            if other.type == PatternTree.VARIABLE and self.value == other.value:
                return True
            else:
                return False
            
        elif self.type == PatternTree.CATEGORY:
            if other.type == PatternTree.VARIABLE and (self.value in other.categories):
                return True
            else:
                return False
        
        elif self.type == PatternTree.XML:
            if other.type == PatternTree.XML and self.value == other.value:
                return True
            else:
                return False
        
        elif self.type == PatternTree.TEXT:
            if other.type == PatternTree.TEXT:
                if self.value == other.value:
                    return True
                else:
                    return False
            else:
                return False
        
        elif self.type == PatternTree.COLLECTOR:
            return True
        
        else:
            raise TypeError('The type number ' + str(self.type) + ' is not recognized. Use the PatternTree constants.')

    def _getTypeString(self):
        if self.type == PatternTree.VARIABLE:
            return 'Variable'
        elif self.type == PatternTree.CATEGORY:
            return 'Category'
        elif self.type == PatternTree.XML:
            return 'XML'
        elif self.type == PatternTree.TEXT:
            return 'Text'
        elif self.type == PatternTree.COLLECTOR:
            return 'Collector'
        
    def _createIndent(self, num):
        out = ''
        for i in range(num):
            out += '     '
        return out
    
    def dump(self, indent=0):
        '''
        Prints out some debug on this thing
        '''
        out = self._createIndent(indent) + self.value 
        out += ' (' + self._getTypeString() + ')'
        
        if len(self.categories) > 0:
            out += ' ['
            for c in self.categories:
                out += c + ', '
            out = out[:-2]  # Remove trailing comma
            out += ']'
            
        if len(self.output) > 0:
            out += ' -> ' + self.output
            
        if self.isMarkedReplace():
            out += ' <Replace>'
            
        if self.isMarkedRemove():
            out += ' <Remove>'
        
        if len(self.children) > 0:
            out += ' {'
            for c in self.children:
                out += '\n' + c.dump(indent + 1)
            out += '\n' + self._createIndent(indent) + '}'
            
        if len(self.expressions) > 0:
            out += '\n' + self._createIndent(indent) + 'Expressions: {'
            for ex in self.expressions:
                out += '\n' + self._createIndent(indent) + str(ex[0])
                for e in ex[1]:
                    out += '\n' + self._createIndent(indent) + '________________________'
                    out += '\n' + e.dump(indent)
            out += '\n' + self._createIndent(indent) + '}'
        
        return out
    
    def __str__(self):
        return self.dump()  

def domToPatternTree(elem):
    
    myTree = PatternTree()
    myTree.type = PatternTree.XML
    
    # Remove namespace from tag
    myTree.value = elem.tag.split('}')[1]
    
    for child in elem:
        
        newChild = PatternTree()
        newChild.value = child.tag.split('}')[1] # Remove namespace
        newChild.type = PatternTree.XML
        
        # If there is text in the node, add it as the first child
        if child.text != None:
            if len(child.text.strip()) > 0:
                textNode = PatternTree()
                textNode.type = PatternTree.TEXT
                textNode.value = child.text.strip()
                newChild.children.append(textNode)
                
        # Also process the children of those children
        if len(child) > 0:
            newChild = domToPatternTree(child)
            
        myTree.children.append(newChild)
        
    return myTree