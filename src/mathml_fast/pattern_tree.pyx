'''
Created on Jul 17, 2013

Same PatternTree structure and everything as before, but faster.

@author: Spencer Graffe
'''
import re

WILDCARD_TOKENS = ['?', '+', '#']
    
cdef class MatchResult:
    def __init__(self, isMatch, nextNode):
        self.match = isMatch
        self.next = nextNode
        
cdef class GatherResult:
    def __init__(self, next, extendList, removeList):
        self.next = next
        self.extends = extendList
        self.removes = removeList

cdef class PatternTree:
    def __init__(self, name, parent=None, nodeType=XML):
        
        self.previous = None
        self.next = None
        self.parent = parent
        self.children = []
        
        # Update other nodes correctly if a parent was said
        if parent != None:
            parent.addChild(self)
        
        self.type = nodeType
        self.name = unicode(name)
        self.attributes = {}
        self.categories = []
        self.output = u''
        
    cpdef int isExpressions(self):
        if self.type == VARIABLE:
            return True
        elif self.type == CATEGORY:
            return True
        elif self.type == XML:
            return False
        elif self.type == TEXT:
            return True
        elif self.type == WILDCARD:
            return True
            
    cpdef MatchResult isMatch(self, PatternTree other):
        '''
        Checks to see if this node, the pattern, matches other. If there is a
        match, it will return the next node to look for in the other pattern.
        Otherwise, it will return None.
        
        The next node will always be the next sibling of other.
        '''
        cdef int parentIsVisible
        cdef MatchResult matchData
        cdef PatternTree currSelf
        cdef PatternTree currOther
        cdef PatternTree curr
        
        # See if the parent is a Variable. If it is, only allow matches for XML,
        # since those nodes will need to be reparsed
        parentIsVariable = False
        if other.parent != None:
            if other.parent.type == VARIABLE:
                parentIsVariable = True
        
        # Do the test for whatever type this is
        if self.type == VARIABLE:
            if parentIsVariable:
                return MatchResult(False, None)
            if self.type == other.type:
                if self.name == other.name:
                    return MatchResult(True, other.next)
                else:
                    return MatchResult(False, other.next)

        elif self.type == CATEGORY:
            if parentIsVariable:
                return MatchResult(False, None)
            if self.name in other.categories:
                return MatchResult(True, other.next)

        elif self.type == XML:
            if self.type == other.type:
                if self.name == other.name:
                    
                    # Check the attributes, if any. This is a subset match, not
                    # a whole match
                    if len(self.attributes) > 0:
                        for k in self.attributes.keys():
                            if k in other.attributes:
                                if self.attributes[k] != other.attributes[k]:
                                    return MatchResult(False, None) 
                            else:
                                return MatchResult(False, None)
                    
                    # Check all of the children and make sure they're good
                    if len(self.children) > 0:
                        currOther = other.getFirstChild()
                        currSelf = self.getFirstChild()
                        while True:
                            if currOther == None:
                                return MatchResult(False, None)
                            matchData = currSelf.isMatch(currOther)
                            if not matchData.match:
                                return MatchResult(False, None)
                            currOther = matchData.next
                            currSelf = currSelf.next
                            if currSelf == None:
                                # If I have more stuff in other, then not match
                                if currOther != None:
                                    return MatchResult(False, None)
                                else:
                                    return MatchResult(True, other.next)
                        
                    else:
                        if len(other.children) > 0:
                            return MatchResult(False, None)
                        else:
                            return MatchResult(True, other.next)

        elif self.type == TEXT:
            if parentIsVariable:
                return MatchResult(False, None)
            if self.type == other.type:
                if self.name == other.name:
                    return MatchResult(True, other.next)

        elif self.type == WILDCARD:
            if parentIsVariable:
                return MatchResult(False, None)
            if self.name == '?':
                return MatchResult(True, other.next)
            
            # Keep going until the pattern after this matches. If there is no
            # pattern after this, then it is all of them. However, there must be
            # at least 1 node.
            elif self.name == '+' or self.name == '#':
                if other == None:
                    return MatchResult(False, None)
                curr = other.next
                while True:
                    if curr == None:
                        return MatchResult(True, curr)
                    if self.next != None:
                        if self.next.isMatch(curr).match:
                            return MatchResult(True, curr)
                    curr = curr.next
                        
        return MatchResult(False, None)
        
    cpdef GatherResult gather(self, PatternTree other):
        '''
        Mutates the other so that it turns into a single expression representing
        itself. It may steal the other's siblings to collect the expressions
        necessary.
        '''
        cdef GatherResult gatherData
        cdef MatchResult matchData
        cdef PatternTree curr
        cdef PatternTree newNode
        
        if self.type == VARIABLE:
            # The other should stay the same, so leave it alone
            return GatherResult(other.next, [other], [])
        
        elif self.type == CATEGORY:
            # The other should stay the same, so leave it alone
            return GatherResult(other.next, [other], [])
        
        elif self.type == XML:
            # Gather the stuff inside it
            curr = other.getFirstChild()
            nodes = []
            removes = []
            for c in self.children:
                gatherData = c.gather(curr)
                nodes.extend(gatherData.extends)
                removes.extend(gatherData.removes)
                curr = gatherData.next
            
            removes.extend([other])
            return GatherResult(other.next, nodes, removes)
        
        elif self.type == TEXT:
            # The other should stay the same, so leave it alone
            return GatherResult(other.next, [other], [])
        
        elif self.type == WILDCARD:
            if self.name == u'?':
                # Create a ? node in its place and put the replaced node
                # under it
                newNode = PatternTree(u'?')
                newNode.type = WILDCARD
                
                other.parent.insertBefore(newNode, other)
                newNode.addChild(other) # This will effectively move it
                
                return GatherResult(newNode.next, [newNode], [])
            
            elif self.name == u'+' or self.name == u'#':
                # Create a + or # node in its place, but this time, steal
                # siblings after other until the next pattern matches or until
                # all of them are taken
                newNode = PatternTree(self.name)
                self.copyData(newNode)
                
                other.parent.insertBefore(newNode, other)
                newNode.addChild(other) # This will effectively move it
                
                # Progressively take siblings after it and put it under itself
                curr = newNode.next
                while True:
                    
                    if not isinstance(curr, PatternTree):
                        break
                    
                    if self.next is not None:
                        matchData = self.next.isMatch(curr)
                        if matchData.match:
                            break
                        
                    # Move it into the new node
                    newNode.addChild(curr)
                    curr = newNode.next
                    
                return GatherResult(newNode.next, [newNode], [])
                
    cpdef list getChildren(self):
        return self.children
        
    cpdef PatternTree getFirstChild(self):
        if len(self.children) > 0:
            return self.children[0]
        else:
            return None
            
    cpdef list getExpressions(self):
        '''
        Gets a list of expressions that are from this tree. Depending on what
        kind of node it is, it will provide different expressions that count
        for it.
        
        Because some of the expressions may include itself, the nodes are not
        disconnected from their parents.
        '''
        if self.type == VARIABLE:
            return [self]
        
        elif self.type == CATEGORY:
            return [] # It doesn't make sense to have anything here
        
        elif self.type == XML:
            exprs = []
            for c in self.children:
                exprs.extend(c.getExpressions())
            return exprs
        
        elif self.type == TEXT:
            return [self]
        
        elif self.type == WILDCARD:
            return [self]
            
    cpdef object addChild(self, PatternTree newNode):
        '''
        Adds a child to the tree. If the child was under a different parent, it
        will be removed from there and be moved under this node.
        '''
        self.insertChild(newNode, len(self.children))
        return None
        
    cpdef object insertChild(self, PatternTree newNode, int index):
        '''
        Inserts a child into the tree. By default, it inserts it at the
        beginning.
        '''
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
        
        return None        
        
    cpdef object insertBefore(self, PatternTree newNode, PatternTree beforeNode):
        '''
        Inserts the new node before the child reference called beforeNode
        '''
        index = self.children.index(beforeNode)
        self.insertChild(newNode, index)
        return None
        
    cpdef PatternTree getNext(self, int includeChildren=True):
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
        
    cpdef unicode getOutput(self):
        '''
        Gets the speech output from this node.
        '''
        cdef unicode out
        cdef int i
        cdef int num
        
        out = u''
        if self.type == VARIABLE:
            # This one is fun. Get a list of all of the expression indices to
            # replace with
            expressionIndices = re.split(r'(\{[0-9]+\})', self.output)
            
            # Remove the empty ones
            i = 0
            while i < len(expressionIndices):
                if expressionIndices[i] == u'':
                    expressionIndices.remove(u'')
                    i = 0
                else:
                    i += 1
                    
            # Now let's do this!
            for c in expressionIndices:
                if c.find(r'{') != -1:
                    # Must generate speech from child object number refers to
                    num = int(c.replace(u'{', u'').replace(u'}', u'').strip()) - 1
                    out += self.children[num].getOutput()
                else:
                    out += c
            
        elif self.type == CATEGORY:
            for c in self.children:
                out += c.getOutput()
            
        elif self.type == XML:
            out += u'[ERROR]'
            
        elif self.type == TEXT:
            out += self.name
            
        elif self.type == WILDCARD:
            
            if self.name == u'?':
                out += self.getFirstChild().getOutput()
            
            elif self.name == u'+':
                for c in self.children:
                    out += c.getOutput() + ' '
                out = out[:-1]
                
            elif self.name == u'#':
                # Make output numbered
                for index in range(len(self.children)):
                    out += u', ' + unicode(index + 1) + u', ' + self.children[index].getOutput() + u' '
                out = out[:-1]
        
        return out
        
    cpdef object disconnect(self):
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
        
        return None
        
    cpdef object copyData(self, PatternTree other):
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
        
        return None
        
    cdef unicode _getTypeString(self):
        if self.type == VARIABLE:
            return u'Variable'
        elif self.type == CATEGORY:
            return u'Category'
        elif self.type == XML:
            return u'XML'
        elif self.type == TEXT:
            return u'Text'
        elif self.type == WILDCARD:
            return u'Wildcard'
        
    cdef unicode _createIndent(self, int num):
        cdef unicode out
        cdef int i
        out = u''
        i = 0
        while i < num:
            out += u'    '
            i += 1
        
        return out
        
    cpdef unicode dump(self, int indent=0):
        '''
        Prints out some debug on this thing
        '''
        cdef unicode out
        
        out = self._createIndent(indent) + self.name
        out += u' (' + self._getTypeString() + u')'
        
        if self.attributes != None:
            if len(self.attributes.keys()) > 0:
                out += u' <'
                for a in self.attributes.keys():
                    out += a + u' = \"' + self.attributes[a] + u'\", '
                out = out[:-2] 
                out += u'>'
        
        if len(self.categories) > 0:
            out += u' ['
            for c in self.categories:
                out += c + u', '
            out = out[:-2]  # Remove trailing comma
            out += u']'
        
        if len(self.output) > 0:
            out += u' -> ' + self.output
        
        if len(self.children) > 0:
            out += u' {'
            for c in self.children:
                out += u'\n' + c.dump(indent + 1)
            out += u'\n' + self._createIndent(indent) + u'}'
            
        return out
        
    def __str__(self):
        return self.dump()
    
    def __unicode__(self):
        return self.dump()
    
    def __repr__(self):
        return str(id(self)) + ': ' + self.dump()

def convertDOMToPatternTree(elem, parent=None):
    cdef unicode name
    cdef PatternTree myTree
    cdef unicode myText
    
    name = unicode(elem.tag)
    if '}' in elem.tag:
        name = unicode(elem.tag.split('}')[1])  # Remove the namespace
    
    myTree = PatternTree(name, parent)
    myTree.type = XML
    
    # Add in the attributes
    myTree.attributes = {}
    for k in elem.attrib.keys():
        myTree.attributes[k] = elem.get(k)
        
    # If there is text in the node, add it as the first child
    if elem.text != None:
        myText = removeGarbageWhitespace(unicode(elem.text))
        if len(myText) > 0:
            textNode = PatternTree(myText, myTree)
            textNode.type = TEXT

    # Convert all children            
    for child in elem:
        convertDOMToPatternTree(child, myTree)
        
    return myTree
    
cdef unicode removeGarbageWhitespace(unicode s):
    '''
    Removes all of the characters from the string that I consider to be
    garbage, which are spaces, carraige returns, and line feeds.
    '''
    return s.replace(u' ', u'').replace(u'\n', u'').replace(u'\r', u'')