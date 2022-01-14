'''
Created on 13 thg 1, 2022

@author: meimei
'''
import unittest

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLinksAPI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_links(self):
        driver = self.driver
        driver.get("https://any-api.com/")
        
        #get the list of elements on the left navigation by css selector
        tag_links = driver.find_elements(By.CLASS_NAME, "tag-link")
        #create a variable to count the active links
        count = 0
        
        #start a loop through the list 
        for index in range(len(tag_links)):
            #click on the link
            tag_links[index].click()
            
            try:
                r = requests.get(driver.current_url)
                assert 200 == r.status_code
                count += 1
            except requests.exceptions.Timeout:
                print("Timeout occur at "+tag_links[index].text)
            except AssertionError:
                print("Fail at "+str(index+1)+" link")
        
        print("Pass "+ str(count) + " links in total")
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
        