from multiprocessing.spawn import _main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe() :
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        #speak("Jay ShreeRram")
        speak("good morning")
       
    elif  hour>=12 and hour<=16:
        #speak("Jay ShreeRram") 
        speak("good afternoon")    
    else:
        #speak("Jay Shree Ram.")
        speak("good evening")
      
    speak("Hii, I am Chittti The Desktop Assistent. Tell me how may i helf you ")
def takecommand():

    #it take inputfrom user microphone and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recogniging....") 
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        #speak("Please say that again......")
        
        #speak("I didn't understand plz say that again......")
        return "None"
    return query
if  __name__ == "__main__":
    wishMe()
    while True:
        query=takecommand().lower()
        #logic for executing task
        
        if 'who are you' in query:
            a='I am Chittti The Desktop Assistent , i am created by sir vipin,Tell me how may i helf you'
            speak(a)
            print(a)

        elif 'wikipedia' in query:
            speak('wikipedia searching your request plz wait minimum 3min.....')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'google' in query:
            speak('google is searching your request.....')
            query=query.replace("google","")
            result=webbrowser.open('google.com/?#q=' +query)
            speak("Sir result is on screen")
            print(result)
            speak(result)       
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            speak('Opening youtue')
            webbrowser.open("youtube.com") 
        elif 'youtube' in query:
            speak('Youtube is searching your request.....')
            #query=query.replace("youtube","")
            kit.playonyt(query)
            speak("Sir result is on screen")      
        elif "what the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}") 
            print(strTime)
        elif 'play song' in query:
            speak("yes sir")
            music_dir='C:\\Users\\91750\\Music\\Playlists\\chitti song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'open code' in query:
            speak('yes sir')    
            code_path="C:\\Users\\91750\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'volume up' in query  or 'up the volume' in query  or 'up volume' in query or 'increse volume' in query or 'increse volume' in query:
            pyautogui.press("volumeup") 
        elif 'volume down' in query  or 'down the volume' in query  or 'down volume' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' in query  or 'mute the volume' in query  or "mute volume" in query:
            pyautogui.press("volumemute")        
             

    





       



