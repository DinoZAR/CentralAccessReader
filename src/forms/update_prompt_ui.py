# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace2\another\src\forms/update_prompt.ui'
#
# Created: Tue Jun 25 08:43:42 2013
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

class Ui_UpdatePromptDialog(object):
    def setupUi(self, UpdatePromptDialog):
        UpdatePromptDialog.setObjectName(_fromUtf8("UpdatePromptDialog"))
        UpdatePromptDialog.resize(405, 128)
        font = QtGui.QFont()
        font.setPointSize(12)
        UpdatePromptDialog.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(UpdatePromptDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(UpdatePromptDialog)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/update_down_arrow_big.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(UpdatePromptDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(UpdatePromptDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.yesButton = QtGui.QPushButton(UpdatePromptDialog)
        self.yesButton.setObjectName(_fromUtf8("yesButton"))
        self.horizontalLayout_2.addWidget(self.yesButton)
        self.noButton = QtGui.QPushButton(UpdatePromptDialog)
        self.noButton.setObjectName(_fromUtf8("noButton"))
        self.horizontalLayout_2.addWidget(self.noButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(UpdatePromptDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdatePromptDialog)
        UpdatePromptDialog.setTabOrder(self.yesButton, self.noButton)

    def retranslateUi(self, UpdatePromptDialog):
        UpdatePromptDialog.setWindowTitle(_translate("UpdatePromptDialog", "Dialog", None))
        self.label.setText(_translate("UpdatePromptDialog", "Update is Available!", None))
        self.label_3.setText(_translate("UpdatePromptDialog", "Would you like to update the program?", None))
        self.yesButton.setText(_translate("UpdatePromptDialog", "Yes", None))
        self.noButton.setText(_translate("UpdatePromptDialog", "No", None))

import resource_rc
