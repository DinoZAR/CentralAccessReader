# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace\nifty-prose-articulator\car\forms/popup_slider.ui'
#
# Created: Tue Jan 07 09:31:56 2014
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

class Ui_PopupSlider(object):
    def setupUi(self, PopupSlider):
        PopupSlider.setObjectName(_fromUtf8("PopupSlider"))
        PopupSlider.resize(242, 63)
        PopupSlider.setStyleSheet(_fromUtf8("background-color: none;\n"
"border: 0px;"))
        self.popupSliderBackground = QtGui.QLabel(PopupSlider)
        self.popupSliderBackground.setGeometry(QtCore.QRect(0, 0, 251, 71))
        self.popupSliderBackground.setText(_fromUtf8(""))
        self.popupSliderBackground.setPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/slider_popup_classic.png")))
        self.popupSliderBackground.setObjectName(_fromUtf8("popupSliderBackground"))
        self.slider = QtGui.QSlider(PopupSlider)
        self.slider.setGeometry(QtCore.QRect(18, 18, 211, 41))
        self.slider.setMaximum(100)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.slider.setObjectName(_fromUtf8("slider"))

        self.retranslateUi(PopupSlider)
        QtCore.QMetaObject.connectSlotsByName(PopupSlider)

    def retranslateUi(self, PopupSlider):
        PopupSlider.setWindowTitle(_translate("PopupSlider", "Form", None))

import resource_rc
