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
            parent.addChild(self)
                
        # Data specific to the pattern
        self.type = nodeType
        self.name = name
        self.expressions = []
        self.attributes = {}
        self.categories = []
        self.output = ''
        
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
                expressions.append(startNode)
#                 accum = Accumulation(self)
#                 accum.newNext = startNode.getNext(includeChildren=False)
#                 expressions.append(Accumulation(startNode))
 
        elif self.type == PatternTree.CATEGORY:
            if self.isMatch(startNode):
                expressions.append(startNode)
#                 accum = Accumulation(self)
#                 accum.newNext = startNode.getNext(includeChildren=False)
#                 expressions.append(Accumulation(startNode))
 
        elif self.type == PatternTree.XML:
            if self.isMatch(startNode):
                expressions.append(startNode)
#                 curr = startNode.getFirstChild()
#                 #expressions.append(startNode)
#                 
#                 if len(self.children) > 0:
#                     for c in self.children:
#                         data = c.accumulate(curr, mark)
#                         if data == None:
#                             return None
#                         else:
#                             accum = Accumulation(self)
#                             accum.newNext = data.newNext
#                              
#                             # Check to see if type is not an XML or Text. If so,
#                             # add it to my additional list of expressions
#                             if data.expressions[0] != PatternTree.XML and data.expressions[0] != PatternTree.TEXT:
#                                 expressions.append(Accumulation(curr))
#                                  
#                             curr = data.newNext
#                              
#                 else:
#                     accum.newNext = startNode.getNext(includeChildren=False)
 
        elif self.type == PatternTree.TEXT:
            if self.isMatch(startNode):
                expressions.append(startNode)
#                 accum = Accumulation(self)
#                 accum.newNext = startNode.getNext()
#                 #expressions.append(startNode)
 
        elif self.type == PatternTree.WILDCARD:
            
            if self.name == '?':
                expressions.append(startNode)
# #                 accum = Accumulation(self)
# #                 accum.newNext = startNode.getNext()
# #                 expressions.append(Accumulation(startNode))
#                  
#             elif self.name == '+' or self.name == '#':
#                 accum = Accumulation(self)
#                 expressions.append(Accumulation(startNode))
#                 if self.next != None:
#                     # Keep accumulating until we match next expression
#                     curr = startNode
#                     gotOne = False
#                     while True:
#                         curr = curr.next
#                         if curr == None:
#                             # This isn't a match because the other pattern
#                             # didn't get matched yet
#                             return None
#                         if self.next.isMatch(curr):
#                             # If I didn't get at least one, then this is not a
#                             # match
#                             if not gotOne:
#                                 return None
#                             accum.newNext = curr.previous
#                             break
#                         else:
#                             gotOne = True
#                              
#                         expressions.append(Accumulation(startNode))
#                              
#                 else:
#                     # Keep accumulating until we run out
#                     curr = startNode
#                     while True:
#                         curr = curr.next
#                         if curr == None:
#                             break
         
#         for i in range(len(expressions)):
#             expressions[i].marked = True
         
