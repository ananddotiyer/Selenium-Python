#!/usr/bin/env python

#############################################################################################################################################
__filename__ = "a_base_page.py"
__description__ = """Represents base page, from which all pages are inherited.

Methods that launch new pages start with get_
Methods that are used for verification/assertion purposes start with is_
Method that perform actions start with do_
Method that perform actions start with verify_

!!Naming of this file is important and must be a_base_page.py; pages are loaded in the order of file names!!
"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Moolya"
__credits__ = ["Anand Iyer"]
__version__ = "1.0"
__maintainer__ = "Anand Iyer"
__email__ = "anand.iyer@moolya.com"
__status__ = "Testing" #Upgrade to Production once tested to function.
#############################################################################################################################################

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class basePage(object):
    def __init__(self, driver):
        self.driver = driver