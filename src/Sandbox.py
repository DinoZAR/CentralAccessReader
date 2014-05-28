'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''

def main():
    print 'Starting!'
    
    from src import math_library

    print math_library.getLibraries()
    
    print 'Done!'

# Just to protect this module when using a process pool
if __name__ == '__main__':
    main()