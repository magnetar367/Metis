#Metis abilities
import webbrowser
import pywhatkit
import datetime
import random

#1) Abilities Using webbrowser

def search(website):#implemented
    url = f"{website}.com"
    chromepath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    return webbrowser.get("chrome").open_new(url)


def news():#implemented
    return webbrowser.open_new("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen")

#2) Abilities Using pywhatkit
def music(song):#implemented
    pywhatkit.playonyt(song)

def googlesearch(site):#implemented
    return pywhatkit.search(site)

#3) Abilities using datetime function from datetime module
def cur_date_time(msg):#implemented
    e = datetime.datetime.now()
    if "date" in msg and "time" in msg:
        return "Current date is %s/%s/%s & current time is %s/%s/%s" % (e.day,e.month,e.year,e.hour,e.minute,e.second)
    elif "date" in msg:
        return "Current date is %s/%s/%s" % (e.day,e.month,e.year)
    else:
        return "Current time is %s/%s/%s" % (e.hour, e.minute, e.second)

#4) Abilities to Answer personal question
def byebye():
    return "I hope you enjoyed using me as much as I did helping you....So thank you:). I will see you when I see you."

def gratitude():
    return random.choice(gratitudes)

def greeting():
    return random.choice(greetings)
#Removing unneccessary special characters for search algo

chrbrwser = ["chr","google"]

#Task list
def dont_know():
    tasklist = '''Sorry, can't help you with that. Recheck your spelling & try again. Here is a list of my abilities
                 1: "To open a website directly",
                 2: "Fill your ears with some sick music",
                 3: "To google search something",
                 4: "Show you today\'s highlights and updates",
                 5: "Display current date and time",
                    '''
    return tasklist
def powers():
    tasklist = '''Here is a list of what I can do
                    1: "To open a website directly",
                    2: "Fill your ears with some sick music",
                    3: "To google search something",
                    4: "Show you today\'s highlights and updates",
                    5: "Display current date and time",
                       '''
    return tasklist
#Keyword List
keyword =     {1: ["open","access","take me","enter","1"],
               2: ["hear","listen","play",'2'],
               3: ["google","search",'3'],
               4: ["highlights", "updates", "news", "4"],
               5: ["date", "time", "6"],
               6: ["leave", "bye", "good night", "seeya", "take care", "close", "terminate", "stop", "nothing",
                    "leaving", "going" , "ttyl"],
               7:["powers", "abilities", "features","what can yo do", "what have you got?"],
               8:["great","awsome","fantastic","thank you","thanks","wow","cool","best"],
               #9:["hey","hai","hello","Whats up?", "hi","how are you"]
               }

gratitudes=["I'm so excited to do more;)","My plesaure_/\\_","Always at your service:D","You are welcome:)"]

greetings=["Heyyy!","Nice to meet you earthling.","Hai","Hey there!","hi"]












