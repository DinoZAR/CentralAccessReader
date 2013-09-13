# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/search_settings.ui'
#
# Created: Fri Sep 13 14:31:12 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SearchSettings(object):
    def setupUi(self, SearchSettings):
        SearchSettings.setObjectName("SearchSettings")
        SearchSettings.resize(184, 121)
        font = QtGui.QFont()
        font.setPointSize(12)
        SearchSettings.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/CAR_Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchSettings.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SearchSettings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.wholeWordCheckBox = QtGui.QCheckBox(SearchSettings)
        self.wholeWordCheckBox.setObjectName("wholeWordCheckBox")
        self.verticalLayout.addWidget(self.wholeWordCheckBox)
        self.matchCaseCheckBox = QtGui.QCheckBox(SearchSettings)
        self.matchCaseCheckBox.setObjectName("matchCaseCheckBox")
        self.verticalLayout.addWidget(self.matchCaseCheckBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.okButton = QtGui.QPushButton(SearchSettings)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(SearchSettings)
        QtCore.QMetaObject.connectSlotsByName(SearchSettings)

    def retranslateUi(self, SearchSettings):
        SearchSettings.setWindowTitle(QtGui.QApplication.translate("SearchSettings", "Search Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.wholeWordCheckBox.setText(QtGui.QApplication.translate("SearchSettings", "Whole Word", None, QtGui.QApplication.UnicodeUTF8))
        self.matchCaseCheckBox.setText(QtGui.QApplication.translate("SearchSettings", "Match Case", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("SearchSettings", "OK", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
