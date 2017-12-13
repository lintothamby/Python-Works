# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver
import time
# iPhone
#driver = webdriver.Remote(browser_name="iphone", command_executor='http://172.24.101.36:3001/hub')

# Android
#driver = webdriver.Remote(browser_name="android", command_executor='http://127.0.0.1:8080/hub')

# Google Chrome 
driver = webdriver.Chrome("C:/Selenium_python/chromedriver_win32/chromedriver.exe")

# Firefox 
#driver = webdriver.Firefox()

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('http://www.xcite.com')

#wait = webdriver

# Select the Python language option
python_link = driver.find_elements_by_xpath("//input[@title='Xcite.com']")#[0]
#python_link.click()

# Enter some text!
text_area = driver.find_element_by_id('search')
text_area.send_keys('iphone' + ' 8')

# Submit the form!
#submit_button = driver.find_element_by_name('submit')
#submit_button.click()
time.sleep(60)
#wait_for(driver,10)
# Make this an actual test. Isn't Python beautiful?
#assert "Hello, World!" in driver.get_page_source()
html_source = driver.page_source
print ("html_source:",html_source)
hello_in_html = "iphone 8" in html_source

# Close the browser!
driver.quit()
assert hello_in_html