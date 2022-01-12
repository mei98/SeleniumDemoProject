'''
Created on 10 thg 1, 2022

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
        driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
        self.assertIn("Upload Button", driver.title)
        
        element = driver.find_element(By.CSS_SELECTOR, "#myFile")
        element.send_keys("C://Users/meimei/Desktop/background/Eren.jpg")
        fileName = driver.find_element(By.CSS_SELECTOR,"#myFile").get_attribute('value') 
        # print(fileName) 
        assert "Eren.jpg" in fileName
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()