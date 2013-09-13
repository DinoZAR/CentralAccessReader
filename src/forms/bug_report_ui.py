# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/forms/bug_report.ui'
#
# Created: Fri Sep 13 14:31:10 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BugReporter(object):
    def setupUi(self, BugReporter):
        BugReporter.setObjectName("BugReporter")
        BugReporter.resize(584, 602)
        font = QtGui.QFont()
        font.setPointSize(12)
        BugReporter.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/report_bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BugReporter.setWindowIcon(icon)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(BugReporter)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(BugReporter)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/report_bug.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(BugReporter)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(BugReporter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(BugReporter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.bugReportTextBox = QtGui.QTextEdit(BugReporter)
        self.bugReportTextBox.setObjectName("bugReportTextBox")
        self.verticalLayout.addWidget(self.bugReportTextBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.noThanksButton = QtGui.QPushButton(BugReporter)
        self.noThanksButton.setObjectName("noThanksButton")
        self.horizontalLayout.addWidget(self.noThanksButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.copyReportButton = QtGui.QPushButton(BugReporter)
        self.copyReportButton.setObjectName("copyReportButton")
        self.horizontalLayout.addWidget(self.copyReportButton)
        self.letUsKnowButton = QtGui.QPushButton(BugReporter)
        self.letUsKnowButton.setObjectName("letUsKnowButton")
        self.horizontalLayout.addWidget(self.letUsKnowButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(BugReporter)
        QtCore.QMetaObject.connectSlotsByName(BugReporter)

    def retranslateUi(self, BugReporter):
        BugReporter.setWindowTitle(QtGui.QApplication.translate("BugReporter", "Report a Bug", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BugReporter", "Whoops.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("BugReporter", "<html>\n"
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
"</html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("BugReporter", "Bug Report:", None, QtGui.QApplication.UnicodeUTF8))
        self.noThanksButton.setText(QtGui.QApplication.translate("BugReporter", "No Thanks", None, QtGui.QApplication.UnicodeUTF8))
        self.copyReportButton.setText(QtGui.QApplication.translate("BugReporter", "Copy Report Text", None, QtGui.QApplication.UnicodeUTF8))
        self.letUsKnowButton.setText(QtGui.QApplication.translate("BugReporter", "Let Central Access Know!", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
