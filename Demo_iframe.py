'''
Created on 11 thg 1, 2022

@author: meimei
'''
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_upload_file(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/html/html_iframe.asp")
        self.assertIn("Iframes", driver.title)
        
        new_frame = driver.find_element(By.CSS_SELECTOR,"#main > div:nth-child(7) > iframe")
        
        driver.switch_to.frame(new_frame)        
        frame_name = driver.find_element(By.CSS_SELECTOR,"#main > h1").text
        print(frame_name)
        
        driver.switch_to.default_content()
        page_name = driver.find_element(By.CSS_SELECTOR,"#main > h1").text
        print(page_name)
        
        assert frame_name != page_name, "2 names must be different"
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()