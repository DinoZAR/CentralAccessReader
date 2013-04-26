'''
Created on Apr 25, 2013

@author: Spencer Graffe
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from lxml import etree
import copy

from src.forms.speech_settings_ui import Ui_SpeechSettings

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
        
        # Get a list of voices to add to combo box
        voiceList = self.mainWindow.speechThread.getVoiceList()
        for v in voiceList:
            self.ui.comboBox.addItem(v[0], userData=v[1])
        self.ui.comboBox.setCurrentIndex(0)
        
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
        self.ui.comboBox.currentIndexChanged.connect(self.comboBox_currentIndexChanged)
        
    def updateSettings(self):
        # Update speech thread with my stuff
        self.mainWindow.changeVolume.emit(self.configuration.volume)
        self.mainWindow.changeRate.emit(self.configuration.rate)
        self.mainWindow.changeVoice.emit(self.configuration.voice)
        
        # Update main window sliders to match
        self.ui.rateSlider.setValue(self.configuration.rate)
        self.ui.volumeSlider.setValue(int(self.configuration.volume * 100))
        
    def applyButton_clicked(self):
        self.beforeConfiguration = copy.deepcopy(self.configuration)
        self.configuration.saveToFile('configuration.xml')
        self.mainWindow.refreshDocument()
        
    def restoreButton_clicked(self):
        self.configuration = copy.deepcopy(self.beforeConfiguration)
        self.updateSettings()
        
    def rateSlider_valueChanged(self, value):
        self.configuration.rate = value
        self.updateSettings()

    def volumeSlider_valueChanged(self, value):
        self.configuration.volume = float(value) / 100.0
        self.updateSettings()
        
    def comboBox_currentIndexChanged(self, index):
        self.configuration.voice = str(self.ui.comboBox.itemData(index).toString())
        self.updateSettings()
        
    def testButton_clicked(self):
        myText = self.ui.testSpeechText.toPlainText()
        self.mainWindow.addToQueue.emit(myText, 'text')
        self.mainWindow.startPlayback.emit()