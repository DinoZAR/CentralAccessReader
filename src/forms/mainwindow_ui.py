# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace\nifty-prose-articulator\src\forms/mainwindow.ui'
#
# Created: Mon Jul 22 10:01:03 2013
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
        MainWindow.resize(1200, 673)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/CAR_Logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(20)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea_2 = QtGui.QScrollArea(self.layoutWidget)
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.scrollArea_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 405, 40))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setMargin(5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.bookmarkZoomInButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.bookmarkZoomInButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_in_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomInButton.setIcon(icon1)
        self.bookmarkZoomInButton.setIconSize(QtCore.QSize(32, 32))
        self.bookmarkZoomInButton.setFlat(True)
        self.bookmarkZoomInButton.setObjectName(_fromUtf8("bookmarkZoomInButton"))
        self.horizontalLayout_2.addWidget(self.bookmarkZoomInButton)
        self.bookmarkZoomOutButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.bookmarkZoomOutButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_out_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomOutButton.setIcon(icon2)
        self.bookmarkZoomOutButton.setIconSize(QtCore.QSize(32, 32))
        self.bookmarkZoomOutButton.setFlat(True)
        self.bookmarkZoomOutButton.setObjectName(_fromUtf8("bookmarkZoomOutButton"))
        self.horizontalLayout_2.addWidget(self.bookmarkZoomOutButton)
        self.expandBookmarksButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.expandBookmarksButton.setIconSize(QtCore.QSize(32, 32))
        self.expandBookmarksButton.setFlat(False)
        self.expandBookmarksButton.setObjectName(_fromUtf8("expandBookmarksButton"))
        self.horizontalLayout_2.addWidget(self.expandBookmarksButton)
        self.collapseBookmarksButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.collapseBookmarksButton.setIconSize(QtCore.QSize(32, 32))
        self.collapseBookmarksButton.setFlat(False)
        self.collapseBookmarksButton.setObjectName(_fromUtf8("collapseBookmarksButton"))
        self.horizontalLayout_2.addWidget(self.collapseBookmarksButton)
        spacerItem = QtGui.QSpacerItem(76, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.bookmarksTab = QtGui.QWidget()
        self.bookmarksTab.setObjectName(_fromUtf8("bookmarksTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.bookmarksTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bookmarksTreeView = QtGui.QTreeView(self.bookmarksTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookmarksTreeView.setFont(font)
        self.bookmarksTreeView.setHeaderHidden(True)
        self.bookmarksTreeView.setObjectName(_fromUtf8("bookmarksTreeView"))
        self.verticalLayout.addWidget(self.bookmarksTreeView)
        self.tabWidget.addTab(self.bookmarksTab, _fromUtf8(""))
        self.pagesTab = QtGui.QWidget()
        self.pagesTab.setObjectName(_fromUtf8("pagesTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.pagesTab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pagesTreeView = QtGui.QTreeView(self.pagesTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pagesTreeView.setFont(font)
        self.pagesTreeView.setHeaderHidden(True)
        self.pagesTreeView.setObjectName(_fromUtf8("pagesTreeView"))
        self.verticalLayout_2.addWidget(self.pagesTreeView)
        self.tabWidget.addTab(self.pagesTab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_3.setStretch(1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.webViewLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.webViewLayout.setSpacing(0)
        self.webViewLayout.setMargin(0)
        self.webViewLayout.setObjectName(_fromUtf8("webViewLayout"))
        self.scrollArea = QtGui.QScrollArea(self.layoutWidget1)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 947, 69))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.playButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon3)
        self.playButton.setIconSize(QtCore.QSize(50, 50))
        self.playButton.setFlat(True)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pauseButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon4)
        self.pauseButton.setIconSize(QtCore.QSize(50, 50))
        self.pauseButton.setFlat(True)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout.addWidget(self.pauseButton)
        self.speechSettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.speechSettingsButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system_config_services.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speechSettingsButton.setIcon(icon5)
        self.speechSettingsButton.setIconSize(QtCore.QSize(50, 50))
        self.speechSettingsButton.setFlat(True)
        self.speechSettingsButton.setObjectName(_fromUtf8("speechSettingsButton"))
        self.horizontalLayout.addWidget(self.speechSettingsButton)
        self.colorSettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.colorSettingsButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/color_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorSettingsButton.setIcon(icon6)
        self.colorSettingsButton.setIconSize(QtCore.QSize(50, 50))
        self.colorSettingsButton.setFlat(True)
        self.colorSettingsButton.setObjectName(_fromUtf8("colorSettingsButton"))
        self.horizontalLayout.addWidget(self.colorSettingsButton)
        self.saveToMP3Button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.saveToMP3Button.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/text_speak.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveToMP3Button.setIcon(icon7)
        self.saveToMP3Button.setIconSize(QtCore.QSize(50, 50))
        self.saveToMP3Button.setFlat(True)
        self.saveToMP3Button.setObjectName(_fromUtf8("saveToMP3Button"))
        self.horizontalLayout.addWidget(self.saveToMP3Button)
        self.zoomInButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
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
        self.zoomOutButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
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
        self.zoomResetButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.zoomResetButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_fit_best.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomResetButton.setIcon(icon10)
        self.zoomResetButton.setIconSize(QtCore.QSize(50, 50))
        self.zoomResetButton.setFlat(True)
        self.zoomResetButton.setObjectName(_fromUtf8("zoomResetButton"))
        self.horizontalLayout.addWidget(self.zoomResetButton)
        self.sliderGridLayout = QtGui.QGridLayout()
        self.sliderGridLayout.setContentsMargins(6, -1, 6, -1)
        self.sliderGridLayout.setHorizontalSpacing(12)
        self.sliderGridLayout.setObjectName(_fromUtf8("sliderGridLayout"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sliderGridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.sliderGridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.rateSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        self.rateSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.rateSlider.setMinimum(0)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 50)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.rateSlider.setTickInterval(10)
        self.rateSlider.setObjectName(_fromUtf8("rateSlider"))
        self.sliderGridLayout.addWidget(self.rateSlider, 0, 1, 1, 1)
        self.volumeSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        self.volumeSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.sliderGridLayout.addWidget(self.volumeSlider, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.sliderGridLayout)
        spacerItem1 = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.getUpdateButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/update_down_arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getUpdateButton.setIcon(icon11)
        self.getUpdateButton.setIconSize(QtCore.QSize(32, 32))
        self.getUpdateButton.setCheckable(False)
        self.getUpdateButton.setFlat(True)
        self.getUpdateButton.setObjectName(_fromUtf8("getUpdateButton"))
        self.horizontalLayout.addWidget(self.getUpdateButton)
        self.horizontalLayout.setStretch(9, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.webViewLayout.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.searchLabel = QtGui.QLabel(self.layoutWidget1)
        self.searchLabel.setObjectName(_fromUtf8("searchLabel"))
        self.horizontalLayout_3.addWidget(self.searchLabel)
        self.searchUpButton = QtGui.QPushButton(self.layoutWidget1)
        self.searchUpButton.setText(_fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchUpButton.setIcon(icon12)
        self.searchUpButton.setIconSize(QtCore.QSize(32, 32))
        self.searchUpButton.setFlat(True)
        self.searchUpButton.setObjectName(_fromUtf8("searchUpButton"))
        self.horizontalLayout_3.addWidget(self.searchUpButton)
        self.searchDownButton = QtGui.QPushButton(self.layoutWidget1)
        self.searchDownButton.setText(_fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchDownButton.setIcon(icon13)
        self.searchDownButton.setIconSize(QtCore.QSize(32, 32))
        self.searchDownButton.setFlat(True)
        self.searchDownButton.setObjectName(_fromUtf8("searchDownButton"))
        self.horizontalLayout_3.addWidget(self.searchDownButton)
        self.searchTextBox = QtGui.QLineEdit(self.layoutWidget1)
        self.searchTextBox.setObjectName(_fromUtf8("searchTextBox"))
        self.horizontalLayout_3.addWidget(self.searchTextBox)
        self.searchSettingsButton = QtGui.QPushButton(self.layoutWidget1)
        self.searchSettingsButton.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/gear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchSettingsButton.setIcon(icon14)
        self.searchSettingsButton.setIconSize(QtCore.QSize(32, 32))
        self.searchSettingsButton.setFlat(True)
        self.searchSettingsButton.setObjectName(_fromUtf8("searchSettingsButton"))
        self.horizontalLayout_3.addWidget(self.searchSettingsButton)
        self.closeSearchButton = QtGui.QPushButton(self.layoutWidget1)
        self.closeSearchButton.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/dialog_close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeSearchButton.setIcon(icon15)
        self.closeSearchButton.setIconSize(QtCore.QSize(32, 32))
        self.closeSearchButton.setFlat(True)
        self.closeSearchButton.setObjectName(_fromUtf8("closeSearchButton"))
        self.horizontalLayout_3.addWidget(self.closeSearchButton)
        self.webViewLayout.addLayout(self.horizontalLayout_3)
        self.webView = QtWebKit.QWebView(self.layoutWidget1)
        self.webView.setSizeIncrement(QtCore.QSize(1, 1))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.webViewLayout.addWidget(self.webView)
        self.webViewLayout.setStretch(2, 1)
        self.verticalLayout_5.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuMathML = QtGui.QMenu(self.menubar)
        self.menuMathML.setObjectName(_fromUtf8("menuMathML"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFunctions = QtGui.QMenu(self.menubar)
        self.menuFunctions.setObjectName(_fromUtf8("menuFunctions"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Docx = QtGui.QAction(MainWindow)
        self.actionOpen_Docx.setObjectName(_fromUtf8("actionOpen_Docx"))
        self.actionOpen_Pattern_Editor = QtGui.QAction(MainWindow)
        self.actionOpen_Pattern_Editor.setObjectName(_fromUtf8("actionOpen_Pattern_Editor"))
        self.actionShow_All_MathML = QtGui.QAction(MainWindow)
        self.actionShow_All_MathML.setObjectName(_fromUtf8("actionShow_All_MathML"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/application_exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon16)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionTutorial = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/help_contents.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTutorial.setIcon(icon17)
        self.actionTutorial.setObjectName(_fromUtf8("actionTutorial"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/help_about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon18)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionReport_a_Bug = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/report_bug.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReport_a_Bug.setIcon(icon19)
        self.actionReport_a_Bug.setObjectName(_fromUtf8("actionReport_a_Bug"))
        self.actionTake_A_Survey = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/spread.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTake_A_Survey.setIcon(icon20)
        self.actionTake_A_Survey.setObjectName(_fromUtf8("actionTake_A_Survey"))
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionPlay = QtGui.QAction(MainWindow)
        self.actionPlay.setIcon(icon3)
        self.actionPlay.setObjectName(_fromUtf8("actionPlay"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setIcon(icon4)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionSave_Selection_to_MP3 = QtGui.QAction(MainWindow)
        self.actionSave_Selection_to_MP3.setIcon(icon7)
        self.actionSave_Selection_to_MP3.setObjectName(_fromUtf8("actionSave_Selection_to_MP3"))
        self.actionSave_All_to_MP3 = QtGui.QAction(MainWindow)
        self.actionSave_All_to_MP3.setIcon(icon7)
        self.actionSave_All_to_MP3.setObjectName(_fromUtf8("actionSave_All_to_MP3"))
        self.actionHighlights_Colors_and_Fonts = QtGui.QAction(MainWindow)
        self.actionHighlights_Colors_and_Fonts.setIcon(icon6)
        self.actionHighlights_Colors_and_Fonts.setObjectName(_fromUtf8("actionHighlights_Colors_and_Fonts"))
        self.actionSpeech = QtGui.QAction(MainWindow)
        self.actionSpeech.setIcon(icon5)
        self.actionSpeech.setObjectName(_fromUtf8("actionSpeech"))
        self.actionZoom_In = QtGui.QAction(MainWindow)
        self.actionZoom_In.setIcon(icon1)
        self.actionZoom_In.setObjectName(_fromUtf8("actionZoom_In"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        self.actionZoom_Out.setIcon(icon2)
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionReset_Zoom = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_fit_best_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_Zoom.setIcon(icon21)
        self.actionReset_Zoom.setObjectName(_fromUtf8("actionReset_Zoom"))
        self.menuFile.addAction(self.actionOpen_Docx)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_All_to_MP3)
        self.menuFile.addAction(self.actionSave_Selection_to_MP3)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuMathML.addAction(self.actionOpen_Pattern_Editor)
        self.menuMathML.addAction(self.actionShow_All_MathML)
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionReport_a_Bug)
        self.menuHelp.addAction(self.actionTake_A_Survey)
        self.menuFunctions.addAction(self.actionPlay)
        self.menuFunctions.addAction(self.actionStop)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionZoom_In)
        self.menuFunctions.addAction(self.actionZoom_Out)
        self.menuFunctions.addAction(self.actionReset_Zoom)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.actionSearch)
        self.menuSettings.addAction(self.actionSpeech)
        self.menuSettings.addAction(self.actionHighlights_Colors_and_Fonts)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuMathML.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Central Access Reader", None))
        self.label_3.setText(_translate("MainWindow", "Navigation:", None))
        self.bookmarkZoomInButton.setToolTip(_translate("MainWindow", "Zoom In", None))
        self.bookmarkZoomOutButton.setToolTip(_translate("MainWindow", "Zoom Out", None))
        self.expandBookmarksButton.setToolTip(_translate("MainWindow", "Expand Bookmarks", None))
        self.expandBookmarksButton.setText(_translate("MainWindow", "Expand", None))
        self.collapseBookmarksButton.setToolTip(_translate("MainWindow", "Collapse Bookmarks", None))
        self.collapseBookmarksButton.setText(_translate("MainWindow", "Collapse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bookmarksTab), _translate("MainWindow", "Headings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pagesTab), _translate("MainWindow", "Pages", None))
        self.playButton.setToolTip(_translate("MainWindow", "Read (Ctrl+R)", None))
        self.pauseButton.setToolTip(_translate("MainWindow", "Stop (Ctrl+S)", None))
        self.speechSettingsButton.setToolTip(_translate("MainWindow", "Speech Settings (F1)", None))
        self.colorSettingsButton.setToolTip(_translate("MainWindow", "Highlighting, Colors, and Fonts Settings (F2)", None))
        self.saveToMP3Button.setToolTip(_translate("MainWindow", "Save All To MP3 (Ctrl+Shift+S)", None))
        self.zoomInButton.setToolTip(_translate("MainWindow", "Zoom In (Ctrl+=)", None))
        self.zoomOutButton.setToolTip(_translate("MainWindow", "Zoom Out (Ctrl+-)", None))
        self.zoomResetButton.setToolTip(_translate("MainWindow", "Reset Zoom (Ctrl+Backspace)", None))
        self.label_2.setText(_translate("MainWindow", "Volume:", None))
        self.label.setText(_translate("MainWindow", "Rate:", None))
        self.rateSlider.setToolTip(_translate("MainWindow", "Rate", None))
        self.volumeSlider.setToolTip(_translate("MainWindow", "Volume", None))
        self.getUpdateButton.setToolTip(_translate("MainWindow", "Update Available!", None))
        self.getUpdateButton.setText(_translate("MainWindow", "Update Available!", None))
        self.searchLabel.setText(_translate("MainWindow", "Search", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuMathML.setTitle(_translate("MainWindow", "&MathML", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.menuFunctions.setTitle(_translate("MainWindow", "F&unctions", None))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings", None))
        self.actionOpen_Docx.setText(_translate("MainWindow", "&Open Word Document", None))
        self.actionOpen_Docx.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionOpen_Pattern_Editor.setText(_translate("MainWindow", "&Open Pattern Editor...", None))
        self.actionShow_All_MathML.setText(_translate("MainWindow", "&Show All MathML...", None))
        self.actionQuit.setText(_translate("MainWindow", "&Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionTutorial.setText(_translate("MainWindow", "&Tutorial", None))
        self.actionTutorial.setShortcut(_translate("MainWindow", "Ctrl+H", None))
        self.actionAbout.setText(_translate("MainWindow", "&About", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+Shift+H", None))
        self.actionReport_a_Bug.setText(_translate("MainWindow", "Report a &Bug", None))
        self.actionTake_A_Survey.setText(_translate("MainWindow", "Take A &Survey", None))
        self.actionSearch.setText(_translate("MainWindow", "S&earch", None))
        self.actionSearch.setToolTip(_translate("MainWindow", "Toggles the search bar on and off.", None))
        self.actionSearch.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionPlay.setText(_translate("MainWindow", "&Read", None))
        self.actionPlay.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionStop.setText(_translate("MainWindow", "&Stop", None))
        self.actionStop.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSave_Selection_to_MP3.setText(_translate("MainWindow", "Save &Selection to MP3", None))
        self.actionSave_Selection_to_MP3.setShortcut(_translate("MainWindow", "Ctrl+Shift+M", None))
        self.actionSave_All_to_MP3.setText(_translate("MainWindow", "Save &All to MP3", None))
        self.actionSave_All_to_MP3.setShortcut(_translate("MainWindow", "Ctrl+M", None))
        self.actionHighlights_Colors_and_Fonts.setText(_translate("MainWindow", "&Highlights, Colors, and Fonts", None))
        self.actionHighlights_Colors_and_Fonts.setShortcut(_translate("MainWindow", "F2", None))
        self.actionSpeech.setText(_translate("MainWindow", "&Speech", None))
        self.actionSpeech.setShortcut(_translate("MainWindow", "F1", None))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out", None))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "Ctrl+-", None))
        self.actionReset_Zoom.setText(_translate("MainWindow", "Reset Zoom", None))
        self.actionReset_Zoom.setShortcut(_translate("MainWindow", "Ctrl+Backspace", None))

from PyQt4 import QtWebKit
import resource_rc
