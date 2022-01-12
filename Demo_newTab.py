'''
Created on 11 thg 1, 2022

@author: meimei
'''
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_upload_file(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/css/css3_buttons.asp")
        self.assertIn("Buttons", driver.title)
        print(driver.title)
        driver.get("https://www.youtube.com/watch?v=1JuYQgpbrW0")
        WebDriverWait(10)
        print(driver.title)
        time.sleep(2)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()