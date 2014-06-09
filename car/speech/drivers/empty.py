'''
Created on Jul 30, 2013

@author: Spencer Graffe
'''

class EmptyDriver(object):
    '''
    This a mock driver that doesn't do anything. Great for testing things.
    '''
    
    def __init__(self, requestSpeechHook=None):
        pass
        
    def setRate(self, rate):
        '''
        Sets the _rate of the _voice,  a value between 0-100
        '''
        pass
        
    def setVolume(self, volume):
        '''
        Sets the _volume of the _voice, from 0-100
        '''
        pass
        
    def setVoice(self, voiceKey):
        '''
        Sets the _voice using the key provided by getVoiceList()
        '''
        pass
            
    def getVoiceList(self):
        '''
        Returns a list of voices using the following format:
        [description, keyOrId]
        
        The keyOrId is what you would use to set the voice later on.
        '''
        return []
        
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
        pass
    
    def start(self):
        '''
        Starts the TTS engine.
        '''
        pass
        
    def voiceTokenFromId(self, id):
        return ''
        
    def stop(self):
        '''
        Stops the TTS playback. The TTS engine will still be running in the
        background
        '''
        pass
        
    def noMoreSpeech(self):
        '''
        Flags the TTS that it won't be expecting any more speech.
        '''
        pass
        
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
        pass
            
    def isFinished(self):
        return True
    
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
        return 0
            
    def handle_onWord(self, stream, pos, char, length):
        pass
        
    
    def handle_onEndStream(self, stream, pos):
        pass
    
    def disconnect(self, handle):
        '''
        Removes the callback from the driver using the handle. The handle is
        provided to you when you call connect().
        '''
        pass