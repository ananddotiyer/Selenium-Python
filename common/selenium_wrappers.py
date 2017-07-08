#!/usr/bin/env python

import time

def try_click (web_element, time_delay=0):
    try:
        web_element.click()
    except:
        click (web_element)
        
    time.sleep (time_delay)
    
def click (web_element, time_delay=0):
    web_element.click()
    time.sleep (time_delay)