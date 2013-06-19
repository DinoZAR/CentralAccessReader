from itertools import groupby, ifilter


myList = [1, 1, 1, 1, 2, 1, 1, 3, 3, 3, 1]
stuff = myList

def convertToNode(elem):
    if elem == 1:
        return ['X', []]
    elif elem == 2:
        return ['T', []]
    elif elem == 3:
        return ['V', []]

myList = map(convertToNode, myList)

print myList

#def determine(elem, replace):
    #if elem == replace:
        #return ('X', [replace])
    #else:
        #return elem

# Replace all 3's with ('X', [3])
#replace = 3
#myList = map((lambda foo: determine(foo, replace)), myList)

#print myList

#print 'Replace all consecutive 2s into single lists...'

#def keyFunc(elem):
    #return elem

#l = []
#for k, g in groupby(myList, key=keyFunc):
    #myG = list(g)
    #if len(myG) > 1:
        #l.append(myG)
    #else:
        #l.extend(myG)

#print 'New list:', l

print 'Accumulate all things to a list until next pattern matches with start point...'

def determine(elem, pattern):
    if pattern == elem:
        return True
    else:
        return False

def keyFunc(elem):
    return elem[0]

def transform(l):
    return ('+', l)
    
def accumTillNextMatch(myList, startIndex, matchElem, matchFunction, idFunc, transformFunc):
    print 'Start:', startIndex
    print 'Next match:', matchElem
    l = myList[0:startIndex]
    l.append([])
    adding = True
    for k, g in groupby(myList[startIndex:], key=idFunc):
        if matchFunction(k, matchElem):
            adding = False
            l[-1] = transformFunc(l[-1])
        if adding:
            l[-1].extend(g)
        else:
            l.extend(g)
    return l

myList = accumTillNextMatch(myList, 3, 'V', determine, keyFunc, transform)
print myList

