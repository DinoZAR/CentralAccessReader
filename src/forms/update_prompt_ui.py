# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/update_prompt.ui'
#
# Created: Fri Sep 13 14:31:13 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_UpdatePromptDialog(object):
    def setupUi(self, UpdatePromptDialog):
        UpdatePromptDialog.setObjectName("UpdatePromptDialog")
        UpdatePromptDialog.resize(439, 164)
        font = QtGui.QFont()
        font.setPointSize(12)
        UpdatePromptDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/update_down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdatePromptDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(UpdatePromptDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(UpdatePromptDialog)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/update_down_arrow_big.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(UpdatePromptDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.contentText = QtGui.QLabel(UpdatePromptDialog)
        self.contentText.setWordWrap(True)
        self.contentText.setObjectName("contentText")
        self.verticalLayout_3.addWidget(self.contentText)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.yesButton = QtGui.QPushButton(UpdatePromptDialog)
        self.yesButton.setObjectName("yesButton")
        self.verticalLayout.addWidget(self.yesButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.noButton = QtGui.QPushButton(UpdatePromptDialog)
        self.noButton.setObjectName("noButton")
        self.verticalLayout_2.addWidget(self.noButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(UpdatePromptDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdatePromptDialog)
        UpdatePromptDialog.setTabOrder(self.noButton, self.yesButton)

    def retranslateUi(self, UpdatePromptDialog):
        UpdatePromptDialog.setWindowTitle(QtGui.QApplication.translate("UpdatePromptDialog", "Install Update", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("UpdatePromptDialog", "Update is Available!", None, QtGui.QApplication.UnicodeUTF8))
        self.contentText.setText(QtGui.QApplication.translate("UpdatePromptDialog", "Would you like to download it?", None, QtGui.QApplication.UnicodeUTF8))
        self.yesButton.setText(QtGui.QApplication.translate("UpdatePromptDialog", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.noButton.setText(QtGui.QApplication.translate("UpdatePromptDialog", "No", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
