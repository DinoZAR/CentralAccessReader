'''
Created on May 20, 2014

@author: Spencer Graffe
'''
import os

from PyQt4.QtCore import QObject
from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QMessageBox, qApp, QAction

from src.forms.math_library_dev_ui import Ui_MathLibraryDev
from src.gui.math_library_editor import MathLibraryEditor
from src.gui.math_library_new import NewMathLibraryDialog
from src.gui.math_save_dialog import MathSaveDialog
from src.gui import configuration
from src import math_library
from src.math_library.library import MathLibrary
try:
    from src.math_to_prose_fast.tts import MathTTS
except ImportError as ex:
    print 'Loading slower MathTTS...', ex
    from src.math_to_prose.tts import MathTTS
from src.speech import driver

class MathLibraryDev(QMainWindow):
    '''
    Provides a development environment for the math libraries, allowing users to
    create and modify their own.
    '''

    _myInstance = None

    @staticmethod
    def getInstance():
        '''
        Get a MathLibraryDev instance. It will create a new one if it was made
        invisible. This makes sure that there is only one of them.
        '''
        if MathLibraryDev._myInstance is None:
            MathLibraryDev._myInstance = MathLibraryDev()
        elif not MathLibraryDev._myInstance.isVisible():
            MathLibraryDev._myInstance = MathLibraryDev()
        else:
            MathLibraryDev._myInstance.raise_()
            MathLibraryDev._myInstance.activateWindow()

        return MathLibraryDev._myInstance

    def __init__(self, parent=None):
        super(MathLibraryDev, self).__init__(parent)
        
        self.ui = Ui_MathLibraryDev()
        self.ui.setupUi(self)
        
        # Adjust some splitter handles
        self.ui.splitter.setSizes([1000, 500])

        self._mathTTS = MathTTS()

        # Set up the TTS driver (use settings from configuration of before)
        self._ttsEngine = driver.get_driver()
        self._ttsEngine.setVolume(configuration.getInt('Volume'))
        self._ttsEngine.setRate(configuration.getInt('Rate'))
        self._ttsEngine.setVoice(configuration.getValue('Voice'))

        # Clear the tabs
        self.ui.libraryTabs.clear()

        # Update my list of installed libraries into the menu
        self.updateInstalledLibraryList()
        
        self.connect_signals()
    
    def connect_signals(self):
        # File menu
        self.ui.actionNew_Library.triggered.connect(self.newLibrary)
        self.ui.actionOpen_Library.triggered.connect(self.openLibrary)
        
        self.ui.actionNew_Pattern.triggered.connect(self.newPattern)
        self.ui.actionOpen_Pattern.triggered.connect(self.openPattern)

        self.ui.actionSave.triggered.connect(self.saveCurrent)
        self.ui.actionExport.triggered.connect(self.exportCurrent)
        
        # MathML menu
        self.ui.actionFrom_Clipboard.triggered.connect(self.importMathFromClipboard)
        
        # Controls
        self.ui.libraryTabs.tabCloseRequested.connect(self.closeLibrary)
        self.ui.runButton.clicked.connect(self.runCurrentLibrary)
        
    def currentLibraryEditor(self):
        return self.ui.libraryTabs.currentWidget()
    
    def importMathFromClipboard(self):
        '''
        Pastes the MathML from the clipboard into the MathML editor, if any.
        '''
        mime = QApplication.clipboard().mimeData()
        
        # Get the text from the clipboard
        if mime.hasHtml():
            self.ui.mathmlEditor.setMath(unicode(mime.html()))
            
        elif mime.hasText():
            self.ui.mathmlEditor.setMath(unicode(QApplication.clipboard().text()))
    
    def newLibrary(self):
        '''
        Appends a new math library to the editor.
        '''
        dialog = NewMathLibraryDialog()
        dialog.exec_()

        if dialog.library is not None:
            w = MathLibraryEditor(dialog.library)
            w.nameChanged.connect(self._updateLibraryName)
            self.ui.libraryTabs.addTab(w, w.name)
            self.ui.libraryTabs.setCurrentWidget(w)

    def openLibrary(self):
        '''
        Opens a library from file.
        '''
        filePath = unicode(QFileDialog.getOpenFileName(self, 'Open Math Library',
                                                       os.path.expanduser('~/Desktop'),
                                                       'Math Library (*.mathlib)'))
        if len(filePath) > 0:
            lib = MathLibrary(filePath)
            w = MathLibraryEditor(library=lib)
            w.nameChanged.connect(self._updateLibraryName)
            self.ui.libraryTabs.addTab(w, w.name)
            self.ui.libraryTabs.setCurrentWidget(w)

    def newPattern(self):
        '''
        Appends a new pattern to the current library.
        '''
        editor = self.currentLibraryEditor()
        if editor is not None:
            editor.newPattern()

    def openPattern(self):
        '''
        Appends a new pattern to the library from file.
        '''
        editor = self.currentLibraryEditor()
        if editor is not None:
            editor.openPattern()

    def closeLibrary(self, tabIndex):
        '''
        Closes the library at the tab location.
        '''

        lib = self.ui.libraryTabs.widget(tabIndex).library

        dialog = MathSaveDialog('Want to save or export {0} before closing?'.format(lib.name), self)
        result = dialog.exec_()
        # result = QMessageBox.question(self, 'Save or Export?', 'Want to save or export {0} before closing?'.format(lib.name), 'Save', 'Export', 'Do Nothing', QMessageBox.Save | QMessageBox.Cancel)

        # Save
        if result == MathSaveDialog.SAVE:
            result = self.saveLibrary(lib, askFirstConfirmation=False)
            if result == QMessageBox.Yes:
                self.ui.libraryTabs.removeTab(tabIndex)

        # Export
        elif result == MathSaveDialog.EXPORT:
            editor = self.ui.libraryTabs.widget(tabIndex)
            if editor.export():
                self.ui.libraryTabs.removeTab(tabIndex)

        # Do Nothing
        elif result == MathSaveDialog.DO_NOTHING:
            self.ui.libraryTabs.removeTab(tabIndex)
    
    def saveCurrent(self):
        '''
        Saves the current library.
        '''
        if self.currentLibraryEditor() is not None:
            self.saveLibrary(self.currentLibraryEditor().library)

    def saveLibrary(self, mathLib, askFirstConfirmation=True):

        if askFirstConfirmation:
            result = QMessageBox.question(self, 'Save Math Library', 'Want to save {0} into CAR?'.format(mathLib.name), QMessageBox.Yes | QMessageBox.No)
        else:
            result = QMessageBox.Yes

        if result == QMessageBox.Yes:
            try:
                badLib = math_library.saveCustomLibrary(mathLib)
                if badLib is not None:
                    result = QMessageBox.question(self, 'Replace Math Library?', '{0} already exists. Want to replace it?'.format(badLib.name), QMessageBox.Yes | QMessageBox.No)
                    if result == QMessageBox.Yes:
                        math_library.saveCustomLibrary(mathLib, replace=True)
                        QMessageBox.information(self, 'Math Library Saved', '{0} was saved successfully.'.format(mathLib.name), QMessageBox.Ok)
                else:
                    QMessageBox.information(self, 'Math Library Saved', '{0} was saved successfully.'.format(mathLib.name), QMessageBox.Ok)

            except ValueError as ex:
                QMessageBox.information(self, 'Can\'t Save Library', ex.message, QMessageBox.Ok)
                return QMessageBox.No

        self.updateInstalledLibraryList()

        return result

    def exportCurrent(self):
        '''
        Exports the current library to file
        '''
        if self.currentLibraryEditor() is not None:
            self.currentLibraryEditor().export()

    def runCurrentLibrary(self):
        '''
        Runs the current library with the MathML.
        '''
        self.ui.proseOutput.setText('Compiling...')
        qApp.processEvents()
        editor = self.currentLibraryEditor()
        if editor is not None:
            lib = editor.library
            pattern = editor.currentPattern()
            if pattern is not None:
                try:
                    self._mathTTS.setMathLibrary(lib, pattern)
                    prose = self._mathTTS.parse(self.ui.mathmlEditor.getMath())
                    self.ui.proseOutput.setText(prose)
                    self._ttsEngine.stop()
                    self._ttsEngine.setSpeechGenerator([(prose, 'math')])
                    self._ttsEngine.start()
                except Exception as ex:
                    self.ui.proseOutput.setText('')
                    QMessageBox.information(self, 'Didn\'t parse correctly', 'Math library did not parse correctly:\n{0}'.format(ex), QMessageBox.Ok)
            else:
                self.ui.proseOutput.setText('')
        else:
            self.ui.proseOutput.setText('')

    def updateInstalledLibraryList(self):
        '''
        Updates the installed library list for the menu item.
        '''
        self.ui.menuInstalled_Libraries.clear()
        for lib in math_library.getLibraries():
            myAction = QAction(self)
            if lib.builtIn:
                myAction.setText(lib.name + ' (default)')
            else:
                myAction.setText(lib.name)
            myAction.setData(lib)
            myAction.triggered.connect(self.openInstalledLibrary)
            self.ui.menuInstalled_Libraries.addAction(myAction)

    def openInstalledLibrary(self):
        myLib = self.sender().data().toPyObject()
        w = MathLibraryEditor(library=myLib)
        w.nameChanged.connect(self._updateLibraryName)
        self.ui.libraryTabs.addTab(w, w.name)
        self.ui.libraryTabs.setCurrentWidget(w)
    
    def _updateLibraryName(self, editor, name):
        i = self.ui.libraryTabs.indexOf(editor)
        self.ui.libraryTabs.setTabText(i, name)

    def closeEvent(self, ev):

        for i in range(self.ui.libraryTabs.count()):
            lib = self.ui.libraryTabs.widget(i).library
            dialog = MathSaveDialog('Want to save or export {0} before closing?'.format(lib.name))
            result = dialog.exec_()

            # Save
            if result == MathSaveDialog.SAVE:
                result = self.saveLibrary(lib, askFirstConfirmation=False)

            # Export
            elif result == MathSaveDialog.EXPORT:
                editor = self.ui.libraryTabs.widget(i)
                editor.export()