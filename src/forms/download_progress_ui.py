# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/download_progress.ui'
#
# Created: Fri Sep 13 14:31:11 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DownloadProgressWidget(object):
    def setupUi(self, DownloadProgressWidget):
        DownloadProgressWidget.setObjectName("DownloadProgressWidget")
        DownloadProgressWidget.resize(735, 32)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/update_down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DownloadProgressWidget.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(DownloadProgressWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(DownloadProgressWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.progressBar = QtGui.QProgressBar(DownloadProgressWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.retryButton = QtGui.QPushButton(DownloadProgressWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retryButton.setIcon(icon1)
        self.retryButton.setIconSize(QtCore.QSize(24, 24))
        self.retryButton.setFlat(True)
        self.retryButton.setObjectName("retryButton")
        self.horizontalLayout.addWidget(self.retryButton)
        self.cancelButton = QtGui.QPushButton(DownloadProgressWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/dialog_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QtCore.QSize(24, 24))
        self.cancelButton.setFlat(True)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(DownloadProgressWidget)
        QtCore.QMetaObject.connectSlotsByName(DownloadProgressWidget)

    def retranslateUi(self, DownloadProgressWidget):
        DownloadProgressWidget.setWindowTitle(QtGui.QApplication.translate("DownloadProgressWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DownloadProgressWidget", "Downloading update...", None, QtGui.QApplication.UnicodeUTF8))
        self.retryButton.setText(QtGui.QApplication.translate("DownloadProgressWidget", "Retry", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("DownloadProgressWidget", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
