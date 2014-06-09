'''
Created on Feb 27, 2013

@author: Spencer Graffe
'''

from PyQt4.QtCore import QSize, QUrl, QEvent
from PyQt4.QtGui import QListWidgetItem, QDialog, QHBoxLayout, QWidget
from PyQt4.QtWebKit import QWebView
from lxml import etree

from car.document.html_document import HTMLDocument
from car.forms.mathmlcodesdialog_ui import Ui_MathMLCodesDialog
from car.misc import temp_path

class MathMLCodesDialog(QDialog):
    '''
    A dialog showing a list of all the MathML codes in the document. Very useful
    in debugging which MathML works and which doesn't.
    '''

    def __init__(self, mathmlCodes, parent=None):
        super(MathMLCodesDialog, self).__init__(parent)
        
        self.ui = Ui_MathMLCodesDialog()
        
        self.ui.setupUi(self)
        self.mathmlCodes = mathmlCodes
        
        # Set the items in the list box using WebViews of all of my MathML code
        # Sort the MathML by index
        sortedData = sorted(self.mathmlCodes.items(), key=lambda x: x[1]['index'])
        for data in sortedData:
            myItem = MathMLItem(data[1]['mathml'])
            #item = QListWidgetItem(data[1]['mathml'])
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 100))
            self.ui.mathmlCodesList.addItem(item)
            self.ui.mathmlCodesList.setItemWidget(item, myItem)
        
        self.connect_signals()

    def connect_signals(self):
        self.ui.mathmlCodesList.itemClicked.connect(self.itemClicked)
        self.ui.closeButton.clicked.connect(self.closeClicked)
        
    def itemClicked(self, item):

        widget = self.ui.mathmlCodesList.itemWidget(item)

        outputText = widget.mathml
        outputText = etree.tostring(etree.fromstring(outputText), pretty_print=True)
        self.ui.mathmlOutput.setPlainText(outputText)
        
    def closeClicked(self):
        self.close()
            

class MathMLItem(QWidget):
    
    def __init__(self, mathml):
        super(MathMLItem, self).__init__()
        
        self.layout = QHBoxLayout(self)

        self.mathml = mathml

        self.mathDocument = HTMLDocument(None, None, None, htmlString=self.mathml)
        
        url = temp_path('import')
        baseUrl = QUrl.fromLocalFile(url)
        
        # Create the web view
        webView = QWebView()
        webView.setHtml(self.mathDocument.getMainPage(), baseUrl)
        
        # Create my widgets
        self.layout.addSpacing(50)
        self.layout.addWidget(webView)
        self.layout.setStretch(0, 1)