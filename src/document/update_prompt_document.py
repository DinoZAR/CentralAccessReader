'''
Created on Dec 9, 2013

@author: Spencer Graffe
'''
from lxml import html
from document import Document

class UpdatePromptDocument(Document):
    '''
    This document shows an update prompt. It has buttons inside that the user
    can click on to accept the update.
    '''

    def __init__(self, filePath, progressHook, cancelHook, hasDownloaded=False):
        Document.__init__(self, filePath, progressHook, cancelHook)
        
        self._name = 'Update!'
        if hasDownloaded:
            self._contentDOM = html.fromstring(self._contentInstall())
        else:
            self._contentDOM = html.fromstring(self._contentDownload())
         
        self._mapMathEquations()
        
        self._exportable = False
        
    def _contentDownload(self):
        s = '''
        <body>
        
        <h1>An update is available!</h1>
        <p>Would you like to download it?</p>
        <div><a class="button" href="command/updateDownloadYes">Yes</a><a class="button" href="command/updateDownloadNo">No</a></div>
        
        </body>
        '''
        return s
    
    def _contentInstall(self):
        s = '''
        <body>
        
        <h1>Update downloaded!</h1>
        <p>Would you like to install it?</p>
        <div><a class="button" href="command/updateInstallYes">Yes</a><a class="button" href="command/updateInstallNo">No</a></div>
        
        </body>
        '''
        return s