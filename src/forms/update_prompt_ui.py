# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/update_prompt.ui'
#
# Created: Mon Sep 16 16:34:05 2013
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

class Ui_UpdatePromptDialog(object):
    def setupUi(self, UpdatePromptDialog):
        UpdatePromptDialog.setObjectName(_fromUtf8("UpdatePromptDialog"))
        UpdatePromptDialog.resize(439, 164)
        font = QtGui.QFont()
        font.setPointSize(12)
        UpdatePromptDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/update_down_arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdatePromptDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(UpdatePromptDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
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
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.contentText = QtGui.QLabel(UpdatePromptDialog)
        self.contentText.setWordWrap(True)
        self.contentText.setObjectName(_fromUtf8("contentText"))
        self.verticalLayout_3.addWidget(self.contentText)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.yesButton = QtGui.QPushButton(UpdatePromptDialog)
        self.yesButton.setObjectName(_fromUtf8("yesButton"))
        self.verticalLayout.addWidget(self.yesButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.noButton = QtGui.QPushButton(UpdatePromptDialog)
        self.noButton.setObjectName(_fromUtf8("noButton"))
        self.verticalLayout_2.addWidget(self.noButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(UpdatePromptDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdatePromptDialog)
        UpdatePromptDialog.setTabOrder(self.noButton, self.yesButton)

    def retranslateUi(self, UpdatePromptDialog):
        UpdatePromptDialog.setWindowTitle(_translate("UpdatePromptDialog", "Install Update", None))
        self.label.setText(_translate("UpdatePromptDialog", "Update is Available!", None))
        self.contentText.setText(_translate("UpdatePromptDialog", "Would you like to download it?", None))
        self.yesButton.setText(_translate("UpdatePromptDialog", "Yes", None))
        self.noButton.setText(_translate("UpdatePromptDialog", "No", None))

import resource_rc
