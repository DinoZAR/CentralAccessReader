'''
Created on Apr 12, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QColor
from lxml import etree
from src.misc import app_data_path, temp_path
import os

class Configuration(object):
    '''
    Object that holds all of the settings for the Nifty Prose Articulator
    '''

    def __init__(self):
        '''
        Fill it with all of the basic stuff.
        '''
        self.restoreDefaults()
        
        # Show Tutorial (first time thing)
        self.showTutorial = True
        
    def restoreDefaults(self):
        '''
        As it implies, restores the configuration back to its default settings.
        '''
        # Speech settings
        self.volume = 100
        self.rate = 50
        self.voice = ''
        
        self.tag_image = False
        self.tag_math = False
        
        # Highlighter settings
        self.highlight_text_enable = True
        self.highlight_line_enable = True
        
        # Color settings
        self.color_contentText = QColor(255,255,255)
        self.color_contentBackground = QColor(10,10,10)
        
        self.color_highlightText = QColor(0,0,0)
        self.color_highlightBackground = QColor(255,255,0)
        
        self.color_highlightLineText = QColor(0,0,0)
        self.color_highlightLineBackground = QColor(0,255,0)
        
        # Font settings
        self.font_all = 'Arial'
    
    def loadFromFile(self, filePath):
        print 'Loading config...'
        
        # Check if the file exists first. Otherwise, create the file
        configFile = None
        configDOM = None
        try:
            configFile = open(filePath, 'r')
            configDOM = etree.parse(configFile)
        except IOError:
            self.saveToFile(filePath)
            configFile = open(filePath, 'r')
            configDOM = etree.parse(configFile)
        except Exception:
            # If the thing doesn't parse, then destroy settings and make new one
            self.saveToFile(filePath)
            configFile = open(filePath, 'r')
            configDOM = etree.parse(configFile)
            
        configFile.close()
        
        # Speech Settings
        self.volume = int(configDOM.xpath('/Configuration/Volume')[0].text)
        self.rate = int(configDOM.xpath('/Configuration/Rate')[0].text)
        self.voice = configDOM.xpath('/Configuration/Voice')[0].text
        if self.voice == None:
            self.voice = ''
            
        self.tag_image = int(configDOM.xpath('/Configuration/TagImage')[0].text)
        if self.tag_image == 1:
            self.tag_image = True
        else:
            self.tag_image = False
        
        self.tag_math = int(configDOM.xpath('/Configuration/TagMath')[0].text)
        if self.tag_math == 1:
            self.tag_math = True
        else:
            self.tag_math = False
        
            
        # Highlighter Settings
        self.highlight_text_enable = int(configDOM.xpath('/Configuration/EnableTextHighlight')[0].text)
        if self.highlight_text_enable == 1:
            self.highlight_text_enable = True
        else:
            self.highlight_text_enable = False
        
        self.highlight_line_enable = int(configDOM.xpath('/Configuration/EnableLineHighlight')[0].text)
        if self.highlight_line_enable == 1:
            self.highlight_line_enable = True
        else:
            self.highlight_line_enable = False
        
        # Color Settings
        self.color_contentText = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/ContentText')[0].text)
        self.color_contentBackground = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/ContentBackground')[0].text)
        
        self.color_highlightText = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightText')[0].text)
        self.color_highlightBackground = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightBackground')[0].text)
        
        self.color_highlightLineText = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightLineText')[0].text)
        self.color_highlightLineBackground = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightLineBackground')[0].text)
        
        # Font Settings
        self.font_all = configDOM.xpath('/Configuration/Fonts/All')[0].text
        
        # Show Tutorial
        b = configDOM.xpath('/Configuration/ShowTutorial')[0].text
        if b == '1':
            self.showTutorial = True
        else:
            self.showTutorial = False
        
    def saveToFile(self, filePath):
        print 'Saving config...'
        
        root = etree.Element("Configuration")
        
        # Speech Settings
        volumeElem = etree.SubElement(root, 'Volume')
        volumeElem.text = str(self.volume)
        rateElem = etree.SubElement(root, 'Rate')
        rateElem.text = str(self.rate)
        voiceElem = etree.SubElement(root, 'Voice')
        voiceElem.text = self.voice
        
        elem = etree.SubElement(root, 'TagImage')
        if self.tag_image:
            elem.text = '1'
        else:
            elem.text = '0'
            
        elem = etree.SubElement(root, 'TagMath')
        if self.tag_math:
            elem.text = '1'
        else:
            elem.text = '0'
        
        # Highlighter Settings
        elem = etree.SubElement(root, 'EnableTextHighlight')
        if self.highlight_text_enable:
            elem.text = '1'
        else:
            elem.text = '0'
            
        elem = etree.SubElement(root, 'EnableLineHighlight')
        if self.highlight_line_enable:
            elem.text = '1'
        else:
            elem.text = '0'
        
        # Color Settings
        colorRoot = etree.SubElement(root, 'Colors')
        elem = etree.SubElement(colorRoot, 'ContentText')
        elem.text = self._createCommaSeparatedFromQColor(self.color_contentText)
        elem = etree.SubElement(colorRoot, 'ContentBackground')
        elem.text = self._createCommaSeparatedFromQColor(self.color_contentBackground)
        elem = etree.SubElement(colorRoot, 'HighlightText')
        elem.text = self._createCommaSeparatedFromQColor(self.color_highlightText)
        elem = etree.SubElement(colorRoot, 'HighlightBackground')
        elem.text = self._createCommaSeparatedFromQColor(self.color_highlightBackground)
        elem = etree.SubElement(colorRoot, 'HighlightLineText')
        elem.text = self._createCommaSeparatedFromQColor(self.color_highlightLineText)
        elem = etree.SubElement(colorRoot, 'HighlightLineBackground')
        elem.text = self._createCommaSeparatedFromQColor(self.color_highlightLineBackground)
        
        # Font settings
        fontRoot = etree.SubElement(root, 'Fonts')
        elem = etree.SubElement(fontRoot, 'All')
        elem.text = self.font_all
        
        # Show Tutorial
        elem = etree.SubElement(root, 'ShowTutorial')
        if self.showTutorial:
            elem.text = '1'
        else:
            elem.text = '0'
        
        configFile = open(filePath, 'w')
        configFile.write(etree.tostring(root, pretty_print=True))
        configFile.close()
        
        self._writeCSS(temp_path('import/defaultStyle.css'))
    
    def _createQColorFromCommaSeparated(self, colorString):
        tokens = colorString.split(',')
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()
        
        return QColor(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    
    def _createRGBStringFromQColor(self, color):
        return 'rgb(' + str(color.red()) + ', ' + str(color.green()) + ', ' + str(color.blue()) + ')'
    
    def _createCommaSeparatedFromQColor(self, color):
        return str(color.red()) + ',' + str(color.green()) + ',' + str(color.blue())
        
    def _writeCSS(self, filePath):
        '''
        Writes out the CSS file that has my configurations in it.
        '''
        print 'Writing CSS file...', filePath
        
        # If text highlighting is disabled, I will give it a completely clear
        # background to imitate that it is off.
        highlightTextColor = ''
        highlightTextBackgroundColor = ''
        if self.highlight_text_enable:
            highlightTextColor = self._createRGBStringFromQColor(self.color_highlightText)
            highlightTextBackgroundColor = self._createRGBStringFromQColor(self.color_highlightBackground)
        else:
            highlightTextColor = self._createRGBStringFromQColor(self.color_contentText)
            highlightTextBackgroundColor = 'transparent'
        
        # BEGIN CSS FILE
        # -------------------------------------------
        
        outtext = '''
