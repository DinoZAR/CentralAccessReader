'''
Created on Dec 13, 2013

@author: Spencer Graffe
'''
import base64

from lxml import html
from PyQt4.QtCore import QIODevice, QFile

from document import Document
from forms import resource_rc

class LandingPageDocument(Document):
    '''
    This page is used to show a user what he/she can do with the program. It
    will show how to load a document into the program, either by drag-n-drop or
    clicking on the provided button to open a document.
    '''

    def __init__(self, filePath, progressHook, cancelHook):
        Document.__init__(self, filePath, progressHook, cancelHook)
        self._name = 'Load a Document!'
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
        dragHereGif = self._getImageUri(':/all/icons/Drag File Here Animation.gif')
        
        s = '''
        <body>
        <h1>Quick Start</h1>
        <p>CAR accepts .docx Word Docs and text from your clipboard. You can access text in the following ways:</p>
        <h2>Click to open</h2>
        <p><a href="command/openDocument" class="button">Open Document</a></p>
        <h2>Drag Word Document file into CAR</h2>
        <p><img src="''' + dragHereGif + '''"/></p>
        <h2>Paste from clipboard</h2>
        <h3>Windows: Ctrl + V</h3>
        <h3>Mac: Command + V</h3>
        </body>
        '''
        return s