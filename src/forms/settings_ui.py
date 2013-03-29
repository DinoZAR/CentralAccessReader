# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jeff Bolyard\Documents\CS 481\src\forms/settings.ui'
#
# Created: Wed Mar 06 13:22:30 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(559, 454)
        self.layoutWidget = QtGui.QWidget(Settings)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 550, 490))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sVolumeSlider = QtGui.QSlider(self.layoutWidget)
        self.sVolumeSlider.setMaximum(100)
        self.sVolumeSlider.setProperty("value", 99)
        self.sVolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sVolumeSlider.setObjectName(_fromUtf8("sVolumeSlider"))
        self.gridLayout.addWidget(self.sVolumeSlider, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.rateSlider = QtGui.QSlider(self.layoutWidget)
        self.rateSlider.setMinimum(100)
        self.rateSlider.setMaximum(300)
        self.rateSlider.setProperty("value", 200)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setObjectName(_fromUtf8("rateSlider"))
        self.gridLayout.addWidget(self.rateSlider, 0, 2, 1, 1)
        self.rateLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rateLabel.setFont(font)
        self.rateLabel.setObjectName(_fromUtf8("rateLabel"))
        self.gridLayout.addWidget(self.rateLabel, 0, 1, 1, 1)
        self.volumeLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setObjectName(_fromUtf8("volumeLabel"))
        self.gridLayout.addWidget(self.volumeLabel, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.testButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.testButton.setFont(font)
        self.testButton.setIconSize(QtCore.QSize(50, 50))
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.horizontalLayout_2.addWidget(self.testButton)
        self.applyButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.applyButton.setFont(font)
        self.applyButton.setIconSize(QtCore.QSize(50, 50))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout_2.addWidget(self.applyButton)
        self.restoreButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.restoreButton.setFont(font)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.horizontalLayout_2.addWidget(self.restoreButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Settings", None))
        self.label_3.setText(_translate("Settings", "Voices:", None))
        self.label_2.setText(_translate("Settings", "Volume:", None))
        self.sVolumeSlider.setToolTip(_translate("Settings", "Volume slider", None))
        self.label.setText(_translate("Settings", "Words Per Min:", None))
        self.rateSlider.setToolTip(_translate("Settings", "Words per minute slider (rate)", None))
        self.rateLabel.setText(_translate("Settings", "100", None))
        self.volumeLabel.setText(_translate("Settings", "200", None))
        self.comboBox.setToolTip(_translate("Settings", "Drop down box for selecting the voice", None))
        self.label_4.setText(_translate("Settings", "<html><head/><body><p>Test Speech Text</p></body></html>", None))
        self.plainTextEdit.setToolTip(_translate("Settings", "The text entered here is used when the test speech button is pressed", None))
        self.plainTextEdit.setPlainText(_translate("Settings", "This is a test of the current text to speech settings", None))
        self.testButton.setToolTip(_translate("Settings", "Apply and test current speech settings", None))
        self.testButton.setText(_translate("Settings", "Test Speech", None))
        self.applyButton.setToolTip(_translate("Settings", "Apply new speech settings", None))
        self.applyButton.setText(_translate("Settings", "Apply Changes", None))
        self.restoreButton.setToolTip(_translate("Settings", "Restores settings to what they were when you opened the window", None))
        self.restoreButton.setText(_translate("Settings", "Restore Settings", None))

