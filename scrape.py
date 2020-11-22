from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time

### Set up the webdriver
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# group, subject, level, year, month
def english(driver, subject, level, year, month):
    try:
        return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%201%20-%20Studies%20in%20Language%20and%20Literature%2FEnglish%20A%20Language%20and%20literature%20HL%2F{year}%20{month}%20Examination%20Session"
    except:
        print("URL Doesn't Exist")
        
def languageB(driver, subject, level, year, month):
    try:
        return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%202%20-%20Language%20Acquisition%2F{subject}%20B%20{level}%2F{year}%20{month}%20Examination%20Session"
    except:
        print("URL Doesn't Exist")

def socials(driver, subject, level, year, month):
    try:
        return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%203%20-%20Individuals%20and%20Societies%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"
    except:
        print("URL Doesn't Exist")    

def science(driver, subject, level, year, month):
    try:
        return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%204%20-%20Sciences%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"
    except:
        print("URL Doesn't Exist") 

def math(driver, subject, level, year, month):
    try:
        return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%205%20-%20Mathematics%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"
    except:
        print("URL Doesn't Exist") 

def arts(driver, subject, level, year, month):
    try:
        return f"https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%206%20-%20The%20arts%2F{subject}%20{level}%2F{year}%20{month}%20Examination%20Session"
    except:
        print("URL Doesn't Exist") 


# def initialize():

#     driver = webdriver.Chrome(resource_path('./chromedriver.exe'))

#     driver.get("https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2F")

#     driver.find_element_by_id("password").send_keys("examsnap")
#     input = driver.find_element_by_id("password-submit")
#     input.click()
#     return driver

def get_link(group, subject, level, year, month):
    # driver = initialize()
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

get_link("2", "French", "HL", "2017", "November")

#https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%201%20-%20Studies%20in%20Language%20and%20Literature%2FEnglish%20A%20Language%20and%20literature%20HL%2F2013%20May%20Examination%20Session
# English HL https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%201%20-%20Studies%20in%20Language%20and%20Literature%2FEnglish%20A%20Language%20and%20literature%20HL%2F2014%20November%20Examination%20Session

#Group 5: Math HL https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%205%20-%20Mathematics%2FMathematics%20HL%2F2001%20November%20Examination%20Session



# def scrape_group(choice):

#     # xpaths is a list of the xpaths for each of the 6 groups
#     driver.implicitly_wait(10)
#     xpaths = ['//*[@id="fileList"]/tr[1]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[2]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[3]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[4]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[5]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[6]/td[1]/a/span[1]/span']
#     for xpath in xpaths:
#         elem = driver.find_element_by_xpath(xpath)
#         if elem.text == choice:
#             elem.click()
    

# def scrape_subject(choice):

#     if choice == "Group 1 - Studies in Language and Literature":
#         time.sleep(5)
#         driver.get('https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%201%20-%20Studies%20in%20Language%20and%20Literature%2FEnglish%20A%20Language%20and%20literature%20HL')
#         # ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="fileList"]/tr[88]/td[1]/a/span[1]')).perform()
#         # # driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/table/tbody/tr[88]/td[1]/a/span[1]/span').click()
#     else:
#         print("No")
    

# def scrape_yearmonth():
#     pass
