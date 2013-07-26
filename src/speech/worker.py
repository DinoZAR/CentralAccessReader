'''
Created on Apr 8, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread, QMutex, pyqtSignal
from PyQt4.QtGui import qApp
from src.speech import driver
import platform
import subprocess
import re
from src.misc import temp_path, program_path

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
        
        self._volume = 100
        self._rate = 50
        self._voice = ''
        
        self._ttsCreated = False
        
        self._stopMP3Creation = False
        
        self._isChange = False
        
    def run(self):
        
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
        self.ttsEngine.connect('onStart', myOnStart)
        self.ttsEngine.connect('onWord', myOnWord)
        self.ttsEngine.connect('onFinish', myOnFinish)
        self.ttsEngine.connect('onEndStream', myOnEndStream)
        
        self.ttsEngine.setVolume(self._volume)
        self.ttsEngine.setRate(self._rate)
        self.ttsEngine.setVoice(self._voice)
        
        self._ttsCreated = True
        
        while True:
            if self._isChange:
                self.ttsEngine.setVolume(self._volume)
                self.ttsEngine.setRate(self._rate)
                self.ttsEngine.setVoice(self._voice)
                self._isChange = False
            QThread.yieldCurrentThread()
        
        return
    
    def startPlayback(self):
        print 'worker: Trying to start TTS'
        self.ttsEngine.start()
    
    def stopPlayback(self):
        print 'worker: Trying to stop TTS'
        self.ttsEngine.stop()
            
    def stopMP3(self):
        self._stopMP3Creation = True
        
    def mp3Interrupted(self):
        return self._stopMP3Creation
            
    def saveToMP3(self, mp3Path, speechGenerator):
        
        self._stopMP3Creation = False
        
        # Create the WAV file first
        def myIsStop():
            return self._stopMP3Creation
        
        def myOnProgress(percent):
            self.onProgress.emit(int((float(percent) / 100.0) * 70.0))
        
        wavSavePath = temp_path('tmp.wav')
        
        self.onProgressLabel.emit('Speaking into WAV...')
        self.ttsEngine.speakToWavFile(wavSavePath, speechGenerator, myOnProgress, myIsStop)
        
        if not self._stopMP3Creation:
            # Then convert it to MP3
            self.onProgressLabel.emit('Converting to MP3...')
            lameExe = ''
            if '64' in platform.architecture()[0]:
                lameExe = program_path('src/lame_64.exe')
            else:
                lameExe = program_path('src/lame_32.exe')
            
            startupInfo = subprocess.STARTUPINFO()
            startupInfo.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
            startupInfo.wShowWindow = subprocess.SW_HIDE
            lameCommand = lameExe + ' -h "' + wavSavePath + '" "' + mp3Path + '"'
            ps = subprocess.Popen(lameCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupInfo)
            
            while ps.poll() == None:
                qApp.processEvents()
                if self._stopMP3Creation:
                    ps.terminate()
                    break
                out = ps.stderr.readline()
                if re.search(r'\([0-9]+%\)', out) != None:
                    percent = int(float(re.search(r'\([0-9]+%\)', out).group(0)[1:-2]) * 0.3)
                    self.onProgress.emit(69 + percent)
        
        self.onProgress.emit(100)
    
    def setVolume(self, v):
        self._volume = v
        self._isChange = True
    
    def setRate(self, r):
        self._rate = r
        self._isChange = True
        
    def setVoice(self, voice):
        self._voice = voice
        self._isChange = True
        
    def getVoiceList(self):
        # Wait until the TTS is created before attempting what I want to do next
        while not self._ttsCreated:
            pass
        return self.ttsEngine.getVoiceList()
    
    def setSpeechGenerator(self, gen):
        self.ttsEngine.setSpeechGenerator(gen)
        
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