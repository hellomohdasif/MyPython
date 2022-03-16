import getpass
import os
import random
import string
import time as Thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

get="111"

if get=="1":
    options = webdriver.ChromeOptions()
    # options.add_argument(r"user-data-dir=C:\tmp\newdir\Profile 1")
    # driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)
    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

    path = "C:\\Users\\Administrator\\Desktop\\3\\"
    uploadpath = "C:\\Users\\Administrator\\Desktop\\1.txt"
elif get=="2":
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\tmp\newdir\Profile 2")
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

    path = "C:\\Users\\Administrator\\Desktop\\2\\"

else:
    options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # options.add_argument('headless')

    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

    path = "C:\\Users\\Asif\\Desktop\\2\\"




a = os.listdir(path)
lnth=0
j=0
while(lnth<len(a)):
    driver.refresh()


    print("Asdas")

    driver.get("https://omwbe.wa.gov/node/add/bids")
    lnth += 99
    b = 0
    while (j < lnth):

        s5 = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.ID, "edit-field-documents-und-"+str(j)+"-upload")))
        s5.send_keys(path+a[j])

        s6 = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.ID, "edit-field-documents-und-"+str(j)+"-upload-button")))
        s6.click()

        j = j + 1

    s4 = WebDriverWait(driver, 8000).until(
        EC.element_to_be_clickable((By.ID, "edit-submit")))
    s4.click()
    print(j)
