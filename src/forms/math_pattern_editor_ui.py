# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/math_pattern_editor.ui'
#
# Created: Wed May 28 11:56:24 2014
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

class Ui_MathPatternEditor(object):
    def setupUi(self, MathPatternEditor):
        MathPatternEditor.setObjectName(_fromUtf8("MathPatternEditor"))
        MathPatternEditor.resize(353, 375)
        self.verticalLayout = QtGui.QVBoxLayout(MathPatternEditor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(MathPatternEditor)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtGui.QLineEdit(MathPatternEditor)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtGui.QPlainTextEdit(MathPatternEditor)
        self.textEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(MathPatternEditor)
        QtCore.QMetaObject.connectSlotsByName(MathPatternEditor)

    def retranslateUi(self, MathPatternEditor):
        MathPatternEditor.setWindowTitle(_translate("MathPatternEditor", "Math Pattern Editor", None))
        self.label.setText(_translate("MathPatternEditor", "Pattern Name:", None))

