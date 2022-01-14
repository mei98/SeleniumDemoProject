'''
Created on 14 thg 1, 2022

@author: meimei
'''
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.close()


    def test_upload_file(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
        self.assertIn("Upload Button", driver.title)
        
        element = driver.find_element(By.CSS_SELECTOR, "#myFile")
        element.send_keys("C://Users/meimei/Desktop/background/Eren.jpg")
        fileName = driver.find_element(By.CSS_SELECTOR,"#myFile").get_attribute('value') 
        assert "Eren.jpg" in fileName

        
    def test_iframe(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/html/html_iframe.asp")
        self.assertIn("Iframes", driver.title)
        
        new_frame = driver.find_element(By.CSS_SELECTOR,"#main > div:nth-child(7) > iframe")
        
        #get the text of #main > h1 from the frame
        driver.switch_to.frame(new_frame)        
        frame_name = driver.find_element(By.CSS_SELECTOR,"#main > h1").text
        #get the text of #main > h1 from the origin page
        driver.switch_to.default_content()
        page_name = driver.find_element(By.CSS_SELECTOR,"#main > h1").text
        
        assert frame_name != page_name, "2 names must be different"
  
        
    def test_new_tab(self):
        driver = self.driver
        driver.get("https://www.encodedna.com/javascript/demo/open-new-window-using-javascript-method.htm")
        # print(driver.title)
        
        #click to open new tab
        newtab = driver.find_element(By.CSS_SELECTOR, "#content > div.post > p:nth-child(4) > input[type=button]:nth-child(2)")
        newtab.click()
                
        #shift the tab control to the 2nd tab
        driver.switch_to.window(driver.window_handles[1])
        new_tab = driver.title
        #shift the tab control to the origin tab
        driver.switch_to.window(driver.window_handles[0])
        origin_tab = driver.title
        
        assert new_tab != origin_tab, "2nd tab is :"+new_tab
        
    def test_popout_window(self):
        driver = self.driver
        driver.get("https://www.encodedna.com/javascript/demo/open-new-window-using-javascript-method.htm")
        # print(driver.title)
        
        #click to open new window
        newwindow = driver.find_element(By.CSS_SELECTOR, "#content > div.post > p:nth-child(4) > input[type=button]:nth-child(1)")
        newwindow.click()
        
        #shift the control to the 2nd window
        driver.switch_to.window(driver.window_handles[1])
        new_window = driver.title
        
        #shift the control to the origin window
        driver.switch_to.window(driver.window_handles[0])
        origin_window = driver.title
        
        assert new_window != origin_window , "2nd window is: "+new_window

        
if __name__ == "__main__":
    unittest.main()