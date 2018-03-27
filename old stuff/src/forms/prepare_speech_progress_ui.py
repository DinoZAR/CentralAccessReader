# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/prepare_speech_progress.ui'
#
# Created: Mon Sep 16 16:34:04 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_PrepareSpeechProgressWidget(object):
    def setupUi(self, PrepareSpeechProgressWidget):
        PrepareSpeechProgressWidget.setObjectName(_fromUtf8("PrepareSpeechProgressWidget"))
        PrepareSpeechProgressWidget.resize(245, 69)
        font = QtGui.QFont()
        font.setPointSize(12)
        PrepareSpeechProgressWidget.setFont(font)
        self.label = QtGui.QLabel(PrepareSpeechProgressWidget)
        self.label.setGeometry(QtCore.QRect(-4, -62, 571, 190))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/prepare_speech_background.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(PrepareSpeechProgressWidget)
        self.progressBar.setGeometry(QtCore.QRect(9, 25, 220, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(PrepareSpeechProgressWidget)
        QtCore.QMetaObject.connectSlotsByName(PrepareSpeechProgressWidget)

    def retranslateUi(self, PrepareSpeechProgressWidget):
        PrepareSpeechProgressWidget.setWindowTitle(_translate("PrepareSpeechProgressWidget", "Form", None))

import resource_rc
