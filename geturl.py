import os
import sys
import time

# group, subject, level, year, month
def english(subject, level, year, month):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%201%20-%20Studies%20in%20Language%20and%20Literature%2FEnglish%20A%20Language%20and%20literature%20HL%2F{year}%20{month}%20Examination%20Session"
        
def languageB(subject, level, year, month):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%202%20-%20Language%20Acquisition%2F{subject}%20B%20{level}%2F{year}%20{month}%20Examination%20Session"


def socials(subject, level, year, month):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%203%20-%20Individuals%20and%20Societies%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"

def science(subject, level, year, month):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%204%20-%20Sciences%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"

def math(subject, level, year, month):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%205%20-%20Mathematics%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"

def arts(subject, level, year, month):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%206%20-%20The%20arts%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"


def get_link(group, subject, level, year, month):

    time.sleep(3)
    if group == "1":
        url = english(subject, level, year, month)
    elif group == "2":
        url = languageB(subject, level, year, month)
    elif group == "3":
        url = socials(subject, level, year, month)
    elif group == "4":
        url = science(subject, level, year, month)
    elif group == "5":
        url = math(subject, level, year, month)
    elif group == "6":
        url = arts(subject, level, year, month)
    else:
        print("Something went terribly wrong")
        raise LookupError
    print(url)
    return url

get_link("3", "ITGS", "HL", "2012", "May")

#English
#French
#Spanish
#Japanese
#Mandarin
#Geography
#History
#ITGS
#Business%20management
#Biology
#Chemistry
#Physics
#Mathematics
#Music
