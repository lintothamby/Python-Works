# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.by import By
from asyncio.tasks import wait
from test._test_multiprocessing import wait_for_handle

class Sample1(unittest.TestCase):
    def setUp(self):
        self.driver = driver = webdriver.Chrome("C:/Selenium_python/chromedriver_win32/chromedriver.exe")
        self.driver.implicitly_wait(60)
        self.base_url = "http://www.xcite.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sample1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(240)

        wishpondelement = driver.find_element_by_xpath("//div[@class='wpcss-close-popup']")
        #for  i in range(360):
        if wishpondelement is not None:
            wait_for_handle(wishpondelement,timeout=360)
            print("found close button for popup")
        driver.implicitly_wait(120)
        wishpondelement.click()               
          

        strelementId = driver.find_element_by_id("sticky-anchor")
       
        if strelementId  is not None:
            print("I got the element")
        driver.implicitly_wait(450)
        closeaction = strelementId.click()
        if closeaction is not None:
            print("i have clicked clsoe action")
        #strpopup = driver.switch_to_window(driver.find_element_by_xpath('/div[@id="wp-html"][@class="class-based-grid desktop"]'))
        #if strpopup  is not None:
        #     print("God is love")
             
       # strlink = driver.find_element_by_link_text("No, I'm not interested")
        #if strlink  is not None:
           # print("I got the Link Text")
        driver.implicitly_wait(450)  
        cssselct = driver.find_element_by_css_selector("a.logo > img[alt=\"Xcite.com\"]")
        if cssselct is not None:
            print(cssselct)
            
        for i in range(120):
            try:
                if "" == driver.find_element_by_css_selector("a.logo > img[alt=\"Xcite.com\"]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        #switch_to.window(window_handle)
        self.assertEqual("", driver.find_element_by_css_selector("a.logo > img[alt=\"Xcite.com\"]").text)
        strelementId = driver.find_element_by_id("sticky-anchor")
        if strelementId  is not None:
            print("I got the element")
        
        self.assertEqual("Xcite.com | Online Shopping in Kuwait | Alghanim Electronics", driver.title)
        for i in range(120):
            try:
                if "Computers & Tablets" == driver.find_element_by_css_selector("a.level-top.maintainHover > span").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("", driver.find_element_by_xpath("//div[@id='rev_slider_24']/ul/li[6]/div[3]/a/span").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
