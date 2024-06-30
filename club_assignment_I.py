'''Objective: To greet user based on the time of day
To install the pymsgbox module return the following in the terminal: pip/pip3 install PyMsgBox'''
from pymsgbox import *
import pymsgbox as p
import time as t #pre installed in python
import random as r #pre installed in python

time = t.strftime("%d %m, %Y %H:%M")
date = t.strftime("%d")
month = t.strftime("%m")
year = t.strftime("%Y")
clock = time[-5:]

if month == "01":
    month = "January"
elif month == "02":
    month = "February"
elif month == "03":
    month = "March"
elif month == "04":
    month = "April"
elif month == "05":
    month = "May"
elif month == "06":
    month = "June"
elif month == "07":
    month = "July"
elif month == "08":
    month = "August"
elif month == "09":
    month = "September"
elif month == "10":
    month = "October"
elif month == "11":
    month = "November"
else:
    month = "December"

morning = {
    'ohayo': 'Japanese',
    'buen dia': 'Spanish',
    'magandang umaga': 'Filipino',
    'suprabhat': 'Hindi',
    'kalimera': 'Greek',
    'Habari za asubuhi': 'Swahili'
}

afternoon = {
    'konichiwa': 'Japanese',
    'buenas tardes': 'Spanish',
    'magandang hapon': 'Filipino',
    'shub dopahar': 'Hindi',
    'kaló apógevma': 'Greek',
    'mchana mwema': 'Swahili'
}

night = {
    'konbanwa': 'Japanese',
    'buenas noches': 'Spanish',
    'magandang gabi': 'Filipino',
    'shubh sandhya': 'Hindi',
    'Kaló apógevma': 'Greek',
    'habari za jioni': 'Swahili'
}

def greet(a):
    for key, name in a.items():
        keys.append(key)
        lang.append(name)
    
    

keys = []
lang = []

#morning
if clock < "12:00":
    greet(morning)
    num = r.randint(0, len(keys))

    alert(text = keys[num] + "! That is good morning in " + lang[num] + "! Hope you have a great day early riser! Today's date is " + date + " " + month + ", " + year + ". Let's get to work!", title = "Greetings early riser!", button = p.OK_TEXT)
#afternoon
elif clock > "12:00" and clock < "18:00":
    greet(afternoon)
    num = r.randint(0, len(keys))

    alert(text = keys[num] + "! That is good afternoon in " + lang[num] + "! Time to catch up, it is already afternoon! Todat's date is " + date + " " + month + ", " + year + ". Let's go!", title = "Wake up sleepyhead!", button = p.OK_TEXT)
#night
elif clock > "18:00" and clock < "00:00":
    greet(night)
    num = r.randint(0, len(keys))

    alert(text = keys[num] + "! That is good evening in " + lang[num] + "! Hope you're enjoying your day! But shouldn't you be sleeping? Get ready for tomorrow! Today is " + date + " " + month + ", " + year + ". Finish up quick!", title = "Don't stay up too late!", button = p.OK_TEXT)