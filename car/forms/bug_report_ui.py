# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Nifty Prose Articulator\workspace\nifty-prose-articulator\car\forms/bug_report.ui'
#
# Created: Tue Jan 07 09:32:08 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_BugReporter(object):
    def setupUi(self, BugReporter):
        BugReporter.setObjectName(_fromUtf8("BugReporter"))
        BugReporter.resize(584, 602)
        font = QtGui.QFont()
        font.setPointSize(12)
        BugReporter.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/report_bug_classic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BugReporter.setWindowIcon(icon)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(BugReporter)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(BugReporter)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/classic/icons/report_bug_classic.png")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(BugReporter)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtGui.QLabel(BugReporter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(BugReporter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.bugReportTextBox = QtGui.QTextEdit(BugReporter)
        self.bugReportTextBox.setObjectName(_fromUtf8("bugReportTextBox"))
        self.verticalLayout.addWidget(self.bugReportTextBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.noThanksButton = QtGui.QPushButton(BugReporter)
        self.noThanksButton.setObjectName(_fromUtf8("noThanksButton"))
        self.horizontalLayout.addWidget(self.noThanksButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.copyReportButton = QtGui.QPushButton(BugReporter)
        self.copyReportButton.setObjectName(_fromUtf8("copyReportButton"))
        self.horizontalLayout.addWidget(self.copyReportButton)
        self.letUsKnowButton = QtGui.QPushButton(BugReporter)
        self.letUsKnowButton.setObjectName(_fromUtf8("letUsKnowButton"))
        self.horizontalLayout.addWidget(self.letUsKnowButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(BugReporter)
        QtCore.QMetaObject.connectSlotsByName(BugReporter)

    def retranslateUi(self, BugReporter):
        BugReporter.setWindowTitle(_translate("BugReporter", "Report a Bug", None))
        self.label.setText(_translate("BugReporter", "Whoops.", None))
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
"</html>", None))
        self.label_6.setText(_translate("BugReporter", "Bug Report:", None))
        self.noThanksButton.setText(_translate("BugReporter", "No Thanks", None))
        self.copyReportButton.setText(_translate("BugReporter", "Copy Report Text", None))
        self.letUsKnowButton.setText(_translate("BugReporter", "Let Central Access Know!", None))

import resource_rc
