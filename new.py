import getpass
import os
import random
import string
import time as Thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

get="xzxz"

if get=="1":
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\tmp\newdir\Profile 1")
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

    path = "C:\\Users\\Administrator\\Desktop\\1\\"
    uploadpath = "C:\\Users\\Administrator\\Desktop\\1.txt"
elif get=="2":
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\tmp\newdir\Profile 2")
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

    path = "C:\\Users\\Administrator\\Desktop\\2\\"
    uploadpath = "C:\\Users\\Administrator\\Desktop\\1.txt"

else:
    options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # options.add_argument('headless')

    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

    path = "C:\\Users\\Asif\\Desktop\\1\\"
    uploadpath = "C:\\Users\\Asif\\Desktop\\1.txt"


base1 = "https://naucenter.as.virginia.edu/sites/naucenter.as.virginia.edu/files/webform/"

a = os.listdir(path)
lnth=0
j=0
while(lnth<len(a)):
        driver.get("https://www.suicidology.community/blogpost/1974079/1")

        s11 = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content-features"]/span/a')))
        s11.click()


        lnth+=100
        b = 0
        while (j < lnth):

            s5 = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.ID, "aAddFile")))


            s5.click()

            s3 = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.NAME, "strFileUpload"+str(b)+"")))
            s3.send_keys(path + a[j])
            b=b+1

            j=j+1

        s4 = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.NAME, "btnSubmit")))
        s4.click()
        Thread.sleep(10)
















