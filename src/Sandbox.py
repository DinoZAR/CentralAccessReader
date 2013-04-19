'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
from src.docx.importer import DocxDocument

if __name__ == '__main__':
    
    testPath = 'tests\\Chapter 3 Test.docx'
    
    mydoc = DocxDocument(testPath)
    
    print 'Done!'