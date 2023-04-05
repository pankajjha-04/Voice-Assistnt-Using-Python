import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello! I'm your personal assistant. How may I assist you?")


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
        print(e)
        speak("Sorry, I didn't get that. Can you please say that again?")
        return "none"
    return query


def calculator(query):
    operators = {'plus': '+', 'minus': '-', 'times': '*', 'divided by': '/', 'mod': '%'}
    for word, operator in operators.items():
        if word in query:
            num_list = query.split(word)
            if len(num_list) >= 2 and num_list[0].strip() and num_list[1].strip():
                num1 = int(num_list[0].strip())
                num2 = int(num_list[1].strip())
                result = eval(str(num1) + operator + str(num2))
                return f"The result of {num1} {word} {num2} is {result}"
            else:
                return "Sorry, I could not find two valid numbers to perform the arithmetic operation."
    return "Sorry, I did not understand the arithmetic operation you requested."



def takeCommand(timeout=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=timeout)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Sorry, I didn't get that. Can you please say that again?")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'calculate' in query:
            speak("What arithmetic operation would you like me to perform?")
            query = takeCommand(timeout=5).lower()
            result = calculator(query)
            if result:
                speak(result)
            else:
                speak("Sorry, I did not understand the arithmetic operation you requested.")
                
        

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir/Madam, the time is {strTime}")
            print(strTime)

        elif 'how are you' in query:
            speak("I am fine. How can I help you?")
            print("I am fine. How can I help you?")

        elif 'open visual studio' in query:
            codePath = "C:/Users/Panka/AppData/Local/Programs/Microsoft VS Code/Code.exe"

            os.startfile(codePath)

        elif 'open notepad' in query:
            os.system('start notepad')

        elif 'open calculator' in query:
            os.system('calc')

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        elif 'please stop' in query:
            speak("Thank you for using me. Have a good day!")
            exit()
