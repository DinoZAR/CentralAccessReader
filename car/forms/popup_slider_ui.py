# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/popup_slider.ui'
#
# Created: Wed Jun 11 15:37:26 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PopupSlider(object):
    def setupUi(self, PopupSlider):
        PopupSlider.setObjectName("PopupSlider")
        PopupSlider.resize(242, 63)
        PopupSlider.setStyleSheet("background-color: none;\n"
"border: 0px;")
        self.popupSliderBackground = QtWidgets.QLabel(PopupSlider)
        self.popupSliderBackground.setGeometry(QtCore.QRect(0, 0, 251, 71))
        self.popupSliderBackground.setText("")
        self.popupSliderBackground.setPixmap(QtGui.QPixmap(":/classic/icons/slider_popup_classic.png"))
        self.popupSliderBackground.setObjectName("popupSliderBackground")
        self.slider = QtWidgets.QSlider(PopupSlider)
        self.slider.setGeometry(QtCore.QRect(18, 18, 211, 41))
        self.slider.setMaximum(100)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider.setObjectName("slider")

        self.retranslateUi(PopupSlider)
        QtCore.QMetaObject.connectSlotsByName(PopupSlider)

    def retranslateUi(self, PopupSlider):
        _translate = QtCore.QCoreApplication.translate
        PopupSlider.setWindowTitle(_translate("PopupSlider", "Form"))

import resource_rc
