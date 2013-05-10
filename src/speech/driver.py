'''
Created on Apr 9, 2013

@author: Spencer Graffe
'''
import time
import thread
import platform
from src.misc import clean_XML_input

if platform.system() == 'Windows':
    import win32com.client
    from src.speech.SapiCOM import SpVoice, SpFileStream

    import pythoncom
    import win32event

def get_driver():
    '''
    Returns the correct TTS driver for the operating system in use. It then
    returns the TTS engine that will work for it.
    '''
    if platform.system() == 'Windows':
        return SAPIDriver()
    else:
        return None

class SAPIDriver(object):
    '''
    Used in interfacing with SAPI 5.
    '''
    
    # Static variable used to generate unique ids for new callbacks
    CALLBACK_GEN = 1
    
    def __init__(self):
        
        self.queue = []
        
        self.rate = 5   # Between -10 to 10
        self.volume = 5 # Between 0 to 100
        self.voiceId = ''
        
        # Used for callback functions
        self.delegator = {'onWord': [], 'onFinish' : []}
        
        self.running = False
        
    def setRate(self, rate):
        '''
        Sets the rate of the voice,  a value between 0-100
        '''
        # 200 BPM = 0
        self.rate = int((rate / 5.0) - 10)
        
    def setVolume(self, volume):
        '''
        Sets the volume of the voice, from 0-100
        '''
        self.volume = int(volume)
        
    def setVoice(self, voice):
        '''
        Sets the voice, represented as a string (normally a URI)
        '''
        if len(voice) > 0:
            self.voiceId = voice
            
    def getVoiceList(self):
        '''
        Returns a list of voices using the following format:
        [description, keyOrId]
        
        The keyOrId is what you would use to set the voice later on.
        '''
        
        # Initialize the speech object so I can do stuff with it
        self.voice = SpVoice()
        
        sapiVoices = self.voice.GetVoices()
        
        myList = []
        for i in range(sapiVoices.Count):
            myItem = sapiVoices.Item(i)
            
            # For this driver, the key is an SpObjectToken
            myList.append([myItem.GetDescription(), myItem.Id])
        
        return myList
        
    def add(self, text, label):
        self.queue.append([text, label, 0])
    
    def start(self):
        '''
        Starts the TTS asynchronously. Should use callbacks if you need to
        do something when it ends.
        '''
        self.running = True
            
        # Run the loop that continually pumps messages during run
        thread.start_new_thread(self.runLoop, ())
        
    def voiceTokenFromId(self, id):
        tokens = self.voice.GetVoices()
        for token in tokens:
            if token.Id == id: return token
        raise ValueError('Unknown voice id %s', id)
            
    def runLoop(self):
        
        pythoncom.CoInitialize()
        
        self.voice = SpVoice()
        
        self.voice.EventInterests = 33790 # SVEAllEvents
        self.voice.AlertBoundary = 64 # SVEPhoneme
        
        # Set the characteristics of the voice
        if len(self.voiceId) > 0:
            token = self.voiceTokenFromId(self.voiceId)
            self.voice.Voice = token
        
        self.voice.Volume = self.volume
        self.voice.Rate = self.rate
        
        # Get the events from the speech playback
        self.advisor = win32com.client.WithEvents(self.voice, SAPIEventSink)
        self.advisor.setDriver(self)
        
        for i in range(len(self.queue)):
            # Make the voice say this asynchronously
            self.queue[i][2] = self.voice.Speak(self.queue[i][0], 1)
        
        while self.running:
            pythoncom.PumpWaitingMessages()
        
        # Use this empty message to completely clear queue
        self.voice.Speak('', 3) # SPF_PURGEBEFORESPEAK
        pythoncom.PumpWaitingMessages()
        
        return
        
    def stop(self):
        '''
        Kills everything so that TTS playback stops.
        '''
        self.running = False
        self.queue = []
        
    def speakToWavFile(self, wavFilePath, outputList, progressCallback):
        '''
        This is a separate function that runs on a different thread.
        This will not return until it has completely written the speech to the
        file.
        
        The output list should be the following:
        [('Speech!', 'label'), ('Speech!', 'label'), ...]
        
        The progressCallback should be a function that takes an int from 0-100,
        100 being when it is done.
        '''
        pythoncom.CoInitialize()
    
        saveFileStream = SpFileStream()
        saveFileStream.Format.Type = 18  # Some magic number that gives good results
        saveFileStream.Open(wavFilePath, 3)
    
        voice = SpVoice()
        voice.AudioOutputStream = saveFileStream
        voice.EventInterests = 33790 # SVEAllEvents
        voice.AlertBoundary = 64 # SVEPhoneme
        
        voice.Volume = self.volume
        voice.Rate = self.rate
        
        # Voice events for updating the progress thing
        advisor = win32com.client.WithEvents(voice, SAPIEventSink)
        advisor.setDriver(self)
        
        for i in range(len(outputList)):
            progressCallback(int(float(i) / len(outputList) * 100.0 - 1))
            voice.Speak(outputList[i][0], 1)
            voice.WaitUntilDone(0xFFFFFFF) # Maximum time
        
        progressCallback(99)
        
        saveFileStream.Close()
        
    def waitUntilDone(self):
        while self.running:
            pass
            
    def isFinished(self):
        return not self.running
    
    def connect(self, eventLabel, callback):
        '''
        Connects the callback function to the event specified by the label.
        The following labels are available:
         - onWord
         - onFinish
         
        Returns a handle to use later for disconnect() for that particular
        callback.
        '''
        SAPIDriver.CALLBACK_GEN = SAPIDriver.CALLBACK_GEN + 1
        
        if eventLabel in self.delegator:
            self.delegator[eventLabel].append([SAPIDriver.CALLBACK_GEN, callback])
            return SAPIDriver.CALLBACK_GEN
        else:
            return -1
            
    def handle_onWord(self, stream, pos, char, length):
        
        # Get the queue item associated with the stream
        i = 0
        while i < len(self.queue):
            if self.queue[i][2] == stream:
                break
            else:
                i += 1
#         word = self.queue[i][0][char:char+length]
        
        # Publish this to everyone in callbacks
        for c in self.delegator['onWord']:
            c[1](char, length, self.queue[i][1], stream)
        
    
    def handle_onEndStream(self, stream, pos):
        
        # Figure out what stream ended and remove it from my queue
        i = 0
        while i < len(self.queue):
            if self.queue[i][2] == stream:
                self.queue.pop(i)
                i = 0
            else:
                i += 1
        
        # If I still have things in my queue, then keep running. Else
        # make everything stop
        if len(self.queue) == 0:
            self.running = False
            
            # Tell everyone else that we stopped
            for c in self.delegator['onFinish']:
                c[1]()
    
    def disconnect(self, handle):
        '''
        Removes the callback from the driver using the handle. The handle is
        provided to you when you call connect().
        '''
        # Search for the handle in all of my callback lists
        for e in self.delegator:
            i = 0
            while i < len(self.delegator[e]):
                if self.delegator[e][i][0] == handle:
                    self.delegator[e].pop(i)
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