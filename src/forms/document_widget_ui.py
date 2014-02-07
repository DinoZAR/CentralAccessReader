# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/document_widget.ui'
#
# Created: Fri Feb 07 09:32:36 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_DocumentWidget(object):
    def setupUi(self, DocumentWidget):
        DocumentWidget.setObjectName(_fromUtf8("DocumentWidget"))
        DocumentWidget.resize(651, 574)
        self.verticalLayout = QtGui.QVBoxLayout(DocumentWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchPrevious = QtGui.QPushButton(DocumentWidget)
        self.searchPrevious.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/up_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchPrevious.setIcon(icon)
        self.searchPrevious.setIconSize(QtCore.QSize(32, 32))
        self.searchPrevious.setFlat(True)
        self.searchPrevious.setObjectName(_fromUtf8("searchPrevious"))
        self.horizontalLayout.addWidget(self.searchPrevious)
        self.searchNext = QtGui.QPushButton(DocumentWidget)
        self.searchNext.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/down_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchNext.setIcon(icon1)
        self.searchNext.setIconSize(QtCore.QSize(32, 32))
        self.searchNext.setFlat(True)
        self.searchNext.setObjectName(_fromUtf8("searchNext"))
        self.horizontalLayout.addWidget(self.searchNext)
        self.searchBox = QtGui.QLineEdit(DocumentWidget)
        self.searchBox.setObjectName(_fromUtf8("searchBox"))
        self.horizontalLayout.addWidget(self.searchBox)
        self.searchSettingsButton = QtGui.QPushButton(DocumentWidget)
        self.searchSettingsButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/search_settings_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchSettingsButton.setIcon(icon2)
        self.searchSettingsButton.setIconSize(QtCore.QSize(32, 32))
        self.searchSettingsButton.setFlat(True)
        self.searchSettingsButton.setObjectName(_fromUtf8("searchSettingsButton"))
        self.horizontalLayout.addWidget(self.searchSettingsButton)
        self.searchCloseButton = QtGui.QPushButton(DocumentWidget)
        self.searchCloseButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/close_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchCloseButton.setIcon(icon3)
        self.searchCloseButton.setIconSize(QtCore.QSize(32, 32))
        self.searchCloseButton.setFlat(True)
        self.searchCloseButton.setObjectName(_fromUtf8("searchCloseButton"))
        self.horizontalLayout.addWidget(self.searchCloseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = NPAWebView(DocumentWidget)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.progressLabel = QtGui.QLabel(DocumentWidget)
        self.progressLabel.setMinimumSize(QtCore.QSize(200, 0))
        self.progressLabel.setMargin(10)
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.horizontalLayout_2.addWidget(self.progressLabel)
        self.progressBar = QtGui.QProgressBar(DocumentWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.progressCancelButton = QtGui.QPushButton(DocumentWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/close_with_circle_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.progressCancelButton.setIcon(icon4)
        self.progressCancelButton.setIconSize(QtCore.QSize(24, 24))
        self.progressCancelButton.setFlat(True)
        self.progressCancelButton.setObjectName(_fromUtf8("progressCancelButton"))
        self.horizontalLayout_2.addWidget(self.progressCancelButton)
        self.showFilesButton = QtGui.QPushButton(DocumentWidget)
        self.showFilesButton.setObjectName(_fromUtf8("showFilesButton"))
        self.horizontalLayout_2.addWidget(self.showFilesButton)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(DocumentWidget)
        QtCore.QMetaObject.connectSlotsByName(DocumentWidget)

    def retranslateUi(self, DocumentWidget):
        DocumentWidget.setWindowTitle(_translate("DocumentWidget", "Form", None))
        self.progressLabel.setText(_translate("DocumentWidget", "Exporting page 179 of 210...", None))
        self.showFilesButton.setText(_translate("DocumentWidget", "Show Files", None))

from gui.npa_webview import NPAWebView
import resource_rc
