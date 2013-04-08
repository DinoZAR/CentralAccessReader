'''
Created on Apr 8, 2013

@author: Spencer Graffe
'''
from PyQt4.QtCore import QThread

class SpeechWorker(QThread):
    
    def __init__(self, outputList, webView, ttsEngine, repeat=False):
        QThread.__init__(self)
        self.outputList = outputList
        self.webView = webView
        self.ttsEngine = ttsEngine
        self.start = True
        self.stop = False
        self.repeat = repeat
        self.lastElement = ["text", 0, 0]
    
    def run(self):
        for o in self.outputList:
            self.ttsEngine.say(text=o[0], name=o[1])
        
        self.ttsEngine.runAndWait()
        
        # Clear the highlight when done
        self.webView.page().mainFrame().evaluateJavaScript('ClearHighlight();')
        
    def onWord(self, name, location, length):
        print name, location, length
        if self.start:
            self.webView.page().mainFrame().evaluateJavaScript('SetBeginning();')
            self.start = False
        else:
            
            if name == "text":
                if name != self.lastElement[0] or (location != self.lastElement[1]):
                    self.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement();')
            elif name == "math":
                if name != self.lastElement[0]:
                    self.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement();')
            elif name == "image":
                if name != self.lastElement[0]:
                    self.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement();')
            else:
                self.webView.page().mainFrame().evaluateJavaScript('HighlightNextElement();')
            
        # Store what the last element was that was being spoken
        self.lastElement = [name, location, length]
        
        if self.stop:
            #print 'Stopping...'
            self.repeat = False
            self.ttsEngine.stop()
            self.stop = False
            self.webView.page().mainFrame().evaluateJavaScript('ClearHighlight();')