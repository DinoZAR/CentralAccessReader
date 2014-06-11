# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GraffeS.PC93667W7\git\central-access-reader\car/forms/bug_report.ui'
#
# Created: Wed Jun 11 15:37:24 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BugReporter(object):
    def setupUi(self, BugReporter):
        BugReporter.setObjectName("BugReporter")
        BugReporter.resize(584, 602)
        font = QtGui.QFont()
        font.setPointSize(12)
        BugReporter.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/classic/icons/report_bug_classic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BugReporter.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(BugReporter)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(BugReporter)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/classic/icons/report_bug_classic.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(BugReporter)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(BugReporter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(BugReporter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.bugReportTextBox = QtWidgets.QTextEdit(BugReporter)
        self.bugReportTextBox.setObjectName("bugReportTextBox")
        self.verticalLayout.addWidget(self.bugReportTextBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.noThanksButton = QtWidgets.QPushButton(BugReporter)
        self.noThanksButton.setObjectName("noThanksButton")
        self.horizontalLayout.addWidget(self.noThanksButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.copyReportButton = QtWidgets.QPushButton(BugReporter)
        self.copyReportButton.setObjectName("copyReportButton")
        self.horizontalLayout.addWidget(self.copyReportButton)
        self.letUsKnowButton = QtWidgets.QPushButton(BugReporter)
        self.letUsKnowButton.setObjectName("letUsKnowButton")
        self.horizontalLayout.addWidget(self.letUsKnowButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(BugReporter)
        QtCore.QMetaObject.connectSlotsByName(BugReporter)

    def retranslateUi(self, BugReporter):
        _translate = QtCore.QCoreApplication.translate
        BugReporter.setWindowTitle(_translate("BugReporter", "Report a Bug"))
        self.label.setText(_translate("BugReporter", "Whoops."))
        self.label_3.setText(_translate("BugReporter", "<html>\n"
"<head/>\n"
"<body>\n"
"<p>The Central Access Reader had a problem. Please let us know exactly what went wrong by sending us the bug report provided below.  The bug report is completely anonymous.</p>\n"
"\n"
"<p>The report will include:\n"
"<ul>\n"
"<li>Your operating system (Windows, Mac, Linux, etc.)</li>\n"
"<li>The code in the Central Access Reader that caused the problem</li>\n"
"<li>Speech, highlighting, and color settings</li>\n"
"</ul>\n"
"</p>\n"
"\n"
"<p>The report will NOT include:\n"
"<ul>\n"
"<li>The text in the Word Doc</li>\n"
"<li>The IP address of your computer</li>\n"
"<li>Location of the Word Doc</li></ul></p>\n"
"</body>\n"
"</html>"))
        self.label_6.setText(_translate("BugReporter", "Bug Report:"))
        self.noThanksButton.setText(_translate("BugReporter", "No Thanks"))
        self.copyReportButton.setText(_translate("BugReporter", "Copy Report Text"))
        self.letUsKnowButton.setText(_translate("BugReporter", "Let Central Access Know!"))

import resource_rc
