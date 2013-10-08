# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace\nifty-prose-articulator\src\forms/export_to_html.ui'
#
# Created: Mon Oct 07 16:53:45 2013
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

class Ui_ExportToHtmlDialog(object):
    def setupUi(self, ExportToHtmlDialog):
        ExportToHtmlDialog.setObjectName(_fromUtf8("ExportToHtmlDialog"))
        ExportToHtmlDialog.resize(471, 83)
        font = QtGui.QFont()
        font.setPointSize(12)
        ExportToHtmlDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/CAR_Logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExportToHtmlDialog.setWindowIcon(icon)
        ExportToHtmlDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(ExportToHtmlDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ExportToHtmlDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(ExportToHtmlDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.cancelButton = QtGui.QPushButton(ExportToHtmlDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/prepare_speech_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QtCore.QSize(24, 24))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ExportToHtmlDialog)
        QtCore.QMetaObject.connectSlotsByName(ExportToHtmlDialog)

    def retranslateUi(self, ExportToHtmlDialog):
        ExportToHtmlDialog.setWindowTitle(_translate("ExportToHtmlDialog", "Export to HTML...", None))
        self.label.setText(_translate("ExportToHtmlDialog", "Starting up...", None))
        self.cancelButton.setText(_translate("ExportToHtmlDialog", "Cancel", None))

import resource_rc
