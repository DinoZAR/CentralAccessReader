# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\src\forms/math_dev_env.ui'
#
# Created: Thu Feb 20 16:14:33 2014
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
        MathDevEnv.resize(1010, 666)
        self.centralwidget = QtGui.QWidget(MathDevEnv)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runButton = QtGui.QPushButton(self.centralwidget)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout.addWidget(self.runButton)
        self.mathProseOutput = QtGui.QLineEdit(self.centralwidget)
        self.mathProseOutput.setObjectName(_fromUtf8("mathProseOutput"))
        self.horizontalLayout.addWidget(self.mathProseOutput)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(10)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.patternTabs = QtGui.QTabWidget(self.layoutWidget)
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
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setMargin(5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.mathmlEditor = MathMLEditor(self.layoutWidget1)
        self.mathmlEditor.setObjectName(_fromUtf8("mathmlEditor"))
        self.verticalLayout_3.addWidget(self.mathmlEditor)
        self.verticalLayout_3.setStretch(1, 1)
        self.layoutWidget2 = QtGui.QWidget(self.splitter)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.expandButton = QtGui.QPushButton(self.layoutWidget2)
        self.expandButton.setObjectName(_fromUtf8("expandButton"))
        self.horizontalLayout_2.addWidget(self.expandButton)
        self.collapseButton = QtGui.QPushButton(self.layoutWidget2)
        self.collapseButton.setObjectName(_fromUtf8("collapseButton"))
        self.horizontalLayout_2.addWidget(self.collapseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.stagesTree = QtGui.QTreeWidget(self.layoutWidget2)
        self.stagesTree.setObjectName(_fromUtf8("stagesTree"))
        self.stagesTree.headerItem().setText(0, _fromUtf8("1"))
        self.stagesTree.header().setVisible(False)
        self.verticalLayout.addWidget(self.stagesTree)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.verticalLayout_4.setStretch(1, 1)
        MathDevEnv.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MathDevEnv)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MathDevEnv.setMenuBar(self.menubar)
        self.actionOpen_Pattern = QtGui.QAction(MathDevEnv)
        self.actionOpen_Pattern.setObjectName(_fromUtf8("actionOpen_Pattern"))
        self.actionGet_MathML = QtGui.QAction(MathDevEnv)
        self.actionGet_MathML.setObjectName(_fromUtf8("actionGet_MathML"))
        self.actionNew_Pattern = QtGui.QAction(MathDevEnv)
        self.actionNew_Pattern.setObjectName(_fromUtf8("actionNew_Pattern"))
        self.actionClose_Pattern = QtGui.QAction(MathDevEnv)
        self.actionClose_Pattern.setObjectName(_fromUtf8("actionClose_Pattern"))
        self.actionPaste_MathML = QtGui.QAction(MathDevEnv)
        self.actionPaste_MathML.setObjectName(_fromUtf8("actionPaste_MathML"))
        self.actionSave_Pattern = QtGui.QAction(MathDevEnv)
        self.actionSave_Pattern.setObjectName(_fromUtf8("actionSave_Pattern"))
        self.actionSave_As = QtGui.QAction(MathDevEnv)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.menuFile.addAction(self.actionNew_Pattern)
        self.menuFile.addAction(self.actionOpen_Pattern)
        self.menuFile.addAction(self.actionPaste_MathML)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Pattern)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Pattern)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MathDevEnv)
        self.patternTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MathDevEnv)

    def retranslateUi(self, MathDevEnv):
        MathDevEnv.setWindowTitle(_translate("MathDevEnv", "Math Pattern Editor", None))
        self.runButton.setToolTip(_translate("MathDevEnv", "Runs the current pattern (Ctrl + R)", None))
        self.runButton.setText(_translate("MathDevEnv", "Run", None))
        self.runButton.setShortcut(_translate("MathDevEnv", "Ctrl+R", None))
        self.label_2.setText(_translate("MathDevEnv", "Patterns:", None))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab), _translate("MathDevEnv", "Tab 1", None))
        self.patternTabs.setTabText(self.patternTabs.indexOf(self.tab_2), _translate("MathDevEnv", "Tab 2", None))
        self.label_3.setText(_translate("MathDevEnv", "MathML:", None))
        self.label.setText(_translate("MathDevEnv", "Stages:", None))
        self.expandButton.setText(_translate("MathDevEnv", "Expand", None))
        self.collapseButton.setText(_translate("MathDevEnv", "Collapse", None))
        self.menuFile.setTitle(_translate("MathDevEnv", "File", None))
        self.actionOpen_Pattern.setText(_translate("MathDevEnv", "Open Pattern", None))
        self.actionOpen_Pattern.setShortcut(_translate("MathDevEnv", "Ctrl+O", None))
        self.actionGet_MathML.setText(_translate("MathDevEnv", "Get MathML From Document", None))
        self.actionNew_Pattern.setText(_translate("MathDevEnv", "New Pattern", None))
        self.actionNew_Pattern.setShortcut(_translate("MathDevEnv", "Ctrl+N", None))
        self.actionClose_Pattern.setText(_translate("MathDevEnv", "Close Pattern", None))
        self.actionClose_Pattern.setShortcut(_translate("MathDevEnv", "Ctrl+W", None))
        self.actionPaste_MathML.setText(_translate("MathDevEnv", "Paste MathML", None))
        self.actionPaste_MathML.setShortcut(_translate("MathDevEnv", "Ctrl+Shift+V", None))
        self.actionSave_Pattern.setText(_translate("MathDevEnv", "Save Pattern", None))
        self.actionSave_Pattern.setShortcut(_translate("MathDevEnv", "Ctrl+S", None))
        self.actionSave_As.setText(_translate("MathDevEnv", "Save As...", None))
        self.actionSave_As.setShortcut(_translate("MathDevEnv", "Ctrl+Shift+S", None))

from gui.mathml_editor import MathMLEditor