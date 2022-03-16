import getpass
import os
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')



for z in range(0, 10):

    driver.get("https://sites.google.com/new")


    s = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.XPATH, '//div/div[2]/div[3]/div/div')))
    s.click()

    s1 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id=":3s.d-h-iv-of"]/div/div')))
    s1.click()

    s2 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id=":5h"]/div/div/div[2]/div')))
    s2.click()

