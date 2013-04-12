'''
Created on Jan 21, 2013

@author: Spencer
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QUrl
from src.forms.settings_ui import Ui_Settings
from lxml import etree
import copy

class Settings(QtGui.QDialog):

    def __init__(self, mainWindow, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_Settings()
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
        self.ui.testButton.clicked.connect(self.testButton_clicked)
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        self.ui.comboBox.currentIndexChanged.connect(self.comboBox_currentIndexChanged)
        
        self.ui.highlighterTextButton.clicked.connect(self.highlighterTextButton_clicked)
        self.ui.highlighterBackgroundButton.clicked.connect(self.highlighterBackgroundButton_clicked)
        
    def updateSettings(self):
        # Update speech thread with my stuff
        self.mainWindow.changeVolume.emit(self.configuration.volume)
        self.mainWindow.changeRate.emit(self.configuration.rate)
        self.mainWindow.changeVoice.emit(self.configuration.voice)
        
        # Update main window sliders to match
        self.ui.rateSlider.setValue(self.configuration.rate)
        self.ui.volumeSlider.setValue(int(self.configuration.volume * 100))
        
        self.ui.rateLabel.setText(str(self.configuration.rate))
        self.ui.volumeLabel.setText(str(int(self.configuration.volume * 100)))
        
        # Update the color boxes
        self.setButtonColor(self.ui.highlighterTextButton, self.configuration.color_highlightText)
        self.setButtonColor(self.ui.highlighterBackgroundButton, self.configuration.color_highlightBackground)
        

    def applyButton_clicked(self):
        self.beforeConfiguration = copy.deepcopy(self.configuration)
        self.configuration.saveToFile('configuration.xml')
        
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
        
    def highlighterTextButton_clicked(self):
        self.configuration.color_highlightText = QtGui.QColorDialog.getColor()
        self.updateSettings()
        
    def highlighterBackgroundButton_clicked(self):
        self.configuration.color_highlightBackground = QtGui.QColorDialog.getColor()
        self.updateSettings()
        
    def setButtonColor(self, button, color):
        '''
        Takes a QColor and sets the color on the button, making sure that the text is readable and still having the
        same size.
        '''
        rgbString = 'rgb(' + str(color.red()) + ', ' + str(color.green()) + ', ' + str(color.blue()) + ')'
        
        # Calculate the font color for the button text that would be most readable
        threshold = 105
        delta = (color.red() * 0.299) + (color.green() * 0.587) + (color.blue() * 0.114)
        fontColor = ''
        if (255 - delta) < threshold:
            # Make it black
            fontColor = 'rgb(0,0,0)'
        else:
            # Make it white
            fontColor = 'rgb(255,255,255)'

        button.setStyleSheet('background-color: ' + rgbString + '; font-size: 16pt; color: ' + fontColor + ';')