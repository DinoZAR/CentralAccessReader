'''
Created on Mar 3, 2013

If I find a problem in the parser and I need to have a small debug environment,
this is the script for that.

@author: Spencer Graffe
'''
MATHML_PATH = 'C:\\Users\\GraffeS\\Desktop\\test.xml'
DATABASE_PATH = 'C:\\Users\\GraffeS\\Desktop\\data.txt'

print 'Starting!'

from lxml import etree
 
from src.mathml.pattern_tree import convertDOMToPatternTree, PatternTree
from src.mathml.database import parse, convertToPatternTree
from src.mathml.parser import transform
from src.misc import program_path
 
# Test my iterator out completely before I try anything
mathmlFile = open(MATHML_PATH, 'r')
mathml = etree.fromstring(mathmlFile.read())
mathmlFile.close()

myTree = convertDOMToPatternTree(mathml)

print 'Tree:'
print unicode(myTree).encode('utf-8')

databaseFile = open(DATABASE_PATH, 'r')
database = parse(databaseFile.read())
databaseFile.close()

print 'Patterns!'
for p in database['patterns']:
    pattern = convertToPatternTree(p)
    print '--------------------------'
    print 'Pattern:'
    print unicode(pattern).encode('utf-8')
     
    myTree = transform(myTree, pattern)
    
    print
    print 'After:'
    print unicode(myTree).encode('utf-8')
     
print
print
print'!===============================================!'
print 'Final:'
print
print unicode(myTree).encode('utf-8')
 
print
print
print '************************************************'
print 'Speech Output:'
print unicode(myTree.getOutput()).encode('utf-8')

print 'Done!'