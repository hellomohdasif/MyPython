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

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

#driver.get("https://dcm.shivtr.com/users/sign_in")
#Thread.sleep(3)
#button1 = driver.find_element_by_name('commit')[0]
#button1.click()
for i in range(0,25):
    driver.get("https://dcm.shivtr.com/forums/2080436")


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    size1 = 12
    size2 = 22
    random1 = (random_string_generator(size1, chars))
    random2 = (random_string_generator(size2, chars))

    # to identify element commit
    #s = driver.find_element_by_id("field_59rydq3")
    # file path specified with send_keys

    #driver.findElement(By.CLASS_NAME("btn-primary btn-add")).click()

    text_area1 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Add Thread')))
    text_area1.click()

    element2 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.ID, 'forum_thread_subject')))
    element2.send_keys(random2)

    with open('E:\\connect\\\html.txt') as f:
        lines = f.readlines()
    f = ''.join(lines)
    f = f.replace('\n', '  ')




    abc = driver.find_element_by_id("forum_thread_posts_attributes_0_message")
    driver.execute_script("arguments[0].value ='"+f+"'", abc)

    button4 = driver.find_element_by_class_name('btn-primary')
    button4.click()
    Thread.sleep(1)
    with open('E:\\connect\\\test.txt', "a") as myfile:
        myfile.write((driver.current_url)+"\n")
        print("Done="+(str(i)))
        Thread.sleep(2)



