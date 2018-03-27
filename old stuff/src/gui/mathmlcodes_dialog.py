'''
Created on Feb 27, 2013

@author: Spen-ZAR
'''
import urllib
import operator
from PyQt4 import QtGui, QtCore
from PyQt4.QtWebKit import QWebView
from lxml import etree, html
from forms.mathmlcodesdialog_ui import Ui_MathMLCodesDialog
from misc import temp_path, program_path

class MathMLCodesDialog(QtGui.QDialog):
    '''
    A dialog showing a list of all the MathML codes in the document. Very useful
    in debugging which MathML works and which doesn't.
    '''

    def __init__(self, mathmlCodes, parent=None):
        QtGui.QDialog.__init__(self, parent)
        
        self.ui = Ui_MathMLCodesDialog()
        
        self.ui.setupUi(self)
        self.mathmlCodes = mathmlCodes
        
        # Set the items in the list box using WebViews of all of my MathML code
        # Sort the MathML by index
        sortedData = sorted(self.mathmlCodes.items(), key=lambda x: x[1]['index'])
        for data in sortedData:
            myItem = MathMLItem(data[1]['mathml'])
            item = QtGui.QListWidgetItem(data[1]['mathml'])
            item.setSizeHint(QtCore.QSize(0, 100))
            self.ui.mathmlCodesList.addItem(item)
            self.ui.mathmlCodesList.setItemWidget(item, myItem)
        
        self.connect_signals()
        
    
    def connect_signals(self):
        self.ui.mathmlCodesList.itemClicked.connect(self.itemClicked)
        self.ui.closeButton.clicked.connect(self.closeClicked)
        
    def itemClicked(self, item):
        outputText = str(item.data(QtCore.Qt.DisplayRole).toString())
        outputText = etree.tostring(etree.fromstring(outputText), pretty_print=True)
        self.ui.mathmlOutput.setText(outputText)       
        
    def closeClicked(self):
        self.close()     
            

class MathMLItem(QtGui.QWidget):
    
    def __init__(self, mathml):
        super(MathMLItem, self).__init__()
        
        self.layout = QtGui.QHBoxLayout(self)
        
        # Generate the correct HTML code to display the MathML
        root = etree.Element('html')
        head = etree.SubElement(root, 'head')
        body = etree.SubElement(root, 'body')
        
        mathjaxScript = etree.Element('script')
        mathjaxScript.attrib['type'] = 'text/javascript'
        mathjaxScript.attrib['src'] = 'file:' + urllib.pathname2url(program_path('mathjax/MathJax.js')) + r'?config=TeX-AMS-MML_HTMLorMML.js'
        
        
        head.append(mathjaxScript)
        
        # Use this div to make the text a whole lot bigger
        div = etree.SubElement(body, 'div')
        div.attrib['style'] = r'font-size: 250%'
        
        # Get MathML
        mathML = etree.fromstring(mathml)
        div.append(mathML)
        
        url = temp_path('import')
        baseUrl = QtCore.QUrl.fromLocalFile(url)
        
        # Create the web view
        webView = QWebView()
        webView.setHtml(html.tostring(root), baseUrl)
        
        # Create my widgets
        self.layout.addSpacing(50)
        self.layout.addWidget(webView)
        self.layout.setStretch(0, 1)
        