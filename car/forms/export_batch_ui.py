# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/export_batch.ui'
#
# Created: Wed Jun 11 15:37:24 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportBatch(object):
    def setupUi(self, ExportBatch):
        ExportBatch.setObjectName("ExportBatch")
        ExportBatch.resize(1090, 332)
        ExportBatch.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/icons/CAR_Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExportBatch.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ExportBatch)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addFilesButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFilesButton.setObjectName("addFilesButton")
        self.horizontalLayout.addWidget(self.addFilesButton)
        self.setFormatButton = QtWidgets.QPushButton(self.centralwidget)
        self.setFormatButton.setObjectName("setFormatButton")
        self.horizontalLayout.addWidget(self.setFormatButton)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setObjectName("convertButton")
        self.horizontalLayout.addWidget(self.convertButton)
        self.showFilesButton = QtWidgets.QPushButton(self.centralwidget)
        self.showFilesButton.setObjectName("showFilesButton")
        self.horizontalLayout.addWidget(self.showFilesButton)
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setText("")
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout.addWidget(self.progressLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.removeFilesButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeFilesButton.setObjectName("removeFilesButton")
        self.horizontalLayout.addWidget(self.removeFilesButton)
        self.cancelJobsButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelJobsButton.setObjectName("cancelJobsButton")
        self.horizontalLayout.addWidget(self.cancelJobsButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(300)
        self.verticalLayout.addWidget(self.tableView)
        ExportBatch.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExportBatch)
        QtCore.QMetaObject.connectSlotsByName(ExportBatch)

    def retranslateUi(self, ExportBatch):
        _translate = QtCore.QCoreApplication.translate
        ExportBatch.setWindowTitle(_translate("ExportBatch", "Batch"))
        self.addFilesButton.setText(_translate("ExportBatch", "Add Files"))
        self.addFilesButton.setShortcut(_translate("ExportBatch", "Ctrl+O"))
        self.setFormatButton.setText(_translate("ExportBatch", "Set Format"))
        self.convertButton.setText(_translate("ExportBatch", "Convert"))
        self.showFilesButton.setText(_translate("ExportBatch", "Show Files"))
        self.removeFilesButton.setText(_translate("ExportBatch", "Remove"))
        self.cancelJobsButton.setText(_translate("ExportBatch", "Cancel"))

import resource_rc
