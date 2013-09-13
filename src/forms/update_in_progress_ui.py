# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/update_in_progress.ui'
#
# Created: Fri Sep 13 14:31:13 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_UpdateInstallProgressDialog(object):
    def setupUi(self, UpdateInstallProgressDialog):
        UpdateInstallProgressDialog.setObjectName("UpdateInstallProgressDialog")
        UpdateInstallProgressDialog.resize(324, 71)
        font = QtGui.QFont()
        font.setPointSize(12)
        UpdateInstallProgressDialog.setFont(font)
        self.horizontalLayout = QtGui.QHBoxLayout(UpdateInstallProgressDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.updateIconLabel = QtGui.QLabel(UpdateInstallProgressDialog)
        self.updateIconLabel.setText("")
        self.updateIconLabel.setPixmap(QtGui.QPixmap(":/icons/icons/update-in-progress.gif"))
        self.updateIconLabel.setObjectName("updateIconLabel")
        self.horizontalLayout.addWidget(self.updateIconLabel)
        self.textLabel = QtGui.QLabel(UpdateInstallProgressDialog)
        self.textLabel.setObjectName("textLabel")
        self.horizontalLayout.addWidget(self.textLabel)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(UpdateInstallProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateInstallProgressDialog)

    def retranslateUi(self, UpdateInstallProgressDialog):
        UpdateInstallProgressDialog.setWindowTitle(QtGui.QApplication.translate("UpdateInstallProgressDialog", "Update In Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel.setText(QtGui.QApplication.translate("UpdateInstallProgressDialog", "Update in progress...", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
