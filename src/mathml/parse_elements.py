'''
Author: Spencer Graffe
'''
from mathml.replacer import ReplaceTree
import copy
import HTMLParser
htmlParser = HTMLParser.HTMLParser()

class ParseElement(object):
	def __init__(self):
		self.name = '<no name set>'
		self.children = []
		
	def dump(self, indent=0):
		myString = self._createIndent(indent) + self.name
		if len(self.children) > 0:
			myString += ' (\n'
			for i in range(len(self.children)):
				myString += self.children[i].dump(indent + 1) + '\n'
			myString += self._createIndent(indent) + ')'
		
		return myString
		
	def _createIndent(self, numIndents):
		myString = ''
		for i in range(numIndents):
			myString += '    '
		return myString

class Database(ParseElement):
	def __init__(self, patterns):
		ParseElement.__init__(self)
		self.children = patterns
		self.name = 'Database'
		
class Patterns(ParseElement):
	def __init__(self, patterns):
		ParseElement.__init__(self)
		self.name = 'Patterns'
		self.children = patterns
		
class Pattern(ParseElement):
	def __init__(self, expressions, variable, output, lineNum, category=None):
		ParseElement.__init__(self)
		self.lineNum = lineNum
		self.variable = variable
		self.output = output
		if category != None:
			self.category = category.values
		else:
			self.category = []
		self.children = [expressions]
		self.name = 'Pattern<' + variable.value + ' -> ' + output.value + ' Ln ' + str(self.lineNum) + '>'
		
	def getReplaceTree(self):
		'''
		Gets the ReplaceTree associated with the pattern
		'''
		myTreeRoot = ReplaceTree()
		myTreeRoot.type = ReplaceTree.SPEECH
		myTreeRoot.value = self.variable.value
		myTreeRoot.categories = self.category
		
		# For each of the children, generate the correct ReplaceTree counterpart
		for child in self.children:
			myTreeRoot.children.append(self._generateReplace(child, myTreeRoot))
		
		return myTreeRoot
	
	def _generateReplace(self, expression, parent):
		'''
		Generates a ReplaceTree node from whatever the expression happens to be.
		'''
		newNode = ReplaceTree()
		newNode.parent = parent
		
		if isinstance(expression, Variable):
			newNode.type = ReplaceTree.SPEECH
			newNode.value = expression.value
			newNode.children = copy.copy(expression.children)
			
		elif isinstance(expression, MathML):
			newNode.type = ReplaceTree.MATHML
			newNode.value = expression.value
			newNode.children = copy.copy(expression.children)
		elif isinstance(expression, Category):
			newNode.type = ReplaceTree.CATEGORY
			newNode.value = expression.values
			newNode.children = []
		else:
			if expression.value == '?':
				newNode.type = ReplaceTree.ANY
				newNode.value = expression.value
				newNode.children = []
			elif expression.value == '+':
				newNode.type = ReplaceTree.ANY_PLUS
				newNode.value = expression.value
				newNode.children = []
			elif expression.value == '#':
				newNode.type = ReplaceTree.ANY_NUMBER_PLUS
				newNode.value = expression.value
				newNode.children = []
			else:
				newNode.type = ReplaceTree.TEXT
				newNode.value = htmlParser.unescape(expression.value.replace('\"', ''))
		
		# Make sure all the new node's children are converted too
		if len(newNode.children) > 0:
			for i in range(len(newNode.children)):
				newNode.children[i] = self._generateReplace(newNode.children[i], newNode)
				
		return newNode
				
class Expressions(ParseElement):
	def __init__(self, expressions):
		ParseElement.__init__(self)
		self.children = expressions
		self.name = 'Expressions'
		
class Expression(ParseElement):
	def __init__(self, expression):
		ParseElement.__init__(self)
		self.value = 'nested'
		if isinstance(expression, basestring):
			self.value = expression
			self.children = []
		else:
			self.children = [expression]
		self.name = 'Expression<' + self.value + '>'
		
	def isLiteral(self):
		'''
		Returns whether this expression refers to a literal or not
		'''
		if len(self.children) > 0:
			if (self.children[0] != '?') or (self.children[0] != '+') or (self.children[0] != '#'):
				return True
			else:
				return False
		else:
			return True
		
class Variable(Expression):
	def __init__(self, identifier):
		ParseElement.__init__(self)
		self.value = identifier
		self.children = []
		self.name = 'Variable<' + self.value + '>'
			
class Category(Expression):
	def __init__(self, values):
		ParseElement.__init__(self)
		self.children = []
		self.values = values
		self.name = 'Category<'
		for i in self.values:
			self.name += i + ','
		self.name += '>'
		
class MathML(Expression):
	def __init__(self, tagname, children):
		ParseElement.__init__(self)
		self.value= tagname
		
		if children is None:
			self.children = []
		else:
			self.children = children
			
		self.name = 'MathML<' + self.value + '>'
		
class Output(ParseElement):
	def __init__(self, outputText):
		ParseElement.__init__(self)
		self.children = []
		self.value = outputText
		self.name = 'Output<' + self.value + '>'