'''
Provides a parser to parse the math equation database used to get the correct
speech output for given MathML patterns. This only creates a parse tree from
the database. It does not handle conversion between MathML structures to 
structures used in the database.

Author: Spencer Graffe
'''

import os
from math_to_prose_fast cimport pattern_tree
import HTMLParser

WILDCARD_TOKENS = ['?', '+', '#']

htmlParser = HTMLParser.HTMLParser()

# ------------------------------------------------------------------------------
# User Functions : These are what other programmers should be using
# ------------------------------------------------------------------------------

def convertToPatternTree(databasePattern):
	'''
	Converts a pattern in a database into a PatternTree 
	'''
	expressions = databasePattern['expressions']
	myTree = pattern_tree.PatternTree(databasePattern['variable']['value'])
	myTree.type = pattern_tree.VARIABLE
	if 'categories' in databasePattern:
		myTree.categories = databasePattern['categories']['value']
	myTree.output = unicode(databasePattern['output'])
	
	_convertExpressions(myTree, expressions)
	
	return myTree
			
def _convertExpressions(tree, expressions):
	
	for i in expressions:
		ex = i['expression']    # This is a little indirect, but hey
			
		if ex['type'] == 'variable':
			newChild = pattern_tree.PatternTree(ex['value'], tree)
			newChild.type = pattern_tree.VARIABLE
				
		elif ex['type'] == 'categories':
			newChild = pattern_tree.PatternTree('<categories>', tree)
			newChild.type = pattern_tree.CATEGORY
			newChild.categories = ex['value']
				
		elif ex['type'] == 'xml':
			newChild = pattern_tree.PatternTree(ex['value'], tree)
			newChild.type = pattern_tree.XML
			newChild.attributes = {}
			if len(ex['attributes']) > 0:
				for attr in ex['attributes']:
					newChild.attributes[attr['name']] = htmlParser.unescape(attr['value'])
			_convertExpressions(newChild, ex['children'])
			
		# For this one, differentiate between a regular expression for a literal
		# or a collector token, such as a +, ?, or #
		elif ex['type'] == 'literal':
			if ex['value'] in WILDCARD_TOKENS:
				newChild = pattern_tree.PatternTree(ex['value'], tree)
				newChild.type = pattern_tree.WILDCARD
				
			else:
				newChild = pattern_tree.PatternTree(htmlParser.unescape(ex['value'][1:-1]), tree)
				newChild.type = pattern_tree.TEXT