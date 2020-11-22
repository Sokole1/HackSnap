from selenium import webdriver
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

driver = webdriver.Chrome(resource_path('./chromedriver.exe'))
###

driver.get("https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2F")

driver.find_element_by_id("password").send_keys("examsnap")
input = driver.find_element_by_id("password-submit")
input.click()

def scrape_group():
    pass

def scrape_subject():
    pass 

def scrape_yearmonth():
    pass


