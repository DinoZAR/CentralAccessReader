# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car\forms/mainwindow.ui'
#
# Created: Wed Jun 11 09:25:30 2014
#      by: PyQt4 UI code generator 4.11
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
        MainWindow.resize(1168, 761)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icons/CAR_About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(25, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.mainMenuButton = QtGui.QPushButton(self.centralwidget)
        self.mainMenuButton.setMaximumSize(QtCore.QSize(16777215, 38))
        self.mainMenuButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainMenuButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/menu_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainMenuButton.setIcon(icon1)
        self.mainMenuButton.setIconSize(QtCore.QSize(32, 32))
        self.mainMenuButton.setObjectName(_fromUtf8("mainMenuButton"))
        self.horizontalLayout_3.addWidget(self.mainMenuButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(20)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.navigationTabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.navigationTabWidget.setUsesScrollButtons(False)
        self.navigationTabWidget.setObjectName(_fromUtf8("navigationTabWidget"))
        self.bookmarksTab = QtGui.QWidget()
        self.bookmarksTab.setObjectName(_fromUtf8("bookmarksTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.bookmarksTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bookmarksTreeView = QtGui.QTreeView(self.bookmarksTab)
        self.bookmarksTreeView.setHeaderHidden(True)
        self.bookmarksTreeView.setObjectName(_fromUtf8("bookmarksTreeView"))
        self.verticalLayout.addWidget(self.bookmarksTreeView)
        self.navigationTabWidget.addTab(self.bookmarksTab, _fromUtf8(""))
        self.pagesTab = QtGui.QWidget()
        self.pagesTab.setObjectName(_fromUtf8("pagesTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.pagesTab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pagesTreeView = QtGui.QTreeView(self.pagesTab)
        self.pagesTreeView.setHeaderHidden(True)
        self.pagesTreeView.setObjectName(_fromUtf8("pagesTreeView"))
        self.verticalLayout_2.addWidget(self.pagesTreeView)
        self.navigationTabWidget.addTab(self.pagesTab, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.navigationTabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.bookmarkZoomInButton = QtGui.QPushButton(self.layoutWidget)
        self.bookmarkZoomInButton.setMaximumSize(QtCore.QSize(32, 32))
        self.bookmarkZoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.bookmarkZoomInButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/magnify_add_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomInButton.setIcon(icon2)
        self.bookmarkZoomInButton.setIconSize(QtCore.QSize(24, 24))
        self.bookmarkZoomInButton.setFlat(True)
        self.bookmarkZoomInButton.setObjectName(_fromUtf8("bookmarkZoomInButton"))
        self.horizontalLayout_2.addWidget(self.bookmarkZoomInButton)
        self.bookmarkZoomOutButton = QtGui.QPushButton(self.layoutWidget)
        self.bookmarkZoomOutButton.setMaximumSize(QtCore.QSize(32, 32))
        self.bookmarkZoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.bookmarkZoomOutButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/magnify_minus_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bookmarkZoomOutButton.setIcon(icon3)
        self.bookmarkZoomOutButton.setIconSize(QtCore.QSize(24, 24))
        self.bookmarkZoomOutButton.setFlat(True)
        self.bookmarkZoomOutButton.setObjectName(_fromUtf8("bookmarkZoomOutButton"))
        self.horizontalLayout_2.addWidget(self.bookmarkZoomOutButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.openDocumentButton = QtGui.QPushButton(self.layoutWidget1)
        self.openDocumentButton.setMaximumSize(QtCore.QSize(60, 30))
        self.openDocumentButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.openDocumentButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/add_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openDocumentButton.setIcon(icon4)
        self.openDocumentButton.setIconSize(QtCore.QSize(24, 24))
        self.openDocumentButton.setFlat(True)
        self.openDocumentButton.setObjectName(_fromUtf8("openDocumentButton"))
        self.verticalLayout_3.addWidget(self.openDocumentButton)
        self.controlPanel = QtGui.QFrame(self.layoutWidget1)
        self.controlPanel.setMaximumSize(QtCore.QSize(62, 16777215))
        self.controlPanel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.controlPanel.setFrameShadow(QtGui.QFrame.Raised)
        self.controlPanel.setLineWidth(0)
        self.controlPanel.setObjectName(_fromUtf8("controlPanel"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.controlPanel)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.playButton = QtGui.QPushButton(self.controlPanel)
        self.playButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.playButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/play_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon5)
        self.playButton.setIconSize(QtCore.QSize(70, 70))
        self.playButton.setFlat(True)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.verticalLayout_7.addWidget(self.playButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem2)
        self.speechSettingsButton = QtGui.QPushButton(self.controlPanel)
        self.speechSettingsButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.speechSettingsButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/speech_settings_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speechSettingsButton.setIcon(icon6)
        self.speechSettingsButton.setIconSize(QtCore.QSize(70, 70))
        self.speechSettingsButton.setCheckable(True)
        self.speechSettingsButton.setFlat(True)
        self.speechSettingsButton.setObjectName(_fromUtf8("speechSettingsButton"))
        self.verticalLayout_7.addWidget(self.speechSettingsButton)
        self.colorSettingsButton = QtGui.QPushButton(self.controlPanel)
        self.colorSettingsButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.colorSettingsButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/color_settings_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.colorSettingsButton.setIcon(icon7)
        self.colorSettingsButton.setIconSize(QtCore.QSize(70, 70))
        self.colorSettingsButton.setCheckable(True)
        self.colorSettingsButton.setFlat(True)
        self.colorSettingsButton.setObjectName(_fromUtf8("colorSettingsButton"))
        self.verticalLayout_7.addWidget(self.colorSettingsButton)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem3)
        self.saveToMP3Button = QtGui.QPushButton(self.controlPanel)
        self.saveToMP3Button.setMaximumSize(QtCore.QSize(16777215, 60))
        self.saveToMP3Button.setFocusPolicy(QtCore.Qt.TabFocus)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/export_mp3_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveToMP3Button.setIcon(icon8)
        self.saveToMP3Button.setIconSize(QtCore.QSize(70, 70))
        self.saveToMP3Button.setFlat(True)
        self.saveToMP3Button.setObjectName(_fromUtf8("saveToMP3Button"))
        self.verticalLayout_7.addWidget(self.saveToMP3Button)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem4)
        self.zoomInButton = QtGui.QPushButton(self.controlPanel)
        self.zoomInButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zoomInButton.setFont(font)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomInButton.setIcon(icon2)
        self.zoomInButton.setIconSize(QtCore.QSize(70, 70))
        self.zoomInButton.setFlat(True)
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.verticalLayout_7.addWidget(self.zoomInButton)
        self.zoomOutButton = QtGui.QPushButton(self.controlPanel)
        self.zoomOutButton.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zoomOutButton.setFont(font)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomOutButton.setIcon(icon3)
        self.zoomOutButton.setIconSize(QtCore.QSize(70, 70))
        self.zoomOutButton.setFlat(True)
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.verticalLayout_7.addWidget(self.zoomOutButton)
        self.zoomResetButton = QtGui.QPushButton(self.controlPanel)
        self.zoomResetButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.zoomResetButton.setFocusPolicy(QtCore.Qt.TabFocus)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/magnify_reset_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomResetButton.setIcon(icon9)
        self.zoomResetButton.setIconSize(QtCore.QSize(70, 70))
        self.zoomResetButton.setFlat(True)
        self.zoomResetButton.setObjectName(_fromUtf8("zoomResetButton"))
        self.verticalLayout_7.addWidget(self.zoomResetButton)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.splitterButton = QtGui.QPushButton(self.controlPanel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitterButton.sizePolicy().hasHeightForWidth())
        self.splitterButton.setSizePolicy(sizePolicy)
        self.splitterButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.splitterButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.splitterButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/sidebar_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.splitterButton.setIcon(icon10)
        self.splitterButton.setIconSize(QtCore.QSize(70, 70))
        self.splitterButton.setCheckable(True)
        self.splitterButton.setChecked(True)
        self.splitterButton.setFlat(True)
        self.splitterButton.setObjectName(_fromUtf8("splitterButton"))
        self.verticalLayout_7.addWidget(self.splitterButton)
        self.verticalLayout_3.addWidget(self.controlPanel)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.documentTabWidget = QtGui.QTabWidget(self.layoutWidget1)
        self.documentTabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.documentTabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.documentTabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.documentTabWidget.setUsesScrollButtons(True)
        self.documentTabWidget.setDocumentMode(False)
        self.documentTabWidget.setTabsClosable(True)
        self.documentTabWidget.setMovable(True)
        self.documentTabWidget.setObjectName(_fromUtf8("documentTabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.documentTabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.documentTabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.documentTabWidget)
        self.updateDownloadProgress = DownloadProgressWidget(self.layoutWidget1)
        self.updateDownloadProgress.setObjectName(_fromUtf8("updateDownloadProgress"))
        self.verticalLayout_5.addWidget(self.updateDownloadProgress)
        self.verticalLayout_5.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1168, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuFunction = QtGui.QMenu(self.menuBar)
        self.menuFunction.setObjectName(_fromUtf8("menuFunction"))
        self.menuMP3 = QtGui.QMenu(self.menuBar)
        self.menuMP3.setObjectName(_fromUtf8("menuMP3"))
        self.menuSettings = QtGui.QMenu(self.menuBar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuMathML = QtGui.QMenu(self.menuBar)
        self.menuMathML.setObjectName(_fromUtf8("menuMathML"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_Docx = QtGui.QAction(MainWindow)
        self.actionOpen_Docx.setObjectName(_fromUtf8("actionOpen_Docx"))
        self.actionOpen_Pattern_Editor = QtGui.QAction(MainWindow)
        self.actionOpen_Pattern_Editor.setObjectName(_fromUtf8("actionOpen_Pattern_Editor"))
        self.actionShow_All_MathML = QtGui.QAction(MainWindow)
        self.actionShow_All_MathML.setObjectName(_fromUtf8("actionShow_All_MathML"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/application_exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon11)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionTutorial = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/help_contents.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTutorial.setIcon(icon12)
        self.actionTutorial.setObjectName(_fromUtf8("actionTutorial"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/help_about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon13)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionReport_a_Bug = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/report_bug.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReport_a_Bug.setIcon(icon14)
        self.actionReport_a_Bug.setObjectName(_fromUtf8("actionReport_a_Bug"))
        self.actionTake_A_Survey = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/spread.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTake_A_Survey.setIcon(icon15)
        self.actionTake_A_Survey.setObjectName(_fromUtf8("actionTake_A_Survey"))
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionPlay = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon16)
        self.actionPlay.setObjectName(_fromUtf8("actionPlay"))
        self.actionStop = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon17)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionSave_Selection_to_MP3 = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/text_speak.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Selection_to_MP3.setIcon(icon18)
        self.actionSave_Selection_to_MP3.setObjectName(_fromUtf8("actionSave_Selection_to_MP3"))
        self.actionSave_All_to_MP3 = QtGui.QAction(MainWindow)
        self.actionSave_All_to_MP3.setIcon(icon18)
        self.actionSave_All_to_MP3.setObjectName(_fromUtf8("actionSave_All_to_MP3"))
        self.actionHighlights_Colors_and_Fonts = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/color_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHighlights_Colors_and_Fonts.setIcon(icon19)
        self.actionHighlights_Colors_and_Fonts.setObjectName(_fromUtf8("actionHighlights_Colors_and_Fonts"))
        self.actionSpeech = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/system_config_services.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeech.setIcon(icon20)
        self.actionSpeech.setObjectName(_fromUtf8("actionSpeech"))
        self.actionZoom_In = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_in_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon21)
        self.actionZoom_In.setObjectName(_fromUtf8("actionZoom_In"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_out_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon22)
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionReset_Zoom = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom_fit_best_small.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_Zoom.setIcon(icon23)
        self.actionReset_Zoom.setObjectName(_fromUtf8("actionReset_Zoom"))
        self.actionIncrease_Volume = QtGui.QAction(MainWindow)
        self.actionIncrease_Volume.setObjectName(_fromUtf8("actionIncrease_Volume"))
        self.actionDecrease_Volume = QtGui.QAction(MainWindow)
        self.actionDecrease_Volume.setObjectName(_fromUtf8("actionDecrease_Volume"))
        self.actionIncrease_Rate = QtGui.QAction(MainWindow)
        self.actionIncrease_Rate.setObjectName(_fromUtf8("actionIncrease_Rate"))
        self.actionDecrease_Rate = QtGui.QAction(MainWindow)
        self.actionDecrease_Rate.setObjectName(_fromUtf8("actionDecrease_Rate"))
        self.actionEntire_Document = QtGui.QAction(MainWindow)
        self.actionEntire_Document.setIcon(icon18)
        self.actionEntire_Document.setObjectName(_fromUtf8("actionEntire_Document"))
        self.actionCurrent_Selection = QtGui.QAction(MainWindow)
        self.actionCurrent_Selection.setIcon(icon18)
        self.actionCurrent_Selection.setObjectName(_fromUtf8("actionCurrent_Selection"))
        self.actionBy_Page = QtGui.QAction(MainWindow)
        self.actionBy_Page.setIcon(icon18)
        self.actionBy_Page.setObjectName(_fromUtf8("actionBy_Page"))
        self.actionExport_to_HTML = QtGui.QAction(MainWindow)
        self.actionExport_to_HTML.setObjectName(_fromUtf8("actionExport_to_HTML"))
        self.actionExport_to_FlexHTML = QtGui.QAction(MainWindow)
        self.actionExport_to_FlexHTML.setObjectName(_fromUtf8("actionExport_to_FlexHTML"))
        self.actionExport_to_MathPlayerHTML = QtGui.QAction(MainWindow)
        self.actionExport_to_MathPlayerHTML.setObjectName(_fromUtf8("actionExport_to_FlexHTML"))
        self.actionExport_to_MathJaxHTML = QtGui.QAction(MainWindow)
        self.actionExport_to_MathJaxHTML.setObjectName(_fromUtf8("actionExport_to_MathJaxHTML"))
        self.actionExport_to_PNGHTML = QtGui.QAction(MainWindow)
        self.actionExport_to_PNGHTML.setObjectName(_fromUtf8("actionExport_to_PNGHTML"))
        self.actionClose_Document = QtGui.QAction(MainWindow)
        self.actionClose_Document.setObjectName(_fromUtf8("actionClose_Document"))
        self.actionPaste_From_Clipboard = QtGui.QAction(MainWindow)
        self.actionPaste_From_Clipboard.setObjectName(_fromUtf8("actionPaste_From_Clipboard"))
        self.actionBatch = QtGui.QAction(MainWindow)
        self.actionBatch.setObjectName(_fromUtf8("actionBatch"))
        self.actionAnnouncements = QtGui.QAction(MainWindow)
        self.actionAnnouncements.setObjectName(_fromUtf8("actionAnnouncements"))
        self.actionQuick_Start = QtGui.QAction(MainWindow)
        self.actionQuick_Start.setCheckable(True)
        self.actionQuick_Start.setObjectName(_fromUtf8("actionQuick_Start"))
        self.menuFile.addAction(self.actionOpen_Docx)
        self.menuFile.addAction(self.actionClose_Document)
        self.menuFile.addAction(self.actionPaste_From_Clipboard)
        self.menuFile.addSeparator()
        #self.menuFile.addAction(self.actionExport_to_HTML)
        #self.menuFile.addAction(self.actionExport_to_MathJaxHTML)
        self.menuFile.addAction(self.actionExport_to_PNGHTML)
        self.menuFile.addAction(self.actionExport_to_FlexHTML)
        self.menuFile.addAction(self.actionExport_to_MathPlayerHTML)
        self.menuFile.addAction(self.actionBatch)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFunction.addAction(self.actionPlay)
        self.menuFunction.addAction(self.actionStop)
        self.menuFunction.addSeparator()
        self.menuFunction.addAction(self.actionZoom_In)
        self.menuFunction.addAction(self.actionZoom_Out)
        self.menuFunction.addAction(self.actionReset_Zoom)
        self.menuFunction.addSeparator()
        self.menuFunction.addAction(self.actionIncrease_Volume)
        self.menuFunction.addAction(self.actionDecrease_Volume)
        self.menuFunction.addAction(self.actionIncrease_Rate)
        self.menuFunction.addAction(self.actionDecrease_Rate)
        self.menuFunction.addSeparator()
        self.menuFunction.addAction(self.actionSearch)
        self.menuMP3.addAction(self.actionSave_All_to_MP3)
        self.menuMP3.addAction(self.actionSave_Selection_to_MP3)
        self.menuMP3.addSeparator()
        self.menuMP3.addAction(self.actionBy_Page)
        self.menuSettings.addAction(self.actionSpeech)
        self.menuSettings.addAction(self.actionHighlights_Colors_and_Fonts)
        self.menuMathML.addAction(self.actionOpen_Pattern_Editor)
        self.menuMathML.addAction(self.actionShow_All_MathML)
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addAction(self.actionAnnouncements)
        self.menuHelp.addAction(self.actionQuick_Start)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionReport_a_Bug)
        self.menuHelp.addAction(self.actionTake_A_Survey)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuFunction.menuAction())
        self.menuBar.addAction(self.menuMP3.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuMathML.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.navigationTabWidget.setCurrentIndex(0)
        self.documentTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Central Access Reader", None))
        self.mainMenuButton.setToolTip(_translate("MainWindow", "Main Menu", None))
        self.navigationTabWidget.setTabText(self.navigationTabWidget.indexOf(self.bookmarksTab), _translate("MainWindow", "Headings", None))
        self.navigationTabWidget.setTabText(self.navigationTabWidget.indexOf(self.pagesTab), _translate("MainWindow", "Pages", None))
        self.bookmarkZoomInButton.setToolTip(_translate("MainWindow", "Zoom In", None))
        self.bookmarkZoomOutButton.setToolTip(_translate("MainWindow", "Zoom Out", None))
        self.openDocumentButton.setToolTip(_translate("MainWindow", "Open Document", None))
        self.playButton.setToolTip(_translate("MainWindow", "Start", None))
        self.speechSettingsButton.setToolTip(_translate("MainWindow", "General Settings", None))
        self.colorSettingsButton.setToolTip(_translate("MainWindow", "Color Settings", None))
        self.saveToMP3Button.setToolTip(_translate("MainWindow", "Save All To MP3", None))
        self.zoomInButton.setToolTip(_translate("MainWindow", "Zoom In", None))
        self.zoomOutButton.setToolTip(_translate("MainWindow", "Zoom Out", None))
        self.zoomResetButton.setToolTip(_translate("MainWindow", "Reset Zoom", None))
        self.splitterButton.setToolTip(_translate("MainWindow", "Show/Hide Navigation", None))
        self.documentTabWidget.setTabText(self.documentTabWidget.indexOf(self.tab_3), _translate("MainWindow", "1701 Essentials of Mathematics", None))
        self.documentTabWidget.setTabText(self.documentTabWidget.indexOf(self.tab_4), _translate("MainWindow", "1551 Ch 01 Statistics for the Behavorial Sciences", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuFunction.setTitle(_translate("MainWindow", "Functions", None))
        self.menuMP3.setTitle(_translate("MainWindow", "MP3", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuMathML.setTitle(_translate("MainWindow", "Math", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_Docx.setText(_translate("MainWindow", "&Open Word Document", None))
        self.actionOpen_Docx.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionOpen_Pattern_Editor.setText(_translate("MainWindow", "&Math Library Development Environment", None))
        self.actionShow_All_MathML.setText(_translate("MainWindow", "&Show All MathML...", None))
        self.actionQuit.setText(_translate("MainWindow", "&Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionTutorial.setText(_translate("MainWindow", "&Tutorial", None))
        self.actionTutorial.setShortcut(_translate("MainWindow", "Ctrl+Shift+H", None))
        self.actionAbout.setText(_translate("MainWindow", "&About", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+Alt+H", None))
        self.actionReport_a_Bug.setText(_translate("MainWindow", "Report a &Bug", None))
        self.actionTake_A_Survey.setText(_translate("MainWindow", "Give Us &Feedback", None))
        self.actionSearch.setText(_translate("MainWindow", "S&earch", None))
        self.actionSearch.setToolTip(_translate("MainWindow", "Toggles the search bar on and off.", None))
        self.actionSearch.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionPlay.setText(_translate("MainWindow", "&Read", None))
        self.actionPlay.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionStop.setText(_translate("MainWindow", "&Stop", None))
        self.actionStop.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSave_Selection_to_MP3.setText(_translate("MainWindow", "Save &Selection", None))
        self.actionSave_Selection_to_MP3.setShortcut(_translate("MainWindow", "Ctrl+Shift+M", None))
        self.actionSave_All_to_MP3.setText(_translate("MainWindow", "Save &All", None))
        self.actionSave_All_to_MP3.setShortcut(_translate("MainWindow", "Ctrl+M", None))
        self.actionHighlights_Colors_and_Fonts.setText(_translate("MainWindow", "&Color", None))
        self.actionHighlights_Colors_and_Fonts.setShortcut(_translate("MainWindow", "F2", None))
        self.actionSpeech.setText(_translate("MainWindow", "&General", None))
        self.actionSpeech.setShortcut(_translate("MainWindow", "F1", None))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out", None))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "Ctrl+-", None))
        self.actionReset_Zoom.setText(_translate("MainWindow", "Reset Zoom", None))
        self.actionReset_Zoom.setShortcut(_translate("MainWindow", "Ctrl+Backspace", None))
        self.actionIncrease_Volume.setText(_translate("MainWindow", "Increase Volume", None))
        self.actionIncrease_Volume.setToolTip(_translate("MainWindow", "Increase Volume", None))
        self.actionIncrease_Volume.setShortcut(_translate("MainWindow", "Ctrl+Up", None))
        self.actionDecrease_Volume.setText(_translate("MainWindow", "Decrease Volume", None))
        self.actionDecrease_Volume.setToolTip(_translate("MainWindow", "Decrease Volume", None))
        self.actionDecrease_Volume.setShortcut(_translate("MainWindow", "Ctrl+Down", None))
        self.actionIncrease_Rate.setText(_translate("MainWindow", "Increase Rate", None))
        self.actionIncrease_Rate.setToolTip(_translate("MainWindow", "Increase Rate", None))
        self.actionIncrease_Rate.setShortcut(_translate("MainWindow", "Ctrl+Right", None))
        self.actionDecrease_Rate.setText(_translate("MainWindow", "Decrease Rate", None))
        self.actionDecrease_Rate.setToolTip(_translate("MainWindow", "Decrease Rate", None))
        self.actionDecrease_Rate.setShortcut(_translate("MainWindow", "Ctrl+Left", None))
        self.actionEntire_Document.setText(_translate("MainWindow", "Entire Document", None))
        self.actionCurrent_Selection.setText(_translate("MainWindow", "Current Selection", None))
        self.actionBy_Page.setText(_translate("MainWindow", "Save By Page", None))
        self.actionExport_to_HTML.setText(_translate("MainWindow", "&[HTML] MathML: Voiceover (iOS/Mac)", None))
        self.actionExport_to_FlexHTML.setText(_translate("MainWindow","&[HTML] Flex", None))
        self.actionExport_to_MathPlayerHTML.setText(_translate("MainWindow","&[HTML] MathPlayer 4.0", None))
        self.actionExport_to_MathJaxHTML.setText(_translate("MainWindow", "&[HTML] MathJax: JAWS 16", None))
        self.actionExport_to_PNGHTML.setText(_translate("MainWindow", "&[HTML] PNG: JAWS 15/NVDA/Windows Eyes", None))
        self.actionClose_Document.setText(_translate("MainWindow", "Close Document", None))
        self.actionClose_Document.setToolTip(_translate("MainWindow", "Closes the current document.", None))
        self.actionClose_Document.setShortcut(_translate("MainWindow", "Ctrl+W", None))
        self.actionPaste_From_Clipboard.setText(_translate("MainWindow", "Paste From Clipboard", None))
        self.actionPaste_From_Clipboard.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionBatch.setText(_translate("MainWindow", "Batch", None))
        self.actionAnnouncements.setText(_translate("MainWindow", "Announcements", None))
        self.actionQuick_Start.setText(_translate("MainWindow", "Quick Start", None))

from car.gui.download_progress import DownloadProgressWidget
import resource_rc
