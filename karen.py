import pyttsx3  #pip install pyttsx3 , Import the pyttsx3 library for text-to-speech
import datetime
import speech_recognition as sr    #pip install SpeechRecognition , 

engine = pyttsx3.init() # Initialize the text-to-speech engine


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time  = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():
    year = str(datetime.datetime.now().year)
    month = datetime.datetime.now().strftime("%B")
    day = str(datetime.datetime.now().day)
    speak("The current date is ")
    speak(month + " " + day + " " + year)

def wishme():
    speak("Welcome back, sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning, sir")
    elif 12 <= hour < 15:
        speak("Good afternoon, sir")
    elif 15 <= hour < 18:
        speak("Good evening, sir")
    else:
        speak("Good night, sir")
    speak("Karen is at your service, sir. Please tell me how can I help you?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)


    try:
        print("Recognizing..")
        query = r.recognize_google(audio ,language='en-in')
        print(query)

    except Exception as e :
        print(e)
        speak("Say that again please...")


        return "None"

    return query


if __name__ == "__main__":
    wishme()

    while True :
        query = takeCommand().lower()

        if 'time' in query :
            time()

        elif 'date' in query :
            date()

        elif 'offline' in query :
            quit()







