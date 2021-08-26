#Metis abilities
import webbrowser
import pywhatkit
import datetime
import random
import os
from tkinter import *
#1) Abilities Using webbrowser

def search(website):
    url = f"{website}.com"
    chromepath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
    return webbrowser.get("chrome").open_new(url)


def news():
    return webbrowser.open_new("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen")

#2) Abilities Using pywhatkit

def music(song):
    pywhatkit.playonyt(song)

def googlesearch(site):
    return pywhatkit.search(site)

#3) Abilities using datetime function from datetime module

def cur_date_time(msg):
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

def feeling():
    return random.choice(feelings)

#Task list
def dont_know():# if the user input something random with Metis is unable to perform
    tasklist = '''Sorry, can't help you with that. Recheck your spelling & try again. Here is a list of my abilities
                 1: "To open a website directly",
                 2: "Fill your ears with some sick music",
                 3: "To google search something",
                 4: "Show you today\'s highlights and updates",
                 5: "Display current date and time",
                 6: "Create a todo_list",        
                 7: "Read from that created list"
                 8: "Add elements to it"         
                 9: "Delete elements from it"    
                 10:"Do modifications like changing the spelling of a word or replacing the entire word"
                    '''
    return tasklist

def powers():
    tasklist = '''Here is a list of what I can do
                    1: "To open a website directly",
                    2: "Fill your ears with some sick music",
                    3: "To google search something",
                    4: "Show you today\'s highlights and updates",
                    5: "Display current date and time"
                    6: "Create a todo_list",
                    7: "Read from that created list"
                    8: "Add elements to it"
                    9: "Delete elements from it"
                    10:"Do modifications like changing the spelling of a word or replacing the entire word"
                       '''
    return tasklist
#Keyword List

keyword =     {1: ["open","access","take me","enter","1"],
               2: ["hear","listen","play",'2'],
               3: ["google","search",'3'],
               4: ["highlights", "updates", "news", "4"],
               5: ["date", "time", "6"],
               7:["powers", "abilities", "features","what can you do", "what have you got"],
               8:["create"],
               9:["add","insert","append","put"],
               10:["delete","remove","clear"],
               11:["show","read","display","todo"],
               12:["modify","replace","change","convert"],
               }

nonab_key={13:["great","awesome","fantastic","thank","wow","cool","best","good","nice","excellent","perfect","love"],
           6: ["leave", "bye", "good night", "seeya", "take care", "close", "terminate", "stop", "nothing",
               "leaving", "going", "ttyl"],
           }

gratitudes=["I'm so excited to do more;)",r"My pleasure_/\_","Always at your service:D","You are welcome:)"]

greetings=["Heyyy!","Nice to meet you earthling.","Hai","Hey there!","hi"]

feelings=["Im fine!" , "Better than ever!", "Never felt better!" , "Always better than before"]

def todo():#choice 12
    with open(r"todo") as f:
        return f.read() if os.stat("todo").st_size!=0 else "The list is empty. There is nothing to display here"

def add(msg):
    for i in msg.split():
        if i.lower() in ["add","insert","append","put"]:
            keyword=i.lower()
            with open("todo","a") as f:
                w = msg.lower().split()
                f.write("\n"+"--->"+' '.join(x for x in w[(w.index(keyword)+1):])+"\n")
            return "Added "+' '.join(x for x in w[(w.index(keyword)+1):])

def delete(msg):
    del_words=["all","clear"]
    for i in msg.split():
        if any(x for x in msg.lower().split() if x in del_words):
            f = open("todo", "w")
            f.close()
            return "Deleted all elements"
        elif i.lower() in ["delete","remove"]:
            keyword=i
            with open("todo","r") as f:
                w = msg.split()
                d = " ".join(x for x in w[(w.index(keyword)+1):])
                new_data = ' '.join(x for x in f.readlines() if d not in x)
            with open("todo","w") as g:
                g.write(new_data)
            return "Deleted "+d


def create():
    f=open("todo","w+")
    f.close()
    return "List created. You can now start adding elements. Once you are done, you can read it, delete items and do other necessary actions"

def mod(imp_data):
    with open(r"todo") as f:
        new_text=f.read().replace(imp_data[0],imp_data[1])
    with open("todo", "w+") as g:
        g.write(new_text)
    return todo()



















