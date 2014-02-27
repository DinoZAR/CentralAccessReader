# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/pattern_editor.ui'
#
# Created: Thu Feb 20 15:55:19 2014
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

class Ui_PatternEditor(object):
    def setupUi(self, PatternEditor):
        PatternEditor.setObjectName(_fromUtf8("PatternEditor"))
        PatternEditor.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(PatternEditor)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEditor = QtGui.QPlainTextEdit(PatternEditor)
        self.textEditor.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.textEditor.setObjectName(_fromUtf8("textEditor"))
        self.verticalLayout.addWidget(self.textEditor)

        self.retranslateUi(PatternEditor)
        QtCore.QMetaObject.connectSlotsByName(PatternEditor)

    def retranslateUi(self, PatternEditor):
        PatternEditor.setWindowTitle(_translate("PatternEditor", "Pattern Editor", None))

