# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Spen-ZAR\workspace\NiftyProseArticulator\src\forms/mainwindow.ui'
#
# Created: Thu Mar 07 06:43:51 2013
#      by: PyQt4 UI code generator 4.9.6
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
        MainWindow.resize(1075, 773)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/cwuLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/cwuLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(12)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMargin(5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.bookmarksTreeView = QtGui.QTreeView(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bookmarksTreeView.setFont(font)
        self.bookmarksTreeView.setHeaderHidden(True)
        self.bookmarksTreeView.setObjectName(_fromUtf8("bookmarksTreeView"))
        self.verticalLayout_2.addWidget(self.bookmarksTreeView)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playButton = QtGui.QPushButton(self.layoutWidget1)
        self.playButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setIconSize(QtCore.QSize(50, 50))
        self.playButton.setFlat(True)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtGui.QPushButton(self.layoutWidget1)
        self.pauseButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setIconSize(QtCore.QSize(50, 50))
        self.pauseButton.setFlat(True)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout.addWidget(self.pauseButton)
        self.repeatButton = QtGui.QPushButton(self.layoutWidget1)
        self.repeatButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/loop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeatButton.setIcon(icon3)
        self.repeatButton.setIconSize(QtCore.QSize(50, 50))
        self.repeatButton.setFlat(True)
        self.repeatButton.setObjectName(_fromUtf8("repeatButton"))
        self.horizontalLayout.addWidget(self.repeatButton)
        self.settingsButton = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setItalic(False)
        self.settingsButton.setFont(font)
        self.settingsButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system_config_services.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon4)
        self.settingsButton.setIconSize(QtCore.QSize(50, 50))
        self.settingsButton.setFlat(True)
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.horizontalLayout.addWidget(self.settingsButton)
        self.lastWordButton = QtGui.QPushButton(self.layoutWidget1)
        self.lastWordButton.setObjectName(_fromUtf8("lastWordButton"))
        self.horizontalLayout.addWidget(self.lastWordButton)
        self.nextWordButton = QtGui.QPushButton(self.layoutWidget1)
        self.nextWordButton.setObjectName(_fromUtf8("nextWordButton"))
        self.horizontalLayout.addWidget(self.nextWordButton)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(6, -1, 6, -1)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.rateSlider = QtGui.QSlider(self.layoutWidget1)
        self.rateSlider.setMinimumSize(QtCore.QSize(160, 0))
        self.rateSlider.setMinimum(100)
        self.rateSlider.setMaximum(300)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setObjectName(_fromUtf8("rateSlider"))
        self.gridLayout.addWidget(self.rateSlider, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.volumeSlider = QtGui.QSlider(self.layoutWidget1)
        self.volumeSlider.setMinimumSize(QtCore.QSize(160, 0))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.gridLayout.addWidget(self.volumeSlider, 1, 2, 1, 1)
        self.rateLabel = QtGui.QLabel(self.layoutWidget1)
        self.rateLabel.setObjectName(_fromUtf8("rateLabel"))
        self.gridLayout.addWidget(self.rateLabel, 0, 1, 1, 1)
        self.volLabel = QtGui.QLabel(self.layoutWidget1)
        self.volLabel.setObjectName(_fromUtf8("volLabel"))
        self.gridLayout.addWidget(self.volLabel, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(7, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(self.layoutWidget1)
        self.webView.setSizeIncrement(QtCore.QSize(1, 1))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuMathML = QtGui.QMenu(self.menubar)
        self.menuMathML.setObjectName(_fromUtf8("menuMathML"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Docx = QtGui.QAction(MainWindow)
        self.actionOpen_Docx.setObjectName(_fromUtf8("actionOpen_Docx"))
        self.actionOpen_HTML = QtGui.QAction(MainWindow)
        self.actionOpen_HTML.setObjectName(_fromUtf8("actionOpen_HTML"))
        self.actionOpen_Pattern_Editor = QtGui.QAction(MainWindow)
        self.actionOpen_Pattern_Editor.setObjectName(_fromUtf8("actionOpen_Pattern_Editor"))
        self.actionShow_All_MathML = QtGui.QAction(MainWindow)
        self.actionShow_All_MathML.setObjectName(_fromUtf8("actionShow_All_MathML"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionManual = QtGui.QAction(MainWindow)
        self.actionManual.setObjectName(_fromUtf8("actionManual"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuMenu.addAction(self.actionOpen_Docx)
        self.menuMenu.addAction(self.actionOpen_HTML)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuMathML.addAction(self.actionOpen_Pattern_Editor)
        self.menuMathML.addAction(self.actionShow_All_MathML)
        self.menuHelp.addAction(self.actionManual)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMathML.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Nifty Prose Articulator", None))
        self.label_3.setText(_translate("MainWindow", "Bookmarks:", None))
        self.playButton.setToolTip(_translate("MainWindow", "Play button", None))
        self.pauseButton.setToolTip(_translate("MainWindow", "Stop button", None))
        self.repeatButton.setToolTip(_translate("MainWindow", "Repeat button", None))
        self.settingsButton.setToolTip(_translate("MainWindow", "Settings button", None))
        self.lastWordButton.setText(_translate("MainWindow", "Last Word", None))
        self.nextWordButton.setText(_translate("MainWindow", "Next Word", None))
        self.label_2.setText(_translate("MainWindow", "Volume:", None))
        self.rateSlider.setToolTip(_translate("MainWindow", "Words per minute slider", None))
        self.label.setText(_translate("MainWindow", "Rate:", None))
        self.volumeSlider.setToolTip(_translate("MainWindow", "Volume slider", None))
        self.rateLabel.setText(_translate("MainWindow", "200", None))
        self.volLabel.setText(_translate("MainWindow", "100", None))
        self.menuMenu.setTitle(_translate("MainWindow", "File", None))
        self.menuMathML.setTitle(_translate("MainWindow", "MathML", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_Docx.setText(_translate("MainWindow", "Open Docx", None))
        self.actionOpen_Docx.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionOpen_HTML.setText(_translate("MainWindow", "Open HTML", None))
        self.actionOpen_HTML.setShortcut(_translate("MainWindow", "Ctrl+Shift+O", None))
        self.actionOpen_Pattern_Editor.setText(_translate("MainWindow", "Open Pattern Editor...", None))
        self.actionShow_All_MathML.setText(_translate("MainWindow", "Show All MathML...", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionManual.setText(_translate("MainWindow", "Manual", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))

from PyQt4 import QtWebKit
import resource_rc
