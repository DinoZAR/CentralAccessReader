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
        from src.speech.drivers.sapi5 import SAPI5Driver
        return SAPI5Driver(requestSpeechHook)
#         from src.speech.drivers.empty import EmptyDriver
#         return EmptyDriver()
    elif sys.platform == 'darwin':
        # Get TTS for Mac
        from src.speech.drivers.nsss import NSSpeechSynthesizerDriver
        return NSSpeechSynthesizerDriver(requestSpeechHook)
        pass
    else:
        from src.speech.drivers.empty import EmptyDriver
        return EmptyDriver()
