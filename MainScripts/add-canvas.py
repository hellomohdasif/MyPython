from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time as Thread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random
import string
import getpass
from selenium.webdriver.common.keys import Keys



# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
# driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)



for i in range(0,200):
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

    with open('D:\\MYNEW\\a\\fb.txt') as f:
        lines = f.readlines()
    f=''.join(lines)
    f = f.replace('\n', ',')

    driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % f)

    driver.switch_to.frame("edit_page_section_0_ifr")
    Thread.sleep(1)
    #abc = driver.find_element_by_id("tinymce")
    #abc.click()

    text_area1 = driver.find_element_by_id('tinymce')
    text_area1.click()


    text_area1.send_keys(Keys.CONTROL, 'a')
    text_area1.send_keys(Keys.CONTROL, 'c')



    driver.switch_to_default_content()


