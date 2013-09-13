# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/update_done.ui'
#
# Created: Fri Sep 13 14:31:13 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_UpdateDoneDialog(object):
    def setupUi(self, UpdateDoneDialog):
        UpdateDoneDialog.setObjectName("UpdateDoneDialog")
        UpdateDoneDialog.resize(351, 133)
        font = QtGui.QFont()
        font.setPointSize(12)
        UpdateDoneDialog.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(UpdateDoneDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(UpdateDoneDialog)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/dialog_ok_apply.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label = QtGui.QLabel(UpdateDoneDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(UpdateDoneDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(UpdateDoneDialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(UpdateDoneDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateDoneDialog)

    def retranslateUi(self, UpdateDoneDialog):
        UpdateDoneDialog.setWindowTitle(QtGui.QApplication.translate("UpdateDoneDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("UpdateDoneDialog", "Done!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("UpdateDoneDialog", "You can go back to what you were doing.", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("UpdateDoneDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
