'''
Created on Apr 8, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread, QMutex
from PyQt4 import QtCore, QtGui
from src.speech import driver
import pythoncom
import os
import subprocess

class SpeechWorker(QThread):
    
    onWord = QtCore.pyqtSignal(int, int, str, int)
    onFinish = QtCore.pyqtSignal()
    onProgress = QtCore.pyqtSignal(int)
    onProgressLabel = QtCore.pyqtSignal(str)
    
    queueLock = QMutex()
    
    def __init__(self):
        QThread.__init__(self)
        
        self.outputList = []
        self.running = False
        
        self.volume = 100
        self.rate = 50
        self.voice = ''
        
        self.isChange = False
        
    def run(self):
        
        def myOnWord(offset, length, label, stream):
            self.onWord.emit(offset, length, label, stream)
        
        def myOnFinish():
            self.running = False
            self.onFinish.emit()
        
        self.ttsEngine = driver.get_driver()
        self.ttsEngine.connect('onWord', myOnWord)
        self.ttsEngine.connect('onFinish', myOnFinish)
        
        self.ttsEngine.setVolume(self.volume)
        self.ttsEngine.setRate(self.rate)
        self.ttsEngine.setVoice(self.voice)
        
        while True:
            if self.running:
                self.queueLock.lock()
                for o in self.outputList:
                    self.ttsEngine.add(text=o[0], label=o[1])
                self.queueLock.unlock()
                    
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
        
        return
    
    
    def startPlayback(self):
        self.running = True
    
    def stopPlayback(self):
        if self.running:
            self.ttsEngine.stop()
            self.running = False
            
    def saveToMP3(self, mp3Path, outputList):
        # Create the WAV file first
        def myOnProgress(percent):
            self.onProgress.emit(int((float(percent) / 100.0) * 70.0))
        
        wavSavePath = os.path.abspath('tmp.wav')
        
        self.onProgressLabel.emit('Speaking into WAV...')
        self.ttsEngine.speakToWavFile(wavSavePath, outputList, myOnProgress)
        
        # Then convert it to MP3
        self.onProgressLabel.emit('Converting to MP3...')
        lameCommand = os.path.abspath('../lame.exe') + ' -h "' + wavSavePath + '" "' + mp3Path + '"'
        ps = subprocess.Popen(lameCommand)
        
        while ps.poll() == None:
            QtGui.qApp.processEvents()
        
        self.onProgress.emit(100)
    
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
        self.queueLock.lock()
        self.outputList.append([unicode(text),unicode(label)])
        self.queueLock.unlock()
        
    def connect_signals(self, mainWindow):
        mainWindow.startPlayback.connect(self.startPlayback)
        mainWindow.stopPlayback.connect(self.stopPlayback)
        mainWindow.addToQueue.connect(self.addToQueue)
        
        