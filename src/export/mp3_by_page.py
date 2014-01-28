'''
Created on Dec 19, 2013

@author: Spencer Graffe
'''
import math
import os
from lxml import html
from export import ExportThread
from speech.worker import SpeechWorker
import misc

class MP3ByPageExportThread(ExportThread):
    '''
    This thread converts the content into MP3 files, split by page.
    '''

    def __init__(self, document, htmlContent, tempDirectory):
        super(MP3ByPageExportThread, self).__init__(document, htmlContent, tempDirectory)
        self._speech = None
        self._ttsCurrentLabel = ''
    
    @staticmethod
    def description():
        return 'MP3 By Page'
    
    @staticmethod
    def getDefaultPath(inputFilePath):
        '''
        Returns a possible default path for the given input file.
        '''
        return os.path.splitext(inputFilePath)[0] + '/'
    
    def run(self):
        super(MP3ByPageExportThread, self).run()
        
        # Create my own speech thread
        self._speech = SpeechWorker()
        self._speech.start()
        
        # Set the speech settings
        self._speech.setConfiguration()
        
        # Set the HTML so that I only get the <body> tag
        query = self._htmlContent.xpath('.//body')
        if query is not None:
            if len(query) > 0:
                self._htmlContent = query[0]
        
        # Split up the body into a list of elements, split by page.
        pages = []
        currentPage = [[], 'Front']
        largestNumberLength = 1
        success = True
        for e in self._htmlContent:
            if e.get('class') == 'pageNumber':
                
                if len(e.text_content()) > 0:
                    
                    # Figure out the number of decimal places of the page number, if possible
                    try:
                        num = math.ceil(math.log10(int(e.text_content())))
                        if num > largestNumberLength:
                            largestNumberLength = int(num)
                    except ValueError:
                        pass
                        
                if len(currentPage[0]) > 0:
                    pages.append(currentPage)
                    
                currentPage = [[], e.text_content()]
            currentPage[0].append(e)
        
        # Add the last page if there's content in it
        if len(currentPage[0]) > 0:
            pages.append(currentPage)
        
        # Save all of the pages!
        self._numPages = len(pages)
        for i in range(self._numPages):
            page = pages[i]
            
            # Tell the dialog what page we are on
            self._currentPagePercentage = int((i+1.0) / self._numPages * 100.0)
            self._currentPageLabel =  'Exporting Page ' + page[1] + '...'
            
            # Prepare the speech of the page
            myHTML = ''
            for e in page[0]:
                myHTML += html.tostring(e)
                
            speechGenerator = self._document.generateSpeech(html.fromstring(myHTML))
        
            # Generate a file name for saving the page number
            fileName = ''
            if misc.is_number(page[1]):
                fileName = 'Pg ' + page[1].zfill(largestNumberLength) + ' ' + self._document.getName()
            else:
                fileName = 'Pg ' + page[1] + ' ' + self._document.getName()
            fileName += '.mp3'
            fileName = os.path.join(self._filePath, fileName)
            
            # Check if the directory exists. If not, make the directories
            if not os.path.exists(os.path.dirname(fileName)):
                os.makedirs(os.path.dirname(fileName))
                            
            # Get the progress of the thing from the speech thread
            def myOnProgress(percent):
                pageProgress = float(percent) * (1.0 / self._numPages) + self._currentPagePercentage
                self.progress.emit(pageProgress, self._currentPageLabel)
            
            self._speech.onProgress.connect(myOnProgress)
            
            self._speech.saveToMP3(fileName, speechGenerator, self._tempDirectory)
                        
            if self._speech.mp3Interrupted():
                success = False
                break
        
        # Show the success message, if I was indeed successful
        if success:
            self.success.emit()
            self.isSuccess = True
    
    def stop(self):
        ExportThread.stop(self)
        self._speech.stopMP3()