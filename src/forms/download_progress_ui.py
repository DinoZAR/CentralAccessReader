# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/download_progress.ui'
#
# Created: Mon Sep 16 16:34:04 2013
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

class Ui_DownloadProgressWidget(object):
    def setupUi(self, DownloadProgressWidget):
        DownloadProgressWidget.setObjectName(_fromUtf8("DownloadProgressWidget"))
        DownloadProgressWidget.resize(735, 32)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/update_down_arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DownloadProgressWidget.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(DownloadProgressWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(DownloadProgressWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.progressBar = QtGui.QProgressBar(DownloadProgressWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.retryButton = QtGui.QPushButton(DownloadProgressWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retryButton.setIcon(icon1)
        self.retryButton.setIconSize(QtCore.QSize(24, 24))
        self.retryButton.setFlat(True)
        self.retryButton.setObjectName(_fromUtf8("retryButton"))
        self.horizontalLayout.addWidget(self.retryButton)
        self.cancelButton = QtGui.QPushButton(DownloadProgressWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/dialog_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QtCore.QSize(24, 24))
        self.cancelButton.setFlat(True)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(DownloadProgressWidget)
        QtCore.QMetaObject.connectSlotsByName(DownloadProgressWidget)

    def retranslateUi(self, DownloadProgressWidget):
        DownloadProgressWidget.setWindowTitle(_translate("DownloadProgressWidget", "Form", None))
        self.label.setText(_translate("DownloadProgressWidget", "Downloading update...", None))
        self.retryButton.setText(_translate("DownloadProgressWidget", "Retry", None))
        self.cancelButton.setText(_translate("DownloadProgressWidget", "Cancel", None))

import resource_rc
