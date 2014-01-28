'''
Created on Dec 18, 2013

@author: Spencer Graffe
'''
import os
from export import ExportThread
from speech.worker import SpeechWorker

class MP3ExportThread(ExportThread):
    '''
    Exports the content to a single MP3 of spoken audio
    '''

    def __init__(self, document, htmlContent, tempDirectory):
        super(MP3ExportThread, self).__init__(document, htmlContent, tempDirectory)
        self._speech = None
        self._ttsCurrentLabel = ''
    
    @staticmethod
    def description():
        return 'MP3'
    
    @staticmethod    
    def getDefaultPath(inputFilePath):
        '''
        Returns a possible default path for the given input file.
        '''
        return os.path.splitext(inputFilePath)[0] + '.mp3'
    
    def run(self):
        super(MP3ExportThread, self).run()
        
        # Get the progress of the thing from the speech thread
        def myOnProgress(percent):
            self.progress.emit(percent, self._ttsCurrentLabel)
            
        def myOnProgressLabel(newLabel):
            self._ttsCurrentLabel = newLabel
                
        # Create my own speech thread
        self._speech = SpeechWorker()
        self._speech.start()
        
        # Set the speech settings
        self._speech.setConfiguration()
        
        # Connect the signals
        self._speech.onProgress.connect(myOnProgress)
        self._speech.onProgressLabel.connect(myOnProgressLabel)
        
        # Set the HTML so that I only get the <body> tag
        query = self._htmlContent.xpath('.//body')
        if query is not None:
            if len(query) > 0:
                self._htmlContent = query[0]
        
        # Create the speech generator object to send to TTS
        speechGenerator = self._document.generateSpeech(self._htmlContent)
        
        # Run the MP3 export (synchronous)
        self._speech.saveToMP3(self._filePath, speechGenerator, self._tempDirectory)
        
        # Show a message box saying the file was successfully saved        
        if not self._speech.mp3Interrupted():
            self.success.emit()
            self.isSuccess = True
    
    def stop(self):
        ExportThread.stop(self)        
        self._speech.stopMP3()