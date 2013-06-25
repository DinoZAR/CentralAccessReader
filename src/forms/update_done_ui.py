# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace2\another\src\forms/update_done.ui'
#
# Created: Tue Jun 25 08:39:25 2013
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

class Ui_UpdateDoneDialog(object):
    def setupUi(self, UpdateDoneDialog):
        UpdateDoneDialog.setObjectName(_fromUtf8("UpdateDoneDialog"))
        UpdateDoneDialog.resize(351, 133)
        font = QtGui.QFont()
        font.setPointSize(12)
        UpdateDoneDialog.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(UpdateDoneDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(UpdateDoneDialog)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/dialog_ok_apply.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label = QtGui.QLabel(UpdateDoneDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(UpdateDoneDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(UpdateDoneDialog)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(UpdateDoneDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateDoneDialog)

    def retranslateUi(self, UpdateDoneDialog):
        UpdateDoneDialog.setWindowTitle(_translate("UpdateDoneDialog", "Dialog", None))
        self.label.setText(_translate("UpdateDoneDialog", "Done!", None))
        self.label_2.setText(_translate("UpdateDoneDialog", "You can go back to what you were doing.", None))
        self.okButton.setText(_translate("UpdateDoneDialog", "OK", None))

import resource_rc
