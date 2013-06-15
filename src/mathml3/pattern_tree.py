'''
Created on June 14, 2013

@author: Spencer Graffe
'''
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

        If there is a match, then it should return an object that has the
        following fields:
        
        .expressions  - the expressions that are a part of this pattern
        .newNext      - the node directly after the last expression in this
                        pattern
        '''
        accum = Accumulation()
        
        if self.type == PatternTree.VARIABLE:
            if self.isMatch(startNode) == startNode.type:
                accum.newNext = startNode.getNext(includeChildren=False)

        elif self.type == PatternTree.CATEGORY:
            if self.isMatch(startNode):
                accum.newNext = startNode.getNext(includeChildren=False)

        elif self.type == PatternTree.XML:
            if self.isMatch(startNode):
                curr = startNode.getFirstChild()
                if len(self.children) > 0:
                    for c in self.children:
                        data = c.accumulate(curr, mark)
                        if data == None:
                            return None
                        else:
                            accum.expressions.extend(data.expressions)
                            accum.newNext = data.newNext
                            curr = data.newNext
                        if curr == None:
                            return None
                else:
                    accum.newNext = startNode.getNext(includeChildren=False)

        elif self.type == PatternTree.TEXT:
            if self.isMatch(startNode):
                accum.newNext = startNode.getNext()

        elif self.type == PatternTree.WILDCARD:
            if self.name == '?':
                accum.expressions.append(startNode)
                accum.newNext
            if self.name == '+' or self.name == '#':
                accum.expressions.append(startNode)
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
                            accum.expressions.append(curr)
                else:
                    # Keep accumulating until we run out
                    curr = startNode
                    while True:
                        curr = curr.next
                        if curr == None:
                            break
                        accum.expressions.append(curr)

        if mark:
            for e in accum.expressions:
                e.marked = True

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

    def isMarked(self):
        return self.marked

    def disconnect(self):
        '''
        Essentially, it removes itself from existance from its parents and
        siblings. It will make connections around itself so that tree isn't
        broken.
        '''
        # Shun yourself away from parent
        self.parent.children.remove(self)
        self.parent = None

        # Make siblings previous and next of this connect (will work for
        # Nones too)
        self.previous.next = self.next
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
        
        return out

    def __str__(self):
        return self.dump()

    def __repr__(self):
        return str(self)

def Accumulation(object):
    '''
    Small object that holds the attributes of an accumulation.
    '''
    def __init__(self):
        self.expressions = []
        self.newNext = None

def convertDOMToPatternTree(elem, parent=None):
    
    name = elem.tag
    if '}' in elem.tag:
        name = elem.tag.split('}')[1]  # Remove the namespace
    
    myTree = PatternTree(name, parent)
    myTree.type = PatternTree.XML
    
    for child in elem:
        name = child.tag
        if '}' in child.tag:
            name = child.tag.split('}')[1]  # Remove the namespace
        newChild = PatternTree(name, myTree)
        newChild.type = PatternTree.XML
        
        # If there is text in the node, add it as the first child
        if child.text != None:
            if len(child.text.strip()) > 0:
                textNode = PatternTree(child.text.strip(), newChild)
                textNode.type = PatternTree.TEXT
                
        # Also process the children of those children
        if len(child) > 0:
            newChild = convertDOMToPatternTree(child, newChild)
        
    return myTree