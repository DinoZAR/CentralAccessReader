# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/speech_settings.ui'
#
# Created: Wed May 28 09:20:04 2014
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
        SpeechSettings.resize(408, 601)
        font = QtGui.QFont()
        font.setPointSize(12)
        SpeechSettings.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/speech_settings_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SpeechSettings.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SpeechSettings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(SpeechSettings)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.rateSlider = QtGui.QSlider(SpeechSettings)
        self.rateSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.rateSlider.setMinimum(0)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 50)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.rateSlider.setTickInterval(10)
        self.rateSlider.setObjectName(_fromUtf8("rateSlider"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.rateSlider)
        self.label_2 = QtGui.QLabel(SpeechSettings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.volumeSlider = QtGui.QSlider(SpeechSettings)
        self.volumeSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.volumeSlider)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout.setItem(4, QtGui.QFormLayout.FieldRole, spacerItem)
        self.label_3 = QtGui.QLabel(SpeechSettings)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.voiceComboBox = QtGui.QComboBox(SpeechSettings)
        self.voiceComboBox.setEditable(False)
        self.voiceComboBox.setObjectName(_fromUtf8("voiceComboBox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.voiceComboBox)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout.setItem(6, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.label_5 = QtGui.QLabel(SpeechSettings)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtGui.QLabel(SpeechSettings)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_4)
        self.pauseSlider = QtGui.QSlider(SpeechSettings)
        self.pauseSlider.setMaximum(10)
        self.pauseSlider.setPageStep(1)
        self.pauseSlider.setOrientation(QtCore.Qt.Horizontal)
        self.pauseSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.pauseSlider.setTickInterval(1)
        self.pauseSlider.setObjectName(_fromUtf8("pauseSlider"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pauseSlider)
        self.label_6 = QtGui.QLabel(SpeechSettings)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.imageTagCheckBox = QtGui.QCheckBox(SpeechSettings)
        self.imageTagCheckBox.setObjectName(_fromUtf8("imageTagCheckBox"))
        self.horizontalLayout_3.addWidget(self.imageTagCheckBox)
        self.mathTagCheckBox = QtGui.QCheckBox(SpeechSettings)
        self.mathTagCheckBox.setObjectName(_fromUtf8("mathTagCheckBox"))
        self.horizontalLayout_3.addWidget(self.mathTagCheckBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.ignoreAltTextCheckBox = QtGui.QCheckBox(SpeechSettings)
        self.ignoreAltTextCheckBox.setObjectName(_fromUtf8("ignoreAltTextCheckBox"))
        self.horizontalLayout_4.addWidget(self.ignoreAltTextCheckBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.formLayout.setLayout(8, QtGui.QFormLayout.FieldRole, self.verticalLayout_3)
        self.mathLibraryTree = QtGui.QTreeView(SpeechSettings)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mathLibraryTree.setFont(font)
        self.mathLibraryTree.setObjectName(_fromUtf8("mathLibraryTree"))
        self.mathLibraryTree.header().setVisible(False)
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.mathLibraryTree)
        self.verticalLayout.addLayout(self.formLayout)
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
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.restoreButton = QtGui.QPushButton(SpeechSettings)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.horizontalLayout.addWidget(self.restoreButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.applyButton = QtGui.QPushButton(SpeechSettings)
        self.applyButton.setIconSize(QtCore.QSize(50, 50))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout.addWidget(self.applyButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(SpeechSettings)
        QtCore.QMetaObject.connectSlotsByName(SpeechSettings)
        SpeechSettings.setTabOrder(self.rateSlider, self.volumeSlider)
        SpeechSettings.setTabOrder(self.volumeSlider, self.voiceComboBox)
        SpeechSettings.setTabOrder(self.voiceComboBox, self.testSpeechText)
        SpeechSettings.setTabOrder(self.testSpeechText, self.testButton)
        SpeechSettings.setTabOrder(self.testButton, self.restoreButton)
        SpeechSettings.setTabOrder(self.restoreButton, self.applyButton)

    def retranslateUi(self, SpeechSettings):
        SpeechSettings.setWindowTitle(_translate("SpeechSettings", "General", None))
        self.label.setText(_translate("SpeechSettings", "Rate:", None))
        self.rateSlider.setToolTip(_translate("SpeechSettings", "Words per minute slider (rate)", None))
        self.label_2.setText(_translate("SpeechSettings", "Volume:", None))
        self.volumeSlider.setToolTip(_translate("SpeechSettings", "Volume slider", None))
        self.label_3.setText(_translate("SpeechSettings", "Voices:", None))
        self.voiceComboBox.setToolTip(_translate("SpeechSettings", "Drop down box for selecting the voice", None))
        self.label_5.setText(_translate("SpeechSettings", "Math:", None))
        self.label_4.setText(_translate("SpeechSettings", "Tag:", None))
        self.label_6.setText(_translate("SpeechSettings", "Pause Length:", None))
        self.imageTagCheckBox.setText(_translate("SpeechSettings", "Image", None))
        self.mathTagCheckBox.setText(_translate("SpeechSettings", "Math", None))
        self.ignoreAltTextCheckBox.setText(_translate("SpeechSettings", "Ignore Alternate Text", None))
        self.testSpeechText.setToolTip(_translate("SpeechSettings", "The text entered here is used when the test speech button is pressed", None))
        self.testSpeechText.setPlainText(_translate("SpeechSettings", "This is a test of the current text to speech settings.", None))
        self.testButton.setToolTip(_translate("SpeechSettings", "Apply and test current speech settings", None))
        self.testButton.setText(_translate("SpeechSettings", "Test Speech", None))
        self.restoreButton.setToolTip(_translate("SpeechSettings", "Restores settings to what they were when you opened the window", None))
        self.restoreButton.setText(_translate("SpeechSettings", "Restore", None))
        self.applyButton.setToolTip(_translate("SpeechSettings", "Apply new speech settings", None))
        self.applyButton.setText(_translate("SpeechSettings", "Apply", None))

import resource_rc
