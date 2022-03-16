from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time as Thread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)
for i in range(0,100):
    driver.get("https://k12.instructure.com/dashboard/eportfolios")


    #to identify element commit
    #s = driver.find_element_by_xpath("//div/div/ul/li/a")
    #file path specified with send_keys

    button1 = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/ul/li[1]/a/span')[0]
    button1.click()
    button2 = driver.find_element_by_link_text('Delete this ePortfolio')
    button2.click()
    #button3 = driver.find_elements_by_xpath('//*[@id="delete_eportfolio_form"]/div/button')[0]
    #button3.click()
    element = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="delete_eportfolio_form"]/div/button')))
    element.click()
