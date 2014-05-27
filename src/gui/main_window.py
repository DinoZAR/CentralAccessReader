'''
Created on Jan 21, 2013

@author: Spencer Graffe
'''
import os

from PyQt4 import QtGui
from PyQt4.QtGui import qApp
from PyQt4.QtWebKit import QWebSettings
from PyQt4.QtCore import Qt, QMutex, pyqtSignal, QTimer

from src.announcements import AnnouncementPullThread, ANNOUNCEMENT_RSS_URL
from src.document.landing_page_document import LandingPageDocument
from src.document.update_prompt_document import UpdatePromptDocument
from src.document.rss.rss_document import RSSDocument
from src.document.widget import DocumentWidget
from src.forms.mainwindow_ui import Ui_MainWindow
from src.gui import configuration
from src.gui import loader
from src.gui.bookmarks import BookmarksTreeModel, BookmarkNode
from src.gui.document_load_progress import DocumentLoadProgressDialog
from src.gui.export_batch import ExportBatchDialog
from src.gui.math_library_dev import MathLibraryDev
from src.gui.pages import PagesTreeModel
from src import misc
from src.speech.worker import SpeechWorker
from src.updater import GetUpdateThread, SETUP_FILE, SETUP_TEMP_FILE, run_update_installer, is_update_downloaded, save_server_version_to_temp

