# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/math_pattern_editor.ui'
#
# Created: Wed Jun 11 15:37:25 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MathPatternEditor(object):
    def setupUi(self, MathPatternEditor):
        MathPatternEditor.setObjectName("MathPatternEditor")
        MathPatternEditor.resize(353, 375)
        self.verticalLayout = QtWidgets.QVBoxLayout(MathPatternEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(MathPatternEditor)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(MathPatternEditor)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QPlainTextEdit(MathPatternEditor)
        self.textEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(MathPatternEditor)
        QtCore.QMetaObject.connectSlotsByName(MathPatternEditor)

    def retranslateUi(self, MathPatternEditor):
        _translate = QtCore.QCoreApplication.translate
        MathPatternEditor.setWindowTitle(_translate("MathPatternEditor", "Math Pattern Editor"))
        self.label.setText(_translate("MathPatternEditor", "Pattern Name:"))

