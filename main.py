#!/usr/bin/env python

from tests import *
import unittest
from importlib import import_module
from common.selenium_wrappers import *
from common.common import euler_setup
import HTMLTestRunner

run_mode = "HTML"
#run_mode = "TEXT"

test_suite = unittest.TestSuite()

total_count = 1
#######################################add one test to test_suite######################################
test_suite.addTest(test_menu_options('test_about_archives'))

#######################################add all tests to test_suite######################################
#test_suite = unittest.TestLoader().loadTestsFromTestCase (test_misc)

#######################################run above test_suite######################################
if run_mode == 'HTML':
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = open("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            verbosity=2,
            title='Euler Test Automation Report',
            description= str (total_count) #don't change this line.  Used inside HTMLTestRunner
            )
    runner.run(test_suite)
    buf.close()
elif run_mode == 'TEXT':
    unittest.TextTestRunner(verbosity=2).run(test_suite)