#         if accum != None:
#             accum.expressions = (self.type, expressions)

        return accum
          
    def isExpression(self):
        if self.type == PatternTree.VARIABLE:
            return True
        elif self.type == PatternTree.CATEGORY:
            return True
        elif self.type == PatternTree.XML:
            return False
        elif self.type == PatternTree.TEXT:
            return True
        elif self.type == PatternTree.WILDCARD:
            return True
    
    def isMatch(self, other):
        '''
        Checks to see if this node, the pattern, matches other. If there is a
        match, it will return the next node to look for in the other pattern.
        Otherwise, it will return None.
        
        The next node will always be the next sibling of other.
        '''
        if self.type == PatternTree.VARIABLE:
            if self.type == other.type:
                return (True, other.next)

        elif self.type == PatternTree.CATEGORY:
            if self.name in other.categories:
                return (True, other.next)

        elif self.type == PatternTree.XML:
            if self.type == other.type:
                if self.name == other.name:
                    
                    # Check the attributes, if any. This is a subset match, not
                    # a whole match
                    if len(self.attributes) > 0:
                        for k in self.attributes.keys():
                            if k in other.attributes:
                                if self.attributes[k] != other.attributes[k]:
                                    return (False, None) 
                            else:
                                return (False, None)
                    
                    # Check all of the children and make sure they're good
                    if len(self.children) > 0:
                        currOther = other.getFirstChild()
                        currSelf = self.getFirstChild()
                        while True:
                            if currOther == None:
                                return (False, None)
                            data = currSelf.isMatch(currOther)
                            if not data[0]:
                                return (False, None)
                            currOther = data[1]
                            currSelf = currSelf.next
                            if currSelf == None:
                                
                                # If I have more stuff in other, then not match
                                if currOther != None:
                                    return (False, None)
                                else:
                                    return (True, other.next)
                        
                    else:
                        return (True, other.next)

        elif self.type == PatternTree.TEXT:
            if self.type == other.type:
                if self.name == other.name:
                    return (True, other.next)

        elif self.type == PatternTree.WILDCARD:
            
            if self.name == '?':
                return (True, other.next)
            
            # Keep going until the pattern after this matches. If there is no
            # pattern after this, then it is all of them. However, there must be
            # at least 1 node.
            elif self.name == '+' or self.name == '#':
                curr = other.next
                if curr == None:
                    return (False, None)
                while True:
                    if curr == None:
                        return (True, curr)
                    if self.next != None:
                        if self.next.isMatch(curr):
                            return (True, curr.previous)
                    curr = curr.next
                        
        return (False, None)

    def gather(self, other):
        '''
        Mutates the other so that it turns into a single expression representing
        itself. It may steal the other's siblings to collect the expressions
        necessary.
        '''
        if self.type == PatternTree.VARIABLE:
            # The other should stay the same, so leave it alone
            return other.next
        
        elif self.type == PatternTree.CATEGORY:
            # The other should stay the same, so leave it alone
            return other.next
        
        elif self.type == PatternTree.XML:
            return other.next
        
        elif self.type == PatternTree.TEXT:
            # The other should stay the same, so leave it alone
            return other.next
        
        elif self.type == PatternTree.WILDCARD:
            
            if self.name == '?':
                # Create a ? node in its place and put the replaced node
                # under it
                newNode = PatternTree('?')
                newNode.type = PatternTree.WILDCARD
                
                other.parent.insertBefore(newNode, other)
                newNode.addChild(other) # This will effectively move it
                
                return newNode.next
            
            elif self.name == '+' or self.name == '#':
                # Create a + or # node in its place, but this time, steal
                # siblings after other until the next pattern matches or until
                # all of them are taken
                newNode = PatternTree(self.name)
                self.copyData(newNode)
                
                other.parent.insertBefore(newNode, other)
                newNode.addChild(other) # This will effectively move it
                
                # Progressively take siblings after it and put it under itself
                current = newNode.next
                while True:
                    
                    if current == None:
                        break
                    
                    if self.next != None:
                        data = self.next.isMatch(current)
                        if data[0]:
                            break
                        
                    # Move it into the new node
                    newNode.addChild(current)
                        
                    current = newNode.next
                        
                return newNode.next
    
    def getChildren(self):
        return self.children

    def getFirstChild(self):
        if len(self.children) > 0:
            return self.children[0]
        else:
            return None
        
    def getExpressions(self):
        '''
        Gets a list of expressions that are from this tree. Depending on what
        kind of node it is, it will provide different expressions that count
        for it.
        
        Because some of the expressions may include itself, the nodes are not
        disconnected from their parents.
        '''
        if self.type == PatternTree.VARIABLE:
            expr
        elif self.type == PatternTree.CATEGORY:
            pass
        elif self.type == PatternTree.XML:
            pass
        elif self.type == PatternTree.TEXT:
            pass
        elif self.type == PatternTree.WILDCARD:
            pass
        
    def addChild(self, newNode):
        '''
        Adds a child to the tree. If the child was under a different parent, it
        will be removed from there and be moved under this node.
        '''
        self.insertChild(newNode, len(self.children))
            
    def insertChild(self, newNode, index = 0):
        '''
        Inserts a child into the tree. By default, it inserts it at the
        beginning.
        '''
        
        # Check if it is already in there. If it is, raise an error
        if newNode in self.children:
            raise ValueError('Child already exists in parent.')
        
        # Disconnect it to make sure it has renounced its previous life.
        # I have to do this so that I don't make copies and have ambiguous
        # parent references.
        newNode.disconnect()
        
        newNode.parent = self
        
        self.children.insert(index, newNode)
        if len(self.children) > 1:
            if index == 0:
                newNode.next = self.children[1]
                self.children[1].previous = newNode
            elif index == (len(self.children) - 1):
                newNode.previous = self.children[-2]
                self.children[-2].next = newNode
            else:
                newNode.previous = self.children[index - 1]
                newNode.next = self.children[index + 1]
                self.children[index - 1].next = newNode
                self.children[index + 1].previous = newNode
                
    def insertBefore(self, newNode, beforeNode):
        '''
        Inserts the new node before the child reference called beforeNode
        '''
        try:
            index = self.children.index(beforeNode)
        except Exception:
            raise ValueError('Before node does not exist.')
        
        self.insertChild(newNode, index)
        
    def getNext(self, includeChildren=True):
        '''
        Gets the next node after this in depth-first order. This means it
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
        Gets the speech output from this node.
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
        broken. It will keep its children references, though.
        '''
        # Shun yourself away from parent
        if self.parent != None:
            try:
                self.parent.children.remove(self)
            except ValueError:
                pass
            self.parent = None

        # Make siblings previous and next of this connect (will work for
        # Nones too)
        if self.previous != None:
            self.previous.next = self.next
        if self.next != None:
            self.next.previous = self.previous

        self.previous = None
        self.next = None
        
    def copyData(self, other):
        '''
        Copies all of the attributes of this node to the other node, mutating it
        to look like this node. The major difference is that the other node
        keeps its parent/children/sibling relationships.
        '''
        other.type = self.type
        other.name = self.name
        other.attributes = self.attributes
        other.categories = self.categories
        other.output = self.output
    
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
    
    def __repr__(self):
        return str(id(self)) + ': ' + self.dump()

class Accumulation(object):
    '''
    Small object that holds the attributes of an accumulation for a specific
    node.
    '''
    def __init__(self, pattern):
        self.pattern = pattern         # A reference to the PatternTree we are accumulating to
        self.expressions = []          # A list of expressions of Accumulation objects
        self.newNext = None            # A reference to the PatternTree after it

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