body
{
background: ''' + self._createRGBStringFromQColor(self.color_contentBackground) + ''';
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
font-size: 12pt;
font-family: "''' + self.font_all + '''";
}

h1
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
text-align: center;
font-size: 300%;
}

h2
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
border-style: dashed;
border-width: 0px 0px 1px 0px;
border-color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
padding: 15px;
font-size: 200%;
}

h3
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
padding: 10px;
font-size: 175%;

}

h4
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
font-size: 150%;
}

p
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
}

img
{
max-width: 300px;
max-height: 300px
}

table, th, td
{
border: 1px solid ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
padding: 15px;
}

.mathmlEquation
{
font-size: 230%;
}

.ui-tooltip
{
background: ''' + self._createRGBStringFromQColor(self.color_contentBackground) + ''';
border: 2px solid ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
}

.ui-tooltip 
{
padding: 10px 20px;
margin-left: 10px;
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
border-radius: 20px;
box-shadow: 0 0 7px ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
}


#npaHighlightLine
{
background-color: ''' + self._createRGBStringFromQColor(self.color_highlightLineBackground) + ''';
color: ''' + self._createRGBStringFromQColor(self.color_highlightLineText) + ''';
-webkit-border-radius: 5px;
}

#npaHighlight
{
background-color: ''' + highlightTextBackgroundColor + ''';
color: ''' + highlightTextColor + ''';
-webkit-border-radius: 3px;
display: inline-block;
}'''
        # -------------------------------------------
        # END CSS FILE
        
        if not os.path.exists(os.path.dirname(filePath)):
            os.makedirs(os.path.dirname(filePath))
        cssFile = open(filePath, 'w')
        cssFile.write(outtext)
        cssFile.close()