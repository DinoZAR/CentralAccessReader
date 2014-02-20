# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/mathml_editor.ui'
#
# Created: Thu Feb 20 14:59:16 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MathMLEditor(object):
    def setupUi(self, MathMLEditor):
        MathMLEditor.setObjectName(_fromUtf8("MathMLEditor"))
        MathMLEditor.resize(388, 420)
        self.verticalLayout_2 = QtGui.QVBoxLayout(MathMLEditor)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(MathMLEditor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.textEditor = QtGui.QPlainTextEdit(self.splitter)
        self.textEditor.setObjectName(_fromUtf8("textEditor"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.webView = QtWebKit.QWebView(self.widget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.refreshMathButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshMathButton.sizePolicy().hasHeightForWidth())
        self.refreshMathButton.setSizePolicy(sizePolicy)
        self.refreshMathButton.setObjectName(_fromUtf8("refreshMathButton"))
        self.verticalLayout.addWidget(self.refreshMathButton)
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(MathMLEditor)
        QtCore.QMetaObject.connectSlotsByName(MathMLEditor)

    def retranslateUi(self, MathMLEditor):
        MathMLEditor.setWindowTitle(_translate("MathMLEditor", "MathML Editor", None))
        self.refreshMathButton.setText(_translate("MathMLEditor", "Refresh Math", None))

from PyQt4 import QtWebKit
