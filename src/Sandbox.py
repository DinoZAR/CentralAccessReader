'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
print 'Starting!'

from lxml import etree
 
from src.mathml3.pattern_tree import convertDOMToPatternTree, PatternTree
from src.mathml3.database import parse, convertToPatternTree
from src.misc import program_path
 
mathmlPath = 'C:\\Users\\GraffeS\\Desktop\\mathml.txt'
#databasePath = program_path('src\\mathml\\parser_pattern_database.txt')
databasePath = 'C:\\Users\\GraffeS\\Desktop\\data.txt'
 
# Test my iterator out completely before I try anything
  
mathmlFile = open(mathmlPath, 'r')
mathml = etree.fromstring(mathmlFile.read())
mathmlFile.close()
  
myTree = convertDOMToPatternTree(mathml)

print myTree

databaseFile = open(databasePath, 'r')
database = parse(databaseFile.read())
databaseFile.close()


# myTree = domToPatternTree(mathml)
#    
# print 'My MathML tree!'
# print myTree
# print '------------------------------------------------------'
#    
# databaseFile = open(databasePath, 'r')
# database = parse(databaseFile.read())
# databaseFile.close()
#             
# print 'Patterns!'
for p in database['patterns']:
    #print p['number'], ':', p['variable']['value'], 'Output:', p['output']
        
    patternTree = convertToPatternTree(p)
    print '--------------------------'
    print 'PatternTree equivalent:'
    print patternTree

print 'Done!'