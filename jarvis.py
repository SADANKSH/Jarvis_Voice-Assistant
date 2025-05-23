import pyttsx3
import datetime 
import webbrowser
import os
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis, your personal assistant. How can I help you today?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Please say it again.")
        return "None"
    return query

def action(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'exit' in query:
        speak("Goodbye Sir")
        exit()
        

if __name__=='__main__':
   wishMe()
   while True:
        query =takeCommand().lower()
        action(query)