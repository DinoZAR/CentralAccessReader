'''
Created on Jan 21, 2013

@author: Spencer
'''
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QUrl, QVariant
from forms.settings_ui import Ui_Settings
from lxml import etree
import copy

class Settings(QtGui.QDialog):

    def __init__(self, mainWindow, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.mainWindow = mainWindow
        
        self.beforeConfiguration = copy.deepcopy(self.mainWindow.configuration)
        self.configuration = copy.deepcopy(self.mainWindow.configuration)
        
        # Get a list of voices to add to combo box
        voiceList = self.mainWindow.speechThread.getVoiceList()
        for v in voiceList:
            self.ui.comboBox.addItem(v[0], userData=v[1])
        self.ui.comboBox.setCurrentIndex(0)
        
        # Update the GUI to match the settings currently employed
        self.updateSettings()
            
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        self.ui.applyButton.clicked.connect(self.applyButton_clicked)
        self.ui.testButton.clicked.connect(self.testButton_clicked)
        self.ui.rateSlider.valueChanged.connect(self.rateSlider_valueChanged)
        self.ui.volumeSlider.valueChanged.connect(self.volumeSlider_valueChanged)
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        self.ui.comboBox.currentIndexChanged.connect(self.comboBox_currentIndexChanged)
        
        # Colors
        self.ui.contentTextButton.clicked.connect(self.contentTextButton_clicked)
        self.ui.contentBackgroundButton.clicked.connect(self.contentBackgroundButton_clicked)
        self.ui.highlighterTextButton.clicked.connect(self.highlighterTextButton_clicked)
        self.ui.highlighterBackgroundButton.clicked.connect(self.highlighterBackgroundButton_clicked)
        self.ui.enableHighlightCheckbox.clicked.connect(self.enableHighlightCheckBox_clicked)
        self.ui.highlighterLineTextButton.clicked.connect(self.highlighterLineTextButton_clicked)
        self.ui.highlighterLineBackgroundButton.clicked.connect(self.highlighterLineBackgroundButton_clicked)
        
        # Fonts
        self.ui.paragraphFontButton.clicked.connect(self.paragraphFontButton_clicked)
        self.ui.header1FontButton.clicked.connect(self.header1FontButton_clicked)
        self.ui.header2FontButton.clicked.connect(self.header2FontButton_clicked)
        self.ui.header3FontButton.clicked.connect(self.header3FontButton_clicked)
        self.ui.header4FontButton.clicked.connect(self.header4FontButton_clicked)
        
    def updateSettings(self):
        # Update speech thread with my stuff
        self.mainWindow.changeVolume.emit(self.configuration.volume)
        self.mainWindow.changeRate.emit(self.configuration.rate)
        self.mainWindow.changeVoice.emit(self.configuration.voice)
        
        # Update main window sliders to match
        self.ui.rateSlider.setValue(self.configuration.rate)
        self.ui.volumeSlider.setValue(int(self.configuration.volume * 100))
        
        self.ui.rateLabel.setText(str(self.configuration.rate))
        self.ui.volumeLabel.setText(str(int(self.configuration.volume * 100)))
        
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
            
        # Update the font buttons
        self.setButtonFont(self.ui.paragraphFontButton, self.configuration.font_paragraph, self.configuration.font_paragraphSize)
        self.setButtonFont(self.ui.header1FontButton, self.configuration.font_header1, self.configuration.font_header1Size)
        self.setButtonFont(self.ui.header2FontButton, self.configuration.font_header2, self.configuration.font_header2Size)
        self.setButtonFont(self.ui.header3FontButton, self.configuration.font_header3, self.configuration.font_header3Size)
        self.setButtonFont(self.ui.header4FontButton, self.configuration.font_header4, self.configuration.font_header4Size)

    def applyButton_clicked(self):
        self.beforeConfiguration = copy.deepcopy(self.configuration)
        self.configuration.saveToFile('configuration.xml')
        self.mainWindow.refreshDocument()
        
    def restoreButton_clicked(self):
        self.configuration = copy.deepcopy(self.beforeConfiguration)
        self.updateSettings()
        
    def rateSlider_valueChanged(self, value):
        self.configuration.rate = value
        self.updateSettings()

    def volumeSlider_valueChanged(self, value):
        self.configuration.volume = float(value) / 100.0
        self.updateSettings()
        
    def comboBox_currentIndexChanged(self, index):
        self.configuration.voice = str(self.ui.comboBox.itemData(index).toString())
        self.updateSettings()
        
    def testButton_clicked(self):
        myText = self.ui.testSpeechText.toPlainText()
        self.mainWindow.addToQueue.emit(myText, 'text')
        self.mainWindow.startPlayback.emit()
    
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
        
    def paragraphFontButton_clicked(self):
        myFont = QtGui.QFontDialog.getFont(QtGui.QFont(self.configuration.font_paragraph, self.configuration.font_paragraphSize))[0]
        self.configuration.font_paragraph = str(myFont.family())
        self.configuration.font_paragraphSize = myFont.pointSize()
        self.updateSettings()
        
    def header1FontButton_clicked(self):
        myFont = QtGui.QFontDialog.getFont(QtGui.QFont(self.configuration.font_header1, self.configuration.font_header1Size))[0]
        self.configuration.font_header1 = str(myFont.family())
        self.configuration.font_header1Size = myFont.pointSize()
        self.updateSettings() 
        
    def header2FontButton_clicked(self):
        myFont = QtGui.QFontDialog.getFont(QtGui.QFont(self.configuration.font_header2, self.configuration.font_header2Size))[0]
        self.configuration.font_header2 = str(myFont.family())
        self.configuration.font_header2Size = myFont.pointSize()
        self.updateSettings() 
        
    def header3FontButton_clicked(self):
        myFont = QtGui.QFontDialog.getFont(QtGui.QFont(self.configuration.font_header3, self.configuration.font_header3Size))[0]
        self.configuration.font_header3 = str(myFont.family())
        self.configuration.font_header3Size = myFont.pointSize()
        self.updateSettings() 
    
    def header4FontButton_clicked(self):
        myFont = QtGui.QFontDialog.getFont(QtGui.QFont(self.configuration.font_header4, self.configuration.font_header4Size))[0]
        self.configuration.font_header4 = str(myFont.family())
        self.configuration.font_header4Size = myFont.pointSize()
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
        
    def setButtonFont(self, button, family, size):
        '''
        Changes the font of the text in the button.
        '''
        button.setFont(QtGui.QFont(family, size))
        