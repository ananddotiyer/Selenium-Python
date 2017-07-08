#!/usr/bin/env python

#############################################################################################################################################
__filename__ = "test_menu_options.py"
__description__ = """Represents all tests in a specific category.  Every test in this file\
will be named after the test case id, so that the coverage can be determined.\
"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2017"
__credits__ = ["Anand Iyer"]
__version__ = "1.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Testing" # Upgrade to Production once tested to function.
#############################################################################################################################################

import unittest
from common.config import *
from common.common import *
from pages.main_page import mainPage
from pages.about_page import aboutPage

class test_menu_options(unittest.TestCase):
    def setUp(self):
        self.driver = euler_setup (browser)

    #################################################################################################################################
    __testids__ = ["EULER_101"]
    #################################################################################################################################
    def test_about_archives(self):
        """Click on about"""
        #home page
        self.main_page_object = mainPage (self.driver)
        self.main_page_object.get_about ()

        self.about_page_object = aboutPage (self.driver)
        self.about_page_object.get_archives ()
        
    def tearDown(self):
        self.driver.quit()
