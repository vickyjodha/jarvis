import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("good Afternoon")
    elif hour >= 18 and hour < 21:
        speak("good Evening")
    else:
        speak("Good night")
    speak("I am Jarvis Sir . Please tell me how I help you ")


def takeCommend():
    # it takes microphone input from the user and returns output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("say that agen please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # email and password set google email less scury
    server.login('youremail', 'youepassword')
    server.sendmail('vs4110690@gmail.com', to, content)


if __name__ == "__main__":
    # speak("vikram singh")
    wishMe()
    while True:
        query = takeCommend().lower()

        # logic for exauting tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'G:\\Music\\01ghoomar1'
            songs = os.listdir(music_dir)
            # print(songs)
            # first song start
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(F"sir, the time is {strtime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommend()
                to = "vikeyjodha@gmail.com"
                sendEmail(to, content)
                speak("Email has be send!")
            except Exception as e:
                print(e)
                speak("sorry my friend Vikram Singh . i am not able to send this email")
        elif 'open chrome' in query:
            chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)
