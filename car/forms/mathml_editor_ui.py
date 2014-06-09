# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car\forms/mathml_editor.ui'
#
# Created: Thu Jun 05 15:43:31 2014
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
        MathMLEditor.resize(547, 560)
        self.verticalLayout_3 = QtGui.QVBoxLayout(MathMLEditor)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(MathMLEditor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.textEditor = QtGui.QPlainTextEdit(self.layoutWidget)
        self.textEditor.setObjectName(_fromUtf8("textEditor"))
        self.verticalLayout_2.addWidget(self.textEditor)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.webView = QtWebKit.QWebView(self.layoutWidget1)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.refreshMathButton = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshMathButton.sizePolicy().hasHeightForWidth())
        self.refreshMathButton.setSizePolicy(sizePolicy)
        self.refreshMathButton.setObjectName(_fromUtf8("refreshMathButton"))
        self.verticalLayout.addWidget(self.refreshMathButton)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(MathMLEditor)
        QtCore.QMetaObject.connectSlotsByName(MathMLEditor)

    def retranslateUi(self, MathMLEditor):
        MathMLEditor.setWindowTitle(_translate("MathMLEditor", "MathML Editor", None))
        self.label.setText(_translate("MathMLEditor", "MathML:", None))
        self.label_2.setText(_translate("MathMLEditor", "Display:", None))
        self.refreshMathButton.setText(_translate("MathMLEditor", "Refresh Math", None))

from PyQt4 import QtWebKit
