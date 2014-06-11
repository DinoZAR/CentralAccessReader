'''
Created on Apr 12, 2013

@author: Spencer Graffe
'''
from datetime import datetime
from threading import Lock
import base64
import os

from PyQt5.QtGui import QColor
from lxml import etree

try:
    from car.math_to_prose_fast.tts import MathTTS
except ImportError as ex:
    print 'Loading slower MathTTS...', ex
    from car.math_to_prose.tts import MathTTS

from car.math_library import getLibraryFromPath
    
# Contains the data for the configuration. The format is as follows:
#
# {key : [value, default, cacheValue, lastCachedValue]}
#
# value - string representing the value of the key
# default - string representing the default value of the key
# cacheValue - object representing the value for the key
# lastCachedValue - string representing the value for when the cache was
#                   generated.

_CONFIG_DATA = {}

INDEX_VALUE = 0
INDEX_DEFAULT = 1
INDEX_CACHE_VALUE = 2
INDEX_LAST_CACHED_VALUE = 3

# ------------------------------------------------------------------------------
# BASE FUNCTIONS
# ------------------------------------------------------------------------------

def getValue(key, defaultValue=None):
    '''
    Gets the value for the key. If the key didn't exist before, the key will be 
    set to the default value, and the default value will be returned.
    
    If no defaultValue was given, and the key doesn't exist, a KeyError is
    raised.
    '''
    if key in _CONFIG_DATA:
        return _CONFIG_DATA[key][INDEX_VALUE]
    else:
        if defaultValue is None:
            raise KeyError('Key ' + key + ' does not exist in configuration, and no default value was provided.')
        else:
            #print 'Creating key:', key, ',', defaultValue
            _CONFIG_DATA[key] = [defaultValue, defaultValue, None, '']
            return defaultValue

def setValue(key, value, defaultValue=None):
    '''
    Sets the key to the value. If the key didn't exist before, it will add the
    key as a new entry. In this case, if the defaultValue is NOT used, the
    default value for that key will be the value given.
    '''
    if key in _CONFIG_DATA:
        _CONFIG_DATA[key][INDEX_VALUE] = value
    else:
        #print 'Creating key:', key, ',', value, ',', defaultValue
        if defaultValue is not None:
            _CONFIG_DATA[key] = [value, defaultValue, None, '']
        else:
            _CONFIG_DATA[key] = [value, value, None, '']

def restoreDefault(key):
    '''
    Restores the key to its default value.
    '''
    if key in _CONFIG_DATA:
        _CONFIG_DATA[key][INDEX_VALUE] = _CONFIG_DATA[key][INDEX_DEFAULT]
    else:
        raise KeyError('Key ' + key + ' does not exist in configuration.')

def restoreDefaults():
    '''
    Restores all keys to their default values.
    '''
    for k in _CONFIG_DATA.keys():
        setValue(k, _CONFIG_DATA[k][INDEX_DEFAULT])

# ------------------------------------------------------------------------------
#
# COMPLEX TYPES
#
# ------------------------------------------------------------------------------

def _convertPathToBase64(path):
    v = ''
    for p in path:
        v += base64.urlsafe_b64encode(p) + '/'
    if v[-1] == '/':
        v = v[:-1]
    return v

def _convertBase64ToPath(b64):
    path = []
    for p in b64.split('/'):
        path.append(base64.urlsafe_b64decode(p.strip()))
    return path

def getMathPatternPath(key, defaultValue=None):
    '''
    Gets the value from the key as a list of strings representing a path to a
    pattern, e.g., ['CAR, 'General']
    '''

    myDefaultPath = defaultValue
    if defaultValue is not None:
        myDefaultPath = _convertPathToBase64(defaultValue)

    return _convertBase64ToPath(getValue(key, myDefaultPath))

def setMathPatternPath(key, value, defaultValue=None):
    '''
    Sets the value to the key. The values are assumed to be a list of strings
    representing a path to a pattern, e.g., ['CAR, 'General']
    '''
    pathValue = _convertPathToBase64(value)
    pathDefault = defaultValue
    if defaultValue is not None:
        pathDefault = _convertPathToBase64(defaultValue)

    setValue(key, pathValue, pathDefault)

