"""
Methods that launch new pages start with get_
Methods that are used for verification/assertion purposes start with is_
Method that perform actions start with do_
Method that perform actions start with verify_
"""

import time
from common.selenium_wrappers import *
from common.common import *
from common.config import *
from pages.a_base_page import basePage
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
