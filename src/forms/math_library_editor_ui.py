# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/math_library_editor.ui'
#
# Created: Wed May 21 09:45:19 2014
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

class Ui_MathLibraryEditor(object):
    def setupUi(self, MathLibraryEditor):
        MathLibraryEditor.setObjectName(_fromUtf8("MathLibraryEditor"))
        MathLibraryEditor.resize(390, 473)
        self.verticalLayout = QtGui.QVBoxLayout(MathLibraryEditor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(MathLibraryEditor)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.patternTabs = QtGui.QTabWidget(MathLibraryEditor)
        self.patternTabs.setTabsClosable(True)
        self.patternTabs.setMovable(True)
        self.patternTabs.setObjectName(_fromUtf8("patternTabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.patternTabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.patternTabs.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.patternTabs)

        self.retranslateUi(MathLibraryEditor)
        self.patternTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MathLibraryEditor)

    def retranslateUi(self, MathLibraryEditor):
        MathLibraryEditor.setWindowTitle(_translate("MathLibraryEditor", "Form", None))
        self.label.setText(_translate("MathLibraryEditor", "Patterns:", None))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab), _translate("MathLibraryEditor", "Tab 1", None))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab_2), _translate("MathLibraryEditor", "Tab 2", None))

