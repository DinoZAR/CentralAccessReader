'''
Created on Jun 11, 2013

@author: Spencer Graffe
'''
import re

class DepthFirstIterator(object):
    
    def __init__(self, treeRoot, level=0):
        self._fringe = []
        self._fringe.append((treeRoot, level))
        self._last = None
        
    def next(self):
        
        data = self._fringe.pop()
        self._last = data
        
        myTree = data[0]
        level = data[1]
        
        # Add that tree's children to the _fringe, reverse order
        if len(myTree.children) > 0:
            for i in range(len(myTree.children)):
                index = len(myTree.children) - 1 - i
                self._fringe.append((myTree.children[index], level + 1))
                
        return data
    
    def jumpToParent(self):
        '''
        Moves the iterator up to the parent of the node that it returned last
        from next()
        '''
        level = self._last[1]
        while self._last[1] >= level:
            level = self._fringe.pop()[1]
        self._fringe.append(self._last)
        self._last = None
                
    def hasNext(self):
        return len(self._fringe) > 0

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
                regex = re.compile(self.value)
                if regex.match(other.value) != None:
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
            out += '   '
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
        
        if len(self.children) > 0:
            out += ' {'
            for c in self.children:
                out += '\n' + c.dump(indent + 1)
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