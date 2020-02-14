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
