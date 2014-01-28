'''
Created on Dec 18, 2013

This is provided so that the list of possible export formats that CAR can export
to can be maintained in one place.

@author: Spencer Graffe
'''

from export.html_single import HTMLSingleExportThread
from export.mp3 import MP3ExportThread
from export.mp3_by_page import MP3ByPageExportThread

def get():
    '''
    Returns a list of ExportThread classes that can be used to export different
    things. To get a description of each export class, use .description() 
    '''
    myList = []
    
    myList.append(MP3ExportThread)
    myList.append(MP3ByPageExportThread)
    myList.append(HTMLSingleExportThread)
    
    return myList