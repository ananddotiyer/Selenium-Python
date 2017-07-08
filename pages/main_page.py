#!/usr/bin/env python
#############################################################################################################################################
__filename__ = "main_page.py"
__description__ = """Represents main page

Methods that launch new pages start with get_
Methods that are used for verification/assertion purposes start with is_
Method that perform actions start with do_
Method that perform verifications start with verify_

"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2017"
__credits__ = ["Anand Iyer"]
__version__ = "1.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Testing" # Upgrade to Production once tested to function.
#############################################################################################################################################

import time
from common.selenium_wrappers import *
from common.common import *
from common.config import *
from a_base_page import basePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class mainPageLocators(object):
    ABOUT = (By.XPATH, "//a[@title='About']")

    PAGE_SYNC = ABOUT
    
class mainPage(basePage):
    def __init__(self, driver):
        super(mainPage, self).__init__(driver)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*mainPageLocators.PAGE_SYNC))
        
    def get_about (self):
        get_about = self.driver.find_element(*mainPageLocators.ABOUT)
        click (get_about, wait_least)