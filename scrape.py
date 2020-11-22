from selenium import webdriver
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

def scrape_group(choice):

    # xpaths is a list of the xpaths for each of the 6 groups
    driver.implicitly_wait(10)
    xpaths = ['//*[@id="fileList"]/tr[1]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[2]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[3]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[4]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[5]/td[1]/a/span[1]/span', '//*[@id="fileList"]/tr[6]/td[1]/a/span[1]/span']
    for xpath in xpaths:
        elem = driver.find_element_by_xpath(xpath)
        if elem.text == choice:
            elem.click()
    

def scrape_subject():
    pass 

def scrape_yearmonth():
    pass

driver = webdriver.Chrome(resource_path('./chromedriver.exe'))
###

driver.get("https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2F")

driver.find_element_by_id("password").send_keys("examsnap")
input = driver.find_element_by_id("password-submit")
input.click()


scrape_group("Group 4 - Sciences")



