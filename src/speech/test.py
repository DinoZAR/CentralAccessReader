'''
Created on Apr 10, 2013

@author: GraffeS
'''

from driver import SAPIDriver
import time

def finished():
    print 'I\'m finished!'
    
def words(word, location, name):
    print 'Word:', word, location, name

if __name__ == '__main__':
    
    driver = SAPIDriver()
    
    handle1 = driver.connect('onWord', words)
    handle2 = driver.connect('onFinish', finished)
    
    driver.add('Your mom goes to college!', 'text')
    driver.add('Thing that you have ever seen. This is a lot of stuff about math.', 'math')
    
    driver.start()
    
    print 'After start!'
    
    time.sleep(3)
    
    print '---------------------------------'
    print 'Three seconds after start!'
    print 'Stopping...'
    print '---------------------------------'
    
    driver.stop()
    
    time.sleep(.5)
    
    driver.add('Your mom goes to college!', 'text')
    
    driver.start()
    
    driver.waitUntilDone()

    print 'Done!'