'''
Created on Dec 17, 2013

@author: Spencer Graffe
'''
import os

from PyQt4.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex, QThread, pyqtSignal
from PyQt4.QtGui import QMainWindow, QStyledItemDelegate, QComboBox, QAbstractItemView, QProgressBar, QPushButton, QFileDialog, QAbstractItemDelegate, QMenu, QAction, qApp
from lxml import html

from car.document.loader import DocumentLoadingThread
from car.export import formats
from car.forms.export_batch_ui import Ui_ExportBatch
from car.headless.renderer import HeadlessRendererThread
from car.threadpool import ThreadPool
from car import misc

class ExportBatchDialog(QMainWindow):
    '''
    Dialog for setting up and converting files to other formats, like MP3 or
    HTML.
    '''

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        
        self.ui = Ui_ExportBatch()
        self.ui.setupUi(self)
        
        self.jobs = JobQueue()
        self.ui.tableView.setModel(self.jobs)
        
        # Set column widths
        self.ui.tableView.setColumnWidth(JobQueue.COL_PROGRESS, 150)
        self.ui.tableView.setColumnWidth(JobQueue.COL_SOURCE, 300)
        self.ui.tableView.setColumnWidth(JobQueue.COL_DEST, 300)
        self.ui.tableView.setColumnWidth(JobQueue.COL_STATUS, 150)
        self.ui.tableView.setColumnWidth(JobQueue.COL_TYPE, 150)
        
        # Set item delegates
        self.progressDelegate = ProgressBarDelegate()
        self.typeDelegate = ComboBoxDelegate()
        self.sourceDelegate = FileChooserSourceDelegate()
        self.destDelegate = FileChooserDestinationDelegate()
        self.ui.tableView.setItemDelegateForColumn(JobQueue.COL_PROGRESS, self.progressDelegate)
        self.ui.tableView.setItemDelegateForColumn(JobQueue.COL_TYPE, self.typeDelegate)
        self.ui.tableView.setItemDelegateForColumn(JobQueue.COL_SOURCE, self.sourceDelegate)
        self.ui.tableView.setItemDelegateForColumn(JobQueue.COL_DEST, self.destDelegate)
        
        # Set event triggers so that I only need to select it once
        self.ui.tableView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        
        # Create the menu to put in the "Set Format" button. This will make
        # setting the output format for all files easy.
        self._formatMenu = QMenu()
        
        # Generate the actions for each of my export options
        myFormats = formats.get()
        for i in range(len(myFormats)):
            newAction = QAction(myFormats[i].description(), self)
            newAction.triggered.connect(self.makeSetFormatCallback(i))
            self._formatMenu.addAction(newAction)
            
        self.ui.setFormatButton.setMenu(self._formatMenu)
        
        # My thread pool
        self.threadPool = ThreadPool(numThreads=1)
        self.threadPool.jobsStarted.connect(self.setControlsDisabled)
        self.threadPool.jobsFinished.connect(self.setControlsEnabled)
        self.threadPool.start()
        
        self.connect_signals()
    
    def closeEvent(self, event):
        self.threadPool.stop()
        
    def connect_signals(self):
        self.ui.addFilesButton.clicked.connect(self.addFiles)
        self.ui.removeFilesButton.clicked.connect(self.removeFiles)
        self.ui.convertButton.clicked.connect(self.runJobs)
        self.ui.showFilesButton.clicked.connect(self.showFiles)
        self.ui.cancelJobsButton.clicked.connect(self.cancelJobs)
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            # Check all of the URLs to make sure that they are all valid
            valid = True
            for u in e.mimeData().urls():
                url = unicode(u.toLocalFile())
                ext = os.path.splitext(url)[1]
                if not ext == '.docx':
                    valid = False
            
            if valid:
                e.setDropAction(Qt.CopyAction)
                e.accept()
            else:
                e.ignore()
        
        else:
            e.ignore()
            
    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            # Check all of the URLs to make sure that they are all valid
            valid = True
            for u in e.mimeData().urls():
                url = unicode(u.toLocalFile())
                ext = os.path.splitext(url)[1]
                if not ext == '.docx':
                    valid = False
            
            if valid:
                e.setDropAction(Qt.CopyAction)
                e.accept()
            else:
                e.ignore()
        
        else:
            e.ignore()
            
    def dropEvent(self, e):
        
        if e.mimeData().hasUrls:
            # Check all of the URLs to make sure that they are all valid
            valid = True
            for u in e.mimeData().urls():
                url = unicode(u.toLocalFile())
                ext = os.path.splitext(url)[1]
                if not ext == '.docx':
                    valid = False
            
            if valid:
                e.setDropAction(Qt.CopyAction)
                e.accept()
                
                for u in e.mimeData().urls():
                    url = unicode(u.toLocalFile())
                    self.jobs.addJob(Job(url, formats.get()[0]))
                
                self.activateWindow()
                
            else:
                e.ignore()
        
        else:
            e.ignore()
    
    def cancelJobs(self):
        self.threadPool.cancelJobs()
    
    def runJobs(self):
        # Do this for all jobs
        for job in self.jobs.getJobs():
            if not job.completed:
                myThread = JobExportThread(job)
                myThread.update.connect(self.jobs.updateJob)
                self.threadPool.addJob(myThread)
    
    def addFiles(self):
        inFiles = QFileDialog.getOpenFileNames(self, caption='Select Files to Convert', directory='', filter='*.docx')
        if len(inFiles) > 0:
            for f in inFiles:
                self.jobs.addJob(Job(unicode(f), formats.get()[0]))
    
    def removeFiles(self):
        '''
        Removes files from queue by using the selected indices.
        '''
        indices = self.ui.tableView.selectedIndexes()
        
        # Group by row number using a dictionary (convert to normal list after)
        rows = {}
        for i in indices:
            rows[i.row()] = 1
        rows = sorted([k for k in rows.keys()])
        
        # Remove the rows/jobs
        while len(rows) > 0:
            self.jobs.removeJob(rows[0])
            rows.pop(0)
            for i in range(len(rows)):
                rows[i] -= 1
                
    def showFiles(self):
        '''
        Shows the files for completed jobs in their own file browsers. Will
        only show files for the jobs that are selected.
        '''
        indices = self.ui.tableView.selectedIndexes()
        
        # Group by row number using a dictionary (convert to normal list after)
        rows = {}
        for i in indices:
            rows[i.row()] = 1
        rows = sorted([k for k in rows.keys()])
        
        # Show the files for each of the jobs (if they are completed)
        for r in rows:
            if self.jobs.getJob(r).completed:
                misc.open_file_browser_to_location(self.jobs.getJob(r).dest)
        
    
    def setFormats(self, exportTypeIndex):
        '''
        Sets the formats of all the currently selected files to the format
        specified by the format index.
        '''
        indices = self.ui.tableView.selectedIndexes()
        
        # Group by row number using a dictionary (convert to normal list after)
        rows = {}
        for i in indices:
            rows[i.row()] = 1
        rows = sorted([k for k in rows.keys()])
        
        # Set the format for each of the jobs
        for r in rows:
            self.jobs.setExportType(r, formats.get()[exportTypeIndex])
        
    def makeSetFormatCallback(self, param):
        return lambda: self.setFormats(param)
    
    def setControlsEnabled(self):
        '''
        Enables controls relevant to adding and modifying jobs.
        '''
        self.ui.addFilesButton.setEnabled(True)
        self.ui.setFormatButton.setEnabled(True)
        self.ui.convertButton.setEnabled(True)
        self.ui.showFilesButton.setEnabled(True)
        self.ui.removeFilesButton.setEnabled(True)
        self.jobs.setEditable(True)
        
    def setControlsDisabled(self):
        '''
        Disables controls relevant to adding and modifying jobs.
        '''
        self.ui.addFilesButton.setEnabled(False)
        self.ui.setFormatButton.setEnabled(False)
        self.ui.convertButton.setEnabled(False)
        self.ui.showFilesButton.setEnabled(False)
        self.ui.removeFilesButton.setEnabled(False)
        self.jobs.setEditable(False)
                
