from selenium import webdriver
from selenium import *
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C:/Selenium_python/chromedriver_win32/chromedriver.exe")
#driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
elem1=driver.find_element_by_id("email")
elem1.send_keys("test.ecommit2014@gmail.com")
elem1.send_keys(Keys.RETURN)
elem2=driver.find_element_by_id("pass")
elem2.send_keys("welcome@12345")  # ("YOUR PASSWORD")
elem2.send_keys(Keys.RETURN)

time.sleep(60)

post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.click()
post_box.send_keys("Testing using Name not ID.Selenium is easy.")
sleep(2)
post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()
#print "Posted..."
	
elem3=driver.find_element_by_id("logoutMenu")
elem3.click()
elem4=driver.find_element_by_xpath("//span[@class='_54nh']")
elem4.click()