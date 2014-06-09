'''
@author: Spencer Graffe
'''
import copy

from PyQt4.QtGui import QDialog

from car.forms.math_library_new_ui import Ui_NewMathLibraryDialog
from car.gui.general_tree import GeneralTree
from car.math_library import getLibraries
from car.math_library.library import MathLibrary
from car import languages

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
        def displayName(mathLib):
            name = mathLib.name
            if mathLib.builtIn:
                name += ' (default)'
            return name
        self._treeModel.addDisplayRule(1, displayName)
        self.ui.copyFromTree.setModel(self._treeModel)
        self.ui.copyFromTree.setVisible(False)

        # Set the language combo box
        self.ui.languageCombo.blockSignals(True)
        for item in sorted(languages.CODES.items(), key=lambda x: x[1]):
            self.ui.languageCombo.addItem(item[1], item[0])
        i = self.ui.languageCombo.findData('en')
        self.ui.languageCombo.setCurrentIndex(i)
        self.ui.languageCombo.blockSignals(False)

        self.library = None

    def connect_signals(self):
        self.ui.copyFromRadio.toggled.connect(self.setCopyFromTreeVisibility)
        self.ui.createButton.clicked.connect(self.finish)

    def setCopyFromTreeVisibility(self, isPressed):
        self.ui.copyFromTree.setVisible(isPressed)

    def finish(self):

        self.library = MathLibrary()

        # Copy the patterns over from what I wanted to copy
        if self.ui.copyFromRadio.isChecked():
            myLib = self._treeModel.getPathFromIndex(self.ui.copyFromTree.currentIndex())
            if len(myLib) == 1:
                myLib = myLib[0]
                for p in myLib.patterns:
                    self.library.patterns.append(copy.copy(p))
                self.library.languageCode = myLib.languageCode

        self.library.name = unicode(self.ui.nameEdit.text())
        self.library.author = unicode(self.ui.authorEdit.text())

        i = self.ui.languageCombo.currentIndex()
        self.library.languageCode = unicode(self.ui.languageCombo.itemData(i).toString())

        print

        self.done(0)