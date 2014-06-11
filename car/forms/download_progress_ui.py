# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/download_progress.ui'
#
# Created: Wed Jun 11 15:37:24 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadProgressWidget(object):
    def setupUi(self, DownloadProgressWidget):
        DownloadProgressWidget.setObjectName("DownloadProgressWidget")
        DownloadProgressWidget.resize(735, 33)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/update_down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DownloadProgressWidget.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DownloadProgressWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(DownloadProgressWidget)
        self.label.setContentsMargins(7, 7, 7, 7)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(DownloadProgressWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.downloadRetryButton = QtWidgets.QPushButton(DownloadProgressWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/classic/icons/reload_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadRetryButton.setIcon(icon1)
        self.downloadRetryButton.setIconSize(QtCore.QSize(24, 24))
        self.downloadRetryButton.setFlat(True)
        self.downloadRetryButton.setObjectName("downloadRetryButton")
        self.horizontalLayout.addWidget(self.downloadRetryButton)
        self.downloadCancelButton = QtWidgets.QPushButton(DownloadProgressWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/classic/icons/close_with_circle_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadCancelButton.setIcon(icon2)
        self.downloadCancelButton.setIconSize(QtCore.QSize(24, 24))
        self.downloadCancelButton.setFlat(True)
        self.downloadCancelButton.setObjectName("downloadCancelButton")
        self.horizontalLayout.addWidget(self.downloadCancelButton)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(DownloadProgressWidget)
        QtCore.QMetaObject.connectSlotsByName(DownloadProgressWidget)

    def retranslateUi(self, DownloadProgressWidget):
        _translate = QtCore.QCoreApplication.translate
        DownloadProgressWidget.setWindowTitle(_translate("DownloadProgressWidget", "Form"))
        self.label.setText(_translate("DownloadProgressWidget", "Downloading update..."))
        self.downloadRetryButton.setText(_translate("DownloadProgressWidget", "Retry"))
        self.downloadCancelButton.setText(_translate("DownloadProgressWidget", "Cancel"))

import resource_rc
