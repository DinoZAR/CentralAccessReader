# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/speech_settings.ui'
#
# Created: Tue Jun 03 09:06:07 2014
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
        SpeechSettings.resize(337, 841)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/speech_settings_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SpeechSettings.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(SpeechSettings)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(SpeechSettings)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 335, 816))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(40)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.rateSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rateSlider.sizePolicy().hasHeightForWidth())
        self.rateSlider.setSizePolicy(sizePolicy)
        self.rateSlider.setMinimum(0)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 50)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.rateSlider.setTickInterval(10)
        self.rateSlider.setObjectName(_fromUtf8("rateSlider"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.rateSlider)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.volumeSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.volumeSlider)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.pauseSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseSlider.sizePolicy().hasHeightForWidth())
        self.pauseSlider.setSizePolicy(sizePolicy)
        self.pauseSlider.setMaximum(10)
        self.pauseSlider.setPageStep(1)
        self.pauseSlider.setOrientation(QtCore.Qt.Horizontal)
        self.pauseSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.pauseSlider.setTickInterval(1)
        self.pauseSlider.setObjectName(_fromUtf8("pauseSlider"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pauseSlider)
        self.verticalLayout_9.addLayout(self.formLayout)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setStyleSheet(_fromUtf8("font-size: 16pt;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.voiceComboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.voiceComboBox.setEditable(False)
        self.voiceComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.voiceComboBox.setObjectName(_fromUtf8("voiceComboBox"))
        self.verticalLayout_5.addWidget(self.voiceComboBox)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setStyleSheet(_fromUtf8("font-size: 16pt;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.mathLibraryDisplay = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.mathLibraryDisplay.setStyleSheet(_fromUtf8("border-width: 5px;"))
        self.mathLibraryDisplay.setReadOnly(True)
        self.mathLibraryDisplay.setObjectName(_fromUtf8("mathLibraryDisplay"))
        self.verticalLayout_2.addWidget(self.mathLibraryDisplay)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.languageLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.languageLabel.setObjectName(_fromUtf8("languageLabel"))
        self.horizontalLayout_2.addWidget(self.languageLabel)
        self.mathLanguageCombo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.mathLanguageCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.mathLanguageCombo.setObjectName(_fromUtf8("mathLanguageCombo"))
        self.horizontalLayout_2.addWidget(self.mathLanguageCombo)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.libraryLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.libraryLabel.setObjectName(_fromUtf8("libraryLabel"))
        self.horizontalLayout.addWidget(self.libraryLabel)
        self.mathAddButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.mathAddButton.setObjectName(_fromUtf8("mathAddButton"))
        self.horizontalLayout.addWidget(self.mathAddButton)
        self.mathRemoveButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.mathRemoveButton.setObjectName(_fromUtf8("mathRemoveButton"))
        self.horizontalLayout.addWidget(self.mathRemoveButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.mathLibraryTree = QtGui.QTreeView(self.scrollAreaWidgetContents)
        self.mathLibraryTree.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mathLibraryTree.setFont(font)
        self.mathLibraryTree.setObjectName(_fromUtf8("mathLibraryTree"))
        self.mathLibraryTree.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.mathLibraryTree)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setStyleSheet(_fromUtf8("font-size: 16pt;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.imageTagCheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.imageTagCheckBox.setObjectName(_fromUtf8("imageTagCheckBox"))
        self.verticalLayout.addWidget(self.imageTagCheckBox)
        self.mathTagCheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.mathTagCheckBox.setObjectName(_fromUtf8("mathTagCheckBox"))
        self.verticalLayout.addWidget(self.mathTagCheckBox)
        self.ignoreAltTextCheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.ignoreAltTextCheckBox.setObjectName(_fromUtf8("ignoreAltTextCheckBox"))
        self.verticalLayout.addWidget(self.ignoreAltTextCheckBox)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.verticalLayout_9.setStretch(4, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.restoreButton = QtGui.QPushButton(SpeechSettings)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.verticalLayout_3.addWidget(self.restoreButton)

        self.retranslateUi(SpeechSettings)
        QtCore.QMetaObject.connectSlotsByName(SpeechSettings)

    def retranslateUi(self, SpeechSettings):
        SpeechSettings.setWindowTitle(_translate("SpeechSettings", "General", None))
        self.label_7.setText(_translate("SpeechSettings", "Rate", None))
        self.rateSlider.setToolTip(_translate("SpeechSettings", "Words per minute slider (rate)", None))
        self.label_2.setText(_translate("SpeechSettings", "Volume", None))
        self.volumeSlider.setToolTip(_translate("SpeechSettings", "Volume slider", None))
        self.label_6.setText(_translate("SpeechSettings", "Pause Length", None))
        self.label_3.setText(_translate("SpeechSettings", "Voices", None))
        self.voiceComboBox.setToolTip(_translate("SpeechSettings", "Drop down box for selecting the voice", None))
        self.label_5.setText(_translate("SpeechSettings", "Math", None))
        self.mathLibraryDisplay.setPlaceholderText(_translate("SpeechSettings", "<current math library>", None))
        self.languageLabel.setText(_translate("SpeechSettings", "Language:", None))
        self.libraryLabel.setText(_translate("SpeechSettings", "Library:", None))
        self.mathAddButton.setToolTip(_translate("SpeechSettings", "Adds math library from file.", None))
        self.mathAddButton.setText(_translate("SpeechSettings", "+", None))
        self.mathRemoveButton.setToolTip(_translate("SpeechSettings", "Removes current math library.", None))
        self.mathRemoveButton.setText(_translate("SpeechSettings", "-", None))
        self.label_4.setText(_translate("SpeechSettings", "Tag", None))
        self.imageTagCheckBox.setText(_translate("SpeechSettings", "Image", None))
        self.mathTagCheckBox.setText(_translate("SpeechSettings", "Math", None))
        self.ignoreAltTextCheckBox.setText(_translate("SpeechSettings", "Ignore Alternate Text", None))
        self.restoreButton.setToolTip(_translate("SpeechSettings", "Restores settings to default values", None))
        self.restoreButton.setText(_translate("SpeechSettings", "Restore to Default Settings", None))

import resource_rc
