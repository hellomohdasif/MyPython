from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import getpass

import time as Thread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import re
import random
import string
options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('headless')

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('headless')

#
# options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
# driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')
options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
s = Service('C:\\chromedriver.exe')

driver = webdriver.Chrome(service=s,options=options)

path = "E:\\1\\"



for i in range(0,100):
    driver.get("https://k12.instructure.com/dashboard/eportfolios")


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    size1 = 12
    size2 = 22
    random1 = (random_string_generator(size1, chars))
    random2 = (random_string_generator(size2, chars))

    #button1 = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/aside/a')[0]
    #button1.click()

    button1 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/aside/a')))

    button1.click()

    element = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.NAME, 'eportfolio[name]')))

    element.send_keys(random1)
    button2 = driver.find_element_by_id('eportfolio_public')
    button2.click()
    button3 = driver.find_element_by_id('eportfolio_submit')
    button3.click()
    #button4 = driver.find_element_by_link_text('Welcome')
    #button3.click()

    element1 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Welcome')))

    element1.click()

    element2 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.LINK_TEXT,'Edit This Page')))

    element2.click()

    element3 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.ID, 'eportfolio_entry_name')))
    element3.send_keys(random2)

    with open('C:\\Users\\Asif\\Desktop\\1.txt') as f:
        lines = f.readlines()
    f=''.join(lines)
    f = f.replace('\n', ',')

    driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % f)

    button4 = driver.find_elements_by_xpath('//*[@id="edit_page_form"]/div[4]/button[3]')[0]
    button4.click()
    Thread.sleep(1)
    with open('C:\\Users\\Asif\\Desktop\\1.txt', "a") as myfile:
        ouuu=driver.current_url
        ouuu = ouuu.replace('/Home/Welcome', '/')
        ouu='<a href="'+ouuu+'">'+random2+'</a>'


        myfile.write((ouu)+"\n")
        print("Done=" + (str(i)))
