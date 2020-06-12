import pyttsx3
import webbrowser
import speech_recognition as sr
import random
import wolframalpha
import wikipedia
import datetime
import os
import sys
from VideoPlayer import playVideo


engine=pyttsx3.init()
client = wolframalpha.Client('GAPU32-XTGXHHK2HH')

def speak(audio):
    print("CUTIE:"+ audio)
    engine.say(audio)
    engine.runAndWait()

def greet():
    ch=int(datetime.datetime.now().hour)
    if ch>=0 and ch<12:
        s=['pleasant morning','good morning','marvelous morning']
        speak(random.choice(s)+" my dear munnaf")

    if ch>=12 and ch<18:
        speak('good afternoon my dear munnaf')

    if ch>=18 and ch!=0:
        speak('good evening my dear munnaf')

greet()

#speak('hello munnaf! I am your digital assistant CUTIE ,lady assistant for singles ')
speak("how may I help you")

def myCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold =1.0
        audio = r.listen(source)

    try:
        query=r.recognize_google(audio,language='en-in')
        print("User:" + query +'\n')
    except sr.UnknownValueError:
        speak('Sorry Sir! I didn\'t get that! Try typing the command')
        query=str(input('Command:'))

    return query


if __name__=='__main__':
    while True:
        query=myCommand()
        query=query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'i want to search' in query or 'search' in query:
            speak('okay')
            speak("what would you like to search")
            que =myCommand()
            
            webbrowser.open('www.google.com/search?q='+ que)

        elif 'play video' in query:
            speak('okay')
            speak('name the video to play')
            que=myCommand()
            li=que.split()
            s="+"
            s1=s.join(li)
            playVideo(self.s1)
            #webbrowser.open('https://www.youtube.com/results?search_query='+s)
            

        elif 'open facebook' in query:
            speak('okay')
            webbrowser.open('www.facebook.com')

        elif 'I love you Cutie'in query or 'I love you'in query or 'be my girlfriend' in query:
            s=['sorry sir!,I am your assistant','I love you','I hate you']
            speak(random.choice(s))

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif "what\'s up" in query or 'how are you' in query:
            smgs=['Just doing my thing!','I am fine!','I am nice and full of energy']
            speak(random.choice(smgs))

        elif 'hello'in query or 'hi'in query or 'hai' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye sir!,have a good day.')
            sys.exit()
        else:
            query=query
            speak('Searching...')
            try:
                try:
                    res=client.query(query)
                    results=next(res.results).text
                    speak('WOLFRAM-ALPHA says -')
                    speak('Got it.')
                    speak(results)

                except:
                    results =wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says -')
                    speak(results)
            except:
                webbrowser.open('www.google.com')

        speak("Next Command Sir")
            





























        
