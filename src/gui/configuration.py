'''
Created on Apr 12, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QColor
from lxml import etree
import platform
from misc import app_data_path, temp_path, pattern_databases
import os
import traceback

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
        self.pause_length = 0  # unit between 0-10
        
        # Tagging
        self.tag_image = False
        self.tag_math = False
        
        # Math database
        self.math_database = 'General'
        
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
        
        # Zoom settings
        self.zoom_content = 1.0
        self.zoom_navigation_ptsize = 14
        
        # Search settings
        self.search_whole_word = False
        self.search_match_case = False
        
        # Font settings
        self.font_all = 'Arial'
        
    def getBugReportString(self):
        '''
        Returns a string describing the settings for the bug report. It will
        not include information that is not anonymous.
        '''
        out = 'Settings:\n'
        out += '----------------------------------------------\n\n'
        
        # Speech
        out += 'Speech:\n'
        out += '- Volume: ' + str(self.volume) + '\n'
        out += '- Rate: ' + str(self.rate) + '\n'
        out += '- Voice: ' + self.voice + '\n'
        out += '- Tag Images: ' + str(self.tag_image) + '\n'
        out += '- Tag Math: ' + str(self.tag_math) + '\n'
        out += '- Math Database: ' + os.path.basename(self.math_database) + '\n'
        out += '\n'
        
        # Colors
        out += 'Colors:\n'
        out += '- Enable Word Highlight: ' + str(self.highlight_text_enable) + '\n'
        out += '- Enable Sentence Highlight: ' + str(self.highlight_line_enable) + '\n'
        out += '- Content Text: ' + self._createRGBStringFromQColor(self.color_contentText) + '\n'
        out += '- Content Background: ' + self._createRGBStringFromQColor(self.color_contentBackground) + '\n'
        out += '- Highlight Text: ' + self._createRGBStringFromQColor(self.color_highlightText) + '\n'
        out += '- Highlight Background: ' + self._createRGBStringFromQColor(self.color_highlightBackground) + '\n'
        out += '- Highlight Line Text: ' + self._createRGBStringFromQColor(self.color_highlightLineText) + '\n'
        out += '- Highlight Line Background: ' + self._createRGBStringFromQColor(self.color_highlightLineBackground) + '\n'
        out += '\n'
        
        # Font
        out += 'Font: ' + self.font_all + '\n'
        
        # Zoom
        out += 'Zoom:\n'
        out += '- Content: ' + str(self.zoom_content) + '\n'
        out += '- Navigation: ' + str(self.zoom_navigation_ptsize) + '\n'
        out += '\n'
        
        # Search
        out += 'Search:\n'
        out += '- Whole Word: ' + str(self.search_whole_word) + '\n'
        out += '- Match Case: ' + str(self.search_match_case) + '\n'
        
        return out
        
    def loadFromFile(self, filePath):
        print 'Loading config...'
        
        # Check if the file exists first. Otherwise, create the file
        configFile = None
        configDOM = None
        success = False
        try:
            configFile = open(filePath, 'r')
            configDOM = etree.parse(configFile)
            configFile.close()
            success = True
        except Exception:
            # If the thing doesn't parse, then destroy settings and make new one
            print 'Exception occurred in loading configuration'
            print traceback.format_exc()                        
            self.restoreDefaults()
            self.saveToFile(filePath)
        
        if success:
            
            # Speech Settings
            query = configDOM.xpath('/Configuration/Volume')
            if len(query) > 0:
                self.volume = int(query[0].text)
            else:
                self.volume = 100
            
            query = configDOM.xpath('/Configuration/Rate')
            if len(query) > 0:
                self.rate = int(query[0].text)
            else:
                self.rate = 50
                
            query = configDOM.xpath('/Configuration/PauseLength')
            if len(query) > 0:
                self.pause_length = int(query[0].text)
            else:
                self.pause_length = 0
            
            query = configDOM.xpath('/Configuration/Voice')
            if len(query) > 0:
                self.voice = query[0].text
                if self.voice is None:
                    self.voice = ''
            else:
                self.voice = ''
            
            # Tagging math or images
            query = configDOM.xpath('/Configuration/TagImage')
            if len(query) > 0:
                self.tag_image = int(query[0].text)
            else:
                self.tag_image = 0
            if self.tag_image == 1:
                self.tag_image = True
            else:
                self.tag_image = False
            
            query = configDOM.xpath('/Configuration/TagMath')
            if len(query) > 0:
                self.tag_math = int(query[0].text)
            else:
                self.tag_math = 0
            if self.tag_math == 1:
                self.tag_math = True
            else:
                self.tag_math = False
            
            # Math database
            query = configDOM.xpath('/Configuration/MathDatabase')
            if len(query) > 0:
                self.math_database = os.path.splitext(os.path.basename(query[0].text))[0]
            else:
                self.math_database = 'General'
                
            # Highlighter Settings
            query = configDOM.xpath('/Configuration/EnableTextHighlight')
            if len(query) > 0:
                self.highlight_text_enable = int(query[0].text)
            else:
                self.highlight_text_enable = 1
            if self.highlight_text_enable == 1:
                self.highlight_text_enable = True
            else:
                self.highlight_text_enable = False
            
            query = configDOM.xpath('/Configuration/EnableLineHighlight')
            if len(query) > 0:
                self.highlight_line_enable = int(query[0].text)
            else:
                self.highlight_line_enable = 1
            if self.highlight_line_enable == 1:
                self.highlight_line_enable = True
            else:
                self.highlight_line_enable = False
            
            # Color Settings
            query = configDOM.xpath('/Configuration/Colors/ContentText')
            if len(query) > 0:
                self.color_contentText = self._createQColorFromCommaSeparated(query[0].text)
            else:
                self.color_contentText = QColor(255,255,255)
            query = configDOM.xpath('/Configuration/Colors/ContentBackground')
            if len(query) > 0:
                self.color_contentBackground = self._createQColorFromCommaSeparated(query[0].text)
            else:
                self.color_contentBackground = QColor(0,0,0)
            
            query = configDOM.xpath('/Configuration/Colors/HighlightText')
            if len(query) > 0:
                self.color_highlightText = self._createQColorFromCommaSeparated(query[0].text)
            else:
                self.color_highlightText = QColor(0,0,0)
            query = configDOM.xpath('/Configuration/Colors/HighlightBackground')
            if len(query) > 0:
                self.color_highlightBackground = self._createQColorFromCommaSeparated(query[0].text)
            else:
                self.color_highlightBackground = QColor(255,255,0)
            
            query = configDOM.xpath('/Configuration/Colors/HighlightLineText')
            if len(query) > 0:
                self.color_highlightLineText = self._createQColorFromCommaSeparated(query[0].text)
            else:
                self.color_highlightLineText = QColor(0,0,0)
                
            query = configDOM.xpath('/Configuration/Colors/HighlightLineBackground')
            if len(query) > 0:
                self.color_highlightLineBackground = self._createQColorFromCommaSeparated(query[0].text)
            else:
                self.color_highlightLineBackground = QColor(0,255,0)
            
            # Font Settings
            query = configDOM.xpath('/Configuration/Fonts/All')
            if len(query) > 0:
                self.font_all = query[0].text
            else:
                self.font_all = 'Arial'
            
            # Zoom Settings
            query = configDOM.xpath('/Configuration/Zooms/Content')
            if len(query) > 0:
                self.zoom_content = float(query[0].text)
            else:
                self.zoom_content = 1.0
            query = configDOM.xpath('/Configuration/Zooms/Navigation')
            if len(query) > 0:
                self.zoom_navigation_ptsize = int(query[0].text)
            else:
                self.zoom_navigation_ptsize = 14
            
            query = configDOM.xpath('/Configuration/Search/WholeWord')
            if len(query) > 0:
                self.search_whole_word = int(query[0].text)
            else:
                self.search_whole_word = 0
            if self.search_whole_word == 1:
                self.search_whole_word = True
            else:
                self.search_whole_word = False
            
            query = configDOM.xpath('/Configuration/Search/MatchCase')
            if len(query) > 0:
                self.search_match_case = int(query[0].text)
            else:
                self.search_match_case = 0
            if self.search_match_case == 1:
                self.search_match_case = True
            else:
                self.search_match_case = False
            
            # Show Tutorial
            query = configDOM.xpath('/Configuration/ShowTutorial')
            if len(query) > 0:
                self.showTutorial = query[0].text
            else:
                self.showTutorial = '1'
            if self.showTutorial == '1':
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
        pauseElem = etree.SubElement(root, 'PauseLength')
        pauseElem.text = str(self.pause_length)
        
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
            
        elem = etree.SubElement(root, 'MathDatabase')
        elem.text = self.math_database
        
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
        
        # Zoom settings
        zoomRoot = etree.SubElement(root, 'Zooms')
        elem = etree.SubElement(zoomRoot, 'Content')
        elem.text = str(self.zoom_content)
        elem = etree.SubElement(zoomRoot, 'Navigation')
        elem.text = str(self.zoom_navigation_ptsize)
        
        # Search Settings
        searchRoot = etree.SubElement(root, 'Search')
        elem = etree.SubElement(searchRoot, 'WholeWord')
        if self.search_whole_word:
            elem.text = '1'
        else:
            elem.text = '0'
        elem = etree.SubElement(searchRoot, 'MatchCase')
        if self.search_match_case:
            elem.text = '1'
        else:
            elem.text = '0'
        
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
        
        # If text highlighting is disabled, I will give it a completely clear
        # background to imitate that it is off.
        highlightTextColor = ''
        highlightTextBackgroundColor = ''
        if self.highlight_text_enable:
            highlightTextColor = self._createRGBStringFromQColor(self.color_highlightText)
            highlightTextBackgroundColor = self._createRGBStringFromQColor(self.color_highlightBackground)
        else:
            if not self.highlight_line_enable:
                highlightTextColor = self._createRGBStringFromQColor(self.color_contentText)
            else:
                highlightTextColor = self._createRGBStringFromQColor(self.color_highlightLineText)
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

a:link
{
color: ''' + self._createRGBStringFromQColor(self.color_highlightLineBackground) + ''';
}

a:visited
{
color: ''' + self._createRGBStringFromQColor(self.color_highlightLineBackground) + ''';
}

a:hover
{
color: ''' + self._createRGBStringFromQColor(self.color_highlightBackground) + ''';
}

a:active
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
margin-top: 2em;
margin-bottom: 2em;
border-collapse: collapse;
border: 1px solid ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
padding: 15px;
}

.mathmlEquation
{
'''
        # If we are on Windows, make it bigger to better match surrounding text
        if platform.system() == 'Windows':
            outtext += r'font-size: 230%;'
        else:
            outtext += r'font-size: 100%;'
    
        outtext += '''
}

.pageNumber
{
border-style:solid;
border-width: 1px 0px 0px 0px;
padding: 5px 0px 0px 25px;
font-size: 150%;
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
box-shadow: 1px 1px 7px ''' + highlightTextBackgroundColor + ''';
-webkit-border-radius: 3px;
display: inline-block;
z-index: 2;
}'''
        # -------------------------------------------
        # END CSS FILE
        
        if not os.path.exists(os.path.dirname(filePath)):
            os.makedirs(os.path.dirname(filePath))
        cssFile = open(filePath, 'w')
        cssFile.write(outtext)
        cssFile.close()