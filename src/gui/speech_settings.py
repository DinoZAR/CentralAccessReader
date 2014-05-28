'''
Created on Apr 25, 2013

@author: Spencer Graffe
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt

from src.forms.speech_settings_ui import Ui_SpeechSettings
from src.gui import configuration
from src.gui.general_tree import GeneralTree
from src import math_library
from src.misc import app_data_path

class SpeechSettings(QtGui.QDialog):
    
    def __init__(self, mainWindow, parent=None):
        QtGui.QDialog.__init__(self, parent)
        
        self.ui = Ui_SpeechSettings()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.mainWindow = mainWindow
        
        # Update the GUI to match the settings currently employed
        self.updateSettings()
            
    def connect_signals(self):
        self.ui.applyButton.clicked.connect(self.applyButton_clicked)
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        
        self.ui.testButton.clicked.connect(self.testButton_clicked)
        
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        self.ui.pauseSlider.valueChanged.connect(self.pauseSlider_valueChanged)
        self.ui.voiceComboBox.currentIndexChanged.connect(self.voiceComboBox_currentIndexChanged)
        
        self.ui.imageTagCheckBox.stateChanged.connect(self.imageTagCheckBox_stateChanged)
        self.ui.mathTagCheckBox.stateChanged.connect(self.mathTagCheckBox_stateChanged)
        
        self.ui.ignoreAltTextCheckBox.stateChanged.connect(self.ignoreAltTextCheckBox_stateChanged)
        
    def updateSettings(self):
        # Update main window sliders to match
        self.ui.rateSlider.setValue(configuration.getInt('Rate'))
        self.ui.volumeSlider.setValue(configuration.getInt('Volume'))
        self.ui.pauseSlider.setValue(configuration.getInt('PauseLength'))
            
        # Update checkboxes
        self.ui.imageTagCheckBox.setChecked(configuration.getBool('TagImage', False))
        self.ui.mathTagCheckBox.setChecked(configuration.getBool('TagMath', False))
        self.ui.ignoreAltTextCheckBox.setChecked(configuration.getBool('IgnoreAltText', False))
        
        # Get a list of voices to add to the voice combo box
        voiceList = self.mainWindow.speechThread.getVoiceList()
        self.ui.voiceComboBox.blockSignals(True)
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
        
        # Get the math libraries
        libraries = math_library.getLibraries()
        self._mathTreeModel = GeneralTree(libraries)
        self._mathTreeModel.addDisplayRule(1, lambda x: x.name)
        self._mathTreeModel.addChildrenRule(1, self.filterPatterns)
        self._mathTreeModel.addSelectableRule(1, lambda x: False)
        self._mathTreeModel.addDisplayRule(2, lambda x: x.name)
        self.ui.mathLibraryTree.setModel(self._mathTreeModel)

        # Select the right one from settings
        mathPatternPath = configuration.getValue('MathLibrary', 'CAR/')

    def filterPatterns(self, mathLibrary):
        '''
        Gets a filtered list of patterns from the math library.
        '''
        for p in mathLibrary.patterns:
            if p.name[0] != '_':
                yield p
        
    def closeEvent(self, ev):
        pass
            
    def applyButton_clicked(self):
        configuration.save(app_data_path('configuration.xml'))
        self.done(0)
        
    def restoreButton_clicked(self):
        configuration.restoreDefaults()
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
        
    def testButton_clicked(self):
        myText = self.ui.testSpeechText.toPlainText()
        self.mainWindow.setSpeechGenerator.emit([(unicode(myText), 'text')])
        self.mainWindow.startPlayback.emit()

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
            configuration.setBool('IgnoreAltText', True);
        else:
            configuration.setBool('IgnoreAltText', False)