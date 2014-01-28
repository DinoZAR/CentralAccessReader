'''
Created on Mar 3, 2013

If I find a problem in the parser and I need to have a small debug environment,
this is the script for that.

@author: Spencer Graffe
'''
from misc import program_path

MATHML_PATH = 'C:\\Users\\GraffeS\\Desktop\\test.xml'
DATABASE_PATH = 'W:\\Nifty Prose Articulator\\workspace2\\another\\src\\math_patterns\\General.txt'

print 'Starting!'

from lxml import etree
 
from mathml.pattern_tree import convertDOMToPatternTree, PatternTree
from mathml.database import parse, convertToPatternTree
from mathml.parser import transform, _testMatch
 
# Test my iterator out completely before I try anything
mathmlFile = open(MATHML_PATH, 'r')
mathml = etree.fromstring(mathmlFile.read())
mathmlFile.close()

myTree = convertDOMToPatternTree(mathml)

print 'Tree:'
print unicode(myTree).encode('utf-8')

databaseFile = open(DATABASE_PATH, 'r')
database = parse(databaseFile.read(), DATABASE_PATH)
databaseFile.close()

print 'Patterns!'
for p in database['patterns']:
    pattern = convertToPatternTree(p)
    
    gotMatch = [False]
    
    myTree = transform(myTree, pattern, gotMatchFlag=gotMatch)
    
    if gotMatch[0]:
        print '--------------------------'
        print 'Pattern:'
        print unicode(pattern).encode('utf-8')
        
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