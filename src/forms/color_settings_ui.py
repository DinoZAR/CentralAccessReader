# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace2\another\src\forms/color_settings.ui'
#
# Created: Tue Jun 04 16:20:43 2013
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

class Ui_ColorSettings(object):
    def setupUi(self, ColorSettings):
        ColorSettings.setObjectName(_fromUtf8("ColorSettings"))
        ColorSettings.resize(455, 301)
        font = QtGui.QFont()
        font.setPointSize(12)
        ColorSettings.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ColorSettings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_9 = QtGui.QLabel(ColorSettings)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.line_5 = QtGui.QFrame(ColorSettings)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_3.addWidget(self.line_5, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(ColorSettings)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setSpacing(8)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(ColorSettings)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.contentBackgroundButton = QtGui.QPushButton(ColorSettings)
        self.contentBackgroundButton.setObjectName(_fromUtf8("contentBackgroundButton"))
        self.horizontalLayout_3.addWidget(self.contentBackgroundButton)
        self.contentTextButton = QtGui.QPushButton(ColorSettings)
        self.contentTextButton.setObjectName(_fromUtf8("contentTextButton"))
        self.horizontalLayout_3.addWidget(self.contentTextButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_4 = QtGui.QLabel(ColorSettings)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.highlighterBackgroundButton = QtGui.QPushButton(ColorSettings)
        self.highlighterBackgroundButton.setObjectName(_fromUtf8("highlighterBackgroundButton"))
        self.horizontalLayout_4.addWidget(self.highlighterBackgroundButton)
        self.highlighterTextButton = QtGui.QPushButton(ColorSettings)
        self.highlighterTextButton.setObjectName(_fromUtf8("highlighterTextButton"))
        self.horizontalLayout_4.addWidget(self.highlighterTextButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_5 = QtGui.QLabel(ColorSettings)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.highlighterLineBackgroundButton = QtGui.QPushButton(ColorSettings)
        self.highlighterLineBackgroundButton.setObjectName(_fromUtf8("highlighterLineBackgroundButton"))
        self.horizontalLayout_5.addWidget(self.highlighterLineBackgroundButton)
        self.highlighterLineTextButton = QtGui.QPushButton(ColorSettings)
        self.highlighterLineTextButton.setObjectName(_fromUtf8("highlighterLineTextButton"))
        self.horizontalLayout_5.addWidget(self.highlighterLineTextButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.gridLayout_3.addLayout(self.formLayout, 1, 2, 1, 1)
        self.line_4 = QtGui.QFrame(ColorSettings)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_3.addWidget(self.line_4, 1, 1, 1, 1)
        self.line_3 = QtGui.QFrame(ColorSettings)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_3.addWidget(self.line_3, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(ColorSettings)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.fontComboBox = QtGui.QFontComboBox(ColorSettings)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.gridLayout_3.addWidget(self.fontComboBox, 2, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.enableHTextCheckBox = QtGui.QCheckBox(ColorSettings)
        self.enableHTextCheckBox.setObjectName(_fromUtf8("enableHTextCheckBox"))
        self.verticalLayout.addWidget(self.enableHTextCheckBox)
        self.enableHLineCheckBox = QtGui.QCheckBox(ColorSettings)
        self.enableHLineCheckBox.setObjectName(_fromUtf8("enableHLineCheckBox"))
        self.verticalLayout.addWidget(self.enableHLineCheckBox)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.restoreButton = QtGui.QPushButton(ColorSettings)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.horizontalLayout.addWidget(self.restoreButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.previewButton = QtGui.QPushButton(ColorSettings)
        self.previewButton.setObjectName(_fromUtf8("previewButton"))
        self.horizontalLayout.addWidget(self.previewButton)
        self.applyButton = QtGui.QPushButton(ColorSettings)
        self.applyButton.setIconSize(QtCore.QSize(50, 50))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.horizontalLayout.addWidget(self.applyButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(ColorSettings)
        QtCore.QMetaObject.connectSlotsByName(ColorSettings)

    def retranslateUi(self, ColorSettings):
        ColorSettings.setWindowTitle(_translate("ColorSettings", "Highlighting, Colors, and Fonts", None))
        self.label_9.setText(_translate("ColorSettings", "Font", None))
        self.label_7.setText(_translate("ColorSettings", "Colors", None))
        self.label_6.setText(_translate("ColorSettings", "Content:", None))
        self.contentBackgroundButton.setText(_translate("ColorSettings", "Background", None))
        self.contentTextButton.setText(_translate("ColorSettings", "Text", None))
        self.label_4.setText(_translate("ColorSettings", "Highlighter Text:", None))
        self.highlighterBackgroundButton.setText(_translate("ColorSettings", "Background", None))
        self.highlighterTextButton.setText(_translate("ColorSettings", "Text", None))
        self.label_5.setText(_translate("ColorSettings", "Highlighter Line:", None))
        self.highlighterLineBackgroundButton.setText(_translate("ColorSettings", "Background", None))
        self.highlighterLineTextButton.setText(_translate("ColorSettings", "Text", None))
        self.label_8.setText(_translate("ColorSettings", "Highlighting", None))
        self.enableHTextCheckBox.setText(_translate("ColorSettings", "Text", None))
        self.enableHLineCheckBox.setText(_translate("ColorSettings", "Line", None))
        self.restoreButton.setToolTip(_translate("ColorSettings", "Restores settings to what they were when you opened the window", None))
        self.restoreButton.setText(_translate("ColorSettings", "Restore", None))
        self.previewButton.setText(_translate("ColorSettings", "Preview", None))
        self.applyButton.setToolTip(_translate("ColorSettings", "Apply new speech settings", None))
        self.applyButton.setText(_translate("ColorSettings", "Apply", None))

