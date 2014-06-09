'''
Created on Dec 12, 2013

@author: Spencer Graffe
'''
from lxml import html
import re
import feedparser

from car.document import Document, html_cleaner

class RSSDocument(Document):
    '''
    This document pulls feeds from an RSS feed and aggregates them into a
    CAR-readable document.
    '''

    def __init__(self, filePath, progressHook, cancelHook, rssUrl='', title=''):
        '''
        Since this is a web source, it doesn't make much sense to specify a
        file path. For this case, set it to blank, or "".
        '''
        Document.__init__(self, filePath, progressHook, cancelHook)
        
        d = feedparser.parse(rssUrl)
        
        if len(title) > 0:
            self._name = title
        else:
            self._name = d.feed.title
        
        title = html.Element('h1')
        title.text = self._name
        self._contentDOM.append(title)
        
        for e in d.entries:
            elems = self._getEntryHTML(e)
            for el in elems:
                self._contentDOM.append(el)
        
        self._mapMathEquations()
        
    def _getEntryHTML(self, entry):
        '''
        Gets the HTML from the feed entry.
        '''
        elems = []
        
        # Title
        root = html.Element('h2')
        root.text = entry.title
        elems.append(root)
        
        # Author
        if 'author' in entry.keys():
            root = html.Element('p')
            
            # Check if it has an email inside parenthesis in the string
            pattern = r'[(].*[)]'
            badEmail = re.search(pattern, entry.author)
            if badEmail is not None:
                badEmail = badEmail.group()
            root.text = 'Author: ' + entry.author.replace(badEmail, '')
            elems.append(root)
        
        # Date Issued
        root = html.Element('p')
        root.text = 'Posted: ' + self._formatDate(entry.published_parsed)
        elems.append(root)
        
        # Content
        root = html.Element('p')
        contentRoot = html_cleaner.clean(html.fromstring(entry.summary))
        root.append(contentRoot)
        elems.append(root)
        
        return elems
    
    def _formatDate(self, parsedDate):
        '''
        Returns a string representing the data given by the Python 9-entry
        tuple.
        '''
        monthDict = {1 : 'January',
                     2 : 'February',
                     3 : 'March',
                     4 : 'April',
                     5 : 'May',
                     6 : 'June',
                     7 : 'July',
                     8 : 'August',
                     9 : 'September',
                     10 : 'October',
                     11 : 'November',
                     12 : 'December'}
        
        dayDict = {6 : 'Sunday',
                   0 : 'Monday',
                   1 : 'Tuesday',
                   2 : 'Wednesday',
                   3 : 'Thursday',
                   4 : 'Friday',
                   5 : 'Saturday'}
        
        # Day of the week
        s = dayDict[parsedDate[6]] + ', '
        
        # Month
        s += monthDict[parsedDate[1]] + ' '
        
        # Day (number)
        s += str(parsedDate[2]) + ', '
        
        # Year
        s += str(parsedDate[0])
        
        return s