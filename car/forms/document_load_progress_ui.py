# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/document_load_progress.ui'
#
# Created: Wed Jun 11 15:37:24 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DocumentLoadProgressDialog(object):
    def setupUi(self, DocumentLoadProgressDialog):
        DocumentLoadProgressDialog.setObjectName("DocumentLoadProgressDialog")
        DocumentLoadProgressDialog.resize(455, 100)
        font = QtGui.QFont()
        font.setPointSize(12)
        DocumentLoadProgressDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/classic/icons/add_document_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DocumentLoadProgressDialog.setWindowIcon(icon)
        DocumentLoadProgressDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DocumentLoadProgressDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DocumentLoadProgressDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(DocumentLoadProgressDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.cancelButton = QtWidgets.QPushButton(DocumentLoadProgressDialog)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 32))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DocumentLoadProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(DocumentLoadProgressDialog)

    def retranslateUi(self, DocumentLoadProgressDialog):
        _translate = QtCore.QCoreApplication.translate
        DocumentLoadProgressDialog.setWindowTitle(_translate("DocumentLoadProgressDialog", "Loading Document..."))
        self.label.setText(_translate("DocumentLoadProgressDialog", "Something..."))
        self.cancelButton.setText(_translate("DocumentLoadProgressDialog", "Cancel"))

import resource_rc