class MainWindow(QtGui.QMainWindow):
    loc = 0
    len = 0
    jumped = False
    
    # TTS control signals
    startPlayback = pyqtSignal()
    stopPlayback = pyqtSignal()
    setSpeechGenerator = pyqtSignal(object)
    noMoreSpeech = pyqtSignal()
    
    # TTS setting signals
    changeVolume = pyqtSignal(int)
    changeRate = pyqtSignal(int)
    changePauseLength = pyqtSignal(int)
    changeVoice = pyqtSignal(str)
    
    # Program update notification
    notifyProgramUpdate = pyqtSignal()
    programUpdateFinish = pyqtSignal()
    
    # Mutex so that only one document is added at a time
    documentAddMutex = QMutex()
    
    def __init__(self, app, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.app = app
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Clear all of the tabs in my document tab widget
        self.ui.documentTabWidget.clear()
        
        # If the mainMenuButton exists, I have to hide the main menu bar and
        # shove all of its actions onto the mainMenuButton
        menu = QtGui.QMenu()
        menu.addActions(self.menuBar().actions())
        self.ui.mainMenuButton.setMenu(menu)
        self.menuBar().hide()
            
        # For the play button, set a custom property on it so that I can style
        # its state change (from play to stop)
        self.ui.playButton.setProperty('isPlaying', False)
        
        # Add the MP3 menu items to the MP3 button
        menu = QtGui.QMenu()
        menu.addAction('Save All', self.saveMP3All)
        menu.addAction('Save Selection', self.saveMP3Selection)
        menu.addAction('Save By Page', self.saveMP3ByPage)
        self.ui.saveToMP3Button.setMenu(menu)
        
        # Set the path for the web cache to save at temp
        QWebSettings.setOfflineStoragePath(misc.temp_path('storageCache'))
        QWebSettings.setOfflineWebApplicationCachePath(misc.temp_path('webAppCache'))
        QWebSettings.globalSettings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        QWebSettings.globalSettings().setAttribute(QWebSettings.LocalContentCanAccessFileUrls, True)
        QWebSettings.globalSettings().setAttribute(QWebSettings.LocalStorageEnabled, True)
        QWebSettings.globalSettings().setAttribute(QWebSettings.AutoLoadImages, True)
        QWebSettings.globalSettings().setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)
        
        # Connect all of my signals
        self.connect_signals()
        
        # This is the tree model used to store our bookmarks
        self.bookmarksModel = BookmarksTreeModel(BookmarkNode(None, 'Something'))
        self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
        
        # Set up my speech driver and start it
        self.speechThread = SpeechWorker()
        
        self.speechThread.onStart.connect(self.onStart)
        self.speechThread.onWord.connect(self.onWord)
        self.speechThread.onEndStream.connect(self.onEndStream)
        self.speechThread.onFinish.connect(self.onSpeechFinished)
        self.speechThread.requestMoreSpeech.connect(self.sendMoreSpeech)
        
        self.startPlayback.connect(self.speechThread.startPlayback)
        self.stopPlayback.connect(self.speechThread.stopPlayback)
        self.setSpeechGenerator.connect(self.speechThread.setSpeechGenerator)
        self.noMoreSpeech.connect(self.speechThread.noMoreSpeech)
        self.changeVolume.connect(self.speechThread.setVolume)
        self.changeRate.connect(self.speechThread.setRate)
        self.changePauseLength.connect(self.speechThread.setPauseLength)
        self.changeVoice.connect(self.speechThread.setVoice)
                
        self.speechThread.start()
                
        # Create the general-purpose progress dialog
        self.progressDialog = QtGui.QProgressDialog('Stuff', 'Cancel', 0, 100, self)
        
        # Check to see if I have a voice. If I don't, grab the first one from
        # the TTS driver
        if len(configuration.getValue('Voice', '')) == 0:
            voiceList = self.speechThread.getVoiceList()
            if len(voiceList) > 0:
                configuration.setValue('Voice', voiceList[0][1])
        
        # Check if my voice exists. If it doesn't, then replace it with the
        # first voice available
        voiceList = self.speechThread.getVoiceList()
        voiceAvailable = False
        for v in voiceList:
            if configuration.getValue('Voice') == v[1]:
                voiceAvailable = True
                break
        if not voiceAvailable:
            if len(voiceList) > 0:
                configuration.setValue('Voice', voiceList[0][1])
        
        self.updateSettings()
        
        # Add the landing page
        doc = LandingPageDocument('', None, None)
        self.addDocument(doc, silent=True, icon=None, hasCommands=True)
        
        # Show the tutorial if the user hasn't seen it yet
        if configuration.getBool('ShowTutorial', True):
            self.openTutorial()
            
            # Immediately turn the switch off
            configuration.setBool('ShowTutorial', False)
            self.updateSettings()
        
        # Hide the download update progress widget
        self.ui.updateDownloadProgress.hide()
        
        # Program updater threads and dialogs
        self.programUpdateFinish.connect(self.finishUpdateDownload)
        
        # Hide the rate slider
        self.ui.rateSlider.hide()
        
        # Run an update check thread
        self.checkUpdateThread = GetUpdateThread()
        self.checkUpdateThread.showUpdate.connect(self.showUpdatePrompt)
        QTimer.singleShot(5000, self.checkUpdateThread.start)
         
        # Run the announcement pull thread after a certain amount of time
        self.announcementPullThread = AnnouncementPullThread()
        self.announcementPullThread.gotAnnouncement.connect(self.showAnnouncement)
        QTimer.singleShot(10000, self.announcementPullThread.start)
    
    def showEvent(self, event):
        # Set the size for the splitter so that the navigation tab widget takes up the least space
        self.toggleNavigationPane(True)
            
    def closeEvent(self, event):
        # Save the configuration before close
        print 'Saving before close...'
        configuration.save(misc.app_data_path('configuration.xml'))
        
        self.speechThread.quit()
        
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            if len(e.mimeData().urls()) > 0:
                url = unicode(e.mimeData().urls()[0].toLocalFile())
                ext = os.path.splitext(url)[1]
                if ext == '.docx' or ext == '.doc':
                    e.setDropAction(Qt.CopyAction)
                    e.accept()
                else:
                    e.ignore()
        else:
            e.ignore()
            
    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            if len(e.mimeData().urls()) > 0:
                url = unicode(e.mimeData().urls()[0].toLocalFile())
                ext = os.path.splitext(url)[1]
                if ext == '.docx' or ext == '.doc':
                    e.setDropAction(Qt.CopyAction)
                    e.accept()
                else:
                    e.ignore()
        else:
            e.ignore()
            
    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            if len(e.mimeData().urls()) > 0:
                e.setDropAction(Qt.CopyAction)
                e.accept()
                url = unicode(e.mimeData().urls()[0].toLocalFile())
                if os.path.splitext(url)[1] == '.docx':
                    self.activateWindow()
                    self.raise_()
                    self.openDocument(url)
                elif os.path.splitext(url)[1] == '.doc':
                    self.showDocNotSupported()
        
    def quit(self):
        self.close()
        
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        # Toolbar buttons
        self.ui.openDocumentButton.clicked.connect(self.showOpenDocumentDialog)
        
        self.ui.playButton.clicked.connect(self.toggleSpeech)
        self.ui.colorSettingsButton.clicked.connect(self.showColorSettings)
        self.ui.speechSettingsButton.clicked.connect(self.showSpeechSettings)
        self.ui.zoomInButton.clicked.connect(self.zoomIn)
        self.ui.zoomOutButton.clicked.connect(self.zoomOut)
        self.ui.zoomResetButton.clicked.connect(self.zoomReset)
        
        self.ui.splitterButton.toggled.connect(self.toggleNavigationPane)
        self.ui.splitter.splitterMoved.connect(self.toggleSplitterButton)
        
        # Document tabs
        self.ui.documentTabWidget.tabCloseRequested.connect(self.closeDocumentTab)
        self.ui.documentTabWidget.currentChanged.connect(self.currentDocumentChanged)
        
        # Main Menu
        
        # File
        self.ui.actionOpen_Docx.triggered.connect(self.showOpenDocumentDialog)
        self.ui.actionClose_Document.triggered.connect(self.closeCurrentDocument)
        self.ui.actionPaste_From_Clipboard.triggered.connect(self.pasteFromClipboard)
        self.ui.actionExport_to_HTML.triggered.connect(self.exportToHTML)
        self.ui.actionBatch.triggered.connect(self.showBatch)
        self.ui.actionQuit.triggered.connect(self.quit)
        
        # Functions
        self.ui.actionPlay.triggered.connect(self.playSpeech)
        self.ui.actionStop.triggered.connect(self.stopSpeech)
        self.ui.actionZoom_In.triggered.connect(self.zoomIn)
        self.ui.actionZoom_Out.triggered.connect(self.zoomOut)
        self.ui.actionReset_Zoom.triggered.connect(self.zoomReset)
        self.ui.actionSearch.triggered.connect(self.toggleSearchBar)
        
        # MP3
        self.ui.actionSave_All_to_MP3.triggered.connect(self.saveMP3All)
        self.ui.actionSave_Selection_to_MP3.triggered.connect(self.saveMP3Selection)
        self.ui.actionBy_Page.triggered.connect(self.saveMP3ByPage)
        
        # Settings
        self.ui.actionHighlights_Colors_and_Fonts.triggered.connect(self.showColorSettings)
        self.ui.actionSpeech.triggered.connect(self.showSpeechSettings)
        
        # MathML
        self.ui.actionOpen_Pattern_Editor.triggered.connect(self.openPatternEditor)
        self.ui.actionShow_All_MathML.triggered.connect(self.showAllMathML)
        
        # Help
        self.ui.actionTutorial.triggered.connect(self.openTutorial)
        self.ui.actionAbout.triggered.connect(self.openAboutDialog)
        self.ui.actionAnnouncements.triggered.connect(self.showAnnouncementWithoutDoc)
        self.ui.actionReport_a_Bug.triggered.connect(self.openReportBugWindow)
        self.ui.actionTake_A_Survey.triggered.connect(self.openSurveyWindow)
        
        # Sliders
        self.ui.rateSliderButton.toggled.connect(self.showRateSlider)
        self.ui.rateSlider.valueChanged.connect(self.changeSpeechRate)
        
        self.ui.actionIncrease_Volume.triggered.connect(self.increaseVolume)
        self.ui.actionDecrease_Volume.triggered.connect(self.decreaseVolume)
        
        self.ui.actionIncrease_Rate.triggered.connect(self.increaseRate)
        self.ui.actionDecrease_Rate.triggered.connect(self.decreaseRate)
        
        # Bookmark and page controls and widgets
        self.ui.bookmarksTreeView.clicked.connect(self.bookmarksTree_clicked)
        self.ui.pagesTreeView.clicked.connect(self.pagesTree_clicked)
        self.ui.bookmarkZoomInButton.clicked.connect(self.bookmarkZoomInButton_clicked)
        self.ui.bookmarkZoomOutButton.clicked.connect(self.bookmarkZoomOutButton_clicked)
        
    def updateSettings(self):
        
        # Change the rate on the slider
        self.ui.rateSlider.setValue(configuration.getInt('Rate', 50))
        
        # Update speech thread with my stuff
        self.changeVolume.emit(configuration.getInt('Volume', 100))
        self.changeRate.emit(configuration.getInt('Rate', 50))
        self.changePauseLength.emit(configuration.getInt('PauseLength', 0))
        self.changeVoice.emit(configuration.getValue('Voice'))
        
        # Zoom settings
        currentFont = self.ui.bookmarksTreeView.font()
        currentFont.setPointSize(int(configuration.getValue('NavigationFontSize', '14')))
        self.ui.bookmarksTreeView.setFont(currentFont)
        self.ui.pagesTreeView.setFont(currentFont)
        
        # Write out the CSS that styles all of the documents
        with open(misc.temp_path('import/defaultStyle.css'), 'w') as f:
            f.write(configuration.getCSS())
    
    def updateNavigationBar(self, headingId, pageId):
        '''
        Sets the highlight of the tree view to the heading and page string
        provided.
        '''
        #print 'New selection to:', headingId, pageId
        myHeading = unicode(headingId)
        myPage = unicode(pageId)
        
        if len(myHeading) > 0:
            myIndex = self.bookmarksModel.getIndexFromId(myHeading)
            if myIndex is not None:
                self.ui.bookmarksTreeView.setCurrentIndex(myIndex)
        
        if len(myPage) > 0:
            myIndex = self.pagesModel.getIndexFromId(myPage)
            if myIndex is not None:
                self.ui.pagesTreeView.setCurrentIndex(myIndex)
            
            
    def playSpeech(self):
        # Stop whatever the speech thread may be saying
        self.stopPlayback.emit()
        
        # Wait for the TTS to stop
        while self.speechThread.isPlaying():
            pass
        
        if self.currentDocument() is not None:
            
            # Disable all controls and settings except for playback
            self.setSettingsEnableState(False)
            
            # Set the beginning of the streamer
            dom = self.currentDocumentWidget().setStreamBeginning()
            
            # Set the speech generator and start playback
            self.setSpeechGenerator.emit(self.currentDocument().generateSpeech(dom))
            self.startPlayback.emit()
            
            self.currentDocumentWidget().setContentFocus()
    
    def stopSpeech(self):
        self.stopPlayback.emit()
        
        # Wait for the TTS to stop
        while self.speechThread.isPlaying():
            pass
        
        self.setSettingsEnableState(True)
        if self.currentDocumentWidget() is not None:
            self.currentDocumentWidget().setContentFocus()
        
    def toggleSpeech(self):
        '''
        Toggles the state of speech playback
        '''
        if self.speechThread.isPlaying():
            self.stopSpeech()
        else:
            self.playSpeech()
    
    def onStart(self, offset, length, label, stream, word):
        self.currentDocumentWidget().onStart(offset, length, label, stream, word)
        
    def onWord(self, offset, length, label, stream, word, isFirst):
        self.currentDocumentWidget().onWord(offset, length, label, stream, word, isFirst)
        
    def onEndStream(self, stream, label):
        self.currentDocumentWidget().onEndStream(stream, label)
        
    def onSpeechFinished(self):
        self.currentDocumentWidget().onSpeechFinished()
        self.setSettingsEnableState(True)
        
    def sendMoreSpeech(self):
        '''
        This is response from requestMoreSpeech from the SpeechWorker thread.
        It will either get more speech for the TTS and send it, or tell it that
        no more speech is available.
        '''
        if self.currentDocumentWidget().hasMoreSpeech():
            self.setSpeechGenerator.emit(self.currentDocument().generateSpeech(self.currentDocumentWidget().streamNextElement()))
            
        else:
            self.noMoreSpeech.emit()
    
    def showRateSlider(self, isOn):
        '''
        Shows a popup slider for the speech rate.
        '''
        self.ui.rateSlider.setVisible(isOn)        
            
    def changeSpeechRate(self, value):
        configuration.setInt('Rate', value)
        self.changeRate.emit(configuration.getInt('Rate'))
        
    def increaseRate(self):
        myRate = configuration.getInt('Rate')
        myRate += 10
        if myRate > 100:
            myRate = 100
        configuration.setInt('Rate', myRate)
        self.changeRate.emit(myRate)
    
    def decreaseRate(self):
        myRate = configuration.getInt('Rate')
        myRate -= 10
        if myRate < 0:
            myRate = 0
        configuration.setInt('Rate', myRate)
        self.changeRate.emit(myRate)

    def changeSpeechVolume(self, value):
        configuration.setInt('Volume', value)
        self.changeVolume.emit(configuration.getInt('Volume'))
    
    def increaseVolume(self):
        myVolume = configuration.getInt('Volume')
        myVolume += 10
        if myVolume > 100:
            myVolume = 100
        self.changeSpeechVolume(myVolume)
    
    def decreaseVolume(self):
        myVolume = configuration.getInt('Volume')
        myVolume -= 10
        if myVolume < 0:
            myVolume = 0
        self.changeSpeechVolume(myVolume)
        
    def saveMP3All(self):
        if self.currentDocumentWidget() is not None:
            self.currentDocumentWidget().saveMP3All()
        
    def saveMP3Selection(self):
        if self.currentDocumentWidget() is not None:
            self.currentDocumentWidget().saveMP3Selection()
    
    def saveMP3ByPage(self):
        if self.currentDocument() is not None:
            self.currentDocumentWidget().saveMP3ByPage()
        
    def showColorSettings(self):
        from src.gui.color_settings import ColorSettings
        dialog = ColorSettings(self)
        result = dialog.exec_()
        
        # Show a message asking the user to restart the system if they have
        # changed the layout
        if (result & ColorSettings.RESULT_NEED_RESTART) > 0:
            messageBox = QtGui.QMessageBox()
            messageBox.setText('Your layout changes will take effect after restarting the Central Access Reader.')
            messageBox.setStandardButtons(QtGui.QMessageBox.Ok)
            messageBox.setDefaultButton(QtGui.QMessageBox.Ok)
            messageBox.setWindowTitle('Restart CAR to Apply Layout Changes')
            messageBox.setIcon(QtGui.QMessageBox.Information)
            messageBox.exec_()
        
        if (result & ColorSettings.RESULT_NEED_REFRESH) > 0:
            self.refreshDocument()
        
        # Set the theme
        loader.load_theme(qApp, configuration.getValue('Theme'))
        self.updateSettings()
        if self.currentDocumentWidget() is not None:
            self.currentDocumentWidget().setContentFocus()
        
    def showSpeechSettings(self):

        # Disconnect my highlighter signals
        self.speechThread.onStart.disconnect(self.onStart)
        self.speechThread.onWord.disconnect(self.onWord)
        self.speechThread.onEndStream.disconnect(self.onEndStream)
        self.speechThread.onFinish.disconnect(self.onSpeechFinished)
        self.speechThread.requestMoreSpeech.disconnect(self.sendMoreSpeech)

        # Show speech settings dialog
        from src.gui.speech_settings import SpeechSettings
        dialog = SpeechSettings(self)
        self.speechThread.requestMoreSpeech.connect(dialog.requestMoreSpeech)
        self.stopPlayback.emit()
        self.speechThread.requestMoreSpeech.disconnect(dialog.requestMoreSpeech)
        dialog.exec_()
        
        # Reload settings
        #configuration.loadFromFile(misc.app_data_path('configuration.xml')) 
        self.updateSettings()

        # Reconnect my highlighter signals
        self.speechThread.onStart.connect(self.onStart)
        self.speechThread.onWord.connect(self.onWord)
        self.speechThread.onEndStream.connect(self.onEndStream)
        self.speechThread.onFinish.connect(self.onSpeechFinished)
        self.speechThread.requestMoreSpeech.connect(self.sendMoreSpeech)
        
        # Set the keyboard focus to the current document
        if self.currentDocumentWidget() is not None:
            self.currentDocumentWidget().setContentFocus()
                    
    def exportToHTML(self):
        '''
        Exports the current document to a MathPage-like web document that can
        be opened in the web browser.
        '''
        if self.currentDocumentWidget() is not None:
            self.currentDocumentWidget().saveToHTML()
    
    def showBatch(self):
        '''
        Shows the batch conversion window.
        '''
        self.batchWindow = ExportBatchDialog()
        self.batchWindow.show()
                
    def zoomIn(self):
        if self.currentDocumentWidget() is not None:
            configuration.setInt('Zoom', self.currentDocumentWidget().zoomIn(), 1)
            self.currentDocumentWidget().setContentFocus()
    
    def zoomOut(self):
        if self.currentDocumentWidget() is not None:
            configuration.setInt('Zoom', self.currentDocumentWidget().zoomOut(), 1)
            self.currentDocumentWidget().setContentFocus()
        
    def zoomReset(self):
        if self.currentDocumentWidget() is not None:
            configuration.setInt('Zoom', self.currentDocumentWidget().zoomReset(), 1)
            self.currentDocumentWidget().setContentFocus()
        
    def addDocument(self, doc, silent=False, icon=None, hasCommands=False):
        '''
        Adds the document to the tabs correctly.
        '''
        #self.documentAddMutex.lock()
        
        if self.ui.documentTabWidget.count() == 1:
            if isinstance(self.currentDocument(), LandingPageDocument):
                self.ui.documentTabWidget.removeTab(0)
        
        name = doc.getName()
        widget = DocumentWidget()
        if not silent:
            widget.loadProgress.connect(self.reportDocumentProgress)
            widget.loadFinished.connect(self.progressDialog.close)
            self.progressDialog.closeEvent = self._unlockAddDocumentMutex
        widget.toggleSpeechPlayback.connect(self.toggleSpeech)
        widget.requestPaste.connect(self.pasteFromClipboard)
        widget.requestReadFromSelection.connect(self.toggleSpeech)
        widget.requestUpdateNavigation.connect(self.updateNavigationBar)
        widget.setZoom(configuration.getInt('Zoom', 1))
        widget.setDocument(doc)
        
        if hasCommands:
            widget.contentCommand.connect(self.documentContentCommand)
        
        if icon is not None:
            self.ui.documentTabWidget.addTab(widget, icon, name)
        else:
            self.ui.documentTabWidget.addTab(widget, name)
        
        if silent:
            pass
            #self.documentAddMutex.unlock()
    
    def _unlockAddDocumentMutex(self, event):
        pass
        #self.documentAddMutex.unlock()

    def openDocument(self, filePath):
        '''
        Opens a file. It will spawn a progress bar and run the task in the
        background to prevent GUI from freezing up.
        '''
        filePath = str(filePath)
        if len(filePath) > 0:
            
            from src.document.loader import DocumentLoadingThread
             
            # Create my importer thread
            self.documentLoadingThread = DocumentLoadingThread(filePath)
            self.documentLoadingThread.progress.connect(self.reportDocumentProgress)
            self.documentLoadingThread.error.connect(self.reportErrorOpenDocument)
            self.documentLoadingThread.finished.connect(self.finishOpenDocument)
            
            # Show a progress dialog
            self.progressDialog = DocumentLoadProgressDialog()
            self.progressDialog.setLabelText('Reading ' + os.path.basename(str(filePath)) + '...')
            self.progressDialog.setProgress(0)
            self.progressDialog.canceled.connect(self.documentLoadingThread.stop)
            self.progressDialog.show()
           
            self.documentLoadingThread.start()
        
    def reportDocumentProgress(self, percent, text):
        self.progressDialog.setProgress(percent - 1)
        self.progressDialog.setLabelText(text)
        
    def reportErrorOpenDocument(self, exception, tb):
        pass
        
    def finishOpenDocument(self):
        
        if self.documentLoadingThread.isSuccess():
            doc = self.documentLoadingThread.getDocument()
            self.addDocument(doc)
            
            # Set the current tab to the last tab
            self.ui.documentTabWidget.setCurrentIndex(self.ui.documentTabWidget.count() - 1)
            self.currentDocumentWidget().setContentFocus()
            
            # NOTE: The progress bar will still be up to allow the page to load
            # and for MathJax to finish typesetting.
        
        else:
            self.progressDialog.close()
            del self.progressDialog
        
    def showOpenDocumentDialog(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self, 'Open Document...',os.path.join(os.path.expanduser('~'), 'Documents'),'(*.docx)')
        self.openDocument(filePath)
        
    def showDocNotSupported(self):
        result = QtGui.QMessageBox.information(self, 'CAR does not support 1997-2003 Word document', 
                                               'Sorry, this is a 1997-2003 Word document that CAR doesn\'t support. Open it in Microsoft Word 2007 or later and save it as "Word Document" (.docx)' 
                                               )
        
    def openTutorial(self):
        self.openDocument(misc.program_path('Tutorial.docx'))
    
    def pasteFromClipboard(self):
        '''
        Adds a document containing the contents of the clipboard.
        '''
        from src.document.loader import DocumentLoadingThread
             
        # Create my importer thread
        self.documentLoadingThread = DocumentLoadingThread('', isClipboard=True)
        self.documentLoadingThread.progress.connect(self.reportDocumentProgress)
        self.documentLoadingThread.error.connect(self.reportErrorOpenDocument)
        self.documentLoadingThread.finished.connect(self.finishOpenDocument)
        
        # Show a progress dialog
        self.progressDialog = DocumentLoadProgressDialog()
        self.progressDialog.setLabelText('Reading...')
        self.progressDialog.setProgress(0)
        self.progressDialog.canceled.connect(self.documentLoadingThread.stop)
        self.progressDialog.show()
       
        self.documentLoadingThread.start()
        
    def closeDocumentTab(self, index):
        '''
        Closes the document in response to a tab close button being pressed.
        '''
        self.stopSpeech()
        
        if not isinstance(self.currentDocument(), LandingPageDocument):   
            
            # Disconnect all signals associated with this widget
            myWidget = self.ui.documentTabWidget.widget(index)
            myWidget.disconnectSignals()            
                     
            self.ui.documentTabWidget.removeTab(index)
            
            if self.ui.documentTabWidget.count() == 0:
                doc = LandingPageDocument('', None, None)
                self.addDocument(doc, silent=True, icon=None, hasCommands=True)
        
    def closeCurrentDocument(self):
        '''
        Closes the current document in focus.
        '''
        self.stopSpeech()
        
        if not isinstance(self.currentDocument(), LandingPageDocument):
            self.ui.documentTabWidget.removeTab(self.ui.documentTabWidget.currentIndex())
            
            if self.ui.documentTabWidget.count() == 0:
                doc = LandingPageDocument('', None, None)
                self.addDocument(doc, silent=True, icon=None, hasCommands=True)
        
    def currentDocumentWidget(self):
        '''
        Returns the current document widget in view.
        '''
        return self.ui.documentTabWidget.currentWidget()
    
    def currentDocument(self):
        '''
        Returns the Document object of the current document widget in view.
        '''
        if self.currentDocumentWidget() is not None:
            return self.currentDocumentWidget().document
        else:
            return None
        
    def currentDocumentChanged(self, index):
        '''
        Alerts when the current document in focus changes because of clicking
        on a different tab.
        '''
        if index >= 0:
            doc = self.ui.documentTabWidget.widget(index).document
            
            # Load the bookmarks
            self.bookmarksModel = BookmarksTreeModel(doc.getHeadings())
            self.ui.bookmarksTreeView.setModel(self.bookmarksModel)
            self.ui.bookmarksTreeView.expandAll()
            
            # Load the pages
            self.pagesModel = PagesTreeModel(doc.getPages())
            self.ui.pagesTreeView.setModel(self.pagesModel)
            self.ui.pagesTreeView.expandAll()
            
        else:
            self.ui.bookmarksTreeView.setModel(None)
            self.ui.pagesTreeView.setModel(None)
            
    def documentContentCommand(self, commandString):
        '''
        For some types of documents, like the document for the update prompt, it
        can issue a command string that can issue a function.
        '''
        
        if 'openDocument' == commandString:
            self.showOpenDocumentDialog()
        
        elif 'disableQuickStart' == commandString:
            print 'Disabling Quick Start!'
        
        elif 'updateDownloadYes' == commandString:
            # Show the update download progress widget
            self.ui.updateDownloadProgress.setUrl(SETUP_FILE)
            self.ui.updateDownloadProgress.setDestination(SETUP_TEMP_FILE)
        
            self.ui.updateDownloadProgress.downloadFinished.connect(self.finishUpdateDownload)
        
            self.ui.updateDownloadProgress.show()
            self.ui.updateDownloadProgress.startDownload()
            
            # Close all UpdatePromptDocuments
            i = 0
            while i < self.ui.documentTabWidget.count():
                self.ui.documentTabWidget.count()
                if isinstance(self.ui.documentTabWidget.widget(i).document, UpdatePromptDocument):
                    self.ui.documentTabWidget.removeTab(i)
                    i = 0
                else:
                    i += 1
            
        elif 'updateDownloadNo' == commandString:
            # Close all UpdatePromptDocuments
            i = 0
            while i < self.ui.documentTabWidget.count():
                self.ui.documentTabWidget.count()
                if isinstance(self.ui.documentTabWidget.widget(i).document, UpdatePromptDocument):
                    self.ui.documentTabWidget.removeTab(i)
                    i = 0
                else:
                    i += 1
        
        elif 'updateInstallYes' == commandString:
            # Close all UpdatePromptDocuments
            i = 0
            while i < self.ui.documentTabWidget.count():
                self.ui.documentTabWidget.count()
                if isinstance(self.ui.documentTabWidget.widget(i).document, UpdatePromptDocument):
                    self.ui.documentTabWidget.removeTab(i)
                    i = 0
                else:
                    i += 1
            
            # Run the installer
            run_update_installer()
            self.close()
                    
        elif 'updateInstallNo' == commandString:
            # Close all UpdatePromptDocuments
            i = 0
            while i < self.ui.documentTabWidget.count():
                self.ui.documentTabWidget.count()
                if isinstance(self.ui.documentTabWidget.widget(i).document, UpdatePromptDocument):
                    self.ui.documentTabWidget.removeTab(i)
                    i = 0
                else:
                    i += 1
            
    def openAboutDialog(self):
        from src.gui.about import AboutDialog
        dialog = AboutDialog()
        dialog.exec_()
        
    def openReportBugWindow(self):
        import webbrowser
        webbrowser.open_new(misc.REPORT_BUG_URL)
        
    def openSurveyWindow(self):
        import webbrowser
        webbrowser.open_new(misc.SURVEY_URL)
    
    def openPatternEditor(self):
        self.patternEditor = MathLibraryDev()
        self.patternEditor.show()
    
    def showAllMathML(self):
        from src.gui.mathmlcodes_dialog import MathMLCodesDialog
        self.mathmlDialog = MathMLCodesDialog(self.currentDocument()._maths)
        self.mathmlDialog.show()
        
    def bookmarksTree_clicked(self, index):
        node = index.internalPointer()
        self.currentDocumentWidget().gotoAnchor(node.anchorId)
        
    def pagesTree_clicked(self, index):
        node = index.internalPointer()
        self.currentDocumentWidget().gotoPage(node.anchorId)
        
    def bookmarkZoomInButton_clicked(self):
        # Get the current font
        currentFont = self.ui.bookmarksTreeView.font()
        
        # Make it a litter bigger
        myPointSize = int(configuration.getValue('NavigationFontSize', '14'))
        myPointSize += 2
        currentFont.setPointSize(myPointSize)
        configuration.setValue('NavigationFontSize', str(myPointSize))
        
        # Set the font
        self.ui.bookmarksTreeView.setFont(currentFont)
        self.ui.pagesTreeView.setFont(currentFont)
        
    def bookmarkZoomOutButton_clicked(self):
        # Get the current font
        currentFont = self.ui.bookmarksTreeView.font()
        
        # Make it a litter smaller
        myPointSize = int(configuration.getValue('NavigationFontSize', '14'))
        myPointSize -= 2
        if myPointSize < 4:
            myPointSize = 4
        currentFont.setPointSize(myPointSize)
        configuration.setValue('NavigationFontSize', str(myPointSize))
        
        # Set the font
        self.ui.bookmarksTreeView.setFont(currentFont)
        self.ui.pagesTreeView.setFont(currentFont)
        
    def expandBookmarksButton_clicked(self):
        self.ui.bookmarksTreeView.expandAll()
        
    def collapseBookmarksButton_clicked(self):
        self.ui.bookmarksTreeView.collapseAll()
        
    def toggleNavigationPane(self, isOn):
        
        # Make the tab widget on the left side disappear if in, appear if out
        if isOn:
            # Reveal
            sizes = self.ui.splitter.sizes()
            sizes[0] = self.ui.navigationTabWidget.minimumSizeHint().width()
            self.ui.splitter.setSizes(sizes)
        
        else:
            # Hide
            sizes = self.ui.splitter.sizes()
            sizes[1] += sizes[0]
            sizes[0] = 0
            self.ui.splitter.setSizes(sizes)
            
    def toggleSplitterButton(self, pos, index):
        '''
        Toggles the splitter button, if it exists, based on whether the side
        holding the navigation pane is visible or not.
        '''
        try:
            self.ui.splitterButton.blockSignals(True)
            if index == 1 and pos == 0:
                self.ui.splitterButton.setChecked(False)
            else:
                self.ui.splitterButton.setChecked(True)
            self.ui.splitterButton.blockSignals(False)
        except Exception:
            pass
        
    def refreshDocument(self):
        print 'Trying to refresh the document...'        
        for i in range(self.ui.documentTabWidget.count()):
            self.ui.documentTabWidget.widget(i).refreshDocument()
            
    def showUpdatePrompt(self):
        '''
        Shows the update prompt when there is one as a new tab.
        '''
        doc = UpdatePromptDocument('', None, None, hasDownloaded=is_update_downloaded())
        self.addDocument(doc, silent=True, icon=QtGui.QIcon(':/classic/icons/update_classic.png'), hasCommands=True)
            
    def finishUpdateDownload(self, success):
        '''
        Does the cleanup logic for downloading an update.
        '''
        # Close all UpdatePromptDocuments
        i = 0
        while i < self.ui.documentTabWidget.count():
            self.ui.documentTabWidget.count()
            if isinstance(self.ui.documentTabWidget.widget(i).document, UpdatePromptDocument):
                self.ui.documentTabWidget.removeTab(i)
                i = 0
            else:
                i += 1
        
        self.ui.updateDownloadProgress.hide()
        if success:
            # Save the version from over there to here
            versionInfo = save_server_version_to_temp()
            
            # Prompt the user if they want to install it
            if len(versionInfo) > 0:
                self.showUpdatePrompt()
    
    def showAnnouncement(self, doc):
        '''
        Shows the announcement, given in the provided document.
        '''
        self.addDocument(doc, silent=True)
            
    def showAnnouncementWithoutDoc(self):
        '''
        Shows the announcements without having the Document prepared. This is
        for the Announcments menu item.
        '''
        doc = RSSDocument('', None, None, rssUrl=ANNOUNCEMENT_RSS_URL, title='Announcements')
        self.addDocument(doc)
            
    def setSettingsEnableState(self, isEnable):
        '''
        Disables or enables the other widgets that shouldn't be active during
        TTS playback.
        '''
        # Set the icon for the play button by changing a property and resetting
        # its style
        self.ui.playButton.setProperty('isPlaying', not isEnable)
        self.ui.playButton.setStyle(qApp.style())
        if isEnable:
            self.ui.playButton.setToolTip('Start')
        else:
            self.ui.playButton.setToolTip('Stop')
        
        if not isEnable:
            
            # Disable all other document tabs except the current tab
            for i in range(self.ui.documentTabWidget.count()):
                if i != self.ui.documentTabWidget.currentIndex():
                    self.ui.documentTabWidget.setTabEnabled(i, False)
                    
            if hasattr(self.ui, 'openDocumentButton'):
                self.ui.openDocumentButton.setEnabled(False)
                
            self.ui.colorSettingsButton.setEnabled(False)
            self.ui.speechSettingsButton.setEnabled(False)
            self.ui.saveToMP3Button.setEnabled(False)
            
            # Disable certain sliders and actions if TTS is not interactive
            if not self.speechThread.areSettingsInteractive():
                self.ui.rateSlider.setEnabled(False)
                self.ui.actionDecrease_Rate.setEnabled(False)
                self.ui.actionIncrease_Rate.setEnabled(False)
                self.ui.actionDecrease_Volume.setEnabled(False)
                self.ui.actionIncrease_Volume.setEnabled(False)
            
            # Actions
            self.ui.actionPlay.setEnabled(False)
            self.ui.actionHighlights_Colors_and_Fonts.setEnabled(False)
            self.ui.actionSpeech.setEnabled(False)
            self.ui.actionSave_All_to_MP3.setEnabled(False)
            self.ui.actionSave_Selection_to_MP3.setEnabled(False)
            self.ui.actionOpen_Docx.setEnabled(False)
            self.ui.actionTutorial.setEnabled(False)
            self.ui.actionSearch.setEnabled(False)
            self.ui.actionEntire_Document.setEnabled(False)
            self.ui.actionCurrent_Selection.setEnabled(False)
            self.ui.actionBy_Page.setEnabled(False)
            self.ui.actionExport_to_HTML.setEnabled(False)
                
            # Cursor
            self.currentDocumentWidget().setKeyboardNavEnabled(False)
            
        else:
            
            # Enable all tabs
            for i in range(self.ui.documentTabWidget.count()):
                self.ui.documentTabWidget.setTabEnabled(i, True)
                
            self.ui.openDocumentButton.setEnabled(True)
            
            self.ui.rateSliderButton.setEnabled(True)
                
            self.ui.colorSettingsButton.setEnabled(True)
            self.ui.speechSettingsButton.setEnabled(True)
            self.ui.saveToMP3Button.setEnabled(True)
            
            # Enable slider bars if TTS is not interactive
            if not self.speechThread.areSettingsInteractive():
                self.ui.rateSlider.setEnabled(True)
            
            # Actions
            self.ui.actionPlay.setEnabled(True)
            self.ui.actionHighlights_Colors_and_Fonts.setEnabled(True)
            self.ui.actionSpeech.setEnabled(True)
            self.ui.actionSave_All_to_MP3.setEnabled(True)
            self.ui.actionSave_Selection_to_MP3.setEnabled(True)
            self.ui.actionOpen_Docx.setEnabled(True)
            self.ui.actionTutorial.setEnabled(True)
            self.ui.actionSearch.setEnabled(True)
            self.ui.actionEntire_Document.setEnabled(True)
            self.ui.actionCurrent_Selection.setEnabled(True)
            self.ui.actionBy_Page.setEnabled(True)
            self.ui.actionExport_to_HTML.setEnabled(True)
            
            # Cursor
            self.currentDocumentWidget().setKeyboardNavEnabled(True)
            
    def toggleSearchBar(self):
        '''
        Toggles the search bar of the current document.
        '''
        self.currentDocumentWidget().toggleSearchBar()
