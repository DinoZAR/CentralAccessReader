'''
Main window for the screen-reader accessible version of CAR

@author: Spencer Graffe
'''

from enum import Enum
import os

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from lxml import html

from car.document.loader import DocumentLoadingThread
from car.export.mp3 import MP3ExportThread
from car.export.mp3_by_page import MP3ByPageExportThread
from car.export.html_single import HTMLSingleExportThread
from car.forms_accessible.main_window_ui import Ui_MainWindow
from car.gui import configuration
from car.misc import app_data_path, temp_path
from car.speech.worker import SpeechWorker

class ConvertTo(Enum):
    MP3 = 1
    MP3PyPage = 2
    HTML = 3

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Start up my worker thread
        self.speechThread = SpeechWorker()
        self.speechThread.start()

        # Document import thread
        self.documentImportThread = None

        # Export thread
        self.exportThread = None

        self.setSettings()

        self.connect_signals()

    def closeEvent(self, ev):
        configuration.save(app_data_path('configuration.xml'))
        self.speechThread.quit()

    def connect_signals(self):

        # Menu items
        self.ui.actionOpen_Document.triggered.connect(self.openDocument)

        # Sliders
        self.ui.rateSlider.valueChanged.connect(self.setRate)
        self.ui.rateSlider.valueChanged.connect(self.speechThread.setRate)

        self.ui.volumeSlider.valueChanged.connect(self.setVolume)
        self.ui.volumeSlider.valueChanged.connect(self.speechThread.setVolume)

        self.ui.pauseLengthSlider.valueChanged.connect(self.setPauseLength)
        self.ui.pauseLengthSlider.valueChanged.connect(self.speechThread.setPauseLength)

        # Convert To radios
        self.ui.convertMP3Radio.toggled.connect(self.toggleConvertToMP3)
        self.ui.convertMP3ByPageRadio.toggled.connect(self.toggleConvertToMP3ByPage)
        self.ui.convertHTMLRadio.toggled.connect(self.toggleConvertToHTML)

        # Checkboxes
        self.ui.tagImageCheckbox.toggled.connect(self.toggleTagImage)
        self.ui.tagMathCheckbox.toggled.connect(self.toggleTagMath)
        self.ui.ignoreAltTextCheckbox.toggled.connect(self.toggleIgnoreAltText)
        self.ui.addTOCToHTMLCheckbox.toggled.connect(self.toggleAddTOCToHTML)

        # Buttons
        self.ui.openDocumentButton.clicked.connect(self.openDocument)
        self.ui.convertButton.clicked.connect(self.convertDocument)

    def setSettings(self):

        # Set the Convert To target
        self.convertTo = ConvertTo.MP3
        self.setConvertToRadio()

        # Hide the progress indicators
        self.setProgressVisible(False)

        # Set the sliders
        self.ui.rateSlider.setValue(configuration.getInt('Rate', defaultValue=50))
        self.ui.volumeSlider.setValue(configuration.getInt('Volume', defaultValue=100))
        self.ui.pauseLengthSlider.setValue(configuration.getInt('PauseLength', defaultValue=0))

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

        # Create the voice list
        voiceList = self.speechThread.getVoiceList()
        self.ui.voiceCombo.clear()
        for v in voiceList:
            self.ui.voiceCombo.addItem(v[0], userData=v[1])

        if len(configuration.getValue('Voice')) > 0:
            i = self.ui.voiceCombo.findData(unicode(configuration.getValue('Voice')))
            if i < 0:
                i = 0
            self.ui.voiceCombo.setCurrentIndex(i)
        else:
            self.ui.voiceCombo.setCurrentIndex(0)

        # Set the checkboxes
        self.ui.tagImageCheckbox.setChecked(configuration.getBool('TagImage', defaultValue=False))
        self.ui.tagMathCheckbox.setChecked(configuration.getBool('TagMath', defaultValue=False))
        self.ui.ignoreAltTextCheckbox.setChecked(configuration.getBool('IgnoreAltText', defaultValue=False))
        self.ui.addTOCToHTMLCheckbox.setChecked(configuration.getBool('AddTOC', defaultValue=True))

    def setRate(self, value):
        configuration.setInt('Rate', value)

    def setVolume(self, value):
        configuration.setInt('Volume', value)

    def setPauseLength(self, value):
        configuration.setInt('PauseLength', value)

    def setConvertToRadio(self):
        if self.convertTo == ConvertTo.MP3:
            self.ui.convertMP3Radio.setChecked(True)
        elif self.convertTo == ConvertTo.MP3PyPage:
            self.ui.convertMP3ByPageRadio.setChecked(True)
        else:
            self.ui.convertHTMLRadio.setChecked(True)

    def toggleConvertToMP3(self, isChecked):
        if isChecked:
            self.convertTo = ConvertTo.MP3

    def toggleConvertToMP3ByPage(self, isChecked):
        if isChecked:
            self.convertTo = ConvertTo.MP3PyPage

    def toggleConvertToHTML(self, isChecked):
        if isChecked:
            self.convertTo = ConvertTo.HTML

    def toggleTagImage(self, isChecked):
        configuration.setBool('TagImage', isChecked, defaultValue=False)

    def toggleTagMath(self, isChecked):
        configuration.setBool('TagMath', isChecked, defaultValue=False)

    def toggleIgnoreAltText(self, isChecked):
        configuration.setBool('IgnoreAltText', isChecked, defaultValue=False)

    def toggleAddTOCToHTML(self, isChecked):
        configuration.setBool('AddTOC', isChecked, defaultValue=True)

    def openDocument(self):
        filePath = unicode(QFileDialog.getOpenFileName(self, 'Open Document', os.path.expanduser('~/Documents'), 'Word Docs (*.docx)')[0])
        if len(filePath) > 0:
            self.ui.filePathEdit.setText(filePath)

    def convertDocument(self):
        filePath = unicode(self.ui.filePathEdit.text())
        if len(filePath) > 0:
            self.setProgressVisible(True)

            myExporterClass = None
            if self.convertTo == ConvertTo.MP3:
                myExporterClass = MP3ExportThread
            elif self.convertTo == ConvertTo.MP3PyPage:
                myExporterClass = MP3ByPageExportThread
            else:
                myExporterClass = HTMLSingleExportThread

            self.exportThread = ExportThread(filePath, myExporterClass)
            self.exportThread.progress.connect(self._documentLoadProgress)
            self.exportThread.exportDone.connect(self._exportDone)
            self.ui.cancelExportButton.clicked.connect(self.exportThread.cancel)

            self.exportThread.start()

        else:
            QMessageBox.information(self, 'No Document Loaded', 'Load a document first before converting.');

    def setProgressVisible(self, isVisible):
        self.ui.progressBar.setVisible(isVisible)
        self.ui.progressLabel.setVisible(isVisible)
        self.ui.cancelExportButton.setVisible(isVisible)

    def _documentLoadProgress(self, percent, label):
        self.ui.progressBar.setValue(percent)
        self.ui.progressLabel.setText(label)

    def _exportDone(self):
        print 'Export all done!'
        self.setProgressVisible(False)

class ExportThread(QThread):
    '''
    Used to export a document.
    '''

    progress = pyqtSignal(int, unicode)
    exportDone = pyqtSignal()

    def __init__(self, filePath, exporterClass):
        super(ExportThread, self).__init__()

        self._filePath = filePath

        self._documentImportThread = DocumentLoadingThread(filePath)
        self._documentImportThread.progress.connect(self.progress)
        self._documentImportThread.finished.connect(self._startExporter)

        self._exporterClass = exporterClass
        self._exportThread = None

        self._isCancel = False

    def run(self):
        self._documentImportThread.start()

    def cancel(self):
        self._isCancel = True
        self._documentImportThread.stop()

        if self._exportThread is not None:
            self._exportThread.stop()

    def _startExporter(self):

        if not self._isCancel:
            doc = self._documentImportThread.getDocument()
            htmlContent = html.fromstring(doc.getMainPage())
            self._exportThread = self._exporterClass(doc, htmlContent, doc._tempFolder)
            self._exportThread.progress.connect(self.progress)
            self._exportThread.finished.connect(self.exportDone)

            # Set the default file path using the exporter
            filePath = self._exporterClass.getDefaultPath(self._filePath)
            self._exportThread.setFilePath(filePath)

            self._exportThread.start()