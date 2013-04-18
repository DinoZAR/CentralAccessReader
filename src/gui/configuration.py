'''
Created on Apr 12, 2013

@author: Spencer Graffe
'''
from PyQt4.QtGui import QColor
from lxml import etree

class Configuration(object):
    '''
    Object that holds all of the settings for the Nifty Prose Articulator
    '''


    def __init__(self):
        '''
        Fill it with all of the basic stuff.
        '''
        # Speech settings
        self.volume = 100
        self.rate = 200
        self.voice = ''
        
        # Highlighter settings
        self.highlight_enable = True
        
        # Color settings
        self.color_contentText = QColor(255,255,255)
        self.color_contentBackground = QColor(10,10,10)
        
        self.color_highlightText = QColor(0,0,0)
        self.color_highlightBackground = QColor(255,255,0)
        
        self.color_highlightLineText = QColor(0,0,0)
        self.color_highlightLineBackground = QColor(0,255,0)
        
        # Font settings
        self.font_paragraph = 'Times New Roman'
        self.font_paragraphSize = 12
        self.font_header1 = 'Times New Roman'
        self.font_header1Size = 42
        self.font_header2 = 'Times New Roman'
        self.font_header2Size = 30
        self.font_header3 = 'Times New Roman'
        self.font_header3Size = 25
        self.font_header4 = 'Times New Roman'
        self.font_header4Size = 20
    
    def loadFromFile(self, filePath):
        
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
            
        configFile.close()
        
        # Speech Settings
        self.volume = float(configDOM.xpath('/Configuration/Volume')[0].text)
        self.rate = int(configDOM.xpath('/Configuration/Rate')[0].text)
        self.voice = configDOM.xpath('/Configuration/Voice')[0].text
        if self.voice == None:
            self.voice = ''
            
        # Highlighter Settings
        self.highlight_enable = int(configDOM.xpath('/Configuration/EnableHighlighter')[0].text)
        if self.highlight_enable == 1:
            self.highlight_enable = True
        else:
            self.highlight_enable = False
        
        # Color Settings
        self.color_contentText = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/ContentText')[0].text)
        self.color_contentBackground = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/ContentBackground')[0].text)
        
        self.color_highlightText = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightText')[0].text)
        self.color_highlightBackground = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightBackground')[0].text)
        
        self.color_highlightLineText = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightLineText')[0].text)
        self.color_highlightLineBackground = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightLineBackground')[0].text)
        
        # Font Settings
        self.font_paragraph = configDOM.xpath('/Configuration/Fonts/ParagraphFont')[0].text
        self.font_paragraphSize = int(configDOM.xpath('/Configuration/Fonts/ParagraphSize')[0].text)
        self.font_header1 = configDOM.xpath('/Configuration/Fonts/Header1Font')[0].text
        self.font_header1Size = int(configDOM.xpath('/Configuration/Fonts/Header1Size')[0].text)
        self.font_header2 = configDOM.xpath('/Configuration/Fonts/Header2Font')[0].text
        self.font_header2Size = int(configDOM.xpath('/Configuration/Fonts/Header2Size')[0].text)
        self.font_header3 = configDOM.xpath('/Configuration/Fonts/Header3Font')[0].text
        self.font_header3Size = int(configDOM.xpath('/Configuration/Fonts/Header3Size')[0].text)
        self.font_header4 = configDOM.xpath('/Configuration/Fonts/Header4Font')[0].text
        self.font_header4Size = int(configDOM.xpath('/Configuration/Fonts/Header4Size')[0].text)
        
    def saveToFile(self, filePath):
        root = etree.Element("Configuration")
        
        # Speech Settings
        volumeElem = etree.SubElement(root, 'Volume')
        volumeElem.text = str(self.volume)
        rateElem = etree.SubElement(root, 'Rate')
        rateElem.text = str(self.rate)
        voiceElem = etree.SubElement(root, 'Voice')
        voiceElem.text = self.voice
        
        # Highlighter Settings
        elem = etree.SubElement(root, 'EnableHighlighter')
        if self.highlight_enable:
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
        elem = etree.SubElement(fontRoot, 'ParagraphFont')
        elem.text = self.font_paragraph
        elem = etree.SubElement(fontRoot, 'ParagraphSize')
        elem.text = str(self.font_paragraphSize)
        elem = etree.SubElement(fontRoot, 'Header1Font')
        elem.text = self.font_header1
        elem = etree.SubElement(fontRoot, 'Header1Size')
        elem.text = str(self.font_header1Size)
        elem = etree.SubElement(fontRoot, 'Header2Font')
        elem.text = self.font_header2
        elem = etree.SubElement(fontRoot, 'Header2Size')
        elem.text = str(self.font_header2Size)
        elem = etree.SubElement(fontRoot, 'Header3Font')
        elem.text = self.font_header3
        elem = etree.SubElement(fontRoot, 'Header3Size')
        elem.text = str(self.font_header3Size)
        elem = etree.SubElement(fontRoot, 'Header4Font')
        elem.text = self.font_header4
        elem = etree.SubElement(fontRoot, 'Header4Size')
        elem.text = str(self.font_header4Size)
        
        configFile = open(filePath, 'w')
        configFile.write(etree.tostring(root, pretty_print=True))
        configFile.close()
        
        self._writeCSS('import/defaultStyle.css')
    
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
        
        # BEGIN CSS FILE
        # -------------------------------------------
        
        outtext = '''
body
{
background: ''' + self._createRGBStringFromQColor(self.color_contentBackground) + ''';
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
font-size: ''' + str(self.font_paragraphSize) + '''pt;
font-family: "''' + self.font_paragraph + '''";
}

h1
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
text-align: center;
font-size: ''' + str(self.font_header1Size) + '''pt;
font-family: "''' + self.font_header1 + '''";
}

h2
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
border-style: dashed;
border-width: 0px 0px 1px 0px;
border-color: #EEEEEE;
padding: 15px;
font-size: ''' + str(self.font_header2Size) + '''pt;
font-family: "''' + self.font_header2 + '''";
}

h3
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
padding: 10px;
font-size: ''' + str(self.font_header3Size) + '''pt;
font-family: "''' + self.font_header3 + '''";

}

h4
{
color: ''' + self._createRGBStringFromQColor(self.color_contentText) + ''';
font-size: ''' + str(self.font_header4Size) + '''pt;
font-family: "''' + self.font_header4 + '''";
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

.mathmlEquation
{
font-size: 230%;
}

#npaHighlightLine
{
background-color: ''' + self._createRGBStringFromQColor(self.color_highlightLineBackground) + ''';
color: ''' + self._createRGBStringFromQColor(self.color_highlightLineText) + ''';
-webkit-border-radius: 5px;
}

#npaHighlight
{
background-color: ''' + self._createRGBStringFromQColor(self.color_highlightBackground) + ''';
color: ''' + self._createRGBStringFromQColor(self.color_highlightText) + ''';
-webkit-border-radius: 5px;
display: inline-block;
}'''
        # -------------------------------------------
        # END CSS FILE
        print 'Writing CSS file...'
            
        cssFile = open(filePath, 'w')
        cssFile.write(outtext)
        cssFile.close()