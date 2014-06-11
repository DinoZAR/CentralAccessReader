# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/math_library_editor.ui'
#
# Created: Wed Jun 11 15:37:25 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MathLibraryEditor(object):
    def setupUi(self, MathLibraryEditor):
        MathLibraryEditor.setObjectName("MathLibraryEditor")
        MathLibraryEditor.resize(715, 520)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MathLibraryEditor)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(MathLibraryEditor)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.authorEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.authorEdit.setObjectName("authorEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.authorEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.languageCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.languageCombo.setObjectName("languageCombo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.languageCombo)
        self.verticalLayout.addLayout(self.formLayout)
        self.treeView = QtWidgets.QTreeView(self.layoutWidget)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setContentsMargins(5, 5, 5, 5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.patternTabs = QtWidgets.QTabWidget(self.layoutWidget1)
        self.patternTabs.setTabsClosable(True)
        self.patternTabs.setMovable(True)
        self.patternTabs.setObjectName("patternTabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.patternTabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.patternTabs.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.patternTabs)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(MathLibraryEditor)
        self.patternTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MathLibraryEditor)

    def retranslateUi(self, MathLibraryEditor):
        _translate = QtCore.QCoreApplication.translate
        MathLibraryEditor.setWindowTitle(_translate("MathLibraryEditor", "Math Library Editor"))
        self.label_3.setText(_translate("MathLibraryEditor", "Library:"))
        self.label.setText(_translate("MathLibraryEditor", "Author:"))
        self.label_4.setText(_translate("MathLibraryEditor", "Language:"))
        self.label_2.setText(_translate("MathLibraryEditor", "Patterns:"))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab), _translate("MathLibraryEditor", "Tab 1"))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab_2), _translate("MathLibraryEditor", "Tab 2"))

