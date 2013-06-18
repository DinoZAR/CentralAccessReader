'''
Created on June 14, 2013

@author: Spencer Graffe
'''
import re
import copy

class PatternTree(object):

    VARIABLE = 1
    CATEGORY = 2
    XML = 3
    TEXT = 4
    WILDCARD = 5
    
    WILDCARD_TOKENS = ['?', '+', '#']
    
    def __init__(self, name, parent=None, nodeType=3):
        
        # Data general to the tree structure
        self.previous = None
        self.next = None
        self.children = []
        self.parent = parent

        # Update other nodes correctly if a parent was said
        if parent != None:
            if len(parent.children) > 0:
                self.previous = parent.children[-1]
                parent.children[-1].next = self
            parent.children.append(self)
                
        # Data specific to the pattern
        self.type = nodeType
        self.name = name
        self.attributes = None
        self.categories = []
        self.expressions = None    # Reserve this only for Variable types
        self.output = ''
        self.marked = False

    def accumulate(self, startNode, mark=False):
        '''
        Accumulates nodes into an expression list that become a part of this
        pattern. If it can't because it is not a match, it should return None.

        If there is a match, then it should return an Accumulation object.
        '''
        accum = None
        expressions = []
        
        if self.type == PatternTree.VARIABLE:
            if self.isMatch(startNode) == startNode.type:
                accum = Accumulation(self)
                accum.newNext = startNode.getNext(includeChildren=False)
                expressions.append(startNode)
 
        elif self.type == PatternTree.CATEGORY:
            if self.isMatch(startNode):
                accum = Accumulation(self)
                accum.newNext = startNode.getNext(includeChildren=False)
                expressions.append(startNode)
 
        elif self.type == PatternTree.XML:
            if self.isMatch(startNode):
                curr = startNode.getFirstChild()
                #expressions.append(startNode)
                
                if len(self.children) > 0:
                    for c in self.children:
                        data = c.accumulate(curr, mark)
                        if data == None:
                            return None
                        else:
                            accum = Accumulation(self)
                            accum.newNext = data.newNext
                            
                            # Check to see if type is not an XML or Text. If so,
                            # add it to my additional list of expressions
                            if data.expressions[0] != PatternTree.XML and data.expressions[0] != PatternTree.TEXT:
                                expressions.append(curr)
                                
                            curr = data.newNext
                            
                else:
                    accum.newNext = startNode.getNext(includeChildren=False)
 
        elif self.type == PatternTree.TEXT:
            if self.isMatch(startNode):
                accum = Accumulation(self)
                accum.newNext = startNode.getNext()
                #expressions.append(startNode)
 
        elif self.type == PatternTree.WILDCARD:
            
            if self.name == '?':
                accum = Accumulation(self)
                accum.newNext = startNode.getNext()
                expressions.append(startNode)
                
            elif self.name == '+' or self.name == '#':
                accum = Accumulation(self)
                expressions.append(startNode)
                if self.next != None:
                    # Keep accumulating until we match next expression
                    curr = startNode
                    gotOne = False
                    while True:
                        curr = curr.next
                        if curr == None:
                            # This isn't a match because the other pattern
                            # didn't get matched yet
                            return None
                        if self.next.isMatch(curr):
                            # If I didn't get at least one, then this is not a
                            # match
                            if not gotOne:
                                return None
                            accum.newNext = curr.previous
                            break
                        else:
                            gotOne = True
                            
                        expressions.append(startNode)
                            
                else:
                    # Keep accumulating until we run out
                    curr = startNode
                    while True:
                        curr = curr.next
                        if curr == None:
                            break
        
        for i in range(len(expressions)):
            removal = expressions[i]
            expressions[i] = copy.deepcopy(expressions[i])
            if mark:
                expressions[i].marked = True
                expressions[i].disconnect()
                removal.disconnect()
        
        if accum != None:
            accum.expressions = (self.type, expressions)

        return accum

    def isMatch(self, other):
        if self.type == PatternTree.VARIABLE:
            if self.type == other.type:
                return True

        elif self.type == PatternTree.CATEGORY:
            if self.name in other.categories:
                return True

        elif self.type == PatternTree.XML:
            if self.type == other.type:
                if self.name == other.name:
                    if len(self.attributes) > 0:
                        for k in self.attributes.keys():
                            if k in other.attributes:
                                if self.attributes[k] != other.attributes[k]:
                                    return False
                            else:
                                return False
                        return True
                    else:
                        return True

        elif self.type == PatternTree.TEXT:
            if self.type == other.type:
                if self.name == other.name:
                    return True

        elif self.type == PatternTree.WILDCARD:
            return True

        return False

    def getChildren(self):
        return self.children

    def getFirstChild(self):
        if len(self.children) > 0:
            return self.children[0]
        else:
            return None

    def getNext(self, includeChildren=True):
        '''
        Gets the next element after this in depth-first order. This means it
        will return the first child of this first, unless includeChildren is
        False.
        '''
        if includeChildren:
            if len(self.children) > 0:
                return self.children[0]

        if self.next != None:
            return self.next

        if self.parent != None:
            return self.parent.getNext(includeChildren=False)

        return None
    
    def getOutput(self):
        '''
        Gets the speech output from this element.
        '''
        out = ''
        
        if self.type == PatternTree.VARIABLE:
            # This one is fun. Get a list of all of the expression indices to
            # replace with
            expressionIndices = re.split(r'(\{[0-9]+\})', self.output)
            
            # Remove the empty ones
            i = 0
            while i < len(expressionIndices):
                if expressionIndices[i] == '':
                    expressionIndices.remove('')
                    i = 0
                else:
                    i += 1
                    
            # Now let's do this!
            for c in expressionIndices:
                if c.find(r'{') != -1:
                    # Must generate speech from child object number refers to
                    num = int(c.replace('{', '').replace('}', '').strip()) - 1
                    type = self.expressions[num][0]
                    for ex in self.expressions[num][1]:
                        out += ' ' + ex.getOutput()
                else:
                    out += ' ' + c
            
        elif self.type == PatternTree.CATEGORY:
            out += ' [ERROR]'
            
        elif self.type == PatternTree.XML:
            out += ' [ERROR]'
            
        elif self.type == PatternTree.TEXT:
            out += ' ' + self.name
            
        elif self.type == PatternTree.WILDCARD:
            out += ' [ERROR]'
        
        else:
            raise TypeError('PatternTree type not recognized: ' + str(self.type))
        
        return out

    def isMarked(self):
        return self.marked

    def disconnect(self):
        '''
        Essentially, it removes itself from existence from its parents and
        siblings. It will make connections around itself so that tree isn't
        broken. It will keep its children references.
        '''
        # Shun yourself away from parent
        if self.parent != None:
            self.parent.children.remove(self)
            self.parent = None

        # Make siblings previous and next of this connect (will work for
        # Nones too)
        if self.previous != None:
            self.previous.next = self.next
        if self.next != None:
            self.next.previous = self.previous

        self.previous = None
        self.next = None
        
    def _getTypeString(self):
        if self.type == PatternTree.VARIABLE:
            return 'Variable'
        elif self.type == PatternTree.CATEGORY:
            return 'Category'
        elif self.type == PatternTree.XML:
            return 'XML'
        elif self.type == PatternTree.TEXT:
            return 'Text'
        elif self.type == PatternTree.WILDCARD:
            return 'WILDCARD'
        
    def _createIndent(self, num):
        out = ''
        for i in range(num):
            out += '     '
        return out

    def dump(self, indent=0):
        '''
        Prints out some debug on this thing
        '''
        out = self._createIndent(indent) + self.name
        out += ' (' + self._getTypeString() + ')'
        
        if self.attributes != None:
            if len(self.attributes.keys()) > 0:
                out += ' <'
                for a in self.attributes.keys():
                    out += a + ' = \"' + self.attributes[a] + '\", '
                out = out[:-2] 
                out += '>'
        
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

