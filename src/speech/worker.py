'''
Created on Apr 8, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread
from PyQt4 import QtCore
from src.speech.driver import SAPIDriver
import pythoncom

class SpeechWorker(QThread):
    
    onWord = QtCore.pyqtSignal(str, int, str, int)
    onFinish = QtCore.pyqtSignal()
    
    def __init__(self):
        QThread.__init__(self)
        
        self.outputList = []
        self.running = False
        
        self.volume = 1.0
        self.rate = 200
        self.voice = ''
        
        self.isChange = False
        
    def run(self):
        
        print 'Running Speech Worker thread...'
        
        def myOnWord(word, location, label, stream):
            self.onWord.emit(word, location, label, stream)
        
        def myOnFinish():
            self.running = False
            self.onFinish.emit()
        
        self.ttsEngine = SAPIDriver()
        self.ttsEngine.connect('onWord', myOnWord)
        self.ttsEngine.connect('onFinish', myOnFinish)
        
        self.ttsEngine.setVolume(self.volume)
        self.ttsEngine.setRate(self.rate)
        self.ttsEngine.setVoice(self.voice)
        
        while True:
            if self.running:
                for o in self.outputList:
                    self.ttsEngine.add(text=o[0], label=o[1])
                    
                self.outputList = []
                
                self.ttsEngine.start()
                
                # Spin here until I'm not running anymore
                while self.running:
                    pass
            
            if self.isChange:
                self.ttsEngine.setVolume(self.volume)
                self.ttsEngine.setRate(self.rate)
                self.ttsEngine.setVoice(self.voice)
                self.isChange = False
        
        print 'Closed thread!'
        
        return
    
    
    def startPlayback(self):
        print 'Starting playback...'
        self.running = True
    
    def stopPlayback(self):
        print 'Stopping playback...'
        if self.running:
            self.ttsEngine.stop()
            self.running = False
    
    def setVolume(self, v):
        self.volume = v
        self.isChange = True
    
    def setRate(self, r):
        self.rate = r
        self.isChange = True
        
    def setVoice(self, voice):
        self.voice = voice
        self.isChange = True
        
    def getVoiceList(self):
        return self.ttsEngine.getVoiceList()
    
    def addToQueue(self, text, label):
        print 'Adding to queue:', text, ',', label
        self.outputList.append([text,label])
        
    def connect_signals(self, mainWindow):
        mainWindow.startPlayback.connect(self.startPlayback)
        mainWindow.stopPlayback.connect(self.stopPlayback)
        mainWindow.addToQueue.connect(self.addToQueue)
        
        