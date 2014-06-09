# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/math_library_new.ui'
#
# Created: Mon Jun 09 08:51:49 2014
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

class Ui_NewMathLibraryDialog(object):
    def setupUi(self, NewMathLibraryDialog):
        NewMathLibraryDialog.setObjectName(_fromUtf8("NewMathLibraryDialog"))
        NewMathLibraryDialog.resize(312, 396)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icons/CAR_About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewMathLibraryDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(NewMathLibraryDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(NewMathLibraryDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.nameEdit = QtGui.QLineEdit(NewMathLibraryDialog)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameEdit)
        self.label_2 = QtGui.QLabel(NewMathLibraryDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.authorEdit = QtGui.QLineEdit(NewMathLibraryDialog)
        self.authorEdit.setObjectName(_fromUtf8("authorEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.authorEdit)
        self.label_3 = QtGui.QLabel(NewMathLibraryDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.emptyProjectRadio = QtGui.QRadioButton(NewMathLibraryDialog)
        self.emptyProjectRadio.setChecked(True)
        self.emptyProjectRadio.setObjectName(_fromUtf8("emptyProjectRadio"))
        self.verticalLayout.addWidget(self.emptyProjectRadio)
        self.copyFromRadio = QtGui.QRadioButton(NewMathLibraryDialog)
        self.copyFromRadio.setObjectName(_fromUtf8("copyFromRadio"))
        self.verticalLayout.addWidget(self.copyFromRadio)
        self.copyFromTree = QtGui.QTreeView(NewMathLibraryDialog)
        self.copyFromTree.setObjectName(_fromUtf8("copyFromTree"))
        self.copyFromTree.header().setVisible(False)
        self.verticalLayout.addWidget(self.copyFromTree)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        self.label_4 = QtGui.QLabel(NewMathLibraryDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.languageCombo = QtGui.QComboBox(NewMathLibraryDialog)
        self.languageCombo.setObjectName(_fromUtf8("languageCombo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.languageCombo)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(NewMathLibraryDialog)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.createButton = QtGui.QPushButton(NewMathLibraryDialog)
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.horizontalLayout.addWidget(self.createButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(NewMathLibraryDialog)
        QtCore.QMetaObject.connectSlotsByName(NewMathLibraryDialog)

    def retranslateUi(self, NewMathLibraryDialog):
        NewMathLibraryDialog.setWindowTitle(_translate("NewMathLibraryDialog", "New Math Library", None))
        self.label.setText(_translate("NewMathLibraryDialog", "Name:", None))
        self.label_2.setText(_translate("NewMathLibraryDialog", "Author:", None))
        self.label_3.setText(_translate("NewMathLibraryDialog", "Template:", None))
        self.emptyProjectRadio.setText(_translate("NewMathLibraryDialog", "Empty Project", None))
        self.copyFromRadio.setText(_translate("NewMathLibraryDialog", "Copy From:", None))
        self.label_4.setText(_translate("NewMathLibraryDialog", "Language:", None))
        self.label_5.setText(_translate("NewMathLibraryDialog", "NOTE: CAR must be restarted in order for the new library to appear.", None))
        self.createButton.setText(_translate("NewMathLibraryDialog", "Create", None))

import resource_rc
