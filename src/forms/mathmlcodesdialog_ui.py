# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/mathmlcodesdialog.ui'
#
# Created: Fri Sep 13 14:31:11 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MathMLCodesDialog(object):
    def setupUi(self, MathMLCodesDialog):
        MathMLCodesDialog.setObjectName("MathMLCodesDialog")
        MathMLCodesDialog.resize(626, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/CAR_Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MathMLCodesDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(MathMLCodesDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtGui.QSplitter(MathMLCodesDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName("splitter")
        self.mathmlCodesList = QtGui.QListWidget(self.splitter)
        self.mathmlCodesList.setObjectName("mathmlCodesList")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.mathmlOutput = QtGui.QTextEdit(self.layoutWidget)
        self.mathmlOutput.setReadOnly(True)
        self.mathmlOutput.setObjectName("mathmlOutput")
        self.verticalLayout.addWidget(self.mathmlOutput)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(MathMLCodesDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(MathMLCodesDialog)
        QtCore.QMetaObject.connectSlotsByName(MathMLCodesDialog)

    def retranslateUi(self, MathMLCodesDialog):
        MathMLCodesDialog.setWindowTitle(QtGui.QApplication.translate("MathMLCodesDialog", "MathML Codes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MathMLCodesDialog", "MathML Code:", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("MathMLCodesDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
