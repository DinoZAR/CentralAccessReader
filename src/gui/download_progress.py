'''
Created on Jul 9, 2013

@author: Spencer Graffe
'''
import urllib2
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtSignal, QThread
from src.forms.download_progress_ui import Ui_DownloadProgressWidget

class DownloadProgressWidget(QWidget):
    '''
    This widget displays and otherwise reports on the progress of a download.
    '''
    
    downloadProgress = pyqtSignal(int)
    downloadFinished = pyqtSignal(bool)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_DownloadProgressWidget()
        self.ui.setupUi(self)
        
        # Connect up the signals of my widgets
        self.ui.retryButton.clicked.connect(self.retryDownload)
        self.ui.cancelButton.clicked.connect(self.stopDownload)
        
        self._downloadThread = DownloadThread()
        self._downloadThread.downloadProgress.connect(self._reportProgress)
        self._downloadThread.finished.connect(self._reportFinished)
        
    def startDownload(self):
        '''
        Starts the download of whatever URL it was told to download.
        '''
        if self._downloadThread.hasUrl() and self._downloadThread.hasDestination():
            self._downloadThread.start()
            
    def retryDownload(self):
        '''
        Restarts the download over.
        '''
        self._downloadThread.finished.disconnect()
        self._downloadThread.stop()
        self._downloadThread.wait()
        self._downloadThread.finished.connect(self._reportFinished)
        self._downloadThread.start()
    
    def setUrl(self, url):
        '''
        Sets the URL that we should download from.
        '''
        self._downloadThread.setUrl(url)
        
    def setDestination(self, dest):
        '''
        Sets the destination of where the file should be downloaded.
        '''
        self._downloadThread.setDestination(dest)
        
    def stopDownload(self):
        '''
        Stops the current download. It will not do anything if there is no
        download currently in progress.
        '''
        self._downloadThread.stop()
    
    def _reportProgress(self, percent):
        '''
        Reports the progress of the download.
        '''
        self.ui.progressBar.setValue(percent)
        self.downloadProgress.emit(percent)
        
    def _reportFinished(self):
        '''
        Reports that a download is finished. It returns a boolean saying whether
        the download completed successfully or not.
        '''
        success = not self._downloadThread._stop
        self.downloadFinished.emit(success)
    

class DownloadThread(QThread):
    '''
    This thread is used to facilitate a download. It will report the progress 
    of its download and can be interrupted at any time.
    '''
    
    downloadProgress = pyqtSignal(int)
    
    def __init__(self):
        QThread.__init__(self)
        self._url = ''
        self._dest = ''
        self._stop = False
        
    def run(self):
        self._stop = False
            
        destFile = open(self._dest, 'wb')
        
        def reportProgress(percent):
            self.downloadProgress.emit(percent)
                        
        response = urllib2.urlopen(self._url)
        contents = self.chunkRead(response, reportProgress)
            
        if not self._stop:
            destFile.write(contents)
        
        destFile.close()
            
    def chunkRead(self, response, reportProgress, chunkSize=8192):
        size = int(response.info().getheader('Content-Length').strip())
        numBytes = 0
        contents = ''
        
        while 1:
            chunk = response.read(chunkSize)
            numBytes += len(chunk)
            
            if not chunk:
                break
            
            if self._stop:
                break
            
            contents += chunk
            reportProgress(int(float(numBytes) / size * 100.0))
        
        return contents
    
    def stop(self):
        self._stop = True
        
    def setUrl(self, url):
        self._url = url
        
    def setDestination(self, dest):
        self._dest = dest
        
    def hasUrl(self):
        return len(self._url) > 0
    
    def hasDestination(self):
        return len(self._dest) > 0