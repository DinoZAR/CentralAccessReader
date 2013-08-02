'''
Created on Aug 1, 2013

@author: Spencer Graff
'''
from AppKit import NSSpeechSynthesizer
from threading import Lock

class NSSpeechSynthesizerDriver(object):
    '''
    Used in interfacing with Apple's NSSpeechSynthesizer.
    '''
    generatorLock = Lock()

    CALLBACK_GEN = 0
    
    def __init__(self, requestSpeechHook=None):
        self._speechGenerator = None
        self._isFirstSpeech = True
        self._delegator = {'onStart' : [], 'onWord' : [], 'onEndStream' : [], 'onFinish' : []}

    def setRate(self, rate):
        '''
        Sets the rate of the voice,  a value between 0-100
        '''
        pass

    def setVolume(self, volume):
        '''
        Sets the volume of the voice, from 0-100
        '''
        pass

    def setVoice(self, voiceKey):
        '''
        Sets the voice using the key provided by getVoiceList()
        '''
        pass

    def getVoiceList(self):
        '''
        Returns a list of voices using the following format:
        [description, keyOrId]
        
        The keyOrId is what you would use to set the voice later on.
        '''
        pass

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

    def stop(self):
        '''
        Stops the TTS playback. The TTS engine will still be running in the
        background.
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
        '''
        Waits until the TTS engine stops running.
        '''
        pass

    def isFinished(self):
        pass

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
        NSSpeechSynthDriver.CALLBACK_GEN = NSSpeechSynthDriver.CALLBACK_GEN + 1

        if eventLabel in self._delegator:
            self._delegator[eventLabel].append([NSSpeechSynthDriver.CALLBACK_GEN, callback])
            return NSSpeechSynthDriver.CALLBACK_GEN
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