class JobExportThread(QThread):
    
    update = pyqtSignal(object)
    
    def __init__(self, job):
        super(JobExportThread, self).__init__()
        self._job = job
        self._success = False
        self._running = True
        self._canceled = False
    
    def run(self):
        self._job.progress = 0
        self._job.status = 'Starting up...'
        self.update.emit(self._job)
        
        # Load the document
        docLoader = DocumentLoadingThread(self._job.source)
        docLoader.progress.connect(self._updateStatus)
        docLoader.start()
        
        while docLoader.isRunning():
            if not self._running:
                docLoader.stop()
            QThread.yieldCurrentThread()
        
        if self._running:
            if docLoader.isSuccess():
                doc = docLoader.getDocument()
                htmlContent = doc.getMainPage()
                
                # Create my headless webpage renderer
                docRenderer = HeadlessRendererThread(htmlContent)
                docRenderer.progress.connect(self._updateStatus)
                docRenderer.start()
                
                while docRenderer.isRunning():
                    if not self._running:
                        docRenderer.stop()
                    QThread.yieldCurrentThread()
                
                if self._running:
                    
                    # Create my export thread using the export class
                    exportThread = self._job.exportClass(doc, html.fromstring(docRenderer.getRenderedHTML()), doc._tempFolder)
                    exportThread.setFilePath(self._job.dest)
                    exportThread.progress.connect(self._updateStatus)
                    exportThread.start()
                    
                    while exportThread.isRunning():
                        if not self._running:
                            exportThread.stop()
                        QThread.yieldCurrentThread()
                    
                    if exportThread.isSuccess:
                        self._success = True
        
        # Used this so that if my threads are still alive, they can't update it
        # after I set this to False
        self._running = False
        
        if self._success:
            self._job.completed = True
            self._job.status = 'Completed!'
            self._job.progress = 100
            self.update.emit(self._job)
            
        else:
            self._job.completed = False
            if self._canceled:
                self._job.status = 'Canceled'
            else:
                self._job.status = 'Error'
            self._job.progress = 0
            self.update.emit(self._job)
        
    def _updateStatus(self, percentComplete, label):
        # This check is used so that we don't run into race conditions
        if self._running:
            self._job.progress = percentComplete
            self._job.status = label
            self.update.emit(self._job)
        
    def stop(self):
        self._canceled = True
        self._running = False
        

