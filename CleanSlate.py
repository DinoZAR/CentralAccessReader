'''
This script clears all of the temp files and user data. This works rather nicely
for testing to make sure that lack of data does not crash the configuration.

@author: Spencer Graffe
'''
from car import misc
import shutil

if __name__ == '__main__':

    # Clean out user data
    userDir = misc.app_data_path('')
    print 'Cleaning out user directory:', userDir
    shutil.rmtree(userDir)

    # Clean out temp
    tempDir = misc.temp_path('')
    print 'Cleaning out temp directory:', tempDir
    shutil.rmtree(tempDir)

    print 'Done!'