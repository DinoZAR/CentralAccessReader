# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car\forms/math_library_dev.ui'
#
# Created: Mon Jun 09 10:07:03 2014
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

class Ui_MathLibraryDev(object):
    def setupUi(self, MathLibraryDev):
        MathLibraryDev.setObjectName(_fromUtf8("MathLibraryDev"))
        MathLibraryDev.resize(1030, 710)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icons/CAR_About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MathLibraryDev.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MathLibraryDev)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runButton = QtGui.QPushButton(self.centralwidget)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.horizontalLayout.addWidget(self.runButton)
        self.proseOutput = QtGui.QLineEdit(self.centralwidget)
        self.proseOutput.setObjectName(_fromUtf8("proseOutput"))
        self.horizontalLayout.addWidget(self.proseOutput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.libraryTabs = QtGui.QTabWidget(self.splitter)
        self.libraryTabs.setTabsClosable(True)
        self.libraryTabs.setMovable(True)
        self.libraryTabs.setObjectName(_fromUtf8("libraryTabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.libraryTabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.libraryTabs.addTab(self.tab_2, _fromUtf8(""))
        self.mathmlEditor = MathMLEditor(self.splitter)
        self.mathmlEditor.setMinimumSize(QtCore.QSize(200, 200))
        self.mathmlEditor.setObjectName(_fromUtf8("mathmlEditor"))
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout.setStretch(1, 1)
        MathLibraryDev.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MathLibraryDev)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuInstalled_Libraries = QtGui.QMenu(self.menuFile)
        self.menuInstalled_Libraries.setObjectName(_fromUtf8("menuInstalled_Libraries"))
        self.menuMathML = QtGui.QMenu(self.menubar)
        self.menuMathML.setObjectName(_fromUtf8("menuMathML"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MathLibraryDev.setMenuBar(self.menubar)
        self.actionNew_Library = QtGui.QAction(MathLibraryDev)
        self.actionNew_Library.setObjectName(_fromUtf8("actionNew_Library"))
        self.actionOpen_Library = QtGui.QAction(MathLibraryDev)
        self.actionOpen_Library.setObjectName(_fromUtf8("actionOpen_Library"))
        self.actionNew_Pattern = QtGui.QAction(MathLibraryDev)
        self.actionNew_Pattern.setObjectName(_fromUtf8("actionNew_Pattern"))
        self.actionOpen_Pattern = QtGui.QAction(MathLibraryDev)
        self.actionOpen_Pattern.setObjectName(_fromUtf8("actionOpen_Pattern"))
        self.actionSave = QtGui.QAction(MathLibraryDev)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MathLibraryDev)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionQuit = QtGui.QAction(MathLibraryDev)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionFrom_Clipboard = QtGui.QAction(MathLibraryDev)
        self.actionFrom_Clipboard.setObjectName(_fromUtf8("actionFrom_Clipboard"))
        self.actionThings = QtGui.QAction(MathLibraryDev)
        self.actionThings.setObjectName(_fromUtf8("actionThings"))
        self.actionExport = QtGui.QAction(MathLibraryDev)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionContents = QtGui.QAction(MathLibraryDev)
        self.actionContents.setObjectName(_fromUtf8("actionContents"))
        self.menuInstalled_Libraries.addAction(self.actionThings)
        self.menuFile.addAction(self.actionNew_Library)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuInstalled_Libraries.menuAction())
        self.menuFile.addAction(self.actionOpen_Library)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_Pattern)
        self.menuFile.addAction(self.actionOpen_Pattern)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menuMathML.addAction(self.actionFrom_Clipboard)
        self.menuHelp.addAction(self.actionContents)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMathML.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MathLibraryDev)
        self.libraryTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MathLibraryDev)

    def retranslateUi(self, MathLibraryDev):
        MathLibraryDev.setWindowTitle(_translate("MathLibraryDev", "Math Library Development Environment", None))
        self.runButton.setText(_translate("MathLibraryDev", "Run", None))
        self.libraryTabs.setTabText(self.libraryTabs.indexOf(self.tab), _translate("MathLibraryDev", "Tab 1", None))
        self.libraryTabs.setTabText(self.libraryTabs.indexOf(self.tab_2), _translate("MathLibraryDev", "Tab 2", None))
        self.menuFile.setTitle(_translate("MathLibraryDev", "File", None))
        self.menuInstalled_Libraries.setTitle(_translate("MathLibraryDev", "Open Library", None))
        self.menuMathML.setTitle(_translate("MathLibraryDev", "MathML", None))
        self.menuHelp.setTitle(_translate("MathLibraryDev", "Help", None))
        self.actionNew_Library.setText(_translate("MathLibraryDev", "New Library", None))
        self.actionNew_Library.setShortcut(_translate("MathLibraryDev", "Ctrl+Shift+N", None))
        self.actionOpen_Library.setText(_translate("MathLibraryDev", "Open Library From File", None))
        self.actionOpen_Library.setShortcut(_translate("MathLibraryDev", "Ctrl+Shift+O", None))
        self.actionNew_Pattern.setText(_translate("MathLibraryDev", "New Pattern", None))
        self.actionNew_Pattern.setShortcut(_translate("MathLibraryDev", "Ctrl+N", None))
        self.actionOpen_Pattern.setText(_translate("MathLibraryDev", "Open Pattern", None))
        self.actionOpen_Pattern.setShortcut(_translate("MathLibraryDev", "Ctrl+O", None))
        self.actionSave.setText(_translate("MathLibraryDev", "Save", None))
        self.actionSave.setShortcut(_translate("MathLibraryDev", "Ctrl+S", None))
        self.actionSave_As.setText(_translate("MathLibraryDev", "Save As...", None))
        self.actionSave_As.setShortcut(_translate("MathLibraryDev", "Ctrl+Shift+S", None))
        self.actionQuit.setText(_translate("MathLibraryDev", "Quit", None))
        self.actionFrom_Clipboard.setText(_translate("MathLibraryDev", "From Clipboard", None))
        self.actionFrom_Clipboard.setShortcut(_translate("MathLibraryDev", "Ctrl+Shift+V", None))
        self.actionThings.setText(_translate("MathLibraryDev", "Things", None))
        self.actionExport.setText(_translate("MathLibraryDev", "Export...", None))
        self.actionContents.setText(_translate("MathLibraryDev", "Guide", None))

from car.gui.mathml_editor import MathMLEditor
import resource_rc
