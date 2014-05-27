# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/about.ui'
#
# Created: Tue May 27 09:27:23 2014
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

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(666, 309)
        font = QtGui.QFont()
        font.setPointSize(12)
        AboutDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icons/CAR_About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.logoLabel = QtGui.QLabel(AboutDialog)
        self.logoLabel.setText(_fromUtf8(""))
        self.logoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/all/icons/CAR_About.png")))
        self.logoLabel.setObjectName(_fromUtf8("logoLabel"))
        self.horizontalLayout_2.addWidget(self.logoLabel)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(AboutDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.versionLabel = QtGui.QLabel(AboutDialog)
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.horizontalLayout.addWidget(self.versionLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(AboutDialog)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_7 = QtGui.QLabel(AboutDialog)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        spacerItem2 = QtGui.QSpacerItem(20, 39, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About", None))
        self.label.setText(_translate("AboutDialog", "Central Access Reader", None))
        self.label_3.setText(_translate("AboutDialog", "Version:", None))
        self.versionLabel.setText(_translate("AboutDialog", "(something)", None))
        self.label_2.setText(_translate("AboutDialog", "Central Washington University", None))
        self.label_4.setText(_translate("AboutDialog", "<html><head/><body><p>Author: <a href=\"http://www.cwu.edu/central-access/developer-bio\"><span style=\" text-decoration: underline; color:#0000ff;\">Spencer Graffe</span></a></p></body></html>", None))
        self.label_7.setText(_translate("AboutDialog", "<html><head/><body><p>Contributers: <a href=\"http://www.cwu.edu/central-access/developer-bio\"><span style=\" text-decoration: underline; color:#0000ff;\">Justin Wilson</span></a></p></body></html>", None))

import resource_rc
