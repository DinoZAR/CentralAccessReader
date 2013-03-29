'''
Created on Jan 21, 2013

@author: Spencer
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QUrl
from src.forms.settings_ui import Ui_Settings
from src import pyttsx

class Settings(QtGui.QDialog):

    def __init__(self, ttsEngine, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_Settings()
        
        self.ui.setupUi(self)
        
        self.connect_signals()
        
        self.ttsEngine = ttsEngine
        self.ttsEngine.connect('started-word', self.onWord)
        
        #gets the current engine properties
        f = open('ttsSettings.txt', 'r')
        self.cVol = float(f.readline())
        self.cRate = float(f.readline())
        self.cVoice = f.readline()
        f.close()
        #Changes the setting to match the current engine properties
        self.ui.sVolumeSlider.setValue(self.cVol*100)
        self.ui.rateLabel.setText(str(int(self.cRate)))
        self.ui.volumeLabel.setText(str(int(self.cVol* 100)))
        self.ui.rateSlider.setValue(self.cRate)
        self.voices = self.ttsEngine.getProperty('voices')
        self.count = 0
        self.voiceNum = 0
        self.cVoiceID =str(self.voices[self.ui.comboBox.currentIndex()].id)
        for x in self.voices:
            self.ui.comboBox.addItem(x.name)
            if str(self.voices[self.ui.comboBox.currentIndex()].id) == self.cVoiceID:
                self.ui.comboBox.setCurrentIndex(self.count)
                self.voiceNum = self.count
            self.count = self.count = 1
        
    def onWord(self, name, location, length):
        print 'word', name, location, length
        if self.stop:
            print 'Stopping...'
            self.ttsEngine.stop()
            self.ttsEngine = pyttsx.init()
            self.stop = False
            
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        pass
        self.ui.applyButton.clicked.connect(self.applyButton_clicked)
        self.ui.testButton.clicked.connect(self.testButton_clicked)
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        self.ui.sVolumeSlider.valueChanged.connect(self.sVolumeSlider_valueChanged)
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        

    def applyButton_clicked(self):
        self.ttsEngine.setProperty('rate', self.ui.rateSlider.value())
        self.vol = self.ui.sVolumeSlider.value()/100.0
        self.ttsEngine.setProperty('volume', self.vol)
        self.ttsEngine.setProperty('voice', self.voices[self.ui.comboBox.currentIndex()].id)
        d = open ('ttsSettings.txt', 'w')
        d.write(str(self.vol))
        d.write('\n')
        d.write(str(self.ui.rateSlider.value()))
        d.write('\n')
        self.sVoice = str(self.voices[self.ui.comboBox.currentIndex()].id)
        d.write(str(self.sVoice))
        d.close()
    def restoreButton_clicked(self):
        self.ttsEngine.setProperty('rate', self.cRate)
        self.ttsEngine.setProperty('voice', self.cVoice)
        self.ttsEngine.setProperty('volume', self.cVol)

        self.ui.rateLabel.setText(str(self.cRate))
        self.ui.volumeLabel.setText(str(self.cVol * 100))

        self.ui.rateSlider.setValue(self.cRate)
        self.ui.sVolumeSlider.setValue(self.cVol * 100)
        self.ui.comboBox.setCurrentIndex(self.voiceNum)
        
    def rateSlider_valueChanged(self, value):
        self.ui.rateLabel.setText(str(value))

    def sVolumeSlider_valueChanged(self, value):
        self.ui.volumeLabel.setText(str(value))
        
    def testButton_clicked(self):
        f = open('ttsSettings.txt', 'r')
        self.tVol = float(f.readline())
        self.tRate = float(f.readline())
        self.tVoice = self.ttsEngine.getProperty('voice')
        f.close()
        self.ttsEngine.setProperty('voice', self.voices[self.ui.comboBox.currentIndex()].id)
        self.vol = self.ui.sVolumeSlider.value()/100.0
        self.ttsEngine.setProperty('volume', self.vol)
        self.ttsEngine.setProperty('rate', self.ui.rateSlider.value())
        self.text = self.ui.plainTextEdit.toPlainText()
        self.ttsEngine.say(self.text)
        self.ttsEngine.runAndWait()
        self.ttsEngine.setProperty('voice', self.tVoice.id)
        self.ttsEngine.setProperty('volume', self.tVol)
        self.ttsEngine.setProperty('rate', self.tRate)
