import pyttsx3  #pip install pyttsx3 , Import the pyttsx3 library for text-to-speech
import datetime
import speech_recognition as sr    #pip install SpeechRecognition , 
import wikipedia  #pip install wikipedia , 
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes

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


def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("rohithkumar2424@gmail.com","arppzhdoxkebjvpl")
    server.sendmail('rohithkumar2424@gmail.com',to , content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at" + usage + "usage")
    
def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at" + battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()

    while True :
        query = takeCommand().lower()

        if 'time' in query :
            time()

        elif 'date' in query :
            date()

        elif 'wikipedia' in query :
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query :
            try :
                speak("what should i say ?")
                content = takeCommand()
                to = 'rohithkumar.k.2019.cse@ritchennai.edu.in'
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e :
                print(e)
                speak("unable to send email")

        elif 'search in chrome' in query :
            speak("what should i search for you ?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query :
            os.system("shutdown -1")

        elif 'shutdown' in query :
            os.system("shutdown /s /t 1")

        elif 'restart' in query :
            os.system("shutdown /r /t 1")

        elif 'play songs' in query :
            songsDir = 'D:\songs'
            songs = os.listdir(songsDir)
            os.startfile(os.path.join(songsDir , songs[0]))

        elif 'remember that' in query :
            speak("what should i remember ?")
            data = takeCommand()
            speak("you said to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query :
            remember = open('data.txt','r')
            speak("you said me to remember that" + remember.read())

        elif 'screenshot' in query :
            screenshot()
            speak("Done!")

        elif 'cpu' in query :
            cpu()

        elif 'battery' in query :
            battery()

        elif 'joke' in query :
            jokes()

        elif 'offline' in query :
            quit()







