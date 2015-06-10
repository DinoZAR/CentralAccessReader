'''
Created on Dec 18, 2013

This is provided so that the list of possible export formats that CAR can export
to can be maintained in one place.

@author: Spencer Graffe
'''

# from car.export.html_single import AppleHTMLSingleExportThread
from car.export.html_single import PNGHTMLSingleExportThread
# from car.export.html_single import MathJaxHTMLSingleExportThread
from car.export.html_single import FlexHTMLSingleExportThread
from car.export.html_single import MathPlayerHTMLSingleExportThread
from car.export.mp3 import MP3ExportThread
from car.export.mp3_by_page import MP3ByPageExportThread

def get():
    '''
    Returns a list of ExportThread classes that can be used to export different
    things. To get a description of each export class, use .description() 
    '''
    myList = []
    
    myList.append(MP3ExportThread)
    myList.append(MP3ByPageExportThread)
    # myList.append(AppleHTMLSingleExportThread)
    # myList.append(MathJaxHTMLSingleExportThread)
    myList.append(PNGHTMLSingleExportThread)
    myList.append(FlexHTMLSingleExportThread)
    myList.append(MathPlayerHTMLSingleExportThread)

    return myList