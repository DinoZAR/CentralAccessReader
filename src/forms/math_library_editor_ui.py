# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/math_library_editor.ui'
#
# Created: Wed May 28 12:00:54 2014
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
        MathLibraryEditor.resize(715, 520)
        self.verticalLayout_3 = QtGui.QVBoxLayout(MathLibraryEditor)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(MathLibraryEditor)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtGui.QLineEdit(self.layoutWidget)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeView = QtGui.QTreeView(self.layoutWidget)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout.addWidget(self.treeView)
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMargin(5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.patternTabs = QtGui.QTabWidget(self.widget)
        self.patternTabs.setTabsClosable(True)
        self.patternTabs.setMovable(True)
        self.patternTabs.setObjectName(_fromUtf8("patternTabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.patternTabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.patternTabs.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.patternTabs)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(MathLibraryEditor)
        self.patternTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MathLibraryEditor)

    def retranslateUi(self, MathLibraryEditor):
        MathLibraryEditor.setWindowTitle(_translate("MathLibraryEditor", "Math Library Editor", None))
        self.label.setText(_translate("MathLibraryEditor", "Library:", None))
        self.label_2.setText(_translate("MathLibraryEditor", "Patterns:", None))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab), _translate("MathLibraryEditor", "Tab 1", None))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab_2), _translate("MathLibraryEditor", "Tab 2", None))

