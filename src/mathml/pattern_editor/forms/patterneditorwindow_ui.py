# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace2\another\src\mathml\pattern_editor\forms/patterneditorwindow.ui'
#
# Created: Thu Jun 06 17:07:40 2013
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

class Ui_PatternEditorWindow(object):
    def setupUi(self, PatternEditorWindow):
        PatternEditorWindow.setObjectName(_fromUtf8("PatternEditorWindow"))
        PatternEditorWindow.resize(996, 544)
        font = QtGui.QFont()
        font.setPointSize(12)
        PatternEditorWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(PatternEditorWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.speakButton = QtGui.QPushButton(self.centralwidget)
        self.speakButton.setObjectName(_fromUtf8("speakButton"))
        self.horizontalLayout.addWidget(self.speakButton)
        self.outputText = QtGui.QLineEdit(self.centralwidget)
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName(_fromUtf8("outputText"))
        self.horizontalLayout.addWidget(self.outputText)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(10)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.databaseLabel = QtGui.QLabel(self.layoutWidget)
        self.databaseLabel.setObjectName(_fromUtf8("databaseLabel"))
        self.verticalLayout_3.addWidget(self.databaseLabel)
        self.databaseEditor = Qsci.QsciScintilla(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.databaseEditor.setFont(font)
        self.databaseEditor.setToolTip(_fromUtf8(""))
        self.databaseEditor.setWhatsThis(_fromUtf8(""))
        self.databaseEditor.setObjectName(_fromUtf8("databaseEditor"))
        self.verticalLayout_3.addWidget(self.databaseEditor)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.mathmlEditor = Qsci.QsciScintilla(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.mathmlEditor.setFont(font)
        self.mathmlEditor.setToolTip(_fromUtf8(""))
        self.mathmlEditor.setWhatsThis(_fromUtf8(""))
        self.mathmlEditor.setObjectName(_fromUtf8("mathmlEditor"))
        self.verticalLayout.addWidget(self.mathmlEditor)
        self.layoutWidget2 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.expandAllButton = QtGui.QPushButton(self.layoutWidget2)
        self.expandAllButton.setObjectName(_fromUtf8("expandAllButton"))
        self.horizontalLayout_2.addWidget(self.expandAllButton)
        self.collapseAllButton = QtGui.QPushButton(self.layoutWidget2)
        self.collapseAllButton.setObjectName(_fromUtf8("collapseAllButton"))
        self.horizontalLayout_2.addWidget(self.collapseAllButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.stagesTreeView = QtGui.QTreeView(self.layoutWidget2)
        self.stagesTreeView.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.stagesTreeView.setRootIsDecorated(True)
        self.stagesTreeView.setHeaderHidden(True)
        self.stagesTreeView.setObjectName(_fromUtf8("stagesTreeView"))
        self.stagesTreeView.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.stagesTreeView)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.verticalLayout_4.setStretch(1, 1)
        PatternEditorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PatternEditorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        PatternEditorWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(PatternEditorWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(PatternEditorWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(PatternEditorWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(PatternEditorWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionQuit = QtGui.QAction(PatternEditorWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOpen_MathML = QtGui.QAction(PatternEditorWindow)
        self.actionOpen_MathML.setObjectName(_fromUtf8("actionOpen_MathML"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_MathML)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PatternEditorWindow)
        QtCore.QMetaObject.connectSlotsByName(PatternEditorWindow)

    def retranslateUi(self, PatternEditorWindow):
        PatternEditorWindow.setWindowTitle(_translate("PatternEditorWindow", "MathML Pattern Editor", None))
        self.speakButton.setToolTip(_translate("PatternEditorWindow", "Parses and speaks the MathML (Ctrl+R works too)", None))
        self.speakButton.setText(_translate("PatternEditorWindow", "Speak", None))
        self.speakButton.setShortcut(_translate("PatternEditorWindow", "Ctrl+R", None))
        self.databaseLabel.setText(_translate("PatternEditorWindow", "Database", None))
        self.label_4.setText(_translate("PatternEditorWindow", "Test MathML", None))
        self.label_2.setText(_translate("PatternEditorWindow", "Stages", None))
        self.expandAllButton.setText(_translate("PatternEditorWindow", "Expand All", None))
        self.collapseAllButton.setText(_translate("PatternEditorWindow", "Collapse All", None))
        self.menuFile.setTitle(_translate("PatternEditorWindow", "File", None))
        self.actionNew.setText(_translate("PatternEditorWindow", "New", None))
        self.actionNew.setShortcut(_translate("PatternEditorWindow", "Ctrl+N", None))
        self.actionOpen.setText(_translate("PatternEditorWindow", "Open Database", None))
        self.actionOpen.setShortcut(_translate("PatternEditorWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("PatternEditorWindow", "Save", None))
        self.actionSave.setShortcut(_translate("PatternEditorWindow", "Ctrl+S", None))
        self.actionSave_As.setText(_translate("PatternEditorWindow", "Save As", None))
        self.actionSave_As.setShortcut(_translate("PatternEditorWindow", "Ctrl+Shift+S", None))
        self.actionQuit.setText(_translate("PatternEditorWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("PatternEditorWindow", "Ctrl+Q", None))
        self.actionOpen_MathML.setText(_translate("PatternEditorWindow", "Open MathML", None))
        self.actionOpen_MathML.setShortcut(_translate("PatternEditorWindow", "Ctrl+Shift+O", None))

from PyQt4 import Qsci
