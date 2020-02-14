"""
Methods that launch new pages start with get_
Methods that are used for verification/assertion purposes start with is_
Method that perform actions start with do_
Method that perform actions start with verify_

**Naming of this file is important and must be a_base_page.py; pages are loaded in the order of file names**
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class basePage(object):
    def __init__(self, driver):
        self.driver = driver
