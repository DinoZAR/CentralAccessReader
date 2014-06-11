cdef enum PatternType:
    VARIABLE, CATEGORY, XML, TEXT, WILDCARD

cdef class PatternTree:
    cdef public PatternTree previous
    cdef public PatternTree next
    cdef public PatternTree parent
    cdef public list children
    
    cdef public int type
    cdef public unicode name
    cdef public dict attributes
    cdef public list categories
    cdef public unicode output
    
    # Functions
    cpdef PatternTree copy(self)
    cpdef int isExpressions(self)
    cpdef MatchResult isMatch(self, PatternTree other)
    cpdef GatherResult gather(self, PatternTree other)
    cpdef list getChildren(self)
    cpdef PatternTree getFirstChild(self)
    cpdef list getExpressions(self)
    cpdef object addChild(self, PatternTree newNode)
    cpdef object insertChild(self, PatternTree newNode, int index)
    cpdef object insertBefore(self, PatternTree newNode, PatternTree beforeNode)
    cpdef PatternTree getNext(self, int includeChildren=*)
    cpdef list getOutput(self)
    cpdef object disconnect(self)
    cpdef object copyData(self, PatternTree other)
    cpdef unicode getTypeString(self)
    cdef unicode _createIndent(self, int num)
    cpdef unicode dump(self, int indent=*)
    
cdef class GatherResult:
    cdef public PatternTree next
    cdef public list extends
    cdef public list removes
    
cdef class MatchResult:
    cdef public int match
    cdef public PatternTree next