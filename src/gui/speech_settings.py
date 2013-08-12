'''
Created on Apr 25, 2013

@author: Spencer Graffe
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from lxml import etree
import copy
from misc import app_data_path, pattern_databases

from forms.speech_settings_ui import Ui_SpeechSettings

class SpeechSettings(QtGui.QDialog):
    '''
    classdocs
    '''
    
    def __init__(self, mainWindow, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_SpeechSettings()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.mainWindow = mainWindow
        
        self.beforeConfiguration = copy.deepcopy(self.mainWindow.configuration)
        self.configuration = copy.deepcopy(self.mainWindow.configuration)
        
        # Update the GUI to match the settings currently employed
        self.updateSettings()
            
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        self.ui.applyButton.clicked.connect(self.applyButton_clicked)
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        
        self.ui.testButton.clicked.connect(self.testButton_clicked)
        
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        self.ui.pauseSlider.valueChanged.connect(self.pauseSlider_valueChanged)
        self.ui.voiceComboBox.currentIndexChanged.connect(self.voiceComboBox_currentIndexChanged)
        
        self.ui.imageTagCheckBox.stateChanged.connect(self.imageTagCheckBox_stateChanged)
        self.ui.mathTagCheckBox.stateChanged.connect(self.mathTagCheckBox_stateChanged)
        self.ui.mathDatabaseComboBox.currentIndexChanged.connect(self.mathDatabaseComboBox_currentIndexChanged)
        
    def updateSettings(self):
        # Update main window sliders to match
        self.ui.rateSlider.setValue(self.configuration.rate)
        self.ui.volumeSlider.setValue(int(self.configuration.volume))
        self.ui.pauseSlider.setValue(self.configuration.pause_length)
            
        # Update checkboxes
        self.ui.imageTagCheckBox.setChecked(self.configuration.tag_image)
        self.ui.mathTagCheckBox.setChecked(self.configuration.tag_math)
        
        # Get a list of voices to add to the voice combo box
        voiceList = self.mainWindow.speechThread.getVoiceList()
        self.ui.voiceComboBox.blockSignals(True)
        for v in voiceList:
            self.ui.voiceComboBox.addItem(v[0], userData=v[1])
        
        if len(self.configuration.voice) > 0:
            
            i = self.ui.voiceComboBox.findData(unicode(self.configuration.voice))
            if i < 0:
                i = 0
            self.ui.voiceComboBox.setCurrentIndex(i)
            self.ui.voiceComboBox.blockSignals(False)
        else:
            self.ui.voiceComboBox.setCurrentIndex(0)
            self.ui.voiceComboBox.blockSignals(False)
        
        # Get a list of patterns to add to the math database combo box
        databases = pattern_databases()
        keys = sorted(databases.keys())
        self.ui.mathDatabaseComboBox.blockSignals(True)
        for k in keys:
            self.ui.mathDatabaseComboBox.addItem(k, userData=k)
            
        if len(self.configuration.math_database) > 0:
            i = self.ui.mathDatabaseComboBox.findData(self.configuration.math_database)
            if i < 0:
                i = self.ui.mathDatabaseComboBox.findData('General')
            self.ui.mathDatabaseComboBox.setCurrentIndex(i)
            self.ui.mathDatabaseComboBox.blockSignals(False)
        else:
            i = self.ui.mathDatabaseComboBox.findData('General')
            self.ui.mathDatabaseComboBox.setCurrentIndex(i)
            self.ui.mathDatabaseComboBox.blockSignals(False)
            
    def applyButton_clicked(self):
        self.beforeConfiguration = copy.deepcopy(self.configuration)
        self.configuration.saveToFile(app_data_path('configuration.xml'))
        self.done(0)
        
    def restoreButton_clicked(self):
        self.configuration.restoreDefaults()
        self.updateSettings()
        
    def rateSlider_valueChanged(self, value):
        self.configuration.rate = value
        self.mainWindow.changeRate.emit(self.configuration.rate)

    def volumeSlider_valueChanged(self, value):
        self.configuration.volume = value
        self.mainWindow.changeVolume.emit(self.configuration.volume)
        
    def pauseSlider_valueChanged(self, value):
        self.configuration.pause_length = value
        self.mainWindow.changePauseLength.emit(self.configuration.pause_length)
        
    def voiceComboBox_currentIndexChanged(self, index):
        self.configuration.voice = unicode(self.ui.voiceComboBox.itemData(index).toString())
        self.mainWindow.changeVoice.emit(self.configuration.voice)
        
    def testButton_clicked(self):
        myText = self.ui.testSpeechText.toPlainText()
        self.mainWindow.setSpeechGenerator.emit([(unicode(myText), 'text')])
        self.mainWindow.startPlayback.emit()

    def requestMoreSpeech(self):
        self.mainWindow.noMoreSpeech.emit()
        
    def imageTagCheckBox_stateChanged(self, state):
        if state == Qt.Checked:
            self.configuration.tag_image = True
        else:
            self.configuration.tag_image = False
        
    def mathTagCheckBox_stateChanged(self, state):
        if state == Qt.Checked:
            self.configuration.tag_math = True
        else:
            self.configuration.tag_math = False
        
    def mathDatabaseComboBox_currentIndexChanged(self, index):
        self.configuration.math_database = str(self.ui.mathDatabaseComboBox.itemData(index).toString())
