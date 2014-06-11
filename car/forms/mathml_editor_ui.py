# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/mathml_editor.ui'
#
# Created: Wed Jun 11 15:37:25 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MathMLEditor(object):
    def setupUi(self, MathMLEditor):
        MathMLEditor.setObjectName("MathMLEditor")
        MathMLEditor.resize(547, 560)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MathMLEditor)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(MathMLEditor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textEditor = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.textEditor.setObjectName("textEditor")
        self.verticalLayout_2.addWidget(self.textEditor)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.webView = QtWebKitWidgets.QWebView(self.layoutWidget1)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.refreshMathButton = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshMathButton.sizePolicy().hasHeightForWidth())
        self.refreshMathButton.setSizePolicy(sizePolicy)
        self.refreshMathButton.setObjectName("refreshMathButton")
        self.verticalLayout.addWidget(self.refreshMathButton)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(MathMLEditor)
        QtCore.QMetaObject.connectSlotsByName(MathMLEditor)

    def retranslateUi(self, MathMLEditor):
        _translate = QtCore.QCoreApplication.translate
        MathMLEditor.setWindowTitle(_translate("MathMLEditor", "MathML Editor"))
        self.label.setText(_translate("MathMLEditor", "MathML:"))
        self.label_2.setText(_translate("MathMLEditor", "Display:"))
        self.refreshMathButton.setText(_translate("MathMLEditor", "Refresh Math"))

from PyQt5 import QtWebKitWidgets
