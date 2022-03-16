import getpass
import os
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
import time as Thread

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
# chrome_driver ="C:\\chromedriver.exe"
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
# driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

options = webdriver.ChromeOptions()

options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')


with open("C:\\Users\\Asif\\Desktop\\Main\\rexdl.txt", 'r') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    lines = [line.replace('  ', '') for line in lines]


i=0
while (i < len(lines)):
    driver.get("https://hesoh.com/wp-admin/admin.php?page=wp_apk_rexdl#menu3")




    s5 = WebDriverWait(driver, 80).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Add Manual')))
    s5.click()
    s5.click()


    s6 = WebDriverWait(driver, 80).until(
        EC.element_to_be_clickable((By.XPATH, '//div[4]/form/input')))
    s6.send_keys(lines[i])

    s7 = WebDriverWait(driver, 80).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='Submit' and @name='wp_sb' and @value='Posting Now']")))
    s7.click()
    Thread.sleep(2)
    try:
        s7 = WebDriverWait(driver, 6).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Debugs')))
        print(i)
    except:
        # s8 = WebDriverWait(driver, 80).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='Submit' and @name='wp_sb' and @value='Posting Now']")))
        # s8.click()
        Thread.sleep(1)


    i = i + 1





