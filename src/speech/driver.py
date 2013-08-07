'''
Created on Apr 9, 2013

@author: Spencer Graffe
'''
import platform

def get_driver(requestSpeechHook=None):
    '''
    Returns the correct TTS driver for the operating system in use.
    '''
    if platform.system() == 'Windows':
        from speech.drivers.sapi5 import SAPI5Driver
        return SAPI5Driver(requestSpeechHook)
#         from src.speech.drivers.empty import EmptyDriver
#         return EmptyDriver()
    elif platform.system() == 'Darwin':
        # Get TTS for Mac
        from speech.drivers.nsss import NSSpeechSynthesizerDriver
        nsObject = NSSpeechSynthesizerDriver.alloc().initWithRequestSpeechHook(requestSpeechHook)
        return nsObject
    else:
        from speech.drivers.empty import EmptyDriver
        return EmptyDriver()
