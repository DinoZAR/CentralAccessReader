# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/search_settings.ui'
#
# Created: Wed Jun 11 15:37:26 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchSettings(object):
    def setupUi(self, SearchSettings):
        SearchSettings.setObjectName("SearchSettings")
        SearchSettings.resize(184, 136)
        font = QtGui.QFont()
        font.setPointSize(12)
        SearchSettings.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/icons/CAR_Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchSettings.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SearchSettings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.wholeWordCheckBox = QtWidgets.QCheckBox(SearchSettings)
        self.wholeWordCheckBox.setObjectName("wholeWordCheckBox")
        self.verticalLayout.addWidget(self.wholeWordCheckBox)
        self.matchCaseCheckBox = QtWidgets.QCheckBox(SearchSettings)
        self.matchCaseCheckBox.setObjectName("matchCaseCheckBox")
        self.verticalLayout.addWidget(self.matchCaseCheckBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.okButton = QtWidgets.QPushButton(SearchSettings)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(SearchSettings)
        QtCore.QMetaObject.connectSlotsByName(SearchSettings)

    def retranslateUi(self, SearchSettings):
        _translate = QtCore.QCoreApplication.translate
        SearchSettings.setWindowTitle(_translate("SearchSettings", "Search Settings"))
        self.wholeWordCheckBox.setText(_translate("SearchSettings", "Whole Word"))
        self.matchCaseCheckBox.setText(_translate("SearchSettings", "Match Case"))
        self.okButton.setText(_translate("SearchSettings", "OK"))

import resource_rc
