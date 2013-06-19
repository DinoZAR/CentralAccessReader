'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
print 'Starting!'

from lxml import etree
 
from src.mathml3.pattern_tree import convertDOMToPatternTree, PatternTree
from src.mathml3.database import parse, convertToPatternTree
from src.mathml3.parser import transform
from src.misc import program_path
 
mathmlPath = 'C:\\Users\\GraffeS\\Desktop\\mathml.xml'
#databasePath = program_path('src\\mathml\\parser_pattern_database.txt')
databasePath = 'C:\\Users\\GraffeS\\Desktop\\data.txt'
 
# Test my iterator out completely before I try anything
mathmlFile = open(mathmlPath, 'r')
mathml = etree.fromstring(mathmlFile.read())
mathmlFile.close()

myTree = convertDOMToPatternTree(mathml)

print 'Tree:'
print myTree

databaseFile = open(databasePath, 'r')
database = parse(databaseFile.read())
databaseFile.close()

# pattern = PatternTree('food')
# w = PatternTree('beans', pattern)
# num = PatternTree('30', w)
# num.type = PatternTree.TEXT
# 
# print
# print 'Pattern:'
# print pattern
# 
# current = myTree
# while True:
#     if current == None:
#         break
#     data = pattern.isMatch(current)
#     print data
#     current = current.getNext()

             
print 'Patterns!'
for p in database['patterns']:
    #print p['number'], ':', p['variable']['value'], 'Output:', p['output']
    pattern = convertToPatternTree(p)
    print '--------------------------'
    print 'Pattern:'
    print pattern
     
#     print
#     print 'Before:'
#     print myTree
     
    transform(myTree, pattern)
    
    print
    print 'After:'
    print myTree
     
print
print
print'!===============================================!'
print 'Final:'
print
print myTree
 
print
print
print '************************************************'
print 'Speech Output:'
print myTree.getOutput()

print 'Done!'