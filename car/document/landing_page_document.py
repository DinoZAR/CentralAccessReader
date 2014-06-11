'''
Created on Dec 13, 2013

@author: Spencer Graffe
'''
import base64

from lxml import html
from PyQt5.QtCore import QIODevice, QFile

from car.document import Document
from car.forms import resource_rc  # needed to get image resource

class LandingPageDocument(Document):
    '''
    This page is used to show a user what he/she can do with the program. It
    will show how to load a document into the program, either by drag-n-drop or
    clicking on the provided button to open a document.
    '''

    def __init__(self, filePath, progressHook, cancelHook):
        Document.__init__(self, filePath, progressHook, cancelHook)
        self._name = 'Quick Start'
        self._contentDOM = html.fromstring(self._myContent()) 
        self._mapMathEquations()
        
    def _getImageUri(self, filePath):
        myImage = QFile(filePath)
        myImage.open(QIODevice.ReadOnly)
        contents = myImage.readAll()
        myImage.close()
        
        return 'data:image/gif;base64,' + base64.b64encode(contents)
        
    def _myContent(self):
        '''
        Returns the content that will be added to this document, as an HTML
        string.
        '''
        arrowImage = self._getImageUri(':/all/icons/arrow-top-left.png')
        
        s = '''
        <body>
        <p><img alt="Arrow points to white plus" title="Arrow points to white plus" src="''' + arrowImage + '''" width="75" height="75"/></p>
        <p>To open a Word Document, press the white plus.</p>
        <br/>
        <p>Other ways to load content into CAR:</p>
        <ul>
        <li><p>Drag Word Document into CAR</p></li>
        <li><p>Paste text from clipboard</p></li>
        </ul>
        <br/>
        <p><a class="button" href="command/disableQuickStart">Disable Quick Start</a>
        </body>
        '''
        return s