class Job(object):
    '''
    This class contains the fields for a particular job. It also has some
    convenience functions, like setting the default values for some of its
    fields.
    '''
    
    def __init__(self, filePath, exportClass):
        self.source = filePath
        self.exportClass = exportClass
        self.dest = self.exportClass.getDefaultPath(self.source)
        self.status = 'Not started'
        self.progress = 0
        self.completed = False
    
    def setExportClass(self, newExportClass):
        self.exportClass = newExportClass
        self.dest = self.exportClass.getDefaultPath(self.source)
    
    def getExportTypeString(self):
        return self.exportClass.description()

class JobQueue(QAbstractTableModel):
    '''
    This model is used to store all the different jobs for batch processing.
    This will be linked into a table view.
    '''
    COL_SOURCE = 0
    COL_DEST = 1
    COL_TYPE = 2
    COL_STATUS = 3
    COL_PROGRESS = 4
    
    NUM_COLS = 5
    
    def __init__(self):
        QAbstractTableModel.__init__(self)
        self._jobs = []
        self._editable = True
        
    def addJob(self, newJob):
        self.beginInsertRows(QModelIndex(), len(self._jobs), len(self._jobs))
        self._jobs.append(newJob)
        self.endInsertRows()
    
    def removeJob(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        self._jobs.pop(index)
        self.endRemoveRows()
        
    def getJob(self, index):
        return self._jobs[index]
    
    def getJobs(self):
        return iter(self._jobs)
    
    def setEditable(self, isEditable):
        self.beginResetModel()
        self._editable = isEditable
        self.endResetModel()
        
    def setExportType(self, index, exportClass):
        self.beginResetModel()
        self._jobs[index].setExportClass(exportClass)
        self.endResetModel()
    
    def setStatus(self, job, newStatus):
        self.beginResetModel()
        self._jobs[self._jobs.index(job)].status = newStatus
        self.endResetModel()
    
    def setProgress(self, job, newProgress):
        self.beginResetModel()
        self._jobs[self._jobs.index(job)].progress = newProgress
        self.endResetModel()
    
    def setCompleted(self, job):
        self.beginResetModel()
        self._jobs[self._jobs.index(job)].completed = True
        self.endResetModel()
    
    def updateJob(self, job):
        self.beginResetModel()        
        self._jobs[self._jobs.index(job)] = job
        self.endResetModel()
    
    def rowCount(self, parentIndex):
        return len(self._jobs)
    
    def columnCount(self, parentIndex):
        return self.NUM_COLS
    
    def data(self, index, role):
        r = index.row()
        c = index.column()
        
        if role == Qt.DisplayRole:
            if c == self.COL_PROGRESS:
                return self._jobs[r].progress
            elif c == self.COL_SOURCE:
                return self._jobs[r].source
            elif c == self.COL_DEST:
                return self._jobs[r].dest
            elif c == self.COL_STATUS:
                return self._jobs[r].status
            elif c == self.COL_TYPE:
                return self._jobs[r].getExportTypeString()
        
        else:
            return QVariant()
        
    def index(self, row, column, parent=QModelIndex()):
        if len(self._jobs) > 0:
            if row < len(self._jobs):
                return self.createIndex(row, column, self._jobs[row])
        
        return QModelIndex()
    
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return QVariant()
        
        if orientation == Qt.Horizontal:
            if section == self.COL_PROGRESS:
                return 'Progress'
            elif section == self.COL_SOURCE:
                return 'Source'
            elif section == self.COL_DEST:
                return 'Destination'
            elif section == self.COL_STATUS:
                return 'Status'
            elif section == self.COL_TYPE:
                return 'Type'
        else:
            # Return the row number
            return str(section + 1)
        
        return 'Unknown'
    
    def flags(self, index):
        
        myFlags = Qt.ItemIsSelectable | Qt.ItemIsEnabled
        
        if index.column() != self.COL_PROGRESS and index.column() != self.COL_STATUS:
            if self._editable:
                myFlags = myFlags | Qt.ItemIsEditable
        
        return myFlags
    
class FileChooserSourceDelegate(QStyledItemDelegate):
    '''
    This dialog is used to open a file chooser
    '''
    
    def __init__(self):
        QStyledItemDelegate.__init__(self)
        
    def createEditor(self, parent, option, index):
        editor = QPushButton(parent)
        editor.setText(index.internalPointer().source)
        editor.setStyleSheet('padding: 0px 8px; text-align: right;')
        editor.clicked.connect(self._showFileDialog)
        return editor
    
    def setEditorData(self, editor, index):
        self._lastFilePath = index.internalPointer().source
        editor.setText(index.internalPointer().source)
    
    def setModelData(self, editor, model, index):
        model._jobs[index.row()].source = self._lastFilePath
    
    def _showFileDialog(self):
        newPath = QFileDialog.getOpenFileName(caption='Set Source Path')
        if len(newPath) > 0:
            self._lastFilePath = newPath
            self.commitData.emit(self.sender())
            self.closeEditor.emit(self.sender(), QAbstractItemDelegate.NoHint)

class FileChooserDestinationDelegate(QStyledItemDelegate):
    '''
    This dialog is used to open a file chooser
    '''
    
    def __init__(self):
        QStyledItemDelegate.__init__(self)
        
    def createEditor(self, parent, option, index):
        editor = QPushButton(parent)
        editor.setText(index.internalPointer().dest)
        editor.setStyleSheet('padding: 0px 8px; text-align: right;')
        editor.clicked.connect(self._showFileDialog)
        return editor
    
    def setEditorData(self, editor, index):
        self._lastFilePath = index.internalPointer().dest
        editor.setText(index.internalPointer().dest)
    
    def setModelData(self, editor, model, index):
        model._jobs[index.row()].dest = self._lastFilePath
    
    def _showFileDialog(self):
        newPath = QFileDialog.getSaveFileName(caption='Set Destination Path')
        if len(newPath) > 0:
            self._lastFilePath = newPath
            self.commitData.emit(self.sender())
            self.closeEditor.emit(self.sender(), QAbstractItemDelegate.NoHint)

class ComboBoxDelegate(QStyledItemDelegate):
    '''
    This delegate uses a combobox to set the different job options.
    '''
    
    def __init__(self):
        QStyledItemDelegate.__init__(self)
        
    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        
        for exportClass in formats.get():
            editor.addItem(exportClass.description(), userData=exportClass)
        
        return editor
    
    def setEditorData(self, editor, index):
        job = index.internalPointer()
        i = editor.findData(job.exportClass)
        if i < 0:
            i = 0
        editor.setCurrentIndex(i)
    
    def setModelData(self, editor, model, index):
        model._jobs[index.row()].setExportClass(editor.itemData(editor.currentIndex()).toPyObject())
        
class ProgressBarDelegate(QStyledItemDelegate):
    '''
    This delegate shows a progress bar for the item in the list.
    '''
    
    def __init__(self):
        QStyledItemDelegate.__init__(self)
    
    def paint(self, painter, option, index):
        QStyledItemDelegate.paint(self, painter, option, index)
        
        progress = index.internalPointer().progress
        
        renderer = QProgressBar()
        
        renderer.resize(option.rect.size())
        renderer.setMinimum(0)
        renderer.setMaximum(100)
        renderer.setValue(progress)
        renderer.setTextVisible(True)
        
        painter.save()
        painter.translate(option.rect.topLeft())
        renderer.render(painter)
        painter.restore()