def getMathTTS(key, defaultValue=None):
    '''
    Gets the value from the key as a MathTTS object. The MathTTS object is
    cached, so it will only be regenerated if the value changes. Otherwise, 
    same behavior applies as getValue.
    
    defaultValue is assumed to be a path to a pattern in a math library, which
    is a list of strings with names, e.g., ['CAR, 'General']
    '''

    myPath = getMathPatternPath(key, defaultValue)

    # Check if value is same as cache value. If not, the math database must
    # be regenerated
    if _CONFIG_DATA[key][INDEX_VALUE] != _CONFIG_DATA[key][INDEX_LAST_CACHED_VALUE]:
        stuff = getLibraryFromPath(myPath)
        newTTS = MathTTS()
        newTTS.setMathLibrary(stuff[0], stuff[1])
        _CONFIG_DATA[key][INDEX_CACHE_VALUE] = newTTS
        _CONFIG_DATA[key][INDEX_LAST_CACHED_VALUE] = _CONFIG_DATA[key][INDEX_VALUE]
        
    return _CONFIG_DATA[key][INDEX_CACHE_VALUE]

def setMathTTS(key, value, defaultValue=None):
    '''
    Sets the value to the key. The values are assumed to be paths represented as
    lists of strings.
    '''
    setMathPatternPath(key, value, defaultValue)

def getColor(key, defaultValue=None):
    '''
    Gets the color from the key as a QColor. Same behavior applies as getValue.
    
    defaultValue is assumed to be a QColor.
    '''
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = _createCommaSeparatedFromQColor(defaultValue)
    
    return _createQColorFromCommaSeparated(getValue(key, myDefaultValue))
        
def setColor(key, value, defaultValue=None):
    '''
    Sets the QColor as a value for the key. Same behavior applies as setValue.
    
    defaultValue is assumed to be a QColor.
    '''
    myValue = _createCommaSeparatedFromQColor(value)
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = _createCommaSeparatedFromQColor(defaultValue)
    
    setValue(key, myValue, myDefaultValue)

def _createQColorFromCommaSeparated(colorString):
    '''
    Creates a QColor from a comma separated string. Good for retrieving a color
    from a configuration value.
    '''
    tokens = colorString.split(',')
    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip()
    
    return QColor(int(tokens[0]), int(tokens[1]), int(tokens[2]))

def _createCommaSeparatedFromQColor(color):
    '''
    Converts a QColor into a comma separated string, which is good for setting
    as a configuration value.
    '''
    return str(color.red()) + ',' + str(color.green()) + ',' + str(color.blue())

def getDate(key, defaultValue=None):
    '''
    Gets a datetime object from the value of the key. Same behavior applies as
    getValue.
    
    defaultValue is assumed to be a datetime object.
    '''
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = defaultValue.isoformat().split('T')[0]
    
    return datetime.strptime(getValue(key, myDefaultValue), '%Y-%m-%d')

def setDate(key, value, defaultValue=None):
    '''
    Sets the value to a key using a datetime object. Same behavior applies as
    setValue.
    
    defaultValue is assumed to be a datetime object.
    '''
    myValue = value.isoformat().split('T')[0]
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = defaultValue.isoformat().split('T')[0]
    
    setValue(key, myValue, myDefaultValue)
    
# ------------------------------------------------------------------------------
#
# PRIMITIVE TYPES
#
# ------------------------------------------------------------------------------
        
def getBool(key, defaultValue=None):
    '''
    Gets a boolean as value from a key. Same behavior applies as getValue.
    
    defaultValue is assumed to be a boolean.
    '''
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = _convertBoolToString(defaultValue)
        
    #print 'Getting bool:', key, ',', getValue(key, myDefaultValue)
    return _convertStringToBool(getValue(key, myDefaultValue))
        
def setBool(key, value, defaultValue=None):
    '''
    Sets a value for a key with a boolean. Same behavior applies as setValue.
    
    defaultValue is assumed to be a boolean.
    '''
    myValue = _convertBoolToString(value)
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = _convertBoolToString(defaultValue)
    
    #print 'Setting value for:', key, myValue
    setValue(key, myValue, myDefaultValue)
    
