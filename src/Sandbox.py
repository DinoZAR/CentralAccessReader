'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
print 'Starting!'


bit = 2
bytes = 8
result = (bytes & bit) > 0
print result

# from lxml import etree
# 
# from src.mathml2.pattern_tree import domToPatternTree, PatternTree, DepthFirstIterator
# from src.mathml2.database import parse, convertToPatternTree
# from src.mathml2.matcher import markMatches
# from src.mathml2.replacer import replaceAndRemove
# from src.misc import program_path
# 
# mathmlPath = 'C:\\Users\\GraffeS\\Desktop\\mathml.txt'
# #databasePath = program_path('src\\mathml\\parser_pattern_database.txt')
# databasePath = 'C:\\Users\\GraffeS\\Desktop\\data.txt'
# 
#  
# # # Test my iterator out completely before I try anything
# #  
# # mathmlFile = open(mathmlPath, 'r')
# # mathml = etree.fromstring(mathmlFile.read())
# # mathmlFile.close()
# #  
# # myTree = domToPatternTree(mathml)
# #  
# #  
# # iter = DepthFirstIterator(myTree)
# #  
# # print 'Starting iteration!'
# #  
# # print '!--!'
# # print iter.next()[0]
# # print '!--!'
# # print iter.next()[0]
# # print '!--!'
# # print iter.next()[0]
# # print '!--!'
# # print iter.next()[0]
# # print '!--!'
# # print iter.next()[0]
# #  
# # print '!@#$%^&* Jumping to parent! !@#$%^&*'
# # iter.jumpToParent()
# #  
# # print '!--!'
# # print iter.next()[0]
# #  
# # print '!--!'
# # print iter.next()[0]
# #  
# # print '!--!'
# # print iter.next()[0]
# 
# 
# mathmlFile = open(mathmlPath, 'r')
# mathml = etree.fromstring(mathmlFile.read())
# mathmlFile.close()
#    
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
# for p in database['patterns']:
#     #print p['number'], ':', p['variable']['value'], 'Output:', p['output']
#       
#     patternTree = convertToPatternTree(p)
#     print '--------------------------'
#     print 'PatternTree equivalent:'
#     print patternTree
#       
#     print 'Match up the pattern...'
#     gotMatches = markMatches(myTree, patternTree)
#     if gotMatches:
#         print '!!!!!!!!!!!!!!!! Got some matches! Here are the changes... !!!!!!!!!!!!!!!!'
#         print 'Before:'
#         print myTree
#         replaceAndRemove(myTree, p['variable']['value'], p['output'])
#         print 'After:'
#         print myTree
#           
#     else:
#         print 'No matches...'
#       
#     print '--------------------------'
      
print 'Done!'