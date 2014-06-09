'''
Created on Mar 3, 2013

@author: Spencer Graffe
'''
import os
from cProfile import Profile

from car import math_library
from car.math_to_prose_fast.tts import MathTTS

def main():
    print 'Starting!'

    dumpPath = os.path.expanduser('~/Desktop/output.profile')

    myProf = Profile()

    myProf.runcall(profiledFunction)
    myProf.dump_stats(dumpPath)

    print 'Done!'

def profiledFunction():
    mathStuff = math_library.getLibraryFromPath(['CAR', 'General'])
    myMath = MathTTS()
    myMath.setMathLibrary(mathStuff[0], mathStuff[1])

# Just to protect this module when using a process pool
if __name__ == '__main__':
    main()