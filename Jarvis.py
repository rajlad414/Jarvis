import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
from urllib.request import urlopen
import wolframalpha  
import time

wolframalpha_app_id="46YH7X-URPG7L2G8L"
engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #I for 12 hr clock and H for 24 hr clock
    speak("The Current time is")
    speak(Time)
def date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak("Today is "+str(day)+" "+str(month)+" "+str(year))

def wishMe():
    speak("Welcome Raj!")
    hour=datetime.datetime.now().hour
    if hour in range(0,12):
        speak("Good Morning")
    elif hour in range(12,18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Jarvis at your service Raj, How can i help you?")

def Introduction():
    speak("I am JARVIS, Personal AI assistant , "
    "I am created by Raj , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def Creator():
    speak("Raj is an extra-ordinary person ,"
        +"He has a very cute smile,"+
        "he is very touched to his work and passion."+
        "He is very kind and inosnet man. Loves and care for everyone everyone ")

    
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-US")
        print(query)
    except Exception as e:
        print(e)
        print("Could not recognized it..")
        print("say that again please..")
        return None
    return query

def send_email(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("2rajlad@gmail.com","9727130190")
    server.sendmail("2rajlad@gmail.com",to,content)
    server.close()
    
def cpu():
    usage=str(psutil.cpu_percent())
    speak("C P U is at "+usage+" percent usage")
    battery=psutil.sensors_battery()
    speak("And the Battery is at "+str(battery.percent)+ " Percentage")
    
if __name__=="__main__":
    wishMe()
    while True:
        query=take_command().lower()
        if "date" in query:
            date()
            
        elif "time" in query:
            time()
            
        elif "greet me" in query:
            wishMe()
            
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine Sir")
            else:
                speak("I hope you get well soon.")
                
        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 
            
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("I love you too dear!!")
            
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()
            
        elif 'tell me about raj' and 'creator' in query:
            Creator()
        
        elif "send email" in query:
            try:
                speak("What do i say??")
                content=take_command().lower()
                speak("who is the receiver??")
                query=take_command().lower()
                if "default":
                    receiver="1rajlad@gmail.com"
                    to=receiver
                    send_email(to,content)
                speak("The content of the mail is ",content)
                speak("Email has been successfull sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
                speak("try again later.")
                
        elif "microsoft office word" in query or "microsoft word" in query or "wordpad" in query:
            speak("Opening Microsoft Office Word")
            dir= r"C:/Program Files (x86)/Microsoft Office/Office12/WINWORD.EXE"
            os.startfile(dir)
                
        elif "browser" in query or "browse" in query:
            speak("what do want to browse sir?")
            search=take_command().lower()
            wb.open_new_tab(search)
            
        elif "note" in query or "notes" in query:
            speak("What should I note sir?")
            notes=take_command()
            file=open('notes.txt','a')
            speak("sir should I note date and time")
            ans=take_command()
            if 'yes' in ans or "sure" in ans or "yeah" in ans:
                time=Time=datetime.datetime.now().strftime("%I:%M:%S")
                year=datetime.datetime.now().year
                month=datetime.datetime.now().month
                day=datetime.datetime.now().day
                file.write("On "+day+" "+month+" "+year+" ")
                file.write("time = "+time)
                file.write(notes)
                speak("Done Sir")
                file.close()
            else:
                file.write(notes)
                speak("Done Sir!")
                file.close()
        
        elif "show note" in query or "show notes" in query:
            speak("showing Notes Sir.")
            file=file.open('notes.txt')
            # speak(file.read())
            ff=""
            for f in file:
                ff+=f
            speak(ff)
            file.close()
            
        elif "calculate" in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            indx=query.lower().split().index('calculate')
            query=query.split()[indx + 1 :]
            res=client.query(''.join(query))
            answer=next(res.results).text
            speak("the answer is :"+answer)
                
        elif "remember that" in query:
            speak("What do I remeber sir?")
            memory=take_command()
            speak("You Asked me to remember that "+memory)
            ans=take_command().lower()
            while "no" in ans:
                speak("What do I remeber sir?")
                memory=take_command()
                speak("You Asked me to remember that "+memory)
                ans=take_command().lower()
            remeber=open("remember.txt","w")
            remeber.write(memory)
            remeber.close()
        
        elif "do you remember" in query or "you remeber" in query:
            speak("Yes Sir I do remeber.")
            file=open('remember.txt','r')
            speak("Yot told me to remember that:")
            speak(file.read())
            file.close()
            
        elif "youtube" in query:
            speak("what do want to watch sir?")
            search=take_command().lower()
            wb.open_new_tab("https://www.youtube.com/results?search_query="+search)
            
        elif "cpu" in query or "pc" in query:
            cpu()
            
        elif "news" in query:
            try:
                jsonObj=urlopen("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ad36ba535d4844b5ae1f7f2f7f9b19e9")
                data=json.load(jsonObj)
                i=1
                speak("Here are some top Headlines for today")
                print("=======Top HeadLines=======")
                for item in data['articles']:
                    print(str(i)+'. '+item['title'])
                    print(item['description'])
                    speak(item['title'])
                    i+=1
            except Exception as e:
                print(str(e))
            
        elif "joke" in query or "comedy" in query:
            speak("Here is the joke sir:")
            speak(pyjokes.get_joke())
            
        elif "where is" in query:
            query=query.replace("where is ","")
            speak("You asked me to search where is "+query)
            wb.open_new_tab("http://www.google.com/maps/place/"+query)
            
        elif "screenshot" in query:
            img=pyautogui.screenshot()
            img.save('./image/screenshot.jpg')
        
        elif "music" in query or "song" in query:
            speak("Here is the list of songs sir")
            songs_dir='C:/Users/rajla/English/'
            music=os.listdir(songs_dir)
            count=1
            for i in music:
                print(count,end=" ")
                count+=1
                print(i)
            speak("What should I play sir? Please Select a number sir")
            ans=take_command().lower()
            if "random" in ans or "any" in ans or "your choice" in ans or "you choose" in ans:
                no=random.randint(0, count)
            else:
                no=int(ans.replace('number',''))
            os.startfile(os.path.join(songs_dir,music[no+1]))
            
        elif "what" in query or "where" in query or "why" in query or "how" in query or "when" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
       
        elif "go offline jarvis" in query:
            speak("Going offline Sir!! Thank you.")
            quit()
        
        elif "shutdown the PC" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart the PC" in query:
            os.system("shutdown /r /t 1")
        