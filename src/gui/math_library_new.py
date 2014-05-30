'''
@author: Spencer Graffe
'''
import copy

from PyQt4.QtGui import QDialog

from src.forms.math_library_new_ui import Ui_NewMathLibraryDialog
from src.gui.general_tree import GeneralTree
from src.math_library import getLibraries
from src.math_library.library import MathLibrary

class NewMathLibraryDialog(QDialog):
    '''
    Provides a wizard for the user to create a new math library with.
    '''

    def __init__(self, parent=None):
        super(NewMathLibraryDialog, self).__init__(parent)

        self.ui = Ui_NewMathLibraryDialog()
        self.ui.setupUi(self)
        self.connect_signals()

        # Set the tree that displays the possible patterns
        self._treeModel = GeneralTree(getLibraries())
        self._treeModel.addDisplayRule(1, lambda x: x.name)
        self.ui.copyFromTree.setModel(self._treeModel)

        self.library = None

    def connect_signals(self):
        self.ui.createButton.clicked.connect(self.finish)

    def finish(self):

        self.library = MathLibrary()

        # Copy the patterns over from what I wanted to copy
        if self.ui.copyFromRadio.isChecked():
            myLib = self._treeModel.getPathFromIndex(self.ui.copyFromTree.currentIndex())
            if len(myLib) == 1:
                myLib = myLib[0]
                for p in myLib.patterns:
                    self.library.patterns.append(copy.copy(p))

        self.library.name = unicode(self.ui.nameEdit.text())
        self.library.author = unicode(self.ui.authorEdit.text())

        self.done(0)