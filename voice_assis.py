import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

time = datetime.datetime.now().strftime("%I%M%p")
print(time)

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data.lower()

        except sr.UnknownValueError:
            return("Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    while True :

        data1 = sptext()

        if not data1:  
            speechtx("I couldn't hear you clearly. Please try again.")

        else:

            if 'your name' in data1:
                name = "My name is Guru but People call me Gaandu"
                speechtx(name)

            elif 'your friend' in data1:
                fnd = "My friend name is NANDHA"
                speechtx(fnd)

            elif 'old are you' in data1:
                age = 'Iam 22 years old'
                speechtx(age)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/watch?v=NvErfPpWvaY")

            elif 'exit' in data1:
                speechtx("Thank You")
            

            else:
                speechtx("Sorry")

