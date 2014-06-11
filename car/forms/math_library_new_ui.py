# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/math_library_new.ui'
#
# Created: Wed Jun 11 15:37:25 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewMathLibraryDialog(object):
    def setupUi(self, NewMathLibraryDialog):
        NewMathLibraryDialog.setObjectName("NewMathLibraryDialog")
        NewMathLibraryDialog.resize(312, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/icons/CAR_About.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewMathLibraryDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NewMathLibraryDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(NewMathLibraryDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameEdit = QtWidgets.QLineEdit(NewMathLibraryDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_2 = QtWidgets.QLabel(NewMathLibraryDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.authorEdit = QtWidgets.QLineEdit(NewMathLibraryDialog)
        self.authorEdit.setObjectName("authorEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.authorEdit)
        self.label_3 = QtWidgets.QLabel(NewMathLibraryDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.emptyProjectRadio = QtWidgets.QRadioButton(NewMathLibraryDialog)
        self.emptyProjectRadio.setChecked(True)
        self.emptyProjectRadio.setObjectName("emptyProjectRadio")
        self.verticalLayout.addWidget(self.emptyProjectRadio)
        self.copyFromRadio = QtWidgets.QRadioButton(NewMathLibraryDialog)
        self.copyFromRadio.setObjectName("copyFromRadio")
        self.verticalLayout.addWidget(self.copyFromRadio)
        self.copyFromTree = QtWidgets.QTreeView(NewMathLibraryDialog)
        self.copyFromTree.setObjectName("copyFromTree")
        self.copyFromTree.header().setVisible(False)
        self.verticalLayout.addWidget(self.copyFromTree)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.label_4 = QtWidgets.QLabel(NewMathLibraryDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.languageCombo = QtWidgets.QComboBox(NewMathLibraryDialog)
        self.languageCombo.setObjectName("languageCombo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.languageCombo)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(NewMathLibraryDialog)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.createButton = QtWidgets.QPushButton(NewMathLibraryDialog)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout.addWidget(self.createButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(NewMathLibraryDialog)
        QtCore.QMetaObject.connectSlotsByName(NewMathLibraryDialog)

    def retranslateUi(self, NewMathLibraryDialog):
        _translate = QtCore.QCoreApplication.translate
        NewMathLibraryDialog.setWindowTitle(_translate("NewMathLibraryDialog", "New Math Library"))
        self.label.setText(_translate("NewMathLibraryDialog", "Name:"))
        self.label_2.setText(_translate("NewMathLibraryDialog", "Author:"))
        self.label_3.setText(_translate("NewMathLibraryDialog", "Template:"))
        self.emptyProjectRadio.setText(_translate("NewMathLibraryDialog", "Empty Project"))
        self.copyFromRadio.setText(_translate("NewMathLibraryDialog", "Copy From:"))
        self.label_4.setText(_translate("NewMathLibraryDialog", "Language:"))
        self.label_5.setText(_translate("NewMathLibraryDialog", "NOTE: CAR must be restarted in order for the new library to appear."))
        self.createButton.setText(_translate("NewMathLibraryDialog", "Create"))

import resource_rc
