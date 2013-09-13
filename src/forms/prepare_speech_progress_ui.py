# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/prepare_speech_progress.ui'
#
# Created: Fri Sep 13 14:31:11 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PrepareSpeechProgressWidget(object):
    def setupUi(self, PrepareSpeechProgressWidget):
        PrepareSpeechProgressWidget.setObjectName("PrepareSpeechProgressWidget")
        PrepareSpeechProgressWidget.resize(245, 69)
        font = QtGui.QFont()
        font.setPointSize(12)
        PrepareSpeechProgressWidget.setFont(font)
        self.label = QtGui.QLabel(PrepareSpeechProgressWidget)
        self.label.setGeometry(QtCore.QRect(-4, -62, 571, 190))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/prepare_speech_background.png"))
        self.label.setObjectName("label")
        self.progressBar = QtGui.QProgressBar(PrepareSpeechProgressWidget)
        self.progressBar.setGeometry(QtCore.QRect(9, 25, 220, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(PrepareSpeechProgressWidget)
        QtCore.QMetaObject.connectSlotsByName(PrepareSpeechProgressWidget)

    def retranslateUi(self, PrepareSpeechProgressWidget):
        PrepareSpeechProgressWidget.setWindowTitle(QtGui.QApplication.translate("PrepareSpeechProgressWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
