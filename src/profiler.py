'''
Created on Jul 10, 2013

Use this script to profile things

@author: Spencer Graffe
'''
from src.docx.importer import DocxDocument
import cProfile
import pstats

if __name__ == '__main__':
    
    #testFile = 'W:\\Nifty Prose Articulator\\test_files\\1244 Automotive Technician Entire Project.docx'
    testFile = 'W:\\Nifty Prose Articulator\\test_files\\Chs 6-11.docx'
    statSave = 'fun_stats.txt'
    
    def progress(percent):
        print ' --', percent, '--'
    
    cProfile.run('DocxDocument(testFile, progress)', filename=statSave)
    myStats = pstats.Stats(statSave)
    
    # Organize my stats by different criteria
    myStats.sort_stats('cumulative', 'name')
    #myStats.sort_stats('time', 'name')
    
    myStats.print_stats()
    