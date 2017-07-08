#!/usr/bin/env python
#############################################################################################################################################
__filename__ = "about_page.py"
__description__ = """Represents about page

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

class aboutPageLocators(object):
    ARCHIVES = (By.XPATH, "//a[@title='Archives']")

    PAGE_SYNC = ARCHIVES
    
class aboutPage(basePage):
    def __init__(self, driver):
        super(aboutPage, self).__init__(driver)
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*aboutPageLocators.PAGE_SYNC))
        
    def get_archives (self):
        get_archives = self.driver.find_element(*aboutPageLocators.ARCHIVES)
        click (get_archives, wait_least)