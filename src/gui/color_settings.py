'''
Created on Apr 25, 2013

@author: Spencer Graffe
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from lxml import etree
import copy

from src.forms.color_settings_ui import Ui_ColorSettings

class ColorSettings(QtGui.QDialog):
    '''
    classdocs
    '''
    
    def __init__(self, mainWindow, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
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
        self.ui.applyButton.clicked.connect(self.applyButton_clicked)
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        
        # Colors
        self.ui.contentTextButton.clicked.connect(self.contentTextButton_clicked)
        self.ui.contentBackgroundButton.clicked.connect(self.contentBackgroundButton_clicked)
        self.ui.highlighterTextButton.clicked.connect(self.highlighterTextButton_clicked)
        self.ui.highlighterBackgroundButton.clicked.connect(self.highlighterBackgroundButton_clicked)
        self.ui.enableHighlightCheckbox.clicked.connect(self.enableHighlightCheckBox_clicked)
        self.ui.highlighterLineTextButton.clicked.connect(self.highlighterLineTextButton_clicked)
        self.ui.highlighterLineBackgroundButton.clicked.connect(self.highlighterLineBackgroundButton_clicked)
        
        # Fonts
        self.ui.fontComboBox.currentFontChanged.connect(self.fontComboBox_currentFontChanged)
        
    def updateSettings(self):
        
        # Update the color boxes
        self.setButtonColor(self.ui.contentTextButton, self.configuration.color_contentText)
        self.setButtonColor(self.ui.contentBackgroundButton, self.configuration.color_contentBackground)
        self.setButtonColor(self.ui.highlighterTextButton, self.configuration.color_highlightText)
        self.setButtonColor(self.ui.highlighterBackgroundButton, self.configuration.color_highlightBackground)
        self.setButtonColor(self.ui.highlighterLineTextButton, self.configuration.color_highlightLineText)
        self.setButtonColor(self.ui.highlighterLineBackgroundButton, self.configuration.color_highlightLineBackground)
        
        # Update the checkboxes
        if self.configuration.highlight_enable:
            self.ui.enableHighlightCheckbox.setCheckState(Qt.Checked)
        else:
            self.ui.enableHighlightCheckbox.setCheckState(Qt.Unchecked)
            
        # Update the font combobox
        myFont = QtGui.QFont(self.configuration.font_all)
        self.ui.fontComboBox.setFont(myFont)

    def applyButton_clicked(self):
        self.beforeConfiguration = copy.deepcopy(self.configuration)
        self.configuration.saveToFile('configuration.xml')
        self.mainWindow.refreshDocument()
        
    def restoreButton_clicked(self):
        self.configuration = copy.deepcopy(self.beforeConfiguration)
        self.updateSettings()
    
    def contentTextButton_clicked(self):
        self.configuration.color_contentText = QtGui.QColorDialog.getColor(initial=self.configuration.color_contentText)
        self.updateSettings()
    
    def contentBackgroundButton_clicked(self):
        self.configuration.color_contentBackground = QtGui.QColorDialog.getColor(initial=self.configuration.color_contentBackground)
        self.updateSettings()
    
    def highlighterTextButton_clicked(self):
        self.configuration.color_highlightText = QtGui.QColorDialog.getColor(initial=self.configuration.color_highlightText)
        self.updateSettings()
        
    def highlighterBackgroundButton_clicked(self):
        self.configuration.color_highlightBackground = QtGui.QColorDialog.getColor(initial=self.configuration.color_highlightBackground)
        self.updateSettings()
        
    def enableHighlightCheckBox_clicked(self):
        state = self.ui.enableHighlightCheckbox.checkState()
        
        if state == Qt.Checked:
            print 'Checkbox is checked!'
            self.configuration.highlight_enable = True
        else:
            print 'Not checked...'
            self.configuration.highlight_enable = False
            
        self.updateSettings()
        
    def highlighterLineTextButton_clicked(self):
        self.configuration.color_highlightLineText = QtGui.QColorDialog.getColor(initial=self.configuration.color_highlightLineText)
        self.updateSettings()
        
    def highlighterLineBackgroundButton_clicked(self):
        self.configuration.color_highlightLineBackground = QtGui.QColorDialog.getColor(initial=self.configuration.color_highlightLineBackground)
        self.updateSettings()
        
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