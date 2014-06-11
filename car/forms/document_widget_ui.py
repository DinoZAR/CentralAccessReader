# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/document_widget.ui'
#
# Created: Wed Jun 11 15:37:24 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DocumentWidget(object):
    def setupUi(self, DocumentWidget):
        DocumentWidget.setObjectName("DocumentWidget")
        DocumentWidget.resize(651, 574)
        self.verticalLayout = QtWidgets.QVBoxLayout(DocumentWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchPrevious = QtWidgets.QPushButton(DocumentWidget)
        self.searchPrevious.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/classic/icons/up_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchPrevious.setIcon(icon)
        self.searchPrevious.setIconSize(QtCore.QSize(32, 32))
        self.searchPrevious.setFlat(True)
        self.searchPrevious.setObjectName("searchPrevious")
        self.horizontalLayout.addWidget(self.searchPrevious)
        self.searchNext = QtWidgets.QPushButton(DocumentWidget)
        self.searchNext.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/classic/icons/down_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchNext.setIcon(icon1)
        self.searchNext.setIconSize(QtCore.QSize(32, 32))
        self.searchNext.setFlat(True)
        self.searchNext.setObjectName("searchNext")
        self.horizontalLayout.addWidget(self.searchNext)
        self.searchBox = QtWidgets.QLineEdit(DocumentWidget)
        self.searchBox.setObjectName("searchBox")
        self.horizontalLayout.addWidget(self.searchBox)
        self.searchSettingsButton = QtWidgets.QPushButton(DocumentWidget)
        self.searchSettingsButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/classic/icons/search_settings_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchSettingsButton.setIcon(icon2)
        self.searchSettingsButton.setIconSize(QtCore.QSize(32, 32))
        self.searchSettingsButton.setFlat(True)
        self.searchSettingsButton.setObjectName("searchSettingsButton")
        self.horizontalLayout.addWidget(self.searchSettingsButton)
        self.searchCloseButton = QtWidgets.QPushButton(DocumentWidget)
        self.searchCloseButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/classic/icons/close_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchCloseButton.setIcon(icon3)
        self.searchCloseButton.setIconSize(QtCore.QSize(32, 32))
        self.searchCloseButton.setFlat(True)
        self.searchCloseButton.setObjectName("searchCloseButton")
        self.horizontalLayout.addWidget(self.searchCloseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = NPAWebView(DocumentWidget)
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressLabel = QtWidgets.QLabel(DocumentWidget)
        self.progressLabel.setMinimumSize(QtCore.QSize(200, 0))
        self.progressLabel.setContentsMargins(10, 10, 10, 10)
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout_2.addWidget(self.progressLabel)
        self.progressBar = QtWidgets.QProgressBar(DocumentWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.progressCancelButton = QtWidgets.QPushButton(DocumentWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/classic/icons/close_with_circle_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.progressCancelButton.setIcon(icon4)
        self.progressCancelButton.setIconSize(QtCore.QSize(24, 24))
        self.progressCancelButton.setFlat(True)
        self.progressCancelButton.setObjectName("progressCancelButton")
        self.horizontalLayout_2.addWidget(self.progressCancelButton)
        self.showFilesButton = QtWidgets.QPushButton(DocumentWidget)
        self.showFilesButton.setObjectName("showFilesButton")
        self.horizontalLayout_2.addWidget(self.showFilesButton)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(DocumentWidget)
        QtCore.QMetaObject.connectSlotsByName(DocumentWidget)

    def retranslateUi(self, DocumentWidget):
        _translate = QtCore.QCoreApplication.translate
        DocumentWidget.setWindowTitle(_translate("DocumentWidget", "Form"))
        self.progressLabel.setText(_translate("DocumentWidget", "Exporting page 179 of 210..."))
        self.showFilesButton.setText(_translate("DocumentWidget", "Show Files"))

from car.gui.npa_webview import NPAWebView
import resource_rc
