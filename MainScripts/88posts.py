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
for i in range(0,50):
    driver.get("https://www.88posts.com/submit.aspx?url=https://www.google.com/")


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    chars1 = string.digits

    size1 = 12
    size2 = 22
    random1 = (random_string_generator(size1, chars1))
    random2 = (random_string_generator(size2, chars))

    # to identify element commit
    #s = driver.find_element_by_id("field_59rydq3")
    # file path specified with send_keys

    #driver.findElement(By.CLASS_NAME("btn-primary btn-add")).click()



    #element2 = WebDriverWait(driver, 8000).until(
        #EC.element_to_be_clickable((By.NAME, 'refurl')))
    #element2.send_keys("https://www.google.com/")
    #Thread.sleep(1)

    element3 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.NAME, 'title')))
    element3.send_keys(random2)
    Thread.sleep(2)

    with open('E:\\connect\\\html.txt') as f:
        lines = f.readlines()
    f = ''.join(lines)
    f = f.replace('\n', '  ')




    # abc = driver.find_element_by_name("info")
    # driver.execute_script("arguments[0].value ='"+f+"'", abc)

    driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % f)

    Thread.sleep(2)

    button4 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'linkbutton')))
    button4.click()
    Thread.sleep(2)

   # button4 = WebDriverWait(driver, 8000).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, 'html>body>div:nth-of-type(3)>div>div:nth-of-type(2)>h3>a')))
    #button4.click()


    Thread.sleep(2)


    element = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/h3/a")
    href = element.get_attribute('href')

    with open('E:\\connect\\\test.txt', "a") as myfile:
        myfile.write((href)+"\n")
        print("Done=" + (str(i)))


