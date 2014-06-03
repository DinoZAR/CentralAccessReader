'''
Created on Apr 8, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread, QMutex, pyqtSignal

from src.speech import driver
from src.gui import configuration

class SpeechWorker(QThread):
    
    # TTS
    onStart = pyqtSignal(int, int, str, int, str)
    onWord = pyqtSignal(int, int, str, int, str, bool)
    onEndStream = pyqtSignal(int, str)
    onFinish = pyqtSignal()
    
    # MP3 Creation
    onProgress = pyqtSignal(int)
    onProgressLabel = pyqtSignal(str)
    
    # Streaming
    requestMoreSpeech = pyqtSignal()
    
    queueLock = QMutex()
    
    def __init__(self):
        QThread.__init__(self)
        
        self._outputList = []
        self._running = True
        self._done = False
        
        self._volume = 100
        self._rate = 50
        self._pauseLength = 0
        self._voice = ''
        
        self._ttsCreated = False
        
        self._stopMP3Creation = False
        
        self._isChange = False
        
    def run(self):
        
        self.setPriority(QThread.HighPriority)
        
        def myOnStart(offset, length, label, stream, word):
            #print 'worker: OnStart'
            self.onStart.emit(offset, length, label, stream, word)
        
        def myOnWord(offset, length, label, stream, word, isFirst):
            #print 'worker: OnWord'
            self.onWord.emit(offset, length, label, stream, word, isFirst)
        
        def myOnEndStream(stream, label):
            #print 'worker: OnEndStream'
            self.onEndStream.emit(stream, label)
        
        def myOnFinish():
            #print 'worker: OnFinish'
            self.onFinish.emit()
            
        def mySpeechRequestHook():
            self.requestMoreSpeech.emit()
        
        self.ttsEngine = driver.get_driver(mySpeechRequestHook)
        startHandle = self.ttsEngine.connect('onStart', myOnStart)
        wordHandle = self.ttsEngine.connect('onWord', myOnWord)
        finishHandle = self.ttsEngine.connect('onFinish', myOnFinish)
        streamHandle = self.ttsEngine.connect('onEndStream', myOnEndStream)
        
        self.ttsEngine.setVolume(self._volume)
        self.ttsEngine.setRate(self._rate)
        self.ttsEngine.setVoice(self._voice)
        
        self._ttsCreated = True
        
        while self._running:
            if self.ttsEngine.areSettingsInteractive():
                if self._isChange:
                    self.ttsEngine.setVolume(self._volume)
                    self.ttsEngine.setRate(self._rate)
                    self.ttsEngine.setPauseLength(self._pauseLength)
                    self.ttsEngine.setVoice(self._voice)
            self._isChange = False
            QThread.yieldCurrentThread()
        
        # Kill and cleanup the TTS driver
        self.ttsEngine.disconnect(startHandle)
        self.ttsEngine.disconnect(wordHandle)
        self.ttsEngine.disconnect(finishHandle)
        self.ttsEngine.disconnect(streamHandle)
        
        self.ttsEngine.stop()
        self.ttsEngine.waitUntilDone()
        self.ttsEngine.destroy()
        del self.ttsEngine
        
        self._done = True
        
        return
    
    def quit(self):
        '''
        Stops this thread. It will block until it has quit successfully.
        '''
        self._running = False
        
        while not self._done:
            pass
    
    def startPlayback(self):
        self.ttsEngine.start()
    
    def stopPlayback(self):
        self.ttsEngine.stop()
        
    def isPlaying(self):
        return self.ttsEngine.isPlaying()
            
    def stopMP3(self):
        self._stopMP3Creation = True
        
    def mp3Interrupted(self):
        return self._stopMP3Creation
            
    def saveToMP3(self, mp3Path, speechGenerator, tempDirectory):
        self._stopMP3Creation = False
        
        def myIsStop():
            return self._stopMP3Creation
        
        def myOnProgress(percent):
            self.onProgress.emit(percent)
        
        def myLabelUpdater(label):
            self.onProgressLabel.emit(label)
        
        # Wait until my TTS engine is fully created
        while not self._ttsCreated:
            pass
        
        # Turn off my signals so that window doesn't try and update
        self.ttsEngine.disableSignals()
        
        self.ttsEngine.speakToFile(mp3Path, speechGenerator, tempDirectory, myOnProgress, myLabelUpdater, myIsStop)
        self.ttsEngine.enableSignals()
    
    def setVolume(self, v):
        self._volume = v
        self._isChange = True
    
    def setRate(self, r):
        self._rate = r
        self._isChange = True
    
    def setPauseLength(self, p):
        self._pauseLength = p
        self._isChange = True
        
    def setVoice(self, voice):
        self._voice = voice
        self._isChange = True
        
    def setConfiguration(self):
        '''
        Convenience function for setting all of the TTS settings at once. This
        allows me to add other qualities to the TTS transparent of those who
        use it.
        '''
        self.setVolume(configuration.getInt('Volume'))
        self.setRate(configuration.getInt('Rate'))
        self.setPauseLength(configuration.getInt('PauseLength'))
        self.setVoice(configuration.getValue('Voice'))
        
    def getVoiceList(self):
        # Wait until the TTS is created before attempting what I want to do next
        while not self._ttsCreated:
            QThread.yieldCurrentThread()
        return self.ttsEngine.getVoiceList()
    
    def setSpeechGenerator(self, gen):
        self.ttsEngine.setSpeechGenerator(gen)
        #print 'worker: finished setting the speech generator'
        
    def noMoreSpeech(self):
        '''
        Flags the TTS engine that no more speech is to be given. The TTS is free
        to close now.
        '''
        self.ttsEngine.noMoreSpeech()
        
    def connect_signals(self, mainWindow):
        mainWindow.startPlayback.connect(self.startPlayback)
        mainWindow.stopPlayback.connect(self.stopPlayback)
        mainWindow.addToQueue.connect(self.addToQueue)