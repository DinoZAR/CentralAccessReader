# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/math_save_dialog.ui'
#
# Created: Wed Jun 11 15:37:25 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MathSaveDialog(object):
    def setupUi(self, MathSaveDialog):
        MathSaveDialog.setObjectName("MathSaveDialog")
        MathSaveDialog.resize(405, 95)
        self.verticalLayout = QtWidgets.QVBoxLayout(MathSaveDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageLabel = QtWidgets.QLabel(MathSaveDialog)
        self.messageLabel.setWordWrap(True)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout.addWidget(self.messageLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(MathSaveDialog)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.exportButton = QtWidgets.QPushButton(MathSaveDialog)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout.addWidget(self.exportButton)
        self.doNothingButton = QtWidgets.QPushButton(MathSaveDialog)
        self.doNothingButton.setObjectName("doNothingButton")
        self.horizontalLayout.addWidget(self.doNothingButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(MathSaveDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MathSaveDialog)
        QtCore.QMetaObject.connectSlotsByName(MathSaveDialog)

    def retranslateUi(self, MathSaveDialog):
        _translate = QtCore.QCoreApplication.translate
        MathSaveDialog.setWindowTitle(_translate("MathSaveDialog", "Save or Export?"))
        self.messageLabel.setText(_translate("MathSaveDialog", "The message."))
        self.saveButton.setText(_translate("MathSaveDialog", "Save"))
        self.exportButton.setText(_translate("MathSaveDialog", "Export"))
        self.doNothingButton.setText(_translate("MathSaveDialog", "Do Nothing"))
        self.cancelButton.setText(_translate("MathSaveDialog", "Cancel"))

