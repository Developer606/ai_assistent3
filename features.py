import webbrowser as web
import os 
import wikipedia


import pyttsx3
import pywhatkit
def say(Text):
   mouths = pyttsx3.init('sapi5')
   voices = mouths.getProperty('voices')
   mouths.setProperty('voice',voices[1].id)
   mouths.setProperty('rate',160)
   print(f"alisa:{Text}")
   mouths.say(text= Text)
   mouths.runAndWait()

def YoutubeScherch(term):
    result = "https://www.youtube.com/results?search_query="+ term
    web.open(result)
    say("this is what am i find for you ")
    pywhatkit.playonyt(term)
    say("that is also help you ")

YoutubeScherch('robotics')

