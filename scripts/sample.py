
from selenium import webdriver

import time
from Selenium.webdriver.common.keys import Keys
capabilities = options.to_capabilities()

print("sample test case started")
# driver = webdriver.Remote("http://seleium:4444/wd/hub" ,desired_Capibilities=Desired_Capibilities.Chrome)

driver = webdriver.Remote( command_executor='http://seleium:4444/wd/hub', desired_capabilities=capabilities)

#driver=webdriver.firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
driver.find_element_by_name("q").send_keys("javatpoint")
time.sleep(3)
#click on the Google search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")