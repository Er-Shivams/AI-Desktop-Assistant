import pyttsx3  #pip install pyttsx3 in cmd
import webbrowser
import smtplib
import random
import speech_recognition as sr                      #pip install pipwin(cmd) pip install SpeechRecognition  #pipwin install pyaudio   
import wikipedia #pip install wikipedia in cmd
import datetime
import wolframalpha #pip install wolframalpha in cmd
import os
import sys

engine = pyttsx3.init('sapi5') # for this do  pip install pypiwin32

client = wolframalpha.Client('U8T7R3-RP9T968R42') # go to the wolframalpha site and do login then from my app take your Appid. 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
        
def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greet_Me():
    current_Hour = int(datetime.datetime.now().hour)
    if current_Hour >= 0 and current_Hour < 12:
        speak('Good Morning!, Sir')

    if current_Hour >= 12 and current_Hour < 18:
        speak('Good Afternoon!, Sir')

    if current_Hour >= 18 and current_Hour !=0:
        speak('Good Evening!, Sir')

greet_Me()
speak('I am your digital assistant Jarvis!')
speak('How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:             
        r.pause_threshold =  1                            
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Me: ' + query + '\n')  # or use f string 
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Please type the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':
    
    while True:
    
        query = myCommand()
        query = query.lower()
    
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query: 
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, Have a good day!.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')
        elif 'bye' in query:
            speak('Bye Sir, Have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = 'F:\\video songs'
            songs = os.listdir(music_folder)
            speak('Okay, here is your music! Enjoy!')
            os.startfile(os.path.join(music_folder, random.choice(songs)))
            random_music = music_folder + random.choice(songs) + '.mp4'
        
                  
            
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=3)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command!, Sir!')