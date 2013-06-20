# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace2\another\src\forms/search_settings.ui'
#
# Created: Thu Jun 20 09:27:08 2013
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

class Ui_SearchSettings(object):
    def setupUi(self, SearchSettings):
        SearchSettings.setObjectName(_fromUtf8("SearchSettings"))
        SearchSettings.resize(181, 148)
        font = QtGui.QFont()
        font.setPointSize(12)
        SearchSettings.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SearchSettings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.wrapCheckBox = QtGui.QCheckBox(SearchSettings)
        self.wrapCheckBox.setObjectName(_fromUtf8("wrapCheckBox"))
        self.verticalLayout.addWidget(self.wrapCheckBox)
        self.wholeWordCheckBox = QtGui.QCheckBox(SearchSettings)
        self.wholeWordCheckBox.setObjectName(_fromUtf8("wholeWordCheckBox"))
        self.verticalLayout.addWidget(self.wholeWordCheckBox)
        self.matchCaseCheckBox = QtGui.QCheckBox(SearchSettings)
        self.matchCaseCheckBox.setObjectName(_fromUtf8("matchCaseCheckBox"))
        self.verticalLayout.addWidget(self.matchCaseCheckBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.okButton = QtGui.QPushButton(SearchSettings)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(SearchSettings)
        QtCore.QMetaObject.connectSlotsByName(SearchSettings)

    def retranslateUi(self, SearchSettings):
        SearchSettings.setWindowTitle(_translate("SearchSettings", "Search Settings", None))
        self.wrapCheckBox.setText(_translate("SearchSettings", "Wrap Search", None))
        self.wholeWordCheckBox.setText(_translate("SearchSettings", "Whole Word", None))
        self.matchCaseCheckBox.setText(_translate("SearchSettings", "Match Case", None))
        self.okButton.setText(_translate("SearchSettings", "OK", None))

