# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace2\another\src\forms/mainwindow.ui'
#
# Created: Thu May 09 08:40:10 2013
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
        MainWindow.resize(1054, 741)
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMargin(5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.bookmarkZoomInButton = QtGui.QPushButton(self.layoutWidget)
        self.bookmarkZoomInButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_in_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomInButton.setIcon(icon1)
        self.bookmarkZoomInButton.setIconSize(QtCore.QSize(32, 32))
        self.bookmarkZoomInButton.setFlat(True)
        self.bookmarkZoomInButton.setObjectName(_fromUtf8("bookmarkZoomInButton"))
        self.horizontalLayout_2.addWidget(self.bookmarkZoomInButton)
        self.bookmarkZoomOutButton = QtGui.QPushButton(self.layoutWidget)
        self.bookmarkZoomOutButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_out_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomOutButton.setIcon(icon2)
        self.bookmarkZoomOutButton.setIconSize(QtCore.QSize(32, 32))
        self.bookmarkZoomOutButton.setFlat(True)
        self.bookmarkZoomOutButton.setObjectName(_fromUtf8("bookmarkZoomOutButton"))
        self.horizontalLayout_2.addWidget(self.bookmarkZoomOutButton)
        self.refreshButton = QtGui.QPushButton(self.layoutWidget)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.horizontalLayout_2.addWidget(self.refreshButton)
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.bookmarksTreeView = QtGui.QTreeView(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookmarksTreeView.setFont(font)
        self.bookmarksTreeView.setHeaderHidden(True)
        self.bookmarksTreeView.setObjectName(_fromUtf8("bookmarksTreeView"))
        self.verticalLayout_2.addWidget(self.bookmarksTreeView)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.webViewLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.webViewLayout.setMargin(0)
        self.webViewLayout.setObjectName(_fromUtf8("webViewLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playButton = QtGui.QPushButton(self.layoutWidget1)
        self.playButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon3)
        self.playButton.setIconSize(QtCore.QSize(50, 50))
        self.playButton.setFlat(True)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtGui.QPushButton(self.layoutWidget1)
        self.pauseButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon4)
        self.pauseButton.setIconSize(QtCore.QSize(50, 50))
        self.pauseButton.setFlat(True)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout.addWidget(self.pauseButton)
        self.speechSettingsButton = QtGui.QPushButton(self.layoutWidget1)
        self.speechSettingsButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system_config_services.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speechSettingsButton.setIcon(icon5)
        self.speechSettingsButton.setIconSize(QtCore.QSize(50, 50))
        self.speechSettingsButton.setFlat(True)
        self.speechSettingsButton.setObjectName(_fromUtf8("speechSettingsButton"))
        self.horizontalLayout.addWidget(self.speechSettingsButton)
        self.colorSettingsButton = QtGui.QPushButton(self.layoutWidget1)
        self.colorSettingsButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/color_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorSettingsButton.setIcon(icon6)
        self.colorSettingsButton.setIconSize(QtCore.QSize(50, 50))
        self.colorSettingsButton.setFlat(True)
        self.colorSettingsButton.setObjectName(_fromUtf8("colorSettingsButton"))
        self.horizontalLayout.addWidget(self.colorSettingsButton)
        self.saveToMP3Button = QtGui.QPushButton(self.layoutWidget1)
        self.saveToMP3Button.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/text_speak.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveToMP3Button.setIcon(icon7)
        self.saveToMP3Button.setIconSize(QtCore.QSize(50, 50))
        self.saveToMP3Button.setFlat(True)
        self.saveToMP3Button.setObjectName(_fromUtf8("saveToMP3Button"))
        self.horizontalLayout.addWidget(self.saveToMP3Button)
        self.zoomInButton = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setItalic(False)
        self.zoomInButton.setFont(font)
        self.zoomInButton.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomInButton.setIcon(icon8)
        self.zoomInButton.setIconSize(QtCore.QSize(50, 50))
        self.zoomInButton.setFlat(True)
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.horizontalLayout.addWidget(self.zoomInButton)
        self.zoomOutButton = QtGui.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setItalic(False)
        self.zoomOutButton.setFont(font)
        self.zoomOutButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomOutButton.setIcon(icon9)
        self.zoomOutButton.setIconSize(QtCore.QSize(50, 50))
        self.zoomOutButton.setFlat(True)
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.horizontalLayout.addWidget(self.zoomOutButton)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(6, -1, 6, -1)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.rateSlider = QtGui.QSlider(self.layoutWidget1)
        self.rateSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.rateSlider.setMinimum(0)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 50)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.rateSlider.setTickInterval(10)
        self.rateSlider.setObjectName(_fromUtf8("rateSlider"))
        self.gridLayout.addWidget(self.rateSlider, 0, 1, 1, 1)
        self.volumeSlider = QtGui.QSlider(self.layoutWidget1)
        self.volumeSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.gridLayout.addWidget(self.volumeSlider, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(8, 1)
        self.webViewLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(self.layoutWidget1)
        self.webView.setSizeIncrement(QtCore.QSize(1, 1))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.webViewLayout.addWidget(self.webView)
        self.webViewLayout.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 21))
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
        self.actionOpen_Pattern_Editor = QtGui.QAction(MainWindow)
        self.actionOpen_Pattern_Editor.setObjectName(_fromUtf8("actionOpen_Pattern_Editor"))
        self.actionShow_All_MathML = QtGui.QAction(MainWindow)
        self.actionShow_All_MathML.setObjectName(_fromUtf8("actionShow_All_MathML"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionTutorial = QtGui.QAction(MainWindow)
        self.actionTutorial.setObjectName(_fromUtf8("actionTutorial"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionReport_a_Bug = QtGui.QAction(MainWindow)
        self.actionReport_a_Bug.setObjectName(_fromUtf8("actionReport_a_Bug"))
        self.menuMenu.addAction(self.actionOpen_Docx)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuMathML.addAction(self.actionOpen_Pattern_Editor)
        self.menuMathML.addAction(self.actionShow_All_MathML)
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionReport_a_Bug)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMathML.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Nifty Prose Articulator", None))
        self.label_3.setText(_translate("MainWindow", "Navigation:", None))
        self.refreshButton.setText(_translate("MainWindow", "Refresh", None))
        self.playButton.setToolTip(_translate("MainWindow", "Play button", None))
        self.playButton.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.pauseButton.setToolTip(_translate("MainWindow", "Stop button", None))
        self.pauseButton.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.zoomInButton.setToolTip(_translate("MainWindow", "Settings button", None))
        self.zoomInButton.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.zoomOutButton.setToolTip(_translate("MainWindow", "Settings button", None))
        self.zoomOutButton.setShortcut(_translate("MainWindow", "Ctrl+-", None))
        self.label_2.setText(_translate("MainWindow", "Volume:", None))
        self.label.setText(_translate("MainWindow", "Rate:", None))
        self.rateSlider.setToolTip(_translate("MainWindow", "Words per minute slider", None))
        self.volumeSlider.setToolTip(_translate("MainWindow", "Volume slider", None))
        self.menuMenu.setTitle(_translate("MainWindow", "File", None))
        self.menuMathML.setTitle(_translate("MainWindow", "MathML", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_Docx.setText(_translate("MainWindow", "Open Word Document", None))
        self.actionOpen_Docx.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionOpen_Pattern_Editor.setText(_translate("MainWindow", "Open Pattern Editor...", None))
        self.actionShow_All_MathML.setText(_translate("MainWindow", "Show All MathML...", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionReport_a_Bug.setText(_translate("MainWindow", "Report a Bug", None))

from PyQt4 import QtWebKit
import resource_rc
