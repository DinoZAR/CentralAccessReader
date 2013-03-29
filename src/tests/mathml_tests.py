'''
Created on Jan 25, 2013

@author: Spencer Graffe
'''
import src.mathml.tts as MathTTS


def main():
    
    # Read my test MathML from my text file
    txt = open('testMathML.txt', 'r')
    mathmlString = txt.read();
    
    # Get the natural reading string from my MathML
    readingString = MathTTS.parse(mathmlString)
    
    # Print and audibly read it (once I have it anyway)
    print readingString

if __name__ == '__main__':
    main()