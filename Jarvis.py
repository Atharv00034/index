import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import pyowm
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def whoAreYou():
    input(f"What is your name")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning sir")

    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("I am jarvis a intelligent program made by Atharv. Please tell how may I help you")


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
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Harish Bansal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'hello' in query:
            speak("hello")

        elif 'when is your birthday' in query:
            speak("4 June")

        elif 'how are you' in query:
            speak("i am fine and how about you ")

        elif 'very good' in query:
            speak("thank you")

        elif 'what are you doing' in query:
            speak("just trying to help you")

        elif 'who made you' in query:
            speak("Atharv bansal")

        elif 'who are you' in query:
            speak("i am a smart software named jarvis made by Atharv")

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\chrome.exe"
            os.startfile(chromePath)

        elif 'what is your name' in query:
            speak("my name is jarvis")

        elif 'exit' in query:
            speak("have a good day sir")
            exit()

        elif 'search' in query:
            sr.Microphone(device_index=1)

            r = sr.Recognizer()

            r.energy_threshold = 1000

            with sr.Microphone() as source:
                speak("Speak")
                audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said:".format(text))
                url = 'https://www.google.com/search?q='
                search_url = url+text
                webbrowser.open(search_url)
            except:
                print("Can't recognise")