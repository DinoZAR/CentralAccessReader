'''
Created on Feb 20, 2014

@author: Spencer Graffe
'''
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QWidget
from PyQt4.QtWebKit import QWebSettings

from lxml import etree

from car.document.html_document import HTMLDocument
from car.forms.mathml_editor_ui import Ui_MathMLEditor
from car import misc

class MathMLEditor(QWidget):
    '''
    Basic editing widget that allows one to see the MathML they are modifying.
    '''

    def __init__(self, parent=None):
        super(MathMLEditor, self).__init__(parent)
        
        self.ui = Ui_MathMLEditor()
        self.ui.setupUi(self)
        
        self.mathDocument = None
        
        self.connect_signals()
        
    def connect_signals(self):
        self.ui.refreshMathButton.clicked.connect(self.refreshMath)
        
    def refreshMath(self):
        '''
        Refreshes the math that gets displayed in the editor.
        '''
        myString = unicode(self.ui.textEditor.toPlainText())
        self.setMath(myString)
        
    def setMath(self, some_string):
        '''
        Finds the first and end <math> tags in a string and extracts it as
        MathML into this control. This allows one to load one from file or
        from a string on the clipboard. If no MathML is detected, nothing
        happens.
        '''
        # See if I got some math in there
        firstIndex = some_string.find('<math')
        secondIndex = some_string.find('</math>')
        
        if firstIndex >= 0 and secondIndex >= 0:
            secondIndex += len('</math>')
            myMath = some_string[firstIndex:secondIndex]
            
            self.mathDocument = HTMLDocument(None, None, None, htmlString=myMath)
            
            # Set the math on the plain text editor
            mathml = etree.fromstring(myMath)
            self.ui.textEditor.setPlainText(etree.tostring(mathml, pretty_print=True))
            
            # Set the math to the web view
            url = misc.temp_path('import')
            baseUrl = QUrl.fromLocalFile(url)
            
            # Clear all of the caches
            QWebSettings.clearIconDatabase()
            QWebSettings.clearMemoryCaches()
            
            self.ui.webView.page().mainFrame().setHtml(self.mathDocument.getMainPage(), baseUrl)
        
    def getMath(self):
        '''
        Returns a Unicode string representing the math equation in the editor.
        '''
        return unicode(self.ui.textEditor.toPlainText())