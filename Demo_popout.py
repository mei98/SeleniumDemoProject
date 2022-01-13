'''
Created on 13 thg 1, 2022

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
        driver.get("https://www.encodedna.com/javascript/demo/open-new-window-using-javascript-method.htm")
        print(driver.title)
        
        #click to open new window
        newwindow = driver.find_element(By.CSS_SELECTOR, "#content > div.post > p:nth-child(4) > input[type=button]:nth-child(1)")
        newwindow.click()
        time.sleep(2)
        
        #shift the control to the 2nd window
        driver.switch_to.window(driver.window_handles[1])
        print(driver.title)
        time.sleep(2)
        
        #shift the control to the origin window
        driver.switch_to.window(driver.window_handles[0])
        print(driver.title)
        time.sleep(2)
        
        #shift the control to the 2nd window
        driver.switch_to.window(driver.window_handles[1])
        print(driver.title)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()