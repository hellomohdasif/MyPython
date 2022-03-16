from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import getpass

import time as Thread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random
import string
options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('headless')

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('headless')


# options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
# driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

path = "E:\\1\\"



for i in range(0,150):


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    size1 = 5
    size2 = 5
    random1 = (random_string_generator(size1, chars))
    random2 = (random_string_generator(size2, chars))


    driver.get("http://www.4mark.net/addlink.aspx?")


    #button1 = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[3]/div[2]/aside/a')[0]
    #button1.click()

    button1 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.NAME, 'url')))
    button1.send_keys("https://www.google.com/?"+random1)

    button2 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.NAME, 'cat')))
    button2.send_keys("music")

    button3 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'main-btn')))
    button3.click()

    with open('C:\\Users\\Asif\\Desktop\\1.txt') as f:
        lines = f.readlines()
    f = ''.join(lines)
    f = f.replace('\n', ',')

    button4 = driver.find_element_by_id("desc")
    driver.execute_script("arguments[0].value ='" + f + "'", button4)

    button = driver.find_element(By.CLASS_NAME, "main-btn")
    button.click()

    #
    # button5 = WebDriverWait(driver, 2).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, 'main-btn')))
    # button5.click()

    with open('C:\\Users\\Asif\\Desktop\\1.txt', "a") as myfile:
        ouuu=driver.current_url
        # ouuu = ouuu.replace('/Home/Welcome', '/')
        ouu='<a href="'+ouuu+'">'+random2+'</a>'

        myfile.write((ouu)+"\n")
        print("Done=" + (str(i)))
