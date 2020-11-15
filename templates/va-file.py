import pyttsx3
import speech_recognition as sr
import webbrowser   
import datetime
import wikipedia
from googleapiclient import discovery
from googleapiclient.discovery import build
from googleapiclient import errors
from google.auth.transport.requests import Request
import datefinder
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pickle
scopes=['https://www.googleapis.com/auth/calendar.events']
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes=scopes)

try:
    credentials = pickle.load(open("token.pkl", "rb"))
except Exception :
#     speak('please follow this link to allow jarvis to vreate evnts')
    print('please follow this link to allow jarvis to vreate evnts\n')
#     speak('Copy and paste the token to autorize the app')
    print('Copy and paste the token to autorize the app\n')
    credentials = flow.run_console()
    pickle.dump(credentials, open("token.pkl", "wb"))

servicecal = build("calendar", "v3", credentials=credentials)


#opening google classrom
#and calender
#little bit about the assistant
#and check the final elif statement
#check open application,model of excel and word

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
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Excel 2010.lnk')
        return
    elif "powerpoint" in input:
        speak("Opening Microsoft PowerPoint")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft PowerPoint 2010.lnk')

    else:

        speak("Application not available")
        return

def takeCommand(): 

  

    r = sr.Recognizer() 

  

    # from the speech_Recognition module  

    # we will use the Microphone module 

    # for listening the command 

    with sr.Microphone() as source: 

        print('Listening') 

          

        # seconds of non-speaking audio before  

        # a phrase is considered complete 

        r.pause_threshold = 0.7

        audio = r.listen(source) 

          

        # Now we will be using the try and catch 

        # method so that if sound is recognized  

        # it is good else we will have exception  

        # handling 

        try: 

            print("Recognizing") 

              

            # for Listening the command in indian 

            # english we can also use 'hi-In'  

            # for hindi recognizing 

            Query = r.recognize_google(audio, language='en-in') 

            print("the command is printed=", Query) 

              

        except Exception as e: 

            print(e) 

            print("Say that again sir") 

            return "None"

          

        return Query 

def speak(audio): 

      

    engine = pyttsx3.init() 

    # getter method(gets the current value 

    # of engine property) 

    voices = engine.getProperty('voices') 

      

    # setter method .[0]=male voice and  

    # [1]=female voice in set Property. 

    engine.setProperty('voice', voices[0].id) 

      

    # Method for the speaking of the the assistant 

    engine.say(audio)   

      

    # Blocks while processing all the currently 

    # queued commands 

    engine.runAndWait()
def view_event():
    result = servicecal.events().list(calendarId='primary',orderBy='updated').execute()
    for i in range(len(result)):
        print('Summary : '+result['items'][i]['summary'])
        try:
            print('Description : '+result['items'][i]['description'])
        except Exception:
            print('No description available')
        try:
            print('Starts at : '+result['items'][i]['start']['dateTime']+'\n')
        except Exception:
            print('No start time found')
# view_event()

def create_event(start_time_str, summary, duration=1, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)
    
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return servicecal.events().insert(calendarId='primary', body=event).execute()

def crcal():
    x=input('Enter the date and time exapmle : 10 july 2PM')
    y=input('Enter teh Event Name  ')
    if create_event(x, y):
        print('You will be notified 1 day before via mail, and ten minutes before the event via popup')
        return True

def tellDay(): 

      

    # This function is for telling the 

    # day of the week 

    day = datetime.datetime.today().weekday() + 1

      

    #this line tells us about the number  

    # that will help us in telling the day 

    Day_dict = {1: 'Monday', 2: 'Tuesday',  

                3: 'Wednesday', 4: 'Thursday',  

                5: 'Friday', 6: 'Saturday', 

                7: 'Sunday'} 

      

    if day in Day_dict.keys(): 

        day_of_the_week = Day_dict[day] 

        print(day_of_the_week) 

        speak("The day is " + day_of_the_week) 

  

  

def tellTime(): 

      

    # This method will give the time 

    time = str(datetime.datetime.now()) 

      

    # the time will be displayed like  

    # this "2020-06-05 17:50:14.582630" 

    #nd then after slicing we can get time 

    print(time) 

    hour = time[11:13] 

    min = time[14:16] 

    speak("The time is sir" + hour + "Hours and" + min + "Minutes")     
    
def Hello(): 

      

    # This function is for when the assistant  

    # is called it will say hello and then  

    # take query 

    speak("hello sir I am your desktop assistant.Tell me how may I help you") 

  

  

def Take_query(): 

  

    # calling the Hello function for  

    # making it more interactive 

    Hello() 

      

    # This loop is infinite as it will take 

    # our queries continuously until and unless 

    # we do not say bye to exit or terminate  

    # the program 

    while(True): 

          

        # taking the query and making it into 

        # lower case so that most of the times  

        # query matches and we get the perfect  

        # output 

        query = takeCommand().lower() 

        if "open geeksforgeeks" in query: 

            speak("Opening GeeksforGeeks ") 

              

            # in the open method we just to give the link 

            # of the website and it automatically open  

            # it in your default browser 

            webbrowser.open("www.geeksforgeeks.com") 

            continue

          

        elif "search" in query: 

            speak("Opening Google")
            query = query.replace("search","")

            webbrowser.open("https://www.google.com/search?q=" +query) 

            continue
         
        elif "in youtube" in query: 

            speak("Opening youtube")
            query = query.replace("in youtube","")
           

            webbrowser.open("https://www.youtube.com/results?search_query="+query)
        
        elif "in stackoverflow" in query: 

            speak("Opening stackoverflow")
            query = query.replace("in stackoverflow","")
           

            webbrowser.open("https://stackoverflow.com/questions/tagged/"+query) 

            continue
    
        elif "youtube" in query: 

            speak("Opening youtube")
           

            webbrowser.open("https://www.youtube.com") 

            continue
        
        elif "open google" in query: 

            speak("Opening Google")
            webbrowser.open("https://www.Google.com") 

            continue

        elif "open classroom" in query: 

            speak("Opening Google Classroom")
            webbrowser.open("https://classroom.google.com/u/0/h")
            continue      

        elif "which day it is" in query: 

            tellDay() 

            continue
        
        elif 'reminder'in query or 'event' in query:
            if crcal():
                speak('Event Created Successfully')
                speak('You will be notified 1 day before via mail, and ten minutes before the event via popup')
            else:
                speak('There was a problem while creating an event')

          

        elif "tell me the time" in query: 

            tellTime() 

            continue

          

        # this will exit and terminate the program 

        elif "bye" in query: 

            speak("Bye and please take care") 

            break

          

        elif "from wikipedia" in query: 

              

            # if any one wants to have a information 

            # from wikipedia 

            speak("Checking the wikipedia ") 

            query = query.replace("wikipedia", "") 

              

            # it will give the summary of 4 lines from  

            # wikipedia we can increase and decrease  

            # it also. 

            result = wikipedia.summary(query, sentences=4) 

            speak("According to wikipedia") 

            speak(result) 
        elif 'open' in query:
            open_application(query.lower())
            
            continue
          

        elif "tell me your name"  in query: 

            speak("I am Jarvis. Your deskstop Assistant")
        
        elif "what can you do" in query: 
            speak ("Hello, I am jarvis. Your personal Assistant. I am here to make your life easier,and help you with your studies i can search for you on wikepedia,youtube,google,and open application like word,excel.") 
        
if __name__ == '__main__':
        Take_query()





