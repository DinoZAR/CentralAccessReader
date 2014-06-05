'''
Created on Apr 25, 2013

@author: Spencer Graffe
'''
import os

from PyQt4.QtGui import QDialog, qApp, QMessageBox, QFileDialog
from PyQt4.QtCore import Qt

from src.forms.speech_settings_ui import Ui_SpeechSettings
from src.gui import configuration
from src.gui.general_tree import GeneralTree
from src.gui.math_library_dev import MathLibraryDev
from src import math_library
from src import languages

class SpeechSettings(QDialog):
    
    def __init__(self, mainWindow, parent=None):
        super(SpeechSettings, self).__init__(parent)
        
        self.ui = Ui_SpeechSettings()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.mainWindow = mainWindow

        self._mathTreeModel = None

        self._mathControlsVisible = False
        self.setMathControlsVisible()

        # Update the GUI to match the settings currently employed
        self.updateSettings()
            
    def connect_signals(self):
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)

        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        self.ui.pauseSlider.valueChanged.connect(self.pauseSlider_valueChanged)
        self.ui.voiceComboBox.currentIndexChanged.connect(self.voiceComboBox_currentIndexChanged)

        self.ui.mathLanguageCombo.currentIndexChanged.connect(self.mathLanguageCombo_currentIndexChanged)
        self.ui.mathLibraryTree.clicked.connect(self.mathLibraryTree_clicked)
        self.ui.mathAddButton.clicked.connect(self.mathAddButton_clicked)
        self.ui.mathRemoveButton.clicked.connect(self.mathRemoveButton_clicked)
        self.ui.openMLDEButton.clicked.connect(self.openMLDEButton_clicked)

        self.ui.mathLibraryDisplay.mousePressEvent = self.mathLibraryDisplay_mousePressed
        self.ui.mathLibraryDisplay.keyPressEvent = self.mathLibraryDisplay_keyPressed
        self.ui.mathLibraryDisplay.enterEvent = self.mathLibraryDisplay_enter
        self.ui.mathLibraryDisplay.leaveEvent = self.mathLibraryDisplay_leave

        self.ui.imageTagCheckBox.stateChanged.connect(self.imageTagCheckBox_stateChanged)
        self.ui.mathTagCheckBox.stateChanged.connect(self.mathTagCheckBox_stateChanged)
        self.ui.ignoreAltTextCheckBox.stateChanged.connect(self.ignoreAltTextCheckBox_stateChanged)
        self.ui.tableOfContentsCheckBox.stateChanged.connect(self.tableOfContentsCheckBox_stateChanged)
        
    def updateSettings(self):
        # Update main window sliders to match
        self.ui.rateSlider.setValue(configuration.getInt('Rate'))
        self.ui.volumeSlider.setValue(configuration.getInt('Volume'))
        self.ui.pauseSlider.setValue(configuration.getInt('PauseLength'))
            
        # Update checkboxes
        self.ui.imageTagCheckBox.setChecked(configuration.getBool('TagImage', False))
        self.ui.mathTagCheckBox.setChecked(configuration.getBool('TagMath', False))
        self.ui.ignoreAltTextCheckBox.setChecked(configuration.getBool('IgnoreAltText', False))
        self.ui.tableOfContentsCheckBox.setChecked(configuration.getBool('AddTOC', True))
        
        # Get a list of voices to add to the voice combo box
        voiceList = self.mainWindow.speechThread.getVoiceList()
        self.ui.voiceComboBox.blockSignals(True)
        self.ui.voiceComboBox.clear()
        for v in voiceList:
            self.ui.voiceComboBox.addItem(v[0], userData=v[1])
        
        if len(configuration.getValue('Voice')) > 0:
            i = self.ui.voiceComboBox.findData(unicode(configuration.getValue('Voice')))
            if i < 0:
                i = 0
            self.ui.voiceComboBox.setCurrentIndex(i)
            self.ui.voiceComboBox.blockSignals(False)
        else:
            self.ui.voiceComboBox.setCurrentIndex(0)
            self.ui.voiceComboBox.blockSignals(False)

        # Load the languages into the combobox, filtered by what's available
        availLanguages = {}
        for lib in math_library.getLibraries():
            availLanguages[lib.languageCode] = languages.CODES[lib.languageCode]

        self.ui.mathLanguageCombo.clear()
        for item in sorted(availLanguages.items(), key=lambda x: x[1]):
            self.ui.mathLanguageCombo.addItem(item[1], item[0])

        # Set the language from the math library
        mathStuff = math_library.getLibraryFromPath(configuration.getMathPatternPath('MathTTS'))
        if mathStuff is None:
            configuration.restoreDefault('MathTTS')
            mathStuff = math_library.getLibraryFromPath(configuration.getMathPatternPath('MathTTS'))

        i = self.ui.mathLanguageCombo.findData(mathStuff[0].languageCode)
        self.ui.mathLanguageCombo.setCurrentIndex(i)
        
        # Get the math libraries
        libraries = math_library.getLibraries()
        self._mathTreeModel = GeneralTree(libraries)

        # Filter the libraries by the current language
        self._mathTreeModel.addChildrenRule(0, lambda x: [i for i in x if i.languageCode == self.ui.mathLanguageCombo.itemData(self.ui.mathLanguageCombo.currentIndex()).toString()])
        self._mathTreeModel.addDisplayRule(1, lambda x: x.name)
        self._mathTreeModel.addChildrenRule(1, self.filterPatterns)
        self._mathTreeModel.addSelectableRule(1, lambda x: False)
        self._mathTreeModel.addDisplayRule(2, lambda x: x.name)
        self.ui.mathLibraryTree.setModel(self._mathTreeModel)
        self.ui.mathLibraryTree.expandAll()

        # Select the right one from settings
        mathPath = configuration.getMathPatternPath('MathTTS')
        index = self._mathTreeModel.getIndexFromPath(mathPath)
        self.ui.mathLibraryTree.setCurrentIndex(index)

        # Cache the math TTS if I haven't already
        self.ui.mathLibraryDisplay.setText('Loading math library...')

        qApp.processEvents()
        configuration.getMathTTS('MathTTS')

        # Set the display text for my library
        self.ui.mathLibraryDisplay.setText('{0} ({1}): {2}'.format(mathStuff[0].name,
                                                                   languages.CODES[mathStuff[0].languageCode],
                                                                   mathStuff[1].name))

    def setMathControlsVisible(self):
        self.ui.mathLanguageCombo.setVisible(self._mathControlsVisible)
        self.ui.mathAddButton.setVisible(self._mathControlsVisible)
        self.ui.mathRemoveButton.setVisible(self._mathControlsVisible)
        self.ui.openMLDEButton.setVisible(self._mathControlsVisible)
        self.ui.mathLibraryTree.setVisible(self._mathControlsVisible)
        self.ui.languageLabel.setVisible(self._mathControlsVisible)
        self.ui.libraryLabel.setVisible(self._mathControlsVisible)
        self.ui.scrollAreaWidgetContents.updateGeometry()

    def filterPatterns(self, mathLibrary):
        '''
        Gets a filtered list of patterns from the math library.
        '''
        for p in mathLibrary.patterns:
            if p.name[0] != '_':
                yield p
        
    def closeEvent(self, ev):
        pass
        
    def restoreButton_clicked(self):

        # Restore settings relevant to this dialog
        configuration.restoreDefault('Rate')
        configuration.restoreDefault('Volume')
        configuration.restoreDefault('PauseLength')
        configuration.restoreDefault('Voice')
        configuration.restoreDefault('MathTTS')
        configuration.restoreDefault('TagImage')
        configuration.restoreDefault('TagMath')
        configuration.restoreDefault('IgnoreAltText')

        self.updateSettings()
        
    def rateSlider_valueChanged(self, value):
        configuration.setInt('Rate', value)
        self.mainWindow.changeRate.emit(configuration.getInt('Rate'))

    def volumeSlider_valueChanged(self, value):
        configuration.setInt('Volume', value)
        self.mainWindow.changeVolume.emit(configuration.getInt('Volume'))
        
    def pauseSlider_valueChanged(self, value):
        configuration.setInt('PauseLength', value)
        self.mainWindow.changePauseLength.emit(configuration.getInt('PauseLength'))
        
    def voiceComboBox_currentIndexChanged(self, index):
        configuration.setValue('Voice', unicode(self.ui.voiceComboBox.itemData(index).toString()))
        self.mainWindow.changeVoice.emit(configuration.getValue('Voice'))

    def mathLanguageCombo_currentIndexChanged(self, index):
        if self._mathTreeModel is not None:
            self._mathTreeModel.update()
            self.ui.mathLibraryTree.expandAll()

    def mathLibraryTree_clicked(self, index):
        myPath = self._mathTreeModel.getPathFromIndex(index)
        if len(myPath) == 2:

            namePath = [i.name for i in myPath]
            configuration.setMathPatternPath('MathTTS', namePath)

            # Cache the TTS engine
            self.ui.mathLibraryDisplay.setText('Loading math library...')
            qApp.processEvents()

            try:
                configuration.getMathTTS('MathTTS')
            except AttributeError as ex:
                configuration.restoreDefault('MathTTS')
                configuration.getMathTTS('MathTTS')

            self.updateSettings()

    def mathAddButton_clicked(self):
        newLib = unicode(QFileDialog.getOpenFileName(self, 'Add Math Library', os.path.expanduser('~/Desktop'), 'Math Library (*.mathlib)'))
        if len(newLib) > 0:
            try:
                badLib = math_library.saveCustomLibrary(newLib)
                if badLib is not None:
                    result = QMessageBox.information(self, 'Replace Math Library?', '{0} already exists. Want to replace it?'.format(badLib.name), QMessageBox.Yes | QMessageBox.No)
                    if result == QMessageBox.Yes:
                        math_library.saveCustomLibrary(newLib, replace=True)
            except ValueError as ex:
                QMessageBox.information(self, 'Can\'t Add Library', ex.message, QMessageBox.Ok)
            self.updateSettings()

    def mathRemoveButton_clicked(self):
        myPath = self._mathTreeModel.getPathFromIndex(self.ui.mathLibraryTree.currentIndex())
        if len(myPath) == 2:
            myLib = myPath[0]
            result = QMessageBox.information(self, 'Remove Math Library?', 'Do you want to remove {0}?'.format(myLib.name), QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                try:
                    math_library.removeLibrary(myLib.name)
                    configuration.restoreDefault('MathTTS')
                except ValueError as ex:
                    QMessageBox.information(self, 'Can\'t Remove Library', ex.message, QMessageBox.Ok)
                self.updateSettings()

    def mathLibraryDisplay_mousePressed(self, ev):
        self._mathControlsVisible = not self._mathControlsVisible
        self.setMathControlsVisible()

    def mathLibraryDisplay_keyPressed(self, ev):
        if ev.key() == Qt.Key_Space or ev.key() == Qt.Key_Enter:
            self._mathControlsVisible = not self._mathControlsVisible
            self.setMathControlsVisible()

    def mathLibraryDisplay_enter(self, ev):
        self._previousDisplayValue = self.ui.mathLibraryDisplay.text()
        if not self._mathControlsVisible:
            self.ui.mathLibraryDisplay.setText('+ ' + self._previousDisplayValue)
        else:
            self.ui.mathLibraryDisplay.setText('- ' + self._previousDisplayValue)

    def mathLibraryDisplay_leave(self, ev):
        self.ui.mathLibraryDisplay.setText(self._previousDisplayValue)

    def openMLDEButton_clicked(self):
        MathLibraryDev.getInstance().show()

    def requestMoreSpeech(self):
        self.mainWindow.noMoreSpeech.emit()
        
    def imageTagCheckBox_stateChanged(self, state):
        if state == Qt.Checked:
            configuration.setBool('TagImage', True)
        else:
            configuration.setBool('TagImage', False)
        
    def mathTagCheckBox_stateChanged(self, state):
        if state == Qt.Checked:
            configuration.setBool('TagMath', True)
        else:
            configuration.setBool('TagMath', False)
            
    def ignoreAltTextCheckBox_stateChanged(self, state):
        if state == Qt.Checked:
            configuration.setBool('IgnoreAltText', True)
        else:
            configuration.setBool('IgnoreAltText', False)

    def tableOfContentsCheckBox_stateChanged(self, state):
        if state == Qt.Checked:
            configuration.setBool('AddTOC', True, defaultValue=True)
        else:
            configuration.setBool('AddTOC', False, defaultValue=True)