'''
@author: Spencer Graffe
'''

from PyQt5.QtWidgets import QDialog

from car.forms.math_save_dialog_ui import Ui_MathSaveDialog

class MathSaveDialog(QDialog):

    SAVE = 1
    EXPORT = 2
    DO_NOTHING = 3
    CANCEL = 4

    def __init__(self, message, parent=None):
        super(MathSaveDialog, self).__init__(parent)

        self.ui = Ui_MathSaveDialog()
        self.ui.setupUi(self)

        self.ui.messageLabel.setText(message)

        self.connect_signals()

    def connect_signals(self):
        self.ui.saveButton.clicked.connect(self.saveButton_clicked)
        self.ui.exportButton.clicked.connect(self.exportButton_clicked)
        self.ui.doNothingButton.clicked.connect(self.doNothingButton_clicked)
        self.ui.cancelButton.clicked.connect(self.cancelButton_clicked)

    def saveButton_clicked(self):
        self.done(self.SAVE)

    def exportButton_clicked(self):
        self.done(self.EXPORT)

    def doNothingButton_clicked(self):
        self.done(self.DO_NOTHING)

    def cancelButton_clicked(self):
        self.done(self.CANCEL)