def _convertStringToBool(s):
    if '1' in s:
        return True
    else:
        return False

def _convertBoolToString(b):
    if b:
        return '1'
    else:
        return '0'

def getInt(key, defaultValue=None):
    '''
    Gets the value from a key as an integer. Same behavior applies as getValue.
    
    defaultValue is assumed to be an integer.
    '''
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = str(defaultValue)
    
    return float(getValue(key, myDefaultValue))

def setInt(key, value, defaultValue=None):
    '''
    Sets the value of a key using an integer. Same behavior applies as setValue.
    
    defaultValue is assumed to be an integer.
    '''
    myValue = str(value)
    myDefaultValue = defaultValue
    if defaultValue is not None:
        myDefaultValue = str(defaultValue)
    
    setValue(key, myValue, myDefaultValue)

def load(filePath):
    '''
    Loads the configuration to file.
    '''
    #print 'Loading configuration file...'
    try:
        with open(filePath, 'r') as f:
            root = etree.fromstring(f.read())
        
        for e in root:
            key = e.tag
            value = e.xpath('.//Value')[0].text
            defaultValue = e.xpath('.//Default')[0].text
            setValue(key, value, defaultValue)
            
    except Exception as e:
        print 'Problem reading configuration from file:', e

def save(filePath):
    '''
    Saves the configuration to file.
    '''
    #print 'Saving configuration file...'
    
    root = etree.Element('Configuration')
    
    for k in _CONFIG_DATA.keys():
        elem = etree.SubElement(root, k)
        value = etree.SubElement(elem, 'Value')
        value.text = _CONFIG_DATA[k][0]
        defaultValue = etree.SubElement(elem, 'Default')
        defaultValue.text = _CONFIG_DATA[k][1]

    if not os.path.exists(os.path.dirname(filePath)):
        os.makedirs(os.path.dirname(filePath))
    
    with open(filePath, 'w') as f:
        f.write(etree.tostring(root))
        
# ------------------------------------------------------------------------------
#
# USEFUL UTILITIES
#
# ------------------------------------------------------------------------------

def getReport():
    '''
    Returns a formatted string reporting on the setting values. Can be used
    for bug reports and things of that nature.
    '''
    out = 'Configuration:\n'
    out += '--------------\n'
    
    for k in _CONFIG_DATA.keys():
        out += ' - ' + k + ': ' + _CONFIG_DATA[k][0] + ', [default: ' + _CONFIG_DATA[k][1] + ']\n'
        
    return out

def getRGBStringFromQColor(color):
    return 'rgb(' + str(color.red()) + ','+ str(color.green()) +',' + str(color.blue()) + ')'

