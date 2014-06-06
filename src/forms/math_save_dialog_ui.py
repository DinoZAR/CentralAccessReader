# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/math_save_dialog.ui'
#
# Created: Fri Jun 06 10:51:47 2014
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

class Ui_MathSaveDialog(object):
    def setupUi(self, MathSaveDialog):
        MathSaveDialog.setObjectName(_fromUtf8("MathSaveDialog"))
        MathSaveDialog.resize(405, 95)
        self.verticalLayout = QtGui.QVBoxLayout(MathSaveDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.messageLabel = QtGui.QLabel(MathSaveDialog)
        self.messageLabel.setWordWrap(True)
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.verticalLayout.addWidget(self.messageLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveButton = QtGui.QPushButton(MathSaveDialog)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.exportButton = QtGui.QPushButton(MathSaveDialog)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout.addWidget(self.exportButton)
        self.doNothingButton = QtGui.QPushButton(MathSaveDialog)
        self.doNothingButton.setObjectName(_fromUtf8("doNothingButton"))
        self.horizontalLayout.addWidget(self.doNothingButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(MathSaveDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MathSaveDialog)
        QtCore.QMetaObject.connectSlotsByName(MathSaveDialog)

    def retranslateUi(self, MathSaveDialog):
        MathSaveDialog.setWindowTitle(_translate("MathSaveDialog", "Save or Export?", None))
        self.messageLabel.setText(_translate("MathSaveDialog", "The message.", None))
        self.saveButton.setText(_translate("MathSaveDialog", "Save", None))
        self.exportButton.setText(_translate("MathSaveDialog", "Export", None))
        self.doNothingButton.setText(_translate("MathSaveDialog", "Do Nothing", None))
        self.cancelButton.setText(_translate("MathSaveDialog", "Cancel", None))

