# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/math_dev_env.ui'
#
# Created: Thu Feb 20 11:51:34 2014
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

class Ui_MathDevEnv(object):
    def setupUi(self, MathDevEnv):
        MathDevEnv.setObjectName(_fromUtf8("MathDevEnv"))
        MathDevEnv.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MathDevEnv)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setMargin(5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.tabWidget = QtGui.QTabWidget(self.widget1)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.widget2 = QtGui.QWidget(self.splitter_2)
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.widget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(self.widget2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.widget2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.treeWidget = QtGui.QTreeWidget(self.widget2)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.verticalLayout_4.setStretch(1, 1)
        MathDevEnv.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MathDevEnv)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MathDevEnv.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MathDevEnv)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MathDevEnv.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MathDevEnv)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionGet_MathML = QtGui.QAction(MathDevEnv)
        self.actionGet_MathML.setObjectName(_fromUtf8("actionGet_MathML"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionGet_MathML)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MathDevEnv)
        QtCore.QMetaObject.connectSlotsByName(MathDevEnv)

    def retranslateUi(self, MathDevEnv):
        MathDevEnv.setWindowTitle(_translate("MathDevEnv", "MainWindow", None))
        self.pushButton_2.setText(_translate("MathDevEnv", "Run", None))
        self.label_3.setText(_translate("MathDevEnv", "MathML:", None))
        self.label_2.setText(_translate("MathDevEnv", "Patterns:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MathDevEnv", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MathDevEnv", "Tab 2", None))
        self.label.setText(_translate("MathDevEnv", "Stages:", None))
        self.pushButton.setText(_translate("MathDevEnv", "Expand", None))
        self.pushButton_3.setText(_translate("MathDevEnv", "Collapse", None))
        self.menuFile.setTitle(_translate("MathDevEnv", "File", None))
        self.actionOpen.setText(_translate("MathDevEnv", "Open Pattern", None))
        self.actionGet_MathML.setText(_translate("MathDevEnv", "Get MathML", None))