def getCSS():
    '''
    Gets the CSS associated with the configuration. Returns the CSS as a string.
    '''
    contentTextColor = 'rgb(' + getValue('ContentTextColor', '255,255,255') + ')'
    contentBackgroundColor = 'rgb(' + getValue('ContentBackgroundColor', '0,0,0') + ')'
    
    highlightTextColor = 'rgb(' + getValue('HighlightTextColor', '0,0,0') + ')'
    highlightBackgroundColor = 'rgb(' + getValue('HighlightBackgroundColor', '255,255,0') + ')'
    
    highlightLineTextColor = 'rgb(' + getValue('HighlightLineTextColor', '0,0,0') + ')'
    highlightLineBackgroundColor = 'rgb(' + getValue('HighlightLineBackgroundColor', '0,255,0') + ')'
    
    # If text highlighting is disabled, I will give it a completely clear
    # background to imitate that it is off.
    myHighlightText = ''
    myHighlightBackground = ''
    
    if getBool('HighlightTextEnable', True):
        myHighlightText = 'rgb(' + getValue('HighlightTextColor', '0,0,0') + ')'
        myHighlightBackground = 'rgb(' + getValue('HighlightBackgroundColor', '255,255,0') + ')'
    else:
        if getBool('HighlightLineEnable', True):
            myHighlightText = 'rgb(' + getValue('ContentTextColor', '255,255,255') + ')'
        else:
            myHighlightText = 'rgb(' + getValue('HighlightLineTextColor', '0,0,0') + ')'
        myHighlightBackground = 'transparent'
        
    # BEGIN CSS FILE
    # -------------------------------------------
    
    outtext = '''
body
{
background: ''' + contentBackgroundColor + ''';
color: ''' + contentTextColor + ''';
font-size: 12pt;
font-family: "''' + getValue('Font', 'Arial') + '''";
}

::selection {
    background: ''' + highlightBackgroundColor + ''';
    color: ''' + highlightTextColor + ''';
}

h1
{
color: ''' + contentTextColor + ''';
text-align: center;
font-size: 300%;
}

h2
{
color: ''' + contentTextColor + ''';
border-style: dashed;
border-width: 0px 0px 1px 0px;
border-color: ''' + contentTextColor + ''';
padding: 15px;
font-size: 200%;
}

h3
{
color: ''' + contentTextColor + ''';
padding: 10px;
font-size: 175%;
}

h4
{
color: ''' + contentTextColor + ''';
font-size: 150%;
}

p
{
color: ''' + contentTextColor + ''';
}

a:link
{
color: ''' + highlightLineBackgroundColor + ''';
}

a:visited
{
color: ''' + highlightLineBackgroundColor + ''';
}

a:hover
{
color: ''' + highlightBackgroundColor + ''';
}

a:active
{
color: ''' + contentTextColor + ''';
}

a.button {
text-decoration: none;
padding: 10px 15px;
margin: 10px;
background: ''' + contentBackgroundColor + ''';
color: ''' + contentTextColor + ''';
-webkit-border-radius: 4px;
-moz-border-radius: 4px;
border-radius: 4px;
border: solid 1px ''' + contentTextColor + ''';
text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.4);
-webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
-moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 1px 1px rgba(0, 0, 0, 0.2);
-webkit-transition-duration: 0.2s;
-moz-transition-duration: 0.2s;
transition-duration: 0.2s;
-webkit-user-select:none;
-moz-user-select:none;
-ms-user-select:none;
user-select:none;
}

a.button:hover {
background: ''' + highlightBackgroundColor + ''';
color: ''' + highlightTextColor + ''';
border: solid 1px #2A4E77;
}

a.button:active {
-webkit-box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
-moz-box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
background: ''' + highlightLineBackgroundColor + ''';
color: ''' + highlightLineTextColor + ''';
box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.6);
border: solid 1px
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
border: 1px solid ''' + contentTextColor + ''';
padding: 15px;
}

.mathmlEquation
{
}

.pageNumber
{
border-style:solid;
border-width: 1px 0px 0px 0px;
padding: 5px 0px 0px 25px;
font-size: 150%;
}

h6
{
border-style:solid;
border-width: 1px 0px 0px 0px;
padding: 5px 0px 0px 25px;
font-size: 150%;
}

.ui-tooltip 
{
background: ''' + contentBackgroundColor + ''';
border: 2px solid ''' + contentTextColor + ''';
padding: 10px 20px;
margin-left: 10px;
color: ''' + contentTextColor + ''';
border-radius: 20px;
box-shadow: 0 0 7px ''' + contentTextColor + ''';
-webkit-user-select: none;
-moz-user-select: -moz-none;
}

#npaHighlightLine
{
background-color: ''' + highlightLineBackgroundColor + ''';
color: ''' + highlightLineTextColor + ''';
-webkit-border-radius: 5px;
}

#npaHighlight
{
background-color: ''' + myHighlightBackground + ''';
color: ''' + myHighlightText + ''';
-webkit-border-radius: 3px;
display: inline-block;
z-index: 2;
}

#npaHighlightSelection
{
background-color: ''' + highlightBackgroundColor + ''';
color: ''' + highlightTextColor + ''';
-webkit-border-radius: 3px;
display: inline-block;
z-index: 2;
}

.table-of-contents
{
border: 1px dashed white;
padding: 1em;
}

.table-of-contents h1
{
text-align: left;
font-size: 1.5em;
}
'''
    # -------------------------------------------
    # END CSS FILE
    
    return outtext