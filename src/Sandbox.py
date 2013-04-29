'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
from src.docx.importer import DocxDocument
import pythoncom
import win32com.client

if __name__ == '__main__':
    
#     testPath = 'tests\\Chapter 3 Test.docx'
#     
#     mydoc = DocxDocument(testPath)
#     
#     print 'Done!'

    pythoncom.CoInitialize()
    
    saveFileStream = win32com.client.Dispatch('SAPI.SpFileStream')
    saveFileStream.Open('C:\\Users\\GraffeS\\Desktop\\speech.wav', 3)
    
    voice = win32com.client.Dispatch('SAPI.SpVoice')
    voice.AudioOutputStream = saveFileStream
    
    print 'Speaking the speech...'
    voice.Speak('Your mom goes to college!', 0)
    
    print 'Waiting till completion...'
    voice.WaitUntilDone(10000)
    
    print 'Closing stream...'
    saveFileStream.Close()
    
    print 'Done!'