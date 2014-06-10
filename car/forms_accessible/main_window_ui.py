# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Jun 10 13:23:21 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.filePathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.filePathEdit.setReadOnly(True)
        self.filePathEdit.setObjectName("filePathEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filePathEdit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.convertMP3Radio = QtWidgets.QRadioButton(self.centralwidget)
        self.convertMP3Radio.setChecked(True)
        self.convertMP3Radio.setObjectName("convertMP3Radio")
        self.verticalLayout_2.addWidget(self.convertMP3Radio)
        self.convertMP3ByPageRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.convertMP3ByPageRadio.setObjectName("convertMP3ByPageRadio")
        self.verticalLayout_2.addWidget(self.convertMP3ByPageRadio)
        self.convertHTMLRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.convertHTMLRadio.setObjectName("convertHTMLRadio")
        self.verticalLayout_2.addWidget(self.convertHTMLRadio)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.openDocumentButton = QtWidgets.QPushButton(self.centralwidget)
        self.openDocumentButton.setObjectName("openDocumentButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.openDocumentButton)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.rateSlider = QtWidgets.QSlider(self.centralwidget)
        self.rateSlider.setMaximum(100)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rateSlider.setTickInterval(10)
        self.rateSlider.setObjectName("rateSlider")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rateSlider)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName("volumeSlider")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.volumeSlider)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.pauseLengthSlider = QtWidgets.QSlider(self.centralwidget)
        self.pauseLengthSlider.setMaximum(10)
        self.pauseLengthSlider.setPageStep(2)
        self.pauseLengthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.pauseLengthSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.pauseLengthSlider.setTickInterval(1)
        self.pauseLengthSlider.setObjectName("pauseLengthSlider")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pauseLengthSlider)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.voiceCombo = QtWidgets.QComboBox(self.centralwidget)
        self.voiceCombo.setObjectName("voiceCombo")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.voiceCombo)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tagImageCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.tagImageCheckbox.setObjectName("tagImageCheckbox")
        self.verticalLayout.addWidget(self.tagImageCheckbox)
        self.tagMathCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.tagMathCheckbox.setObjectName("tagMathCheckbox")
        self.verticalLayout.addWidget(self.tagMathCheckbox)
        self.ignoreAltTextCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.ignoreAltTextCheckbox.setObjectName("ignoreAltTextCheckbox")
        self.verticalLayout.addWidget(self.ignoreAltTextCheckbox)
        self.addTOCToHTMLCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.addTOCToHTMLCheckbox.setObjectName("addTOCToHTMLCheckbox")
        self.verticalLayout.addWidget(self.addTOCToHTMLCheckbox)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setObjectName("convertButton")
        self.verticalLayout_4.addWidget(self.convertButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setObjectName("progressLabel")
        self.verticalLayout_3.addWidget(self.progressLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.cancelExportButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelExportButton.setObjectName("cancelExportButton")
        self.horizontalLayout.addWidget(self.cancelExportButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Document = QtWidgets.QAction(MainWindow)
        self.actionOpen_Document.setObjectName("actionOpen_Document")
        self.menuFile.addAction(self.actionOpen_Document)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.openDocumentButton, self.filePathEdit)
        MainWindow.setTabOrder(self.filePathEdit, self.convertMP3Radio)
        MainWindow.setTabOrder(self.convertMP3Radio, self.convertMP3ByPageRadio)
        MainWindow.setTabOrder(self.convertMP3ByPageRadio, self.convertHTMLRadio)
        MainWindow.setTabOrder(self.convertHTMLRadio, self.rateSlider)
        MainWindow.setTabOrder(self.rateSlider, self.volumeSlider)
        MainWindow.setTabOrder(self.volumeSlider, self.pauseLengthSlider)
        MainWindow.setTabOrder(self.pauseLengthSlider, self.voiceCombo)
        MainWindow.setTabOrder(self.voiceCombo, self.tagImageCheckbox)
        MainWindow.setTabOrder(self.tagImageCheckbox, self.tagMathCheckbox)
        MainWindow.setTabOrder(self.tagMathCheckbox, self.ignoreAltTextCheckbox)
        MainWindow.setTabOrder(self.ignoreAltTextCheckbox, self.addTOCToHTMLCheckbox)
        MainWindow.setTabOrder(self.addTOCToHTMLCheckbox, self.convertButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Central Access Reader"))
        self.filePathEdit.setAccessibleName(_translate("MainWindow", "File Path"))
        self.label_8.setText(_translate("MainWindow", "Convert To:"))
        self.convertMP3Radio.setAccessibleName(_translate("MainWindow", "MP3"))
        self.convertMP3Radio.setAccessibleDescription(_translate("MainWindow", "Convert document to MP3 file of spoken text."))
        self.convertMP3Radio.setText(_translate("MainWindow", "MP3"))
        self.convertMP3ByPageRadio.setAccessibleName(_translate("MainWindow", "MP3 By Page"))
        self.convertMP3ByPageRadio.setAccessibleDescription(_translate("MainWindow", "Convert document into MP3 files of spoken text divided by page."))
        self.convertMP3ByPageRadio.setText(_translate("MainWindow", "MP3 By Page"))
        self.convertHTMLRadio.setAccessibleName(_translate("MainWindow", "HTML"))
        self.convertHTMLRadio.setAccessibleDescription(_translate("MainWindow", "Convert document to single HTML file."))
        self.convertHTMLRadio.setText(_translate("MainWindow", "HTML"))
        self.openDocumentButton.setText(_translate("MainWindow", "Open"))
        self.label_3.setText(_translate("MainWindow", "General Settings"))
        self.label_4.setText(_translate("MainWindow", "Rate:"))
        self.rateSlider.setAccessibleName(_translate("MainWindow", "Rate"))
        self.rateSlider.setAccessibleDescription(_translate("MainWindow", "A value from 0 to 100 that sets the rate of the voice."))
        self.label_5.setText(_translate("MainWindow", "Volume:"))
        self.volumeSlider.setAccessibleName(_translate("MainWindow", "Volume"))
        self.volumeSlider.setAccessibleDescription(_translate("MainWindow", "A value from 0 to 100 that sets the volume of the voice."))
        self.label_6.setText(_translate("MainWindow", "Pause Length:"))
        self.pauseLengthSlider.setAccessibleName(_translate("MainWindow", "Pause Length"))
        self.pauseLengthSlider.setAccessibleDescription(_translate("MainWindow", "A value from 0 to 10 that sets the pause length between elements."))
        self.label_7.setText(_translate("MainWindow", "Voice:"))
        self.voiceCombo.setAccessibleName(_translate("MainWindow", "Voice"))
        self.voiceCombo.setAccessibleDescription(_translate("MainWindow", "Sets the voice used for the TTS engine."))
        self.tagImageCheckbox.setText(_translate("MainWindow", "Tag Image"))
        self.tagMathCheckbox.setText(_translate("MainWindow", "Tag Math"))
        self.ignoreAltTextCheckbox.setText(_translate("MainWindow", "Ignore Alternate Text"))
        self.addTOCToHTMLCheckbox.setText(_translate("MainWindow", "Add Table of Contents to HTML"))
        self.convertButton.setText(_translate("MainWindow", "Convert!"))
        self.progressLabel.setText(_translate("MainWindow", "Progress Label"))
        self.cancelExportButton.setText(_translate("MainWindow", "Cancel"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.actionOpen_Document.setText(_translate("MainWindow", "&Open Document"))
        self.actionOpen_Document.setShortcut(_translate("MainWindow", "Ctrl+O"))

