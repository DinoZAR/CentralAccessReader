'''
Created on Apr 25, 2013

@author: Spencer Graffe
'''
from PySide import QtGui
from PySide.QtCore import Qt
from lxml import etree
import copy
from misc import app_data_path

from forms.color_settings_ui import Ui_ColorSettings

class ColorSettings(QtGui.QDialog):
    '''
    classdocs
    '''
    
    RESULT_NEED_REFRESH = 2
    
    def __init__(self, mainWindow, parent=None):
        QtGui.QDialog.__init__(self, parent)
        
        self.ui = Ui_ColorSettings()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.mainWindow = mainWindow
        
        self.beforeConfiguration = copy.deepcopy(self.mainWindow.configuration)
        self.configuration = copy.deepcopy(self.mainWindow.configuration)
        
        # Update the GUI to match the settings currently employed
        self.updateSettings()
            
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        # Highlighter
        self.ui.enableHTextCheckBox.clicked.connect(self.enableHTextCheckBox_clicked)
        self.ui.enableHLineCheckBox.clicked.connect(self.enableHLineCheckBox_clicked)
        
        # Colors
        self.ui.contentTextButton.clicked.connect(self.contentTextButton_clicked)
        self.ui.contentBackgroundButton.clicked.connect(self.contentBackgroundButton_clicked)
        self.ui.highlighterTextButton.clicked.connect(self.highlighterTextButton_clicked)
        self.ui.highlighterBackgroundButton.clicked.connect(self.highlighterBackgroundButton_clicked)
        self.ui.highlighterLineTextButton.clicked.connect(self.highlighterLineTextButton_clicked)
        self.ui.highlighterLineBackgroundButton.clicked.connect(self.highlighterLineBackgroundButton_clicked)
        
        # Fonts
        self.ui.fontComboBox.currentFontChanged.connect(self.fontComboBox_currentFontChanged)
        
        # Bottom dialog buttons
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        self.ui.previewButton.clicked.connect(self.previewButton_clicked)
        self.ui.applyButton.clicked.connect(self.applyButton_clicked)
        
        # When this window closes
        self.finished.connect(self.this_finished)
        
    def updateSettings(self):
        
        # Update the color boxes
        self.setButtonColor(self.ui.contentTextButton, self.configuration.color_contentText)
        self.setButtonColor(self.ui.contentBackgroundButton, self.configuration.color_contentBackground)
        self.setButtonColor(self.ui.highlighterTextButton, self.configuration.color_highlightText)
        self.setButtonColor(self.ui.highlighterBackgroundButton, self.configuration.color_highlightBackground)
        self.setButtonColor(self.ui.highlighterLineTextButton, self.configuration.color_highlightLineText)
        self.setButtonColor(self.ui.highlighterLineBackgroundButton, self.configuration.color_highlightLineBackground)
        
        # Update the checkboxes
        if self.configuration.highlight_text_enable:
            self.ui.enableHTextCheckBox.setCheckState(Qt.Checked)
        else:
            self.ui.enableHTextCheckBox.setCheckState(Qt.Unchecked)
            
        if self.configuration.highlight_line_enable:
            self.ui.enableHLineCheckBox.setCheckState(Qt.Checked)
        else:
            self.ui.enableHLineCheckBox.setCheckState(Qt.Unchecked)
            
        # Update the font combobox
        myFont = QtGui.QFont(self.configuration.font_all)
        self.ui.fontComboBox.setFont(myFont)
        self.ui.fontComboBox.setCurrentFont(myFont)

    def applyButton_clicked(self):
        self.beforeConfiguration = copy.deepcopy(self.configuration)
        self.done(ColorSettings.RESULT_NEED_REFRESH)
        
    def previewButton_clicked(self):
        self.configuration.saveToFile(app_data_path('configuration.xml'))
        self.mainWindow.refreshDocument()
        
    def restoreButton_clicked(self):
        self.configuration.restoreDefaults()
        self.configuration.saveToFile(app_data_path('configuration.xml'))
        self.mainWindow.refreshDocument()
        self.updateSettings()
        
    def this_finished(self):
        self.beforeConfiguration.saveToFile(app_data_path('configuration.xml'))
    
    def contentTextButton_clicked(self):
        dialog = QtGui.QColorDialog()
        def myAccept():
            self.configuration.color_contentText = dialog.currentColor()
            self.updateSettings()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
    
    def contentBackgroundButton_clicked(self):
        dialog = QtGui.QColorDialog()
        def myAccept():
            self.configuration.color_contentBackground = dialog.currentColor()
            self.updateSettings()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
    
    def highlighterTextButton_clicked(self):
        dialog = QtGui.QColorDialog()
        def myAccept():
            self.configuration.color_highlightText = dialog.currentColor()
            self.updateSettings()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def highlighterBackgroundButton_clicked(self):
        dialog = QtGui.QColorDialog()
        def myAccept():
            self.configuration.color_highlightBackground = dialog.currentColor()
            self.updateSettings()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def enableHTextCheckBox_clicked(self):
        state = self.ui.enableHTextCheckBox.checkState()
        
        if state == Qt.Checked:
            self.configuration.highlight_text_enable = True
        else:
            self.configuration.highlight_text_enable = False
            
        self.updateSettings()
    
    def enableHLineCheckBox_clicked(self):
        state = self.ui.enableHLineCheckBox.checkState()
        
        if state == Qt.Checked:
            self.configuration.highlight_line_enable = True
        else:
            self.configuration.highlight_line_enable = False
            
        self.updateSettings()
        
    def highlighterLineTextButton_clicked(self):
        dialog = QtGui.QColorDialog()
        def myAccept():
            self.configuration.color_highlightLineText = dialog.currentColor()
            self.updateSettings()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def highlighterLineBackgroundButton_clicked(self):
        dialog = QtGui.QColorDialog()
        def myAccept():
            self.configuration.color_highlightLineBackground = dialog.currentColor()
            self.updateSettings()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def fontComboBox_currentFontChanged(self, newFont):
        fontFamily = str(newFont.family())
        self.configuration.font_all = fontFamily
        self.updateSettings()
        
    def setButtonColor(self, button, color):
        '''
        Takes a QColor and sets the color on the button, making sure that the text is readable and still having the
        same size.
        '''
        rgbString = 'rgb(' + str(color.red()) + ', ' + str(color.green()) + ', ' + str(color.blue()) + ')'
        
        # Calculate the font color for the button text that would be most readable
        threshold = 105
        delta = (color.red() * 0.299) + (color.green() * 0.587) + (color.blue() * 0.114)
        fontColor = ''
        if (255 - delta) < threshold:
            # Make it black
            fontColor = 'rgb(0,0,0)'
        else:
            # Make it white
            fontColor = 'rgb(255,255,255)'

        button.setStyleSheet('background-color: ' + rgbString + '; font-size: 16pt; color: ' + fontColor + ';')