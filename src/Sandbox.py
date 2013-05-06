'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
from src.docx.importer import DocxDocument
import pythoncom
import win32com.client
from glob import glob
import os

if __name__ == '__main__':
    
    # Using this to figure out my Unicode problems
    myTestString = 'Try it out on Herman Melville\xe2\x80\x99s Moby Dick below:'
    
    s = myTestString.decode('utf-8')
    
    print s
    