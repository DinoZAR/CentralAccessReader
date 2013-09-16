# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_mp3_pages_dialog.ui'
#
# Created: Mon Sep 16 14:39:00 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SaveMP3ByPageDialog(object):
    def setupUi(self, SaveMP3ByPageDialog):
        SaveMP3ByPageDialog.setObjectName("SaveMP3ByPageDialog")
        SaveMP3ByPageDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SaveMP3ByPageDialog.resize(391, 166)
        SaveMP3ByPageDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SaveMP3ByPageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statusLabel = QtGui.QLabel(SaveMP3ByPageDialog)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.statusProgressBar = QtGui.QProgressBar(SaveMP3ByPageDialog)
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setObjectName("statusProgressBar")
        self.verticalLayout.addWidget(self.statusProgressBar)
        self.pageLabel = QtGui.QLabel(SaveMP3ByPageDialog)
        self.pageLabel.setObjectName("pageLabel")
        self.verticalLayout.addWidget(self.pageLabel)
        self.pageProgressBar = QtGui.QProgressBar(SaveMP3ByPageDialog)
        self.pageProgressBar.setProperty("value", 0)
        self.pageProgressBar.setObjectName("pageProgressBar")
        self.verticalLayout.addWidget(self.pageProgressBar)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtGui.QPushButton(SaveMP3ByPageDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/dialog_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SaveMP3ByPageDialog)
        QtCore.QMetaObject.connectSlotsByName(SaveMP3ByPageDialog)

    def retranslateUi(self, SaveMP3ByPageDialog):
        SaveMP3ByPageDialog.setWindowTitle(QtGui.QApplication.translate("SaveMP3ByPageDialog", "Saving By Page", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("SaveMP3ByPageDialog", "Writing to MP3...", None, QtGui.QApplication.UnicodeUTF8))
        self.pageLabel.setText(QtGui.QApplication.translate("SaveMP3ByPageDialog", "Page 1...", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("SaveMP3ByPageDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setShortcut(QtGui.QApplication.translate("SaveMP3ByPageDialog", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
