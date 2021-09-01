#Metis abilities
import webbrowser
import pywhatkit
import datetime
import random
import os
#1) Abilities Using webbrowser

def search(website):

    global chromepath
    url = f"{website}.com"

    '''Note: The main creating a lists is beacuse starting soon, Google Chrome
       will install in the C:\Program Files\ folder by default on Windows if it 
       is a 64-bit installer. Chrome 64-bit versions installed in the C:\Program Files (x86)\ 
       folder will continue to work and will be updated just like before.'''

    chromepath_options = [r"c:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                          r"C:\Program Files\Google\Chrome\Application\chrome.exe"]

    for i in chromepath_options:
        if os.path.exists(i) == True:
            chromepath = i
        else:
            chromepath = i

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
perspective = ["me","us","them"]

keyword =     {1: ["open","access", "take me to" , "take us to" , "take them to" , "enter"],
               2: ["listen","play"],
               3: ["google","search"],
               4: ["highlights", "updates", "news"],
               5: ["date", "time"],
               7:["powers", "abilities", "features","what can you do", "what have you got"],
               8:["create"],
               10:["delete","remove","clear"],
               9:["add","insert","append","put"],
               11:["show","read","display","todo"],
               12:["modify","replace","change","convert"],
               }

nonab_key={6: ["leave", "bye", "good night", "seeya", "take care", "close", "terminate", "stop", "nothing",
               "leaving", "going", "ttyl"],
           13:["great","awesome","fantastic","thank","wow","cool","best","good","nice","excellent","perfect","love","epic","fabulous"],
           }

#friendly responses

gratitudes=["I'm so excited to do more;)",r"My pleasure_/\_","Always at your service:D","You are welcome:)"]

greetings=["Heyyy!","Nice to meet you earthling.","Hai","Hey there!","hi"]

feelings=["Im fine!" , "Better than ever!", "Never felt better!" , "Always better than before"]

# To-Do-List

def todo():#choice 12

    try:
        with open("todo","r+") as f:
            return f.read() if os.stat("todo").st_size!=0 else "The list is empty. There is nothing to display here"
    except:
        with open("todo","w+") as f:
            return "The list is empty. There is nothing to display here"


def add(msg):

    for i in msg.split():
        if i.lower() in ["add","insert","append","put"]:
            keyword = i
            with open("todo","a") as f:
                elem = msg.rpartition(keyword+" ")[-1]
                if os.stat("todo").st_size!=0:
                    f.write(elem+"\n")
                else:
                    f.write(elem + "\n")
            return "Added "+elem

def delete(msg):

    del_words=["all","clear"]

    for i in msg.split():
        if any(x for x in msg.lower().split() if x in del_words):
            f = open("todo", "w")
            f.write("\n\n")
            f.close()
            return "Deleted all elements"
        elif i.lower() in ["delete","remove"]:
            keyword=i
            with open("todo","r") as f:
                w = msg.split()
                d = " ".join(x for x in w[(w.index(keyword)+1):])
                new_data = '\n'.join(x for x in f.readlines() if d not in x)
            with open("todo","w+") as g:
                g.write(new_data)
            return "Deleted "+d


def create():

    f=open("todo","w+")
    f.write("\n\n")
    f.close()
    return "List created. You can now start adding elements. Once you are done, you can read it, delete items and do other necessary actions"

def mod(imp_data):

    with open(r"todo") as f:
        dat ="\n\n"+"\n".join([x if x!=imp_data[0] else imp_data[1] for x in f.read().split()])
    with open("todo","w+") as g:
        g.write(dat)
    return todo()























