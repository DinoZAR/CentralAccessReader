# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace\nifty-prose-articulator\src\forms/download_progress.ui'
#
# Created: Tue Jan 07 09:31:58 2014
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
        DownloadProgressWidget.resize(735, 33)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/update_down_arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DownloadProgressWidget.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(DownloadProgressWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(DownloadProgressWidget)
        self.label.setMargin(7)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.progressBar = QtGui.QProgressBar(DownloadProgressWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.downloadRetryButton = QtGui.QPushButton(DownloadProgressWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/reload_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadRetryButton.setIcon(icon1)
        self.downloadRetryButton.setIconSize(QtCore.QSize(24, 24))
        self.downloadRetryButton.setFlat(True)
        self.downloadRetryButton.setObjectName(_fromUtf8("downloadRetryButton"))
        self.horizontalLayout.addWidget(self.downloadRetryButton)
        self.downloadCancelButton = QtGui.QPushButton(DownloadProgressWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/close_with_circle_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadCancelButton.setIcon(icon2)
        self.downloadCancelButton.setIconSize(QtCore.QSize(24, 24))
        self.downloadCancelButton.setFlat(True)
        self.downloadCancelButton.setObjectName(_fromUtf8("downloadCancelButton"))
        self.horizontalLayout.addWidget(self.downloadCancelButton)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(DownloadProgressWidget)
        QtCore.QMetaObject.connectSlotsByName(DownloadProgressWidget)

    def retranslateUi(self, DownloadProgressWidget):
        DownloadProgressWidget.setWindowTitle(_translate("DownloadProgressWidget", "Form", None))
        self.label.setText(_translate("DownloadProgressWidget", "Downloading update...", None))
        self.downloadRetryButton.setText(_translate("DownloadProgressWidget", "Retry", None))
        self.downloadCancelButton.setText(_translate("DownloadProgressWidget", "Cancel", None))

import resource_rc
