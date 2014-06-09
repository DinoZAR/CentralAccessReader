'''
Created on Apr 25, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QDialog, QColor, QFont, qApp, QColorDialog
from PyQt4.QtCore import Qt, pyqtSignal

from car.forms.color_settings_ui import Ui_ColorSettings
from car.gui import configuration
from car.gui import loader
from car.misc import app_data_path, temp_path

class ColorSettings(QDialog):

    documentRefreshRequested = pyqtSignal()
    
    def __init__(self, mainWindow, parent=None):
        super(ColorSettings, self).__init__(parent)
        
        self.ui = Ui_ColorSettings()
        self.ui.setupUi(self)
        self.connect_signals()
        
        self.mainWindow = mainWindow
        
        # Update the GUI to match the settings currently employed
        self.updateSettings()
            
    def connect_signals(self):
        '''
        A method I made to connect all of my signals to the correct functions.
        '''
        # Highlighter
        self.ui.enableHTextCheckBox.clicked.connect(self.enableHTextCheckBox_clicked)
        self.ui.enableHLineCheckBox.clicked.connect(self.enableHLineCheckBox_clicked)
        self.ui.followInsideParagraphCheckBox.clicked.connect(self.followInsideParagraphCheckBox_clicked)
        
        # Colors
        self.ui.contentTextButton.clicked.connect(self.contentTextButton_clicked)
        self.ui.contentBackgroundButton.clicked.connect(self.contentBackgroundButton_clicked)
        self.ui.highlighterTextButton.clicked.connect(self.highlighterTextButton_clicked)
        self.ui.highlighterBackgroundButton.clicked.connect(self.highlighterBackgroundButton_clicked)
        self.ui.highlighterLineTextButton.clicked.connect(self.highlighterLineTextButton_clicked)
        self.ui.highlighterLineBackgroundButton.clicked.connect(self.highlighterLineBackgroundButton_clicked)
        
        # Fonts
        self.ui.fontComboBox.currentFontChanged.connect(self.fontComboBox_currentFontChanged)
        
        # Layout and theme
#         self.ui.layoutComboBox.currentIndexChanged.connect(self.layoutComboBox_currentIndexChanged)
        self.ui.themeComboBox.currentIndexChanged.connect(self.themeComboBox_currentIndexChanged)
        
        # Bottom dialog buttons
        self.ui.restoreButton.clicked.connect(self.restoreButton_clicked)
        
    def updateSettings(self):
        
        # Update the color boxes
        self._setButtonColor(self.ui.contentTextButton, configuration.getColor('ContentTextColor', QColor(255, 255, 255)))
        self._setButtonColor(self.ui.contentBackgroundButton, configuration.getColor('ContentBackgroundColor', QColor(0, 0, 0)))
        self._setButtonColor(self.ui.highlighterTextButton, configuration.getColor('HighlightTextColor', QColor(0, 0, 0)))
        self._setButtonColor(self.ui.highlighterBackgroundButton, configuration.getColor('HighlightBackgroundColor', QColor(255, 255, 0)))
        self._setButtonColor(self.ui.highlighterLineTextButton, configuration.getColor('HighlightLineTextColor', QColor(0, 0, 0)))
        self._setButtonColor(self.ui.highlighterLineBackgroundButton, configuration.getColor('HighlightLineBackgroundColor', QColor(0, 255, 0)))
        
        # Update the checkboxes
        if configuration.getBool('HighlightTextEnable', True):
            self.ui.enableHTextCheckBox.setCheckState(Qt.Checked)
        else:
            self.ui.enableHTextCheckBox.setCheckState(Qt.Unchecked)
            
        if configuration.getBool('HighlightLineEnable', True):
            self.ui.enableHLineCheckBox.setCheckState(Qt.Checked)
        else:
            self.ui.enableHLineCheckBox.setCheckState(Qt.Unchecked)
            
        if configuration.getBool('FollowInsideParagraph', True):
            self.ui.followInsideParagraphCheckBox.setCheckState(Qt.Checked)
        else:
            self.ui.followInsideParagraphCheckBox.setCheckState(Qt.Unchecked)
            
        # Update the font combobox
        myFont = QFont(configuration.getValue('Font', 'Arial'))
        self.ui.fontComboBox.setFont(myFont)
        self.ui.fontComboBox.setCurrentFont(myFont)
        
        # Update the layout combobox
#         self.ui.layoutComboBox.blockSignals(True)
#         self.ui.layoutComboBox.clear()
#         layouts = loader.get_layouts()
#         for l in layouts:
#             self.ui.layoutComboBox.addItem(l, userData=l)
#             
#         i = self.ui.layoutComboBox.findData(self.configuration.gui_layout)
#         if i < 0:
#             i = 0
#         self.ui.layoutComboBox.setCurrentIndex(i)
#         self.ui.layoutComboBox.blockSignals(False)
       
        # Update the theme combobox
        self.ui.themeComboBox.blockSignals(True)
        self.ui.themeComboBox.clear()
        themes = loader.get_themes()
        for t in themes:
            self.ui.themeComboBox.addItem(t, userData=t)
            
        i = self.ui.themeComboBox.findData(configuration.getValue('Theme'))
        if i < 0:
            i = 0
        self.ui.themeComboBox.setCurrentIndex(i)
        self.ui.themeComboBox.blockSignals(False)
        
    def restoreButton_clicked(self):

        # Restore settings related to this pane
        configuration.restoreDefault('HighlightTextEnable')
        configuration.restoreDefault('HighlightLineEnable')
        configuration.restoreDefault('FollowInsideParagraph')

        configuration.restoreDefault('ContentTextColor')
        configuration.restoreDefault('ContentBackgroundColor')
        configuration.restoreDefault('HighlightTextColor')
        configuration.restoreDefault('HighlightBackgroundColor')
        configuration.restoreDefault('HighlightLineTextColor')
        configuration.restoreDefault('HighlightLineBackgroundColor')

        configuration.restoreDefault('Font')
        configuration.restoreDefault('Theme')

        # Update presentation
        self.updateSettings()
        with open(temp_path('import/defaultStyle.css'), 'w') as f:
            f.write(configuration.getCSS())
        self.mainWindow.refreshDocument()
        loader.load_theme(qApp, configuration.getValue('Theme'))
    
    def contentTextButton_clicked(self):
        dialog = QColorDialog()
        def myAccept():
            configuration.setColor('ContentTextColor', dialog.currentColor())
            self.updateSettings()
            configuration.save(app_data_path('configuration.xml'))
            with open(temp_path('import/defaultStyle.css'), 'w') as f:
                f.write(configuration.getCSS())
            self.mainWindow.refreshDocument()
        self.mainWindow.refreshDocument()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
    
    def contentBackgroundButton_clicked(self):
        dialog = QColorDialog()
        def myAccept():
            configuration.setColor('ContentBackgroundColor', dialog.currentColor())
            self.updateSettings()
            configuration.save(app_data_path('configuration.xml'))
            with open(temp_path('import/defaultStyle.css'), 'w') as f:
                f.write(configuration.getCSS())
            self.mainWindow.refreshDocument()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
    
    def highlighterTextButton_clicked(self):
        dialog = QColorDialog()
        def myAccept():
            configuration.setColor('HighlightTextColor', dialog.currentColor())
            self.updateSettings()
            configuration.save(app_data_path('configuration.xml'))
            with open(temp_path('import/defaultStyle.css'), 'w') as f:
                f.write(configuration.getCSS())
            self.mainWindow.refreshDocument()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def highlighterBackgroundButton_clicked(self):
        dialog = QColorDialog()
        def myAccept():
            configuration.setColor('HighlightBackgroundColor', dialog.currentColor())
            self.updateSettings()
            configuration.save(app_data_path('configuration.xml'))
            with open(temp_path('import/defaultStyle.css'), 'w') as f:
                f.write(configuration.getCSS())
            self.mainWindow.refreshDocument()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def enableHTextCheckBox_clicked(self):
        state = self.ui.enableHTextCheckBox.checkState()
        
        if state == Qt.Checked:
            configuration.setBool('HighlightTextEnable', True)
        else:
            configuration.setBool('HighlightTextEnable', False)
            
        self.updateSettings()
        
    def followInsideParagraphCheckBox_clicked(self):
        state = self.ui.followInsideParagraphCheckBox.checkState()
        
        if state == Qt.Checked:
            configuration.setBool('FollowInsideParagraph', True, True)
        else:
            configuration.setBool('FollowInsideParagraph', False, True)
    
    def enableHLineCheckBox_clicked(self):
        state = self.ui.enableHLineCheckBox.checkState()
        
        if state == Qt.Checked:
            configuration.setBool('HighlightLineEnable', True)
        else:
            configuration.setBool('HighlightLineEnable', False)
            
        self.updateSettings()
        
    def highlighterLineTextButton_clicked(self):
        dialog = QColorDialog()
        def myAccept():
            configuration.setColor('HighlightLineTextColor', dialog.currentColor())
            self.updateSettings()
            configuration.save(app_data_path('configuration.xml'))
            with open(temp_path('import/defaultStyle.css'), 'w') as f:
                f.write(configuration.getCSS())
            self.mainWindow.refreshDocument()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def highlighterLineBackgroundButton_clicked(self):
        dialog = QColorDialog()
        def myAccept():
            configuration.setColor('HighlightLineBackgroundColor', dialog.currentColor())
            self.updateSettings()
            configuration.save(app_data_path('configuration.xml'))
            with open(temp_path('import/defaultStyle.css'), 'w') as f:
                f.write(configuration.getCSS())
            self.mainWindow.refreshDocument()
        dialog.accepted.connect(myAccept)
        dialog.exec_()
        
    def fontComboBox_currentFontChanged(self, newFont):
        fontFamily = str(newFont.family())
        configuration.setValue('Font', fontFamily)
        self.updateSettings()
        configuration.save(app_data_path('configuration.xml'))
        with open(temp_path('import/defaultStyle.css'), 'w') as f:
            f.write(configuration.getCSS())
        self.mainWindow.refreshDocument()
    
    def themeComboBox_currentIndexChanged(self, index):
        configuration.setValue('Theme', unicode(self.ui.themeComboBox.itemData(index).toString()))
        loader.load_theme(qApp, configuration.getValue('Theme'))
        
    def _setButtonColor(self, button, color):
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
    
    def _colorsChanged(self):
        '''
        Returns whether the colors have changed since before configuration.
        '''
        return True
#         changed = self.beforeConfiguration.color_contentText != self.configuration.color_contentText
#         changed = changed or (self.beforeConfiguration.color_contentBackground != self.configuration.color_contentBackground)
#         changed = changed or (self.beforeConfiguration.color_highlightText != self.configuration.color_highlightText)
#         changed = changed or (self.beforeConfiguration.color_highlightBackground != self.configuration.color_highlightBackground)
#         changed = changed or (self.beforeConfiguration.color_highlightLineText != self.configuration.color_highlightLineText)
#         changed = changed or (self.beforeConfiguration.color_highlightLineBackground != self.configuration.color_highlightLineBackground)
#         
#         changed = changed or (self.beforeConfiguration.highlight_text_enable != self.configuration.highlight_text_enable)
#         changed = changed or (self.beforeConfiguration.highlight_line_enable != self.configuration.highlight_line_enable)
#         
#         return changed