# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace2\another\src\forms/speech_settings.ui'
#
# Created: Mon May 06 09:28:19 2013
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

class Ui_SpeechSettings(object):
    def setupUi(self, SpeechSettings):
        SpeechSettings.setObjectName(_fromUtf8("SpeechSettings"))
        SpeechSettings.resize(492, 318)
        font = QtGui.QFont()
        font.setPointSize(12)
        SpeechSettings.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(SpeechSettings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rateSlider = QtGui.QSlider(SpeechSettings)
        self.rateSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.rateSlider.setMinimum(0)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 50)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.rateSlider.setTickInterval(10)
        self.rateSlider.setObjectName(_fromUtf8("rateSlider"))
        self.gridLayout.addWidget(self.rateSlider, 0, 1, 1, 1)
        self.label = QtGui.QLabel(SpeechSettings)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(SpeechSettings)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(SpeechSettings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(SpeechSettings)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.volumeSlider = QtGui.QSlider(SpeechSettings)
        self.volumeSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.gridLayout.addWidget(self.volumeSlider, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.testSpeechText = QtGui.QPlainTextEdit(SpeechSettings)
        self.testSpeechText.setObjectName(_fromUtf8("testSpeechText"))
        self.horizontalLayout_2.addWidget(self.testSpeechText)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.testButton = QtGui.QPushButton(SpeechSettings)
        self.testButton.setIconSize(QtCore.QSize(50, 50))
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.verticalLayout_2.addWidget(self.testButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.restoreButton = QtGui.QPushButton(SpeechSettings)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.horizontalLayout.addWidget(self.restoreButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.applyButton = QtGui.QPushButton(SpeechSettings)
        self.applyButton.setIconSize(QtCore.QSize(50, 50))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout.addWidget(self.applyButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SpeechSettings)
        QtCore.QMetaObject.connectSlotsByName(SpeechSettings)

    def retranslateUi(self, SpeechSettings):
        SpeechSettings.setWindowTitle(_translate("SpeechSettings", "Dialog", None))
        self.rateSlider.setToolTip(_translate("SpeechSettings", "Words per minute slider (rate)", None))
        self.label.setText(_translate("SpeechSettings", "Rate:", None))
        self.comboBox.setToolTip(_translate("SpeechSettings", "Drop down box for selecting the voice", None))
        self.label_2.setText(_translate("SpeechSettings", "Volume:", None))
        self.label_3.setText(_translate("SpeechSettings", "Voices:", None))
        self.volumeSlider.setToolTip(_translate("SpeechSettings", "Volume slider", None))
        self.testSpeechText.setToolTip(_translate("SpeechSettings", "The text entered here is used when the test speech button is pressed", None))
        self.testSpeechText.setPlainText(_translate("SpeechSettings", "This is a test of the current text to speech settings.", None))
        self.testButton.setToolTip(_translate("SpeechSettings", "Apply and test current speech settings", None))
        self.testButton.setText(_translate("SpeechSettings", "Test Speech", None))
        self.restoreButton.setToolTip(_translate("SpeechSettings", "Restores settings to what they were when you opened the window", None))
        self.restoreButton.setText(_translate("SpeechSettings", "Restore", None))
        self.applyButton.setToolTip(_translate("SpeechSettings", "Apply new speech settings", None))
        self.applyButton.setText(_translate("SpeechSettings", "Apply", None))

