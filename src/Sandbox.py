'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
import os
import platform
import re
if __name__ == '__main__':
    
    percents = '        (100%)    '
    regular = r'\([0-9]+%\)'
    m = re.search(regular, percents)
    if m != None:
        print 'Got!', int(m.group(0)[1:-2])
    else:
        print 'Nothing...'