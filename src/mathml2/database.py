'''
Provides a parser to parse the math equation database used to get the correct
speech output for given MathML patterns. This only creates a parse tree from
the database. It does not handle conversion between MathML structures to 
structures used in the database.

Author: Spencer Graffe
'''

import ply.lex as lex
import ply.yacc as yacc
from parse_elements import *
from pattern_tree import PatternTree

# LEXER

tokens = [
		'COMMENT',
		'ID',
		'STRING',
		'LITERAL',
		'ASSIGNS',
		'OUTPUTS',
		'ANYEXPR',
		'MULTIEXPR',
		'MULTINUMBEREDEXPR',
		'LEFTPAREN',
		'RIGHTPAREN',
		'LEFTBRACKET',
		'RIGHTBRACKET',
		'COMMA',
		'NEWLINE',
		'WS'
		]

t_ignore_COMMENT = r'//.*'

t_ID = r'[a-zA-Z_]+'
t_STRING = r'\'.*\''
t_LITERAL = r'\"[^\"]*\"'

t_ASSIGNS = r'='
t_OUTPUTS = r'->'

t_ANYEXPR = r'\?'
t_MULTIEXPR = r'\+'
t_MULTINUMBEREDEXPR = r'\#'

t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'

t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'

t_COMMA = r','
	
def t_NEWLINE(t):
	r'[\r]?\n'
	t.lexer.lineno += len(t.value)
	
t_ignore  = ' \t'

def t_error(t):
	raise TypeError("Unknown text '%s'" % (t.value,))

# Create my lexer now after all of these definitions
lexer = lex.lex()

# ------------------------
# Parser things
# ------------------------

def p_program(p):
	'''
	database : patterns
	'''
	p[0] = {'patterns' : p[1]}
	
def p_patterns(p):
	'''
	patterns : pattern patterns
			 | pattern
	'''
	if len(p) == 3:
		l = [p[1]]
		l.extend(p[2])
		p[0] = l
	else:
		p[0] = [p[1]]

def p_pattern(p):
	'''
	pattern : variable categories ASSIGNS expressions OUTPUTS output
	        | variable ASSIGNS expressions OUTPUTS output
	'''
	if len(p) == 7:
		p[0] = {'variable' : p[1], 'categories' : p[2], 'expressions' : p[4], 'output' : p[6], 'number' : p.lineno(2)}
		#print 'Pattern:', p[0]
	else:
		p[0] = {'variable' : p[1], 'expressions' : p[3], 'output' : p[5], 'number' : p.lineno(2)}
		#print 'Pattern:', p[0]
	
def p_expressions(p):
	'''
	expressions : expression expressions 
	            | expression
	'''
	if len(p) == 3:
		#print 'Trying to combine:', p[1], p[2]
		l = [p[1]]
		l.extend(p[2])
		p[0] = l
		#print 'Expressions:', p[0]
	else:
		#print 'Making into list:', p[1]
		p[0] = [p[1]]
		#print 'Expressions:', p[0]
	
def p_expression(p):
	'''
	expression : xml
	           | variable
	           | categories
			   | LITERAL
			   | ANYEXPR
			   | MULTIEXPR
			   | MULTINUMBEREDEXPR
	'''
	p[0] = {'expression' : p[1]}
	if isinstance(p[0]['expression'], basestring):
		if p[0]['expression'][-1] == '"':
			p[0]['expression'] = {'type' : 'literal', 'value' : p[0]['expression'][1:-1]}
		else:
			p[0]['expression'] = {'type' : 'literal', 'value' : p[0]['expression']}
	#print 'Expression:', p[0]
	
def p_variable(p):
	'''
	variable : ID
	'''
	p[0] = {'type' : 'variable', 'value' : p[1]}
	#print 'Variable', p[0]

def p_categories(p):
	'''
	categories : LEFTBRACKET categValues RIGHTBRACKET
	'''
	p[0] = {'type' : 'categories', 'value' : p[2]}
	#print 'Categories:', p[0]
	
def p_categValues(p):
	'''
	categValues : categValue COMMA categValues
			  | categValue
	'''
	if len(p) == 4:
		l = [p[1]]
		l.extend(p[3])
		p[0] = l
		#print 'Categ Values:', p[0]
	else:
		p[0] = [p[1]]
		#print 'Categ Values:', p[0]
		
def p_categValue(p):
	'''
	categValue : ID
	'''
	p[0] = p[1]
	#print 'Categ Value:', p[0]
	
def p_xml(p):
	'''
	xml : ID LEFTPAREN expressions RIGHTPAREN
	       | ID LEFTPAREN RIGHTPAREN
	'''
	if len(p) == 5:
		p[0] = {'type' : 'xml', 'value' : p[1], 'children' : p[3]}
		#print 'XML:', p[0]
	else:
		p[0] = {'type' : 'xml', 'value' : p[1], 'children' : []}
		#print 'XML:', p[0]
	
def p_output(p):
	'''
	output : STRING
	'''
	p[0] = p[1][1:-1]
	#print 'Output:', p[0]
	
def p_error(p):
	print 'Error culprit:', p
	
# Create my parser from these definitions
parser = yacc.yacc(debug=False)

# ------------------------------------------------------------------------------
# User Functions : These are what other programmers should be using
# ------------------------------------------------------------------------------

def parse(inputString):
	
	# Give the lexer some input
	lexer.input(inputString)
	tree = parser.parse(inputString, lexer=lexer)
	return tree


def convertToPatternTree(databasePattern):
	'''
	Converts a pattern in a database into a PatternTree 
	'''
	expressions = databasePattern['expressions']
	myTree = PatternTree()
	myTree.value = databasePattern['variable']['value']
	myTree.type = PatternTree.VARIABLE
	if 'categories' in databasePattern:
		myTree.categories = databasePattern['categories']['value']
	myTree.output = databasePattern['output']
	
	_convertExpressions(myTree, expressions)
	
	return myTree
			
def _convertExpressions(tree, expressions):
	
	childList = []
	for i in expressions:
		ex = i['expression']    # This is a little indirect, but hey
		
		if ex['type'] == 'variable':
			newChild = PatternTree()
			newChild.type = PatternTree.VARIABLE
			newChild.value = ex['value']
			childList.append(newChild)
			
		elif ex['type'] == 'categories':
			newChild = PatternTree()
			newChild.type = PatternTree.CATEGORY
			newChild.categories = ex['value']
			childList.append(newChild)
			
		elif ex['type'] == 'xml':
			newChild = PatternTree()
			newChild.type = PatternTree.XML
			newChild.value = ex['value']
			_convertExpressions(newChild, ex['children'])
			childList.append(newChild)
		
		# For this one, differentiate between a regular expression for a literal
		# or a collector token, such as a +, ?, or #
		elif ex['type'] == 'literal':
			if ex['value'] in PatternTree.COLLECTOR_TOKENS:
				newChild = PatternTree()
				newChild.type = PatternTree.COLLECTOR
				newChild.value = ex['value']
				childList.append(newChild)
				
			else:
				newChild = PatternTree()
				newChild.type = PatternTree.TEXT
				newChild.value = ex['value']
				childList.append(newChild)
				
	tree.children = childList