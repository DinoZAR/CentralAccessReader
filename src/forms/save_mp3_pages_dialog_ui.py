# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_mp3_pages_dialog.ui'
#
# Created: Wed Sep 18 13:29:49 2013
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

class Ui_SaveMP3ByPageDialog(object):
    def setupUi(self, SaveMP3ByPageDialog):
        SaveMP3ByPageDialog.setObjectName(_fromUtf8("SaveMP3ByPageDialog"))
        SaveMP3ByPageDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        SaveMP3ByPageDialog.resize(391, 166)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/text_speak.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SaveMP3ByPageDialog.setWindowIcon(icon)
        SaveMP3ByPageDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SaveMP3ByPageDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.statusLabel = QtGui.QLabel(SaveMP3ByPageDialog)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.verticalLayout.addWidget(self.statusLabel)
        self.statusProgressBar = QtGui.QProgressBar(SaveMP3ByPageDialog)
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setObjectName(_fromUtf8("statusProgressBar"))
        self.verticalLayout.addWidget(self.statusProgressBar)
        self.pageLabel = QtGui.QLabel(SaveMP3ByPageDialog)
        self.pageLabel.setObjectName(_fromUtf8("pageLabel"))
        self.verticalLayout.addWidget(self.pageLabel)
        self.pageProgressBar = QtGui.QProgressBar(SaveMP3ByPageDialog)
        self.pageProgressBar.setProperty("value", 0)
        self.pageProgressBar.setObjectName(_fromUtf8("pageProgressBar"))
        self.verticalLayout.addWidget(self.pageProgressBar)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtGui.QPushButton(SaveMP3ByPageDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/dialog_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SaveMP3ByPageDialog)
        QtCore.QMetaObject.connectSlotsByName(SaveMP3ByPageDialog)

    def retranslateUi(self, SaveMP3ByPageDialog):
        SaveMP3ByPageDialog.setWindowTitle(_translate("SaveMP3ByPageDialog", "Saving By Page", None))
        self.statusLabel.setText(_translate("SaveMP3ByPageDialog", "Writing to MP3...", None))
        self.pageLabel.setText(_translate("SaveMP3ByPageDialog", "Page 1...", None))
        self.cancelButton.setText(_translate("SaveMP3ByPageDialog", "Cancel", None))
        self.cancelButton.setShortcut(_translate("SaveMP3ByPageDialog", "Ctrl+S", None))

import resource_rc
