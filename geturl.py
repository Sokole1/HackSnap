# group, subject, level, year, month
def english(subject, level, month, year):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%201%20-%20Studies%20in%20Language%20and%20Literature%2FEnglish%20A%20Language%20and%20literature%20HL%2F{year}%20{month}%20Examination%20Session"
        
def languageB(subject, level, month, year):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%202%20-%20Language%20Acquisition%2F{subject}%20B%20{level}%2F{year}%20{month}%20Examination%20Session"

def socials(subject, level, month, year):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%203%20-%20Individuals%20and%20Societies%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"

def science(subject, level, month, year):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%204%20-%20Sciences%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"

def math(subject, level, month, year):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%205%20-%20Mathematics%2FMath%20{level}%2F{year}%20{month}%20Examination%20Session"

def arts(subject, level, month, year):
    return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%206%20-%20The%20arts%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"


def get_link(group, subject, level, month, year):

    if group == "Group 1 - Studies in Language and Literature":
        url = english(subject, level, month, year)
    elif group == "Group 2 - Language Acquisition":
        url = languageB(subject, level, month, year)
    elif group == "Group 3 - Individuals and Societies":
        url = socials(subject, level, month, year)
    elif group == "Group 4 - Experimental Sciences":
        url = science(subject, level, month, year)
    elif group == "Group 5 - Mathematics":
        url = math(subject, level, month, year)
    elif group == "Group 6 - The Arts":
        url = arts(subject, level, month, year)
    else:
        print("Something went terribly wrong")
        raise LookupError

    return url


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

#https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%204%20-%20Sciences%2FChemistry%20HL%2F2018%20May%20Examination%20Session