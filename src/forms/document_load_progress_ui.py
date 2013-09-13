# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/document_load_progress.ui'
#
# Created: Fri Sep 13 14:31:11 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DocumentLoadProgressDialog(object):
    def setupUi(self, DocumentLoadProgressDialog):
        DocumentLoadProgressDialog.setObjectName("DocumentLoadProgressDialog")
        DocumentLoadProgressDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        DocumentLoadProgressDialog.resize(443, 100)
        font = QtGui.QFont()
        font.setPointSize(12)
        DocumentLoadProgressDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/document_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DocumentLoadProgressDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DocumentLoadProgressDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(DocumentLoadProgressDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtGui.QProgressBar(DocumentLoadProgressDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.cancelButton = QtGui.QPushButton(DocumentLoadProgressDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/prepare_speech_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(24, 24))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(DocumentLoadProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(DocumentLoadProgressDialog)

    def retranslateUi(self, DocumentLoadProgressDialog):
        DocumentLoadProgressDialog.setWindowTitle(QtGui.QApplication.translate("DocumentLoadProgressDialog", "Loading Document...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DocumentLoadProgressDialog", "Something...", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("DocumentLoadProgressDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
