# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/document_load_progress.ui'
#
# Created: Wed Oct 16 12:37:37 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_DocumentLoadProgressDialog(object):
    def setupUi(self, DocumentLoadProgressDialog):
        DocumentLoadProgressDialog.setObjectName(_fromUtf8("DocumentLoadProgressDialog"))
        DocumentLoadProgressDialog.resize(455, 100)
        font = QtGui.QFont()
        font.setPointSize(12)
        DocumentLoadProgressDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/document_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DocumentLoadProgressDialog.setWindowIcon(icon)
        DocumentLoadProgressDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(DocumentLoadProgressDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DocumentLoadProgressDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(DocumentLoadProgressDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.cancelButton = QtGui.QPushButton(DocumentLoadProgressDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/prepare_speech_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(24, 24))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DocumentLoadProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(DocumentLoadProgressDialog)

    def retranslateUi(self, DocumentLoadProgressDialog):
        DocumentLoadProgressDialog.setWindowTitle(_translate("DocumentLoadProgressDialog", "Loading Document...", None))
        self.label.setText(_translate("DocumentLoadProgressDialog", "Something...", None))
        self.cancelButton.setText(_translate("DocumentLoadProgressDialog", "Cancel", None))

import resource_rc
