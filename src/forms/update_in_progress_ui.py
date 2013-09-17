# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/update_in_progress.ui'
#
# Created: Mon Sep 16 16:34:05 2013
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

class Ui_UpdateInstallProgressDialog(object):
    def setupUi(self, UpdateInstallProgressDialog):
        UpdateInstallProgressDialog.setObjectName(_fromUtf8("UpdateInstallProgressDialog"))
        UpdateInstallProgressDialog.resize(324, 71)
        font = QtGui.QFont()
        font.setPointSize(12)
        UpdateInstallProgressDialog.setFont(font)
        self.horizontalLayout = QtGui.QHBoxLayout(UpdateInstallProgressDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.updateIconLabel = QtGui.QLabel(UpdateInstallProgressDialog)
        self.updateIconLabel.setText(_fromUtf8(""))
        self.updateIconLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/update-in-progress.gif")))
        self.updateIconLabel.setObjectName(_fromUtf8("updateIconLabel"))
        self.horizontalLayout.addWidget(self.updateIconLabel)
        self.textLabel = QtGui.QLabel(UpdateInstallProgressDialog)
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.horizontalLayout.addWidget(self.textLabel)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(UpdateInstallProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateInstallProgressDialog)

    def retranslateUi(self, UpdateInstallProgressDialog):
        UpdateInstallProgressDialog.setWindowTitle(_translate("UpdateInstallProgressDialog", "Update In Progress", None))
        self.textLabel.setText(_translate("UpdateInstallProgressDialog", "Update in progress...", None))

import resource_rc