#         if self.expressions != None:            
#             if len(self.expressions) > 0:
#                 out += '\n' + self._createIndent(indent) + '-- Expressions'
#                 for i in range(len(self.expressions)):
#                     out += '\n' + self._createIndent(indent) + str(i + 1) + ': ' + self.expressions[i].dump(indent + 1)[len(self._createIndent(indent)):]
#                 out += '\n' + self._createIndent(indent) + '--'
            
        return out

    def __str__(self):
        return self.dump()

class Accumulation(object):
    '''
    Small object that holds the attributes of an accumulation for a specific
    element.
    '''
    def __init__(self, pattern):
        self.pattern = pattern         # A reference to the PatternTree we are accumulating to
        self.expressions = []       # A list of expressions that are for that type
        self.newNext = None         # A reference to the PatternTree after it

def convertDOMToPatternTree(elem, parent=None):
    
    name = elem.tag
    if '}' in elem.tag:
        name = elem.tag.split('}')[1]  # Remove the namespace
    
    myTree = PatternTree(name, parent)
    myTree.type = PatternTree.XML
    
    # Add in the attributes
    myTree.attributes = {}
    for k in elem.attrib.keys():
        myTree.attributes[k] = elem.get(k)
        
    # If there is text in the node, add it as the first child
    if elem.text != None:
        if len(elem.text.strip()) > 0:
            textNode = PatternTree(elem.text.strip(), myTree)
            textNode.type = PatternTree.TEXT

    # Convert all children            
    for child in elem:
        convertDOMToPatternTree(child, myTree)
        
    return myTree