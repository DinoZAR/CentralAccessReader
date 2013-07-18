'''
Provides a parser to parse the math equation database used to get the correct
speech output for given MathML patterns. This only creates a parse tree from
the database. It does not handle conversion between MathML structures to 
structures used in the database.

Author: Spencer Graffe
'''

import ply.lex as lex
import ply.yacc as yacc
import os
from pattern_tree import PatternTree, VARIABLE, CATEGORY, XML, TEXT, WILDCARD, WILDCARD_TOKENS
import HTMLParser

htmlParser = HTMLParser.HTMLParser()

# LEXER

reserved = {
		'import' : 'IMPORT'
		}

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
		'LEFTCARET',
		'RIGHTCARET',
		'COMMA',
		'NEWLINE',
		'WS'
		] + list(reserved.values())

t_ignore_COMMENT = r'//.*'

def t_ID(t):
	r'[a-zA-Z_\.]+'
	t.type = reserved.get(t.value, 'ID')
	return t
	
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

t_LEFTCARET = r'<'
t_RIGHTCARET = r'>'

t_COMMA = r','
	
def t_NEWLINE(t):
	r'[\r]?\n'
	t.lexer.lineno += len(t.value)
	
t_ignore  = ' \t'

def t_error(t):
	raise TypeError("Unknown text '%s'" % (t.value,))

# Create my lexer now after all of these definitions
lexer = lex.lex(debug=False)

# ------------------------
# Parser things
# ------------------------

def p_database(p):
	'''
	database : patterns
	'''
	p[0] = {'patterns' : p[1]}
	
def p_patterns(p):
	'''
	patterns : pattern patterns
			 | import patterns
			 | pattern
			 | import
	'''
	if len(p) == 3:
		l = [p[1]]
		l.extend(p[2])
		p[0] = l
	else:
		p[0] = [p[1]]

def p_import(p):
	'''
	import : IMPORT ID
	'''
	p[0] = {'type' : 'import', 'value' : p[2]}

def p_pattern(p):
	'''
	pattern : variable categories ASSIGNS expressions OUTPUTS output
	        | variable ASSIGNS expressions OUTPUTS output
	'''
	if len(p) == 7:
		p[0] = {'type' : 'pattern', 'variable' : p[1], 'categories' : p[2], 'expressions' : p[4], 'output' : p[6], 'number' : p.lineno(2)}
		#print 'Pattern:', p[0]
	else:
		p[0] = {'type' : 'pattern', 'variable' : p[1], 'expressions' : p[3], 'output' : p[5], 'number' : p.lineno(2)}
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
	xml : ID LEFTCARET attributes RIGHTCARET LEFTPAREN expressions RIGHTPAREN
	      | ID LEFTCARET attributes RIGHTCARET LEFTPAREN RIGHTPAREN
	      | ID LEFTPAREN expressions RIGHTPAREN
	      | ID LEFTPAREN RIGHTPAREN
	'''
	
	if len(p) == 8:
		p[0] = {'type' : 'xml', 'value' : p[1], 'children' : p[6], 'attributes' : p[3]}
	elif len(p) == 7:
		p[0] = {'type' : 'xml', 'value' : p[1], 'children' : [], 'attributes' : p[3]}
	elif len(p) == 5:
		p[0] = {'type' : 'xml', 'value' : p[1], 'children' : p[3], 'attributes' : []}
	else:
		p[0] = {'type' : 'xml', 'value' : p[1], 'children' : [], 'attributes' : []}
		
def p_attributes(p):
	'''
	attributes : attribute COMMA attributes
				| attribute
	'''
	if len(p) == 4:
		myList = [p[1]]
		myList.extend(p[3])
		p[0] = myList
	else:
		p[0] = [p[1]]
		
def p_attribute(p):
	'''
	attribute : ID ASSIGNS LITERAL
	'''
	p[0] = {'name' : p[1], 'value' : p[3].replace('"', '')}
	
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

def parse(inputString, filePath):
	
	# Give the lexer some input
	lexer.input(inputString)
	tree = parser.parse(inputString, lexer=lexer)
	
	# Get the imports for it
	if filePath != None:
		i = 0
		patterns = tree['patterns']
		while i < len(patterns):
			
			if patterns[i]['type'] == 'import':
				path = os.path.join(os.path.dirname(filePath), patterns[i]['value'])
				f = open(path, 'r')
				contents = f.read()
				f.close()
				
				lexer.input(contents)
				t = parser.parse(contents, lexer=lexer)
				
				# Replace the import statement with my patterns
				patterns.pop(i)
				patterns[i:i] = t['patterns']
				
			else:
				i += 1
			
		tree['imports'] = []
	
	return tree

def convertToPatternTree(databasePattern):
	'''
	Converts a pattern in a database into a PatternTree 
	'''
	expressions = databasePattern['expressions']
	myTree = PatternTree(databasePattern['variable']['value'])
	myTree.type = VARIABLE
	if 'categories' in databasePattern:
		myTree.categories = databasePattern['categories']['value']
	myTree.output = unicode(databasePattern['output'])
	
	_convertExpressions(myTree, expressions)
	
	return myTree
			
def _convertExpressions(tree, expressions):
	
	for i in expressions:
		ex = i['expression']    # This is a little indirect, but hey
			
		if ex['type'] == 'variable':
			newChild = PatternTree(ex['value'], tree)
			newChild.type = VARIABLE
				
		elif ex['type'] == 'categories':
			newChild = PatternTree('<categories>', tree)
			newChild.type = CATEGORY
			newChild.categories = ex['value']
				
		elif ex['type'] == 'xml':
			newChild = PatternTree(ex['value'], tree)
			newChild.type = XML
			newChild.attributes = {}
			if len(ex['attributes']) > 0:
				for attr in ex['attributes']:
					newChild.attributes[attr['name']] = attr['value']
			_convertExpressions(newChild, ex['children'])
			
		# For this one, differentiate between a regular expression for a literal
		# or a collector token, such as a +, ?, or #
		elif ex['type'] == 'literal':
			if ex['value'] in WILDCARD_TOKENS:
				newChild = PatternTree(ex['value'], tree)
				newChild.type = WILDCARD
				
			else:
				newChild = PatternTree(htmlParser.unescape(ex['value'][1:-1]), tree)
				newChild.type = TEXT