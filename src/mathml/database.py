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
		'LEFTPAREN',
		'RIGHTPAREN',
		'LEFTBRACKET',
		'RIGHTBRACKET',
		'COMMA',
		'NEWLINE',
		'WS'
		]

t_ignore_COMMENT = r'\#.*'

t_ID = r'[a-zA-Z_]+'
t_STRING = r'\'.*\''
t_LITERAL = r'\"[^\"]*\"'

t_ASSIGNS = r'='
t_OUTPUTS = r'->'

t_ANYEXPR = r'\?'
t_MULTIEXPR = r'\+'

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
	database : pattern patterns
	        | pattern
	'''
	#print 'Program:', p
	if len(p) == 3:
		p[0] = Database([p[1], p[2]])
	else:
		p[0] = Database([p[1]])
	
def p_patterns(p):
	'''
	patterns : pattern patterns
			 | pattern
	'''
	#print 'Patterns:', p
	if len(p) == 3:
		p[0] = Patterns([p[1], p[2]])
	else:
		p[0] = Patterns([p[1]])

def p_pattern(p):
	'''
	pattern : variable category ASSIGNS expressions OUTPUTS output
	        | variable ASSIGNS expressions OUTPUTS output
	'''
	#print 'Pattern:', p, 'Line Num:', p.lineno(2)
	if len(p) == 7:
		p[0] = Pattern(expressions=p[4], variable=p[1], category=p[2], output=p[6], lineNum=p.lineno(2))
	else:
		p[0] = Pattern(expressions=p[3], variable=p[1], output=p[5], lineNum=p.lineno(2))
	
def p_expressions(p):
	'''
	expressions : expression expressions
	            | expression
	'''
	#print 'Expression:', p
	if len(p) == 3:
		p[0] = Expressions([p[1], p[2]])
	else:
		p[0] = Expressions([p[1]])
	
def p_expression(p):
	'''
	expression : mathml
	           | variable
	           | category
			   | LITERAL
			   | ANYEXPR
			   | MULTIEXPR
	'''
	if type(p[1]) is MathML:
		p[0] = p[1]
	elif type(p[1]) is Variable:
		p[0] = p[1]
	elif type(p[1]) is Category:
		p[0] = p[1]
	else:
		p[0] = Expression(p[1])
	
def p_variable(p):
	'''
	variable : ID
	'''
	#print 'Variable:', p
	p[0] = Variable(p[1])

def p_category(p):
	'''
	category : LEFTBRACKET categValues RIGHTBRACKET
	'''
	p[0] = Category(p[2])
	
def p_categValues(p):
	'''
	categValues : categValue COMMA categValues
			  | categValue
	'''
	if len(p) == 4:
		myList = []
		myList.append(p[1])
		myList.extend(p[3])
		p[0] = myList
	else:
		p[0] = [p[1]]
		
def p_categValue(p):
	'''
	categValue : ID
	'''
	p[0] = p[1]
	
def p_mathml(p):
	'''
	mathml : ID LEFTPAREN expressions RIGHTPAREN
	       | ID LEFTPAREN RIGHTPAREN
	'''
	#print 'MathML:', p
	if len(p) == 5:
		p[0] = MathML(p[1], [p[3]])
	else:
		p[0] = MathML(p[1], [])
	
def p_output(p):
	'''
	output : STRING
	'''
	#print 'Output:', p
	p[0] = Output(p[1])
	
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
	_simplify(tree)
	return tree
	
def _simplify(parseTree):
	'''
	This collapses certain elements in the tree so that they appear sequentially
	instead of recursively. This will make anything with Patterns collapse into
	a list of type Pattern and Expressions into a list of type Expression.
	
	Also, it sorts the Pattern's by line number to enforce order of application.
	'''
	recursiveSeriesTypes = [Patterns, Expressions]
	_collapseRecursiveSeries(parseTree, recursiveSeriesTypes)
	pass
	
def _collapseRecursiveSeries(tree, recurseSeriesList):
	'''
    This function will collapse all tree nodes that are recursively defined as
    a series. This will make sure that series are represented as an array and
    not as a one-legged tree.
    
    The recurseSeriesList is a list of BreezeElement types that are recursively
    defined this way.
    '''
	
	# Define my recursive collapsing function and my list making thing
	def recurseToList(root, t):
		myList = []
		if len(root.children) > 0:
			for child in root.children:
				if type(child) is t:
					myList.extend(recurseToList(child, t))
				else:
					collapseType(child, t)
					myList.append(child)
					
		return myList
		
	def collapseType(root, t):
		if len(root.children) > 0:
			myList = []
			for child in root.children:
				if type(child) is t:
					myList.extend(recurseToList(child, t))
				else:
					collapseType(child, t)
					myList.append(child)
					
				root.children = myList
			
	# For each item in the list, collapse the said tree
	for t in recurseSeriesList:
		collapseType(tree, t)
	