'''
Created on Dec 12, 2013

@author: Spencer Graffe
'''
import datetime

import feedparser
from PyQt5.QtCore import QThread, pyqtSignal
from time import mktime

from car.document.rss.rss_document import RSSDocument
from car.gui import configuration

ANNOUNCEMENT_RSS_URL = 'http://centralaccessreader.blogspot.com/feeds/posts/default'

class AnnouncementPullThread(QThread):
    '''
    This thread checks to see if there are any new announcements in our RSS
    thread. If there are, it will prepare a document for it and send it out
    on its signal.
    '''
    
    # object - Document containing announcement
    gotAnnouncement = pyqtSignal(object)

    def __init__(self):
        QThread.__init__(self)
        
    def run(self):
        self.setPriority(QThread.LowestPriority)
        QThread.yieldCurrentThread()
        
        d = feedparser.parse(ANNOUNCEMENT_RSS_URL)
        lastUpdated = datetime.datetime.fromtimestamp(mktime(d.updated_parsed))
        
        defaultTime = datetime.datetime(year=1980, month=1, day=1)
        pulledTime = configuration.getDate('AnnouncementsLastPulled', defaultTime)
        
        if lastUpdated > pulledTime:
            doc = RSSDocument('', None, None, rssUrl=ANNOUNCEMENT_RSS_URL, title='Announcements')
            
            # Add a day to the last time updated so we don't have it pop up
            # everytime on the same day
            lastUpdated += datetime.timedelta(days=1)
            
            # Set that I have pulled from that last updated time
            configuration.setDate('AnnouncementsLastPulled', lastUpdated)
            
            self.gotAnnouncement.emit(doc)