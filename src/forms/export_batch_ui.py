# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/export_batch.ui'
#
# Created: Wed Jan  8 15:43:53 2014
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

class Ui_ExportBatch(object):
    def setupUi(self, ExportBatch):
        ExportBatch.setObjectName(_fromUtf8("ExportBatch"))
        ExportBatch.resize(1090, 332)
        ExportBatch.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icons/CAR_Logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExportBatch.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ExportBatch)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addFilesButton = QtGui.QPushButton(self.centralwidget)
        self.addFilesButton.setObjectName(_fromUtf8("addFilesButton"))
        self.horizontalLayout.addWidget(self.addFilesButton)
        self.setFormatButton = QtGui.QPushButton(self.centralwidget)
        self.setFormatButton.setObjectName(_fromUtf8("setFormatButton"))
        self.horizontalLayout.addWidget(self.setFormatButton)
        self.convertButton = QtGui.QPushButton(self.centralwidget)
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.horizontalLayout.addWidget(self.convertButton)
        self.showFilesButton = QtGui.QPushButton(self.centralwidget)
        self.showFilesButton.setObjectName(_fromUtf8("showFilesButton"))
        self.horizontalLayout.addWidget(self.showFilesButton)
        self.progressLabel = QtGui.QLabel(self.centralwidget)
        self.progressLabel.setText(_fromUtf8(""))
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.horizontalLayout.addWidget(self.progressLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.removeFilesButton = QtGui.QPushButton(self.centralwidget)
        self.removeFilesButton.setObjectName(_fromUtf8("removeFilesButton"))
        self.horizontalLayout.addWidget(self.removeFilesButton)
        self.cancelJobsButton = QtGui.QPushButton(self.centralwidget)
        self.cancelJobsButton.setObjectName(_fromUtf8("cancelJobsButton"))
        self.horizontalLayout.addWidget(self.cancelJobsButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setDefaultSectionSize(300)
        self.verticalLayout.addWidget(self.tableView)
        ExportBatch.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExportBatch)
        QtCore.QMetaObject.connectSlotsByName(ExportBatch)

    def retranslateUi(self, ExportBatch):
        ExportBatch.setWindowTitle(_translate("ExportBatch", "Batch", None))
        self.addFilesButton.setText(_translate("ExportBatch", "Add Files", None))
        self.addFilesButton.setShortcut(_translate("ExportBatch", "Ctrl+O", None))
        self.setFormatButton.setText(_translate("ExportBatch", "Set Format", None))
        self.convertButton.setText(_translate("ExportBatch", "Convert", None))
        self.showFilesButton.setText(_translate("ExportBatch", "Show Files", None))
        self.removeFilesButton.setText(_translate("ExportBatch", "Remove", None))
        self.cancelJobsButton.setText(_translate("ExportBatch", "Cancel", None))

import resource_rc
