#!/usr/bin/env python

#############################################################################################################################################
__filename__ = "common.py"
__description__ = """Consists of common functions at the browser level, and at the system (buzzmove) level"""
__author__ = "Anand Iyer"
__copyright__ = "Copyright 2017"
__credits__ = ["Anand Iyer"]
__version__ = "1.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Testing" # Upgrade to Production once tested to function.
#############################################################################################################################################

from selenium import webdriver
from config import *
from selenium_wrappers import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import requests

def euler_setup (browser, url_to_open=site_url):
    #Start a selenium server "java -jar selenium-server-standalone-3.4.0.jar -port 4444 -role hub"
    if browser == "Firefox":
        driver = webdriver.Firefox(executable_path="D:\Software\WebDrivers\geckodriver.exe")
        #Alternatively,start a selenium client "java -Dwebdriver.gecko.driver=".\WebDrivers\geckodriver.exe" -jar selenium-server-standalone-3.4.0.jar -port 5556 -role webdriver -hub http://127.0.0.1:4444/grid/register -browser browserName="firefox""
        # driver = webdriver.Remote(
        #    command_executor='http://127.0.0.1:5556/wd/hub', #Port should the server port (4444).  Bug#https://github.com/SeleniumHQ/selenium/issues/3808
        #    desired_capabilities={'browserName': 'firefox', 'platform': 'ANY'})

        driver.implicitly_wait(wait_most)  # seconds
        driver.maximize_window()
        driver.get(url_to_open)
    elif browser == "Chrome":
        driver = webdriver.Chrome("D:\Software\WebDrivers\chromedriver.exe")
        #Alternatively,start a selenium client "java -Dwebdriver.chrome.driver=".\WebDrivers\chromedriver.exe" -jar selenium-server-standalone-3.4.0.jar -port 5555 -role webdriver -hub http://127.0.0.1:4444/grid/register -browser browserName="chrome""
        # driver = webdriver.Remote(
        #    command_executor='http://127.0.0.1:5555/wd/hub', #Port should the server port (4444).  Bug#https://github.com/SeleniumHQ/selenium/issues/3808
        #    desired_capabilities={'browserName': 'chrome', 'platform': 'ANY'})

        driver.implicitly_wait(wait_most) # seconds
        driver.maximize_window()
        driver.get(url_to_open)
    
    return driver

def select_date_in_calendar (driver, calendar, date_xpath):
    click (calendar, wait_less)
    
    #date = driver.find_element_by_xpath("(//td[@data-title='r5c6'])[3]")
    date = driver.find_element_by_xpath (date_xpath)
    click (date, wait_least)

def select_in_dropdown (dropdown, option_text, search_mode="full"):
    for option in dropdown.options:
        if option_text in option.text:
            dropdown.select_by_visible_text (option.text)
            break

def call_api(parameters):
    if "api_type" in parameters.keys():
        api_type = parameters["api_type"]
    else:
        api_type = "GET"

    base_url = parameters["base_url"]

    if "port" in parameters.keys():
        port = parameters["port"]
    else:
        port = ""
        
    api_url = parameters["api_url"]

    api_params = parameters["api_params"]    

    if "api_headers" in parameters.keys():
        api_headers = parameters["api_headers"]
    else:
        api_headers = ""

    #forming the request
    api_url = base_url + ":" + str (port) + "/" + api_url
    
    if api_type == "GET":
        api_params_set = "?"
        for param in api_params.keys():
            api_params_set = api_params_set + param + "=" + api_params[param] + "&"
    
        api_url = (api_url + api_params_set)[:-1]

    #making the request
    if api_type == "GET":
        response = requests.get (api_url, headers=api_headers)
       
    if api_type == "DELETE":
        response = requests.delete (api_url)

    if api_type == "PUT":
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.put(api_url, data = json.dumps (api_params), headers=headers)

    if api_type == "POST":
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.post (api_url, data = json.dumps (api_params), headers=headers)

    return response

class UniqueDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)

def get_cookies(driver):
    target = open(".\\cookies.csv", 'w')
    #Header
    target.write ("domain, ")
    target.write ("secure, ")
    target.write ("value, ")
    target.write ("expiry, ")
    target.write ("path, ")
    target.write ("name\n")

    #Values
    for cookie in driver.get_cookies ():
        target.write (str (cookie["domain"]) + ", "),
        target.write (str (cookie["secure"]) + ", "),
        target.write (str (cookie["value"]) + ", "),
        if "expiry" in cookie.keys():
            target.write (str (cookie["expiry"]) + ", "),
        else:
            target.write (",")
        target.write (str (cookie["path"]) + ", "),
        target.write (str (cookie["name"]) + "\n")
        
def minutes_seconds (timedelta):
    minutes = int (timedelta / 60)
    seconds = int (timedelta % 60)
    return (minutes, seconds)

def make_unicode(input):
    if type(input) != unicode:
        input = input.decode('utf-8')
        return input
    else:
        return input

def write (f, column=None, embed=True, blanks=1):
    if not column is None:
        if isinstance (column, list):
            all_each = ""
            for each in column:
                all_each += each + ","
            column = all_each #concatenate everything into a string
        elif isinstance  (column, int):
            column = str (column)

        if embed:
            f.write ("\"")

        f.write (column.replace ("\"", "'").encode('utf-8')),

        if embed:
            f.write ("\"")

    for blank in range (blanks):
        f.write (",")
            
def writeline (f, column=None, embed=True):
    write (f, column, embed)
    f.write ("\n")

def split_to_columns (line, num_columns):
    columns = line.split ('",')
    for index in range (num_columns):
        columns[index] = make_unicode (columns[index].strip ('"'))

    return columns