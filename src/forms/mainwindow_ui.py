# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/mainwindow.ui'
#
# Created: Fri Sep 13 14:31:11 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 633)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/CAR_Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(20)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bookmarkZoomInButton = QtGui.QPushButton(self.layoutWidget)
        self.bookmarkZoomInButton.setMaximumSize(QtCore.QSize(32, 32))
        self.bookmarkZoomInButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/zoom_in_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomInButton.setIcon(icon1)
        self.bookmarkZoomInButton.setIconSize(QtCore.QSize(32, 32))
        self.bookmarkZoomInButton.setFlat(True)
        self.bookmarkZoomInButton.setObjectName("bookmarkZoomInButton")
        self.horizontalLayout_2.addWidget(self.bookmarkZoomInButton)
        self.bookmarkZoomOutButton = QtGui.QPushButton(self.layoutWidget)
        self.bookmarkZoomOutButton.setMaximumSize(QtCore.QSize(32, 32))
        self.bookmarkZoomOutButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/zoom_out_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomOutButton.setIcon(icon2)
        self.bookmarkZoomOutButton.setIconSize(QtCore.QSize(32, 32))
        self.bookmarkZoomOutButton.setFlat(True)
        self.bookmarkZoomOutButton.setObjectName("bookmarkZoomOutButton")
        self.horizontalLayout_2.addWidget(self.bookmarkZoomOutButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.bookmarksTab = QtGui.QWidget()
        self.bookmarksTab.setObjectName("bookmarksTab")
        self.verticalLayout = QtGui.QVBoxLayout(self.bookmarksTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bookmarksTreeView = QtGui.QTreeView(self.bookmarksTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookmarksTreeView.setFont(font)
        self.bookmarksTreeView.setHeaderHidden(True)
        self.bookmarksTreeView.setObjectName("bookmarksTreeView")
        self.verticalLayout.addWidget(self.bookmarksTreeView)
        self.tabWidget.addTab(self.bookmarksTab, "")
        self.pagesTab = QtGui.QWidget()
        self.pagesTab.setObjectName("pagesTab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.pagesTab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pagesTreeView = QtGui.QTreeView(self.pagesTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pagesTreeView.setFont(font)
        self.pagesTreeView.setHeaderHidden(True)
        self.pagesTreeView.setObjectName("pagesTreeView")
        self.verticalLayout_2.addWidget(self.pagesTreeView)
        self.tabWidget.addTab(self.pagesTab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.webViewLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.webViewLayout.setSpacing(0)
        self.webViewLayout.setContentsMargins(0, 0, 0, 0)
        self.webViewLayout.setObjectName("webViewLayout")
        self.scrollArea = QtGui.QScrollArea(self.layoutWidget1)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 945, 76))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.playButton.setMaximumSize(QtCore.QSize(60, 50))
        self.playButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon3)
        self.playButton.setIconSize(QtCore.QSize(50, 50))
        self.playButton.setFlat(True)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pauseButton.setMaximumSize(QtCore.QSize(60, 50))
        self.pauseButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon4)
        self.pauseButton.setIconSize(QtCore.QSize(50, 50))
        self.pauseButton.setFlat(True)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.speechSettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.speechSettingsButton.setMaximumSize(QtCore.QSize(60, 50))
        self.speechSettingsButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/system_config_services.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speechSettingsButton.setIcon(icon5)
        self.speechSettingsButton.setIconSize(QtCore.QSize(50, 50))
        self.speechSettingsButton.setFlat(True)
        self.speechSettingsButton.setObjectName("speechSettingsButton")
        self.horizontalLayout.addWidget(self.speechSettingsButton)
        self.colorSettingsButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.colorSettingsButton.setMaximumSize(QtCore.QSize(60, 50))
        self.colorSettingsButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/color_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorSettingsButton.setIcon(icon6)
        self.colorSettingsButton.setIconSize(QtCore.QSize(50, 50))
        self.colorSettingsButton.setFlat(True)
        self.colorSettingsButton.setObjectName("colorSettingsButton")
        self.horizontalLayout.addWidget(self.colorSettingsButton)
        self.saveToMP3Button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.saveToMP3Button.setMaximumSize(QtCore.QSize(60, 50))
        self.saveToMP3Button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/text_speak.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveToMP3Button.setIcon(icon7)
        self.saveToMP3Button.setIconSize(QtCore.QSize(50, 50))
        self.saveToMP3Button.setFlat(True)
        self.saveToMP3Button.setObjectName("saveToMP3Button")
        self.horizontalLayout.addWidget(self.saveToMP3Button)
        self.zoomInButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.zoomInButton.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setItalic(False)
        self.zoomInButton.setFont(font)
        self.zoomInButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomInButton.setIcon(icon8)
        self.zoomInButton.setIconSize(QtCore.QSize(50, 50))
        self.zoomInButton.setFlat(True)
        self.zoomInButton.setObjectName("zoomInButton")
        self.horizontalLayout.addWidget(self.zoomInButton)
        self.zoomOutButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.zoomOutButton.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setItalic(False)
        self.zoomOutButton.setFont(font)
        self.zoomOutButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomOutButton.setIcon(icon9)
        self.zoomOutButton.setIconSize(QtCore.QSize(50, 50))
        self.zoomOutButton.setFlat(True)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.horizontalLayout.addWidget(self.zoomOutButton)
        self.zoomResetButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.zoomResetButton.setMaximumSize(QtCore.QSize(60, 50))
        self.zoomResetButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/zoom_fit_best.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomResetButton.setIcon(icon10)
        self.zoomResetButton.setIconSize(QtCore.QSize(50, 50))
        self.zoomResetButton.setFlat(True)
        self.zoomResetButton.setObjectName("zoomResetButton")
        self.horizontalLayout.addWidget(self.zoomResetButton)
        self.sliderGridLayout = QtGui.QGridLayout()
        self.sliderGridLayout.setContentsMargins(6, -1, 6, -1)
        self.sliderGridLayout.setHorizontalSpacing(12)
        self.sliderGridLayout.setObjectName("sliderGridLayout")
        self.volumeLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.volumeLabel.setObjectName("volumeLabel")
        self.sliderGridLayout.addWidget(self.volumeLabel, 1, 0, 1, 1)
        self.rateLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.rateLabel.setObjectName("rateLabel")
        self.sliderGridLayout.addWidget(self.rateLabel, 0, 0, 1, 1)
        self.rateSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        self.rateSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.rateSlider.setMinimum(0)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setProperty("value", 50)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.rateSlider.setTickInterval(10)
        self.rateSlider.setObjectName("rateSlider")
        self.sliderGridLayout.addWidget(self.rateSlider, 0, 1, 1, 1)
        self.volumeSlider = QtGui.QSlider(self.scrollAreaWidgetContents)
        self.volumeSlider.setMinimumSize(QtCore.QSize(201, 0))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName("volumeSlider")
        self.sliderGridLayout.addWidget(self.volumeSlider, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.sliderGridLayout)
        spacerItem2 = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.getUpdateButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/update_down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getUpdateButton.setIcon(icon11)
        self.getUpdateButton.setIconSize(QtCore.QSize(32, 32))
        self.getUpdateButton.setCheckable(False)
        self.getUpdateButton.setFlat(True)
        self.getUpdateButton.setObjectName("getUpdateButton")
        self.horizontalLayout.addWidget(self.getUpdateButton)
        self.horizontalLayout.setStretch(9, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.webViewLayout.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchLabel = QtGui.QLabel(self.layoutWidget1)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout_3.addWidget(self.searchLabel)
        self.searchUpButton = QtGui.QPushButton(self.layoutWidget1)
        self.searchUpButton.setMaximumSize(QtCore.QSize(45, 32))
        self.searchUpButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchUpButton.setIcon(icon12)
        self.searchUpButton.setIconSize(QtCore.QSize(32, 32))
        self.searchUpButton.setFlat(True)
        self.searchUpButton.setObjectName("searchUpButton")
        self.horizontalLayout_3.addWidget(self.searchUpButton)
        self.searchDownButton = QtGui.QPushButton(self.layoutWidget1)
        self.searchDownButton.setMaximumSize(QtCore.QSize(45, 32))
        self.searchDownButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchDownButton.setIcon(icon13)
        self.searchDownButton.setIconSize(QtCore.QSize(32, 32))
        self.searchDownButton.setFlat(True)
        self.searchDownButton.setObjectName("searchDownButton")
        self.horizontalLayout_3.addWidget(self.searchDownButton)
        self.searchTextBox = QtGui.QLineEdit(self.layoutWidget1)
        self.searchTextBox.setObjectName("searchTextBox")
        self.horizontalLayout_3.addWidget(self.searchTextBox)
        self.searchSettingsButton = QtGui.QPushButton(self.layoutWidget1)
        self.searchSettingsButton.setMaximumSize(QtCore.QSize(45, 32))
        self.searchSettingsButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchSettingsButton.setIcon(icon14)
        self.searchSettingsButton.setIconSize(QtCore.QSize(32, 32))
        self.searchSettingsButton.setFlat(True)
        self.searchSettingsButton.setObjectName("searchSettingsButton")
        self.horizontalLayout_3.addWidget(self.searchSettingsButton)
        self.closeSearchButton = QtGui.QPushButton(self.layoutWidget1)
        self.closeSearchButton.setMaximumSize(QtCore.QSize(45, 32))
        self.closeSearchButton.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/icons/dialog_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeSearchButton.setIcon(icon15)
        self.closeSearchButton.setIconSize(QtCore.QSize(32, 32))
        self.closeSearchButton.setFlat(True)
        self.closeSearchButton.setObjectName("closeSearchButton")
        self.horizontalLayout_3.addWidget(self.closeSearchButton)
        self.webViewLayout.addLayout(self.horizontalLayout_3)
        self.webView = QtWebKit.QWebView(self.layoutWidget1)
        self.webView.setSizeIncrement(QtCore.QSize(1, 1))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webViewLayout.addWidget(self.webView)
        self.webViewLayout.setStretch(2, 1)
        self.horizontalLayout_4.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMathML = QtGui.QMenu(self.menubar)
        self.menuMathML.setObjectName("menuMathML")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFunctions = QtGui.QMenu(self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Docx = QtGui.QAction(MainWindow)
        self.actionOpen_Docx.setObjectName("actionOpen_Docx")
        self.actionOpen_Pattern_Editor = QtGui.QAction(MainWindow)
        self.actionOpen_Pattern_Editor.setObjectName("actionOpen_Pattern_Editor")
        self.actionShow_All_MathML = QtGui.QAction(MainWindow)
        self.actionShow_All_MathML.setObjectName("actionShow_All_MathML")
        self.actionQuit = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/icons/application_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon16)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTutorial = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/icons/help_contents.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTutorial.setIcon(icon17)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/icons/help_about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon18)
        self.actionAbout.setObjectName("actionAbout")
        self.actionReport_a_Bug = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/icons/report_bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReport_a_Bug.setIcon(icon19)
        self.actionReport_a_Bug.setObjectName("actionReport_a_Bug")
        self.actionTake_A_Survey = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/icons/spread.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTake_A_Survey.setIcon(icon20)
        self.actionTake_A_Survey.setObjectName("actionTake_A_Survey")
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionPlay = QtGui.QAction(MainWindow)
        self.actionPlay.setIcon(icon3)
        self.actionPlay.setObjectName("actionPlay")
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setIcon(icon4)
        self.actionStop.setObjectName("actionStop")
        self.actionSave_Selection_to_MP3 = QtGui.QAction(MainWindow)
        self.actionSave_Selection_to_MP3.setIcon(icon7)
        self.actionSave_Selection_to_MP3.setObjectName("actionSave_Selection_to_MP3")
        self.actionSave_All_to_MP3 = QtGui.QAction(MainWindow)
        self.actionSave_All_to_MP3.setIcon(icon7)
        self.actionSave_All_to_MP3.setObjectName("actionSave_All_to_MP3")
        self.actionHighlights_Colors_and_Fonts = QtGui.QAction(MainWindow)
        self.actionHighlights_Colors_and_Fonts.setIcon(icon6)
        self.actionHighlights_Colors_and_Fonts.setObjectName("actionHighlights_Colors_and_Fonts")
        self.actionSpeech = QtGui.QAction(MainWindow)
        self.actionSpeech.setIcon(icon5)
        self.actionSpeech.setObjectName("actionSpeech")
        self.actionZoom_In = QtGui.QAction(MainWindow)
        self.actionZoom_In.setIcon(icon1)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        self.actionZoom_Out.setIcon(icon2)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionReset_Zoom = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/icons/zoom_fit_best_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_Zoom.setIcon(icon21)
        self.actionReset_Zoom.setObjectName("actionReset_Zoom")
        self.actionIncrease_Volume = QtGui.QAction(MainWindow)
        self.actionIncrease_Volume.setObjectName("actionIncrease_Volume")
        self.actionDecrease_Volume = QtGui.QAction(MainWindow)
        self.actionDecrease_Volume.setObjectName("actionDecrease_Volume")
        self.actionIncrease_Rate = QtGui.QAction(MainWindow)
        self.actionIncrease_Rate.setObjectName("actionIncrease_Rate")
        self.actionDecrease_Rate = QtGui.QAction(MainWindow)
        self.actionDecrease_Rate.setObjectName("actionDecrease_Rate")
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
        self.menuFunctions.addAction(self.actionIncrease_Volume)
        self.menuFunctions.addAction(self.actionDecrease_Volume)
        self.menuFunctions.addAction(self.actionIncrease_Rate)
        self.menuFunctions.addAction(self.actionDecrease_Rate)
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Central Access Reader", None, QtGui.QApplication.UnicodeUTF8))
        self.bookmarkZoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.bookmarkZoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bookmarksTab), QtGui.QApplication.translate("MainWindow", "Headings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pagesTab), QtGui.QApplication.translate("MainWindow", "Pages", None, QtGui.QApplication.UnicodeUTF8))
        self.playButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Read", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.speechSettingsButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Speech Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.colorSettingsButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Highlighting, Colors, and Fonts Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.saveToMP3Button.setToolTip(QtGui.QApplication.translate("MainWindow", "Save All To MP3", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomResetButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Reset Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeLabel.setText(QtGui.QApplication.translate("MainWindow", "Volume:", None, QtGui.QApplication.UnicodeUTF8))
        self.rateLabel.setText(QtGui.QApplication.translate("MainWindow", "Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.rateSlider.setToolTip(QtGui.QApplication.translate("MainWindow", "Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.volumeSlider.setToolTip(QtGui.QApplication.translate("MainWindow", "Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.getUpdateButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Update Available!", None, QtGui.QApplication.UnicodeUTF8))
        self.getUpdateButton.setText(QtGui.QApplication.translate("MainWindow", "Update Available!", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLabel.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchUpButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Previous Occurrence", None, QtGui.QApplication.UnicodeUTF8))
        self.searchDownButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Next Occurrence", None, QtGui.QApplication.UnicodeUTF8))
        self.searchSettingsButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Search Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.closeSearchButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Close Search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMathML.setTitle(QtGui.QApplication.translate("MainWindow", "&MathML", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFunctions.setTitle(QtGui.QApplication.translate("MainWindow", "F&unctions", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Docx.setText(QtGui.QApplication.translate("MainWindow", "&Open Word Document", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Docx.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Pattern_Editor.setText(QtGui.QApplication.translate("MainWindow", "&Open Pattern Editor...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_All_MathML.setText(QtGui.QApplication.translate("MainWindow", "&Show All MathML...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTutorial.setText(QtGui.QApplication.translate("MainWindow", "&Tutorial", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTutorial.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReport_a_Bug.setText(QtGui.QApplication.translate("MainWindow", "Report a &Bug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTake_A_Survey.setText(QtGui.QApplication.translate("MainWindow", "Take A &Survey", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("MainWindow", "S&earch", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setToolTip(QtGui.QApplication.translate("MainWindow", "Toggles the search bar on and off.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setText(QtGui.QApplication.translate("MainWindow", "&Read", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "&Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Selection_to_MP3.setText(QtGui.QApplication.translate("MainWindow", "Save &Selection to MP3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Selection_to_MP3.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_All_to_MP3.setText(QtGui.QApplication.translate("MainWindow", "Save &All to MP3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_All_to_MP3.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlights_Colors_and_Fonts.setText(QtGui.QApplication.translate("MainWindow", "&Highlights, Colors, and Fonts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlights_Colors_and_Fonts.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpeech.setText(QtGui.QApplication.translate("MainWindow", "&Speech", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpeech.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset_Zoom.setText(QtGui.QApplication.translate("MainWindow", "Reset Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset_Zoom.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncrease_Volume.setText(QtGui.QApplication.translate("MainWindow", "Increase Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncrease_Volume.setToolTip(QtGui.QApplication.translate("MainWindow", "Increase Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncrease_Volume.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecrease_Volume.setText(QtGui.QApplication.translate("MainWindow", "Decrease Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecrease_Volume.setToolTip(QtGui.QApplication.translate("MainWindow", "Decrease Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecrease_Volume.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Down", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncrease_Rate.setText(QtGui.QApplication.translate("MainWindow", "Increase Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncrease_Rate.setToolTip(QtGui.QApplication.translate("MainWindow", "Increase Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncrease_Rate.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecrease_Rate.setText(QtGui.QApplication.translate("MainWindow", "Decrease Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecrease_Rate.setToolTip(QtGui.QApplication.translate("MainWindow", "Decrease Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecrease_Rate.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Left", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
import resource_rc
