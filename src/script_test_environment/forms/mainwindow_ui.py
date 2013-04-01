# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Documents\Special Projects\Graffe, Spencer\workspace\nifty-prose-articulator\src\script_test_environment\forms/mainwindow.ui'
#
# Created: Mon Apr 01 09:53:22 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(888, 706)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(15)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.resetButton = QtGui.QPushButton(self.widget)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.horizontalLayout_2.addWidget(self.resetButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.documentView = QtWebKit.QWebView(self.widget)
        self.documentView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.documentView.setObjectName(_fromUtf8("documentView"))
        self.verticalLayout.addWidget(self.documentView)
        self.verticalLayout.setStretch(1, 1)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runButton = QtGui.QPushButton(self.widget1)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout.addWidget(self.runButton)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.commandLine = QtGui.QLineEdit(self.widget1)
        self.commandLine.setObjectName(_fromUtf8("commandLine"))
        self.horizontalLayout.addWidget(self.commandLine)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.javascriptTabs = QtGui.QTabWidget(self.widget1)
        self.javascriptTabs.setTabsClosable(True)
        self.javascriptTabs.setMovable(True)
        self.javascriptTabs.setObjectName(_fromUtf8("javascriptTabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.javascriptTabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.javascriptTabs.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.javascriptTabs)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Docx = QtGui.QAction(MainWindow)
        self.actionOpen_Docx.setObjectName(_fromUtf8("actionOpen_Docx"))
        self.actionOpen_Javascript = QtGui.QAction(MainWindow)
        self.actionOpen_Javascript.setObjectName(_fromUtf8("actionOpen_Javascript"))
        self.actionSave_Current = QtGui.QAction(MainWindow)
        self.actionSave_Current.setObjectName(_fromUtf8("actionSave_Current"))
        self.actionSave_All = QtGui.QAction(MainWindow)
        self.actionSave_All.setObjectName(_fromUtf8("actionSave_All"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionNew_Script = QtGui.QAction(MainWindow)
        self.actionNew_Script.setObjectName(_fromUtf8("actionNew_Script"))
        self.menuFile.addAction(self.actionNew_Script)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Docx)
        self.menuFile.addAction(self.actionOpen_Javascript)
        self.menuFile.addAction(self.actionSave_Current)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Javascript Test Environment", None))
        self.label.setText(_translate("MainWindow", "Document:", None))
        self.resetButton.setText(_translate("MainWindow", "Reset", None))
        self.runButton.setText(_translate("MainWindow", "Run", None))
        self.label_2.setText(_translate("MainWindow", "Command:", None))
        self.javascriptTabs.setTabText(self.javascriptTabs.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.javascriptTabs.setTabText(self.javascriptTabs.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen_Docx.setText(_translate("MainWindow", "Open Docx", None))
        self.actionOpen_Docx.setShortcut(_translate("MainWindow", "Ctrl+Shift+O", None))
        self.actionOpen_Javascript.setText(_translate("MainWindow", "Open Script", None))
        self.actionOpen_Javascript.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave_Current.setText(_translate("MainWindow", "Save Current", None))
        self.actionSave_Current.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSave_All.setText(_translate("MainWindow", "Save All", None))
        self.actionSave_All.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionNew_Script.setText(_translate("MainWindow", "New Script", None))
        self.actionNew_Script.setShortcut(_translate("MainWindow", "Ctrl+N", None))

from PyQt4 import QtWebKit
