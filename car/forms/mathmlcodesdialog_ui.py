# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/mathmlcodesdialog.ui'
#
# Created: Wed Jun 11 15:37:25 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MathMLCodesDialog(object):
    def setupUi(self, MathMLCodesDialog):
        MathMLCodesDialog.setObjectName("MathMLCodesDialog")
        MathMLCodesDialog.resize(626, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/icons/CAR_About.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MathMLCodesDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MathMLCodesDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(MathMLCodesDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName("splitter")
        self.mathmlCodesList = QtWidgets.QListWidget(self.splitter)
        self.mathmlCodesList.setObjectName("mathmlCodesList")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.mathmlOutput = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.mathmlOutput.setObjectName("mathmlOutput")
        self.verticalLayout.addWidget(self.mathmlOutput)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(MathMLCodesDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(MathMLCodesDialog)
        QtCore.QMetaObject.connectSlotsByName(MathMLCodesDialog)

    def retranslateUi(self, MathMLCodesDialog):
        _translate = QtCore.QCoreApplication.translate
        MathMLCodesDialog.setWindowTitle(_translate("MathMLCodesDialog", "MathML In Document"))
        self.label.setText(_translate("MathMLCodesDialog", "MathML:"))
        self.closeButton.setText(_translate("MathMLCodesDialog", "Close"))

import resource_rc
