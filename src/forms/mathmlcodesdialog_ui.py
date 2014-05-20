# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/mathmlcodesdialog.ui'
#
# Created: Tue May 20 14:48:32 2014
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

class Ui_MathMLCodesDialog(object):
    def setupUi(self, MathMLCodesDialog):
        MathMLCodesDialog.setObjectName(_fromUtf8("MathMLCodesDialog"))
        MathMLCodesDialog.resize(626, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/CAR_Logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MathMLCodesDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(MathMLCodesDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(MathMLCodesDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.mathmlCodesList = QtGui.QListWidget(self.splitter)
        self.mathmlCodesList.setObjectName(_fromUtf8("mathmlCodesList"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.mathmlOutput = QtGui.QTextEdit(self.layoutWidget)
        self.mathmlOutput.setReadOnly(True)
        self.mathmlOutput.setObjectName(_fromUtf8("mathmlOutput"))
        self.verticalLayout.addWidget(self.mathmlOutput)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(MathMLCodesDialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(MathMLCodesDialog)
        QtCore.QMetaObject.connectSlotsByName(MathMLCodesDialog)

    def retranslateUi(self, MathMLCodesDialog):
        MathMLCodesDialog.setWindowTitle(_translate("MathMLCodesDialog", "MathML Codes", None))
        self.label.setText(_translate("MathMLCodesDialog", "MathML Code:", None))
        self.closeButton.setText(_translate("MathMLCodesDialog", "Close", None))

import resource_rc
