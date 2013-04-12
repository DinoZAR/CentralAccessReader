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
        
        # Color settings
        self.color_highlightText = QColor(0,0,0)
        self.color_highlightBackground = QColor(255,255,0)
    
    def loadFromFile(self, filePath):
        
        configFile = open(filePath, 'r+')
        configDOM = etree.parse(configFile)
        configFile.close()
        
        # Speech Settings
        self.volume = float(configDOM.xpath('/Configuration/Volume')[0].text)
        self.rate = int(configDOM.xpath('/Configuration/Rate')[0].text)
        self.voice = configDOM.xpath('/Configuration/Voice')[0].text
        if self.voice == None:
            self.voice = ''
        
        # Color Settings
        self.color_highlightText = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightText')[0].text)
        self.color_highlightBackground = self._createQColorFromCommaSeparated(configDOM.xpath('/Configuration/Colors/HighlightBackground')[0].text)
        
    def saveToFile(self, filePath):
        root = etree.Element("Configuration")
        
        # Speech Settings
        volumeElem = etree.SubElement(root, 'Volume')
        volumeElem.text = str(self.volume)
        rateElem = etree.SubElement(root, 'Rate')
        rateElem.text = str(self.rate)
        voiceElem = etree.SubElement(root, 'Voice')
        voiceElem.text = self.voice
        
        # Color Settings
        colorRoot = etree.SubElement(root, 'Colors')
        elem = etree.SubElement(colorRoot, 'HighlightText')
        elem.text = self._createCommaSeparatedFromQColor(self.color_highlightText)
        elem = etree.SubElement(colorRoot, 'HighlightBackground')
        elem.text = self._createCommaSeparatedFromQColor(self.color_highlightBackground)
        
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
        
        outtext = '''body
{
background: #333333;
color: #F3F3F3;
font-size: 14pt;
}

h1
{
color: #EEEEEE;
text-align: center;
text-shadow: 2px 2px 5px #111111;
font-size: 42pt;
}

h2
{
color: #EEEEEE;
text-shadow: 2px 2px 5px #111111;
border-style: dashed;
border-width: 0px 0px 1px 0px;
border-color: #EEEEEE;
padding: 15px;
font-size: 30pt;
}

h3
{
color: #EEEEEE;
text-shadow: 2px 2px 5px #111111;
font-size: 25pt;
padding: 10px;
}

h4
{
color: #EEEEEE;
text-shadow: 2px 2px 5px #111111;
font-size: 20pt;
}

p
{
color: white;
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

#npaHighlight
{
background-color: ''' + self._createRGBStringFromQColor(self.color_highlightBackground) + ''';
color: ''' + self._createRGBStringFromQColor(self.color_highlightText) + ''';
-webkit-border-radius: 5px;
padding: 5px;
}'''
        
        print 'Writing CSS file...'
        print outtext
            
        cssFile = open(filePath, 'w')
        cssFile.write(outtext)
        cssFile.close()