'''
Created on May 19, 2014

@author: Spencer Graffe
'''

class MathLibrary(object):
    '''
    Math library used for the math-to-prose engine. This will be used for both
    the built-in libraries and for custom libraries that one can import.
    '''

    def __init__(self, title):
        self.title = ''
        self.author = ''
        self.patterns = []
        
    def write(self, f):
        '''
        Writes out this library to file object.
        '''
        pass
    
    def read(self, f):
        '''
        Reads in a math library from file object.
        '''
        pass