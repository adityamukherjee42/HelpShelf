from flask import Flask,render_template,redirect,url_for

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

import datefinder

from datetime import datetime, timedelta
import os

import pickle

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('Untitled-1.html')

@app.route('/weeklyplanner')
def wp():
    return render_template('2s.html')

@app.route('/stickynotes')
def sn():
    return render_template('asdf.html')

@app.route('/calculator')
def calc():
    return render_template('1.html')

@app.route("/voice_assistant")
def voice():



    def open_application(input):
        if "chrome" in input:
            speak("Google Chrome")
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            return

        elif "firefox" in input or "mozilla" in input:
            speak("Opening Mozilla Firefox")
            os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
            return

        elif "word" in input:
            speak("Opening Microsoft Word")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2010.lnk')
            return

        elif "excel" in input:
            speak("Opening Microsoft Excel")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Excel 2010.lnk')
            return
        elif "powerpoint" in input:
            speak("Opening Microsoft PowerPoint")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft PowerPoint 2010.lnk')

        else:

            speak("Application not available")
            return

    def takeCommand():

        r = sr.Recognizer()

        with sr.Microphone() as source:

            print('Listening')


            r.pause_threshold = 0.7

            audio = r.listen(source)


            try:

                print("Recognizing")


                Query = r.recognize_google(audio, language='en-in')

                print("the command is printed=", Query)



            except Exception as e:

                print(e)

                print("Say that again sir")

                return "None"

            return Query

    def speak(audio):

        engine = pyttsx3.init()



        voices = engine.getProperty('voices')



        engine.setProperty('voice', voices[0].id)



        engine.say(audio)



        engine.runAndWait()



    def tellDay():



        day = datetime.datetime.today().weekday() + 1



        Day_dict = {1: 'Monday', 2: 'Tuesday',

                    3: 'Wednesday', 4: 'Thursday',

                    5: 'Friday', 6: 'Saturday',

                    7: 'Sunday'}

        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]

            print(day_of_the_week)

            speak("The day is " + day_of_the_week)

    def tellTime():



        time = str(datetime.datetime.now())



        print(time)

        hour = time[11:13]

        min = time[14:16]

        speak("The time is sir" + hour + "Hours and" + min + "Minutes")

    def Hello():



        speak("hello sir I am your desktop assistant.Tell me how may I help you")

    def Take_query():



        Hello()


        while (True):



            query = takeCommand().lower()

            if "open geeksforgeeks" in query:

                speak("Opening GeeksforGeeks ")



                webbrowser.open("www.geeksforgeeks.com")

                break



            elif "search" in query:

                speak("Opening Google")
                query = query.replace("search", "")

                webbrowser.open("https://www.google.com/search?q=" + query)

                break

            elif "in youtube" in query:

                speak("Opening youtube")
                query = query.replace("in youtube", "")

                webbrowser.open("https://www.youtube.com/results?search_query=" + query)

            elif "in stackoverflow" in query:

                speak("Opening stackoverflow")
                query = query.replace("in stackoverflow", "")

                webbrowser.open("https://stackoverflow.com/questions/tagged/" + query)

                break

            elif "youtube" in query:

                speak("Opening youtube")

                webbrowser.open("https://www.youtube.com")

                break

            elif "open google" in query:

                speak("Opening Google")
                webbrowser.open("https://www.Google.com")

                break
            elif "open gmail" in query:

                speak("Opening Mail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

                break
            elif "open classroom" in query:

                speak("Opening Google Classroom")
                webbrowser.open("https://classroom.google.com/u/0/h")
                break

            elif "which day it is" in query:

                tellDay()

                break





            elif "tell me the time" in query:

                tellTime()

                break





            elif "bye" in query:

                speak("Bye and please take care")

                break



            elif "from wikipedia" in query:



                speak("Checking the wikipedia ")

                query = query.replace("wikipedia", "")



                result = wikipedia.summary(query, sentences=4)

                speak("According to wikipedia")

                speak(result)
            elif 'open' in query:
                open_application(query.lower())

                break


            elif "tell me your name" in query:

                speak("I am Neo. Your desktop Assistant")

            elif "what can you do" in query:
                speak("Hello, I am Neo. Your personal Assistant. I am here to make your life easier,and help you with your studies i can search for you on wikepedia,youtube,google,and open application like word,excel.")
    Take_query()


if __name__=='__main__':
    app.run(debug=True)