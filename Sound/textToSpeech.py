#First import pyttsx3 after installing using pip install pyttsx3
import pyttsx3 as pyt;
e = pyt.init()
e.say("Hello there!")
e.runAndWait() 

#List all availablle voices
voices = e.getProperty('voices')
for each in voices: print(str(voices))

#Set another voice
e.setProperty('voice', voices[1].id)
e.say("General Kenobi!")
e.runAndWait()
