'''
Created on Aug 1, 2013

@author: Spencer Graff
'''
from Foundation import NSObject, NSString
from AppKit import NSSpeechSynthesizer
from PyObjCTools import AppHelper
from PyQt4.QtCore import QMutex
import thread
import time

class NSSpeechSynthesizerDriver(NSObject):
    '''
    Used in interfacing with Apple's NSSpeechSynthesizer.
    '''
    generatorLock = QMutex()

    CALLBACK_GEN = 0
    
    def initWithRequestSpeechHook(self, requestSpeechHook=None):
        self = super(NSSpeechSynthesizerDriver, self).init()
        if self:
            self._speechGenerator = None
            self._currentLabel = 'text'
            self._currentStream = 0
            self._isFirstSpeech = True
            self._delegator = {'onStart' : [], 'onWord' : [], 'onEndStream' : [], 'onFinish' : []}
            self._grabbingSpeech = False
            self._requestSpeechHook = requestSpeechHook
            
            self._tts = NSSpeechSynthesizer.alloc().initWithVoice_(None)
            self._tts.setDelegate_(self)
            
            self._tts.setVolume_(1.0)
            self._tts.setRate_(200)
            self._pauseLength = 0
        
        return self
    
    def destroy(self):
        self._tts.setDelegate_(None)
        del self._tts

    def setRate(self, rate):
        '''
        Sets the rate of the voice, a value between 0-100
        '''
        # Transform 0-100 between a specific words-per-minute range
        # Average rate is 180-220 wpm
        wpmMin = 50
        wpmMax = 350
        myRate = wpmMin + ((wpmMax - wpmMin) * float(rate) / 100.0)
        self._tts.setRate_(myRate)

    def setVolume(self, volume):
        '''
        Sets the volume of the voice, from 0-100
        '''
        self._tts.setVolume_(float(volume) / 100.0)
        
    def setPauseLength(self, pauseLength):
        '''
        Sets the pause length between elements. The value is between 0-10, which
        can be scaled however appropriate for the TTS driver.
        '''
        self._pauseLength = pauseLength

    def setVoice(self, voiceKey):
        '''
        Sets the voice using a key provided by getVoiceList()
        '''
        vol = self._tts.volume()
        rate = self._tts.rate()
        if len(voiceKey) > 0:
            self._tts.setVoice_(unicode(voiceKey))
        
        self._tts.setVolume_(vol)
        self._tts.setRate_(rate)
        
    def areSettingsInteractive(self):
        return False

    def getVoiceList(self):
        '''
        Returns a list of voices using the following format:
        [description, keyOrId]
        
        The keyOrId is what you would use to set the voice later on.
        '''
        voiceList = NSSpeechSynthesizer.availableVoices()
        
        myList = []
        for v in voiceList:
            descr = v.split('.')[-1]
            myList.append((unicode(descr), unicode(v)))
        
        return myList

    def setSpeechGenerator(self, gen):
        '''
        Sets the speech generator for speech playback. The generator is a Python
        generator object or iterable that returns tuples of the following:
        (text, label)
        '''
        self.generatorLock.lock()
        self._speechGenerator = gen
        self.generatorLock.unlock()
    
    def start(self):
        '''
        Starts the TTS engine.
        '''
        print 'driver: starting TTS'
        self._isFirstSpeech = True
        self._currentLabel = 'text'
        self._grabbingSpeech = True
        self._alreadyRequestedSpeech = False
        self._running = True
        
        # Run a thread that will continually read through the speech
        thread.start_new_thread(self._runLoop, ())
    
    def _runLoop(self):
        '''
        This loop is used to queue my speech onto the TTS engine.
        '''
        while self._grabbingSpeech and self._running:
            self.generatorLock.lock()
            if self._speechGenerator is not None:
                for speech in self._speechGenerator:
                    self._currentLabel = speech[1]
                    self._tts.startSpeakingString_(speech[0])
                    self._currentStream += 1
                    
                    # Wait until it has finished, checking for cancel
                    while self._tts.isSpeaking() and self._running:
                        pass
                    
                    if not self._running:
                        break
                    
                    # Pause here if it is set
                    if self._grabbingSpeech and self._running:
                        print 'driver: pausing between paragraphs'
                        time.sleep(self._pauseLength / 5.0)
            
                self._speechGenerator = None
                self._alreadyRequestedSpeech = False
            self.generatorLock.unlock()
            
            # Request to get some more speech, if I didn't already
            if not self._alreadyRequestedSpeech:
                self._alreadyRequestedSpeech = True
                if self._requestSpeechHook is not None:
                    self._requestSpeechHook()
        
        # Tell everyone that the TTS is done
        for c in self._delegator['onFinish']:
            c[1]()
        
        print 'driver: done!'
        
        return

    def stop(self):
        '''
        Stops the TTS playback. The TTS engine will still be running in the
        background.
        '''
        print 'driver: stopping TTS'
        self._running = False
        self._tts.stopSpeaking()

    def noMoreSpeech(self):
        '''
        Flags the TTS that it won't be expecting any more speech.
        '''
        self._grabbingSpeech = False

    def speakToWavFile(self, wavFilePath, speechGenerator, progressCallback, checkStopFunction):
        '''
        This is a separate function that runs on a different thread.
        This will not return until it has completely written the speech to the
        file.
        
        The output list should be the following:
        [('Speech!', 'label'), ('Speech!', 'label'), ...]
        
        The progressCallback should be a function that takes an int from 0-100,
        100 being when it is done.
        
        The checkStopFunction returns a boolean value saying whether we need to
        stop creation, False being don't stop, and True being stop.
        '''
        pass

    def waitUntilDone(self):
        '''
        Waits until the TTS engine stops running.
        '''
        pass

    def isFinished(self):
        return not (self._running and self._tts.isSpeaking())

    def connect(self, eventLabel, callback):
        '''
        Connects the callback function to the event specified by the label.
        The following labels are available:
         - onStart
         - onWord
         - onFinish
         - onEndStream
         
        Returns a handle to use later for disconnect() for that particular
        callback.
        '''
        NSSpeechSynthesizerDriver.CALLBACK_GEN = NSSpeechSynthesizerDriver.CALLBACK_GEN + 1

        if eventLabel in self._delegator:
            self._delegator[eventLabel].append([NSSpeechSynthesizerDriver.CALLBACK_GEN, callback])
            return NSSpeechSynthesizerDriver.CALLBACK_GEN
        else:
            raise ValueError('Event ' + eventLabel + ' is not available for callback.')

    def disconnect(self, handle):
        '''
        Removes the callback from the driver using the handle. The handle is
        provided to you when you call connect().
        '''
        # Search for the handle in all of my callback lists
        for e in self._delegator:
            i = 0
            while i < len(self._delegator[e]):
                if self._delegator[e][i][0] == handle:
                    self._delegator[e].pop(i)
                    i = 0
                else:
                    i += 1
    
    def speechSynthesizer_didFinishSpeaking_(self, tts, success):
        '''
        This is called when a queue of text is spoken. It's like the end of a
        stream.
        '''
        # Tell everyone that a stream has ended
        for c in self._delegator['onEndStream']:
            c[1](self._currentStream, self._currentLabel)
    
    def speechSynthesizer_willSpeakWord_ofString_(self, tts, wordRange, text):
        '''
        This is called right before a word is about to be spoken. This is the
        perfect place to call onStart and onWord's. 
        '''
        word = text[wordRange.location:wordRange.location + wordRange.length]
        
        # If it is the first word, set the beginning
        if self._isFirstSpeech:
            for c in self._delegator['onStart']:
                c[1](wordRange.location, wordRange.length, self._currentLabel, self._currentStream, word)
            self._isFirstSpeech = False
        
        # Notify everyone that I am saying a word
        for cb in self._delegator['onWord']:
            cb[1](wordRange.location, wordRange.length, self._currentLabel, self._currentStream, word, self._isFirstSpeech)
            
    def __del__(self):
        self.destroy()
        