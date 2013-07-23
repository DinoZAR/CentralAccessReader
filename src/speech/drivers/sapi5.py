'''
Created on Jul 22, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QMutex
import win32com.client
import pythoncom
import win32event
import thread

from src.speech.drivers.SapiCOM import SpVoice, SpFileStream

class SAPI5Driver(object):
    '''
    Used in interfacing with SAPI 5.
    '''
    queueLock = QMutex()
    
    # Static variable used to generate unique ids for new callbacks
    CALLBACK_GEN = 1
    
    def __init__(self):
        self._queue = {}
        self._speechGenerator = None
        self._isFirstSpeech = True
        
        self._rate = 5   # Between -10 to 10
        self._volume = 100 # Between 0 to 100
        self._voiceId = ''
        self._settingsChanged = False
        
        self._voice = None
        
        # Used for callback functions
        self._delegator = {'onStart' : [], 'onWord' : [], 'onEndStream' : [], 'onFinish' : []}
        self._speechCounter = 0
        
        self._running = False
        self._stop = False
        
    def setRate(self, rate):
        '''
        Sets the _rate of the _voice,  a value between 0-100
        '''
        # 200 BPM = 0
        self._rate = int((rate / 5.0) - 10)
        self._settingsChanged = True
        
    def setVolume(self, volume):
        '''
        Sets the _volume of the _voice, from 0-100
        '''
        self._volume = int(volume)
        self._settingsChanged = True
        
    def setVoice(self, voiceKey):
        '''
        Sets the _voice using the key provided by getVoiceList()
        '''
        if len(voiceKey) > 0:
            self._voiceId = voiceKey
            self._settingsChanged = True
            
    def getVoiceList(self):
        '''
        Returns a list of voices using the following format:
        [description, keyOrId]
        
        The keyOrId is what you would use to set the voice later on.
        '''
        
        # Initialize the speech object so I can do stuff with it
        self._voice = SpVoice()
        
        sapiVoices = self._voice.GetVoices()
        
        myList = []
        for i in range(sapiVoices.Count):
            myItem = sapiVoices.Item(i)
            
            # For this driver, the key is an SpObjectToken
            myList.append([myItem.GetDescription(), myItem.Id])
        
        return myList
        
#     def add(self, text, label):
#         if self._isQueuing:
#             self.queueLock.lock()
#             print 'driver: Adding speech to queue'
#             self._speechCounter += 1
#             self._unqueued[self._speechCounter] = [text, label, 0]
#             self.queueLock.unlock()

    def setSpeechGenerator(self, gen):
        '''
        Sets the speech generator for speech playback. The generator is a Python
        generator object or iterable that returns tuples of the following:
        (text, label)
        '''
        #print 'driver: setting the speech generator'
        self._speechGenerator = gen
        self._speechCounter = 0
    
    def start(self):
        '''
        Starts the TTS engine.
        '''
        self._running = True
        self._isFirstSpeech = True
            
        # Run the loop that continually pumps messages during run
        thread.start_new_thread(self.runLoop, ())
        
    def voiceTokenFromId(self, id):
        tokens = self._voice.GetVoices()
        for token in tokens:
            if token.Id == id: return token
        raise ValueError('Unknown _voice id %s', id)
            
    def runLoop(self):
        '''
        The main loop of the SAPI driver. It runs as a server, constantly
        listening for instructions.
        '''
        
        #print 'Starting SAPI5 loop...'
        
        self.queueLock.lock()
        self._queue = {}
        self._unqueued = {}
        self.queueLock.unlock()
        
        pythoncom.CoInitialize()
        
        self._voice = SpVoice()
        
        self._voice.EventInterests = 33790 # SVEAllEvents
        self._voice.AlertBoundary = 64 # SVEPhoneme
        
        # Set the characteristics of the _voice
        if len(self._voiceId) > 0:
            self._voice.Voice = self.voiceTokenFromId(self._voiceId)
        
        self._voice.Volume = self._volume
        self._voice.Rate = self._rate
        
        # Get the events from the speech playback
        self.advisor = win32com.client.WithEvents(self._voice, SAPIEventSink)
        self.advisor.setDriver(self)
        
        # Run the TTS playback
        for speech in self._speechGenerator:
            #print 'driver: queuing speech to voice'
            self._queue[self._speechCounter] = [speech[0], speech[1], None]
            self._queue[self._speechCounter][2] = self._voice.Speak(self._queue[self._speechCounter][0], 1)
            self._speechCounter += 1
            
            # Check if my settings have changed
            if self._settingsChanged:
                self._voice.Volume = self._volume
                self._voice.Rate = self._rate
                if len(self._voiceId) > 0:
                    self._voice.Voice = self.voiceTokenFromId(self._voiceId)
                self._settingsChanged = False
            
            pythoncom.PumpWaitingMessages()
            
            # Check if I am being interrupted
            if not self._running:
                break
    
        # Spin until everything is done
        while len(self._queue) > 0 and self._running:
            
            # Check if my settings have changed
            if self._settingsChanged:
                self._voice.Volume = self._volume
                self._voice.Rate = self._rate
                if len(self._voiceId) > 0:
                    self._voice.Voice = self.voiceTokenFromId(self._voiceId)
                self._settingsChanged = False
                
            pythoncom.PumpWaitingMessages()
                
        # Use this empty message to completely clear queue
        #print 'driver: Emptying out queue in SAPI voice'
        self._voice.Speak('', 3) # SPF_PURGEBEFORESPEAK
            
        #print 'driver: Publishing OnFinish'
        for c in self._delegator['onFinish']:
            c[1]()
            
        pythoncom.PumpWaitingMessages()
        
        #print 'SAPI5 driver done!'
        
        return
        
    def stop(self):
        '''
        Stops the TTS playback. The TTS engine will still be running in the
        background
        '''
        self._running = False
        
    def speakToWavFile(self, wavFilePath, outputList, progressCallback, checkStopFunction):
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
        pythoncom.CoInitialize()
    
        saveFileStream = SpFileStream()
        saveFileStream.Format.Type = 18  # Some magic number that gives good results
        saveFileStream.Open(wavFilePath, 3)
    
        self._voice = SpVoice()
        self._voice.AudioOutputStream = saveFileStream
        self._voice.EventInterests = 33790 # SVEAllEvents
        self._voice.AlertBoundary = 64 # SVEPhoneme
        
        if len(self._voiceId) > 0:
            token = self.voiceTokenFromId(self._voiceId)
            self._voice.Voice = token
            
        self._voice.Volume = self._volume
        self._voice.Rate = self._rate
        
        # Voice events for updating the progress thing
        advisor = win32com.client.WithEvents(self._voice, SAPIEventSink)
        advisor.setDriver(self)
        
        for i in range(len(outputList)):
            progressCallback(int(float(i) / len(outputList) * 100.0 - 1))
            self._voice.Speak(outputList[i][0], 1)
            while not self._voice.WaitUntilDone(10):
                if checkStopFunction():
                    break
            if checkStopFunction():
                break
        
        saveFileStream.Close()
        progressCallback(99)
        
    def waitUntilDone(self):
        while self._running:
            pass
            
    def isFinished(self):
        return not self._running
    
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
        SAPI5Driver.CALLBACK_GEN = SAPI5Driver.CALLBACK_GEN + 1
        
        if eventLabel in self._delegator:
            self._delegator[eventLabel].append([SAPI5Driver.CALLBACK_GEN, callback])
            return SAPI5Driver.CALLBACK_GEN
        else:
            raise ValueError('Event ' + eventLabel + ' is not available for callback.')
            
    def handle_onWord(self, stream, pos, char, length):
        
        #print 'driver: OnWord!'
        
        # Get the _queue item associated with the stream
        i = -1
        self.queueLock.lock()
        for k in self._queue.keys():
            if self._queue[k][2] == stream:
                i = k
                break
        
        if i >= 0:
            word = self._queue[i][0][char:char+length]
            self.queueLock.unlock()
            
            # Publish onStart if it is so
            myIsFirst = self._isFirstSpeech
            if self._isFirstSpeech:
                for c in self._delegator['onStart']:
                    #print 'driver: Publishing onStart'
                    c[1](char, length, self._queue[i][1], stream, word)
                self._isFirstSpeech = False
            
            # Publish onWord
            for c in self._delegator['onWord']:
                #print 'driver: Publishing onWord'
                c[1](char, length, self._queue[i][1], stream, word, myIsFirst)
        
    
    def handle_onEndStream(self, stream, pos):
        #print 'driver: OnEndStream!'
        # Figure out what stream ended and remove it from my queue
        i = 0
        #print 'driver: OnEndStream, obtaining queue lock'
        self.queueLock.lock()
        #print 'driver: OnEndStream, got lock!'
        for k in self._queue.keys():
            if self._queue[k][2] == stream:
                
                # Tell all of the people that a stream ended
                for c in self._delegator['onEndStream']:
                    #print 'driver: Publishing onEndStream callbacks'
                    c[1](stream, self._queue[k][1])
                    
                del self._queue[k]
                break
        self.queueLock.unlock()
    
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
    
        
class SAPIEventSink(object):
    '''
    A class used in getting the events from the SAPI playback. One must setup 
    the link to get these messages of this class by using the setDriver method.
    '''
    def __init__(self):
        self._driver = None
        
    def setDriver(self, driver):
        self._driver = driver
    
    def OnWord(self, stream, pos, char, length):
        self._driver.handle_onWord(stream, pos, char, length)
        
    def OnEndStream(self, stream, pos):
        self._driver.handle_onEndStream(stream, pos)