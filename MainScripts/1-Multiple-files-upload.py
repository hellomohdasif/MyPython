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


driver.refresh()
a = os.listdir(path)
lnth=0
j=0
while(lnth<len(a)):

        # driver.get("https://www.nmnpc.org/blogpost/1979357/LOL13")
        # driver.get("https://www.iiah.org/blogpost/1979826/abc")
        # driver.get("https://wrma.org/blogpost/1979840/111")
        driver.get("https://iaoms.site-ym.com/blogpost/1987498/1")
        # driver.get("https://ncnla.com/blogpost/1980302/test")





        s11 = WebDriverWait(driver, 8000).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Add New Post')))
        s11.click()


        lnth+=150
        b = 0
        while (j < lnth):

            s5 = WebDriverWait(driver, 8000).until(
            EC.element_to_be_clickable((By.ID, "aAddFile")))


            s5.click()

            s3 = WebDriverWait(driver, 8000).until(
            EC.element_to_be_clickable((By.NAME, "strFileUpload"+str(b)+"")))
            s3.send_keys(path + a[j])
            b=b+1

            j=j+1

        s4 = WebDriverWait(driver, 8000).until(
            EC.element_to_be_clickable((By.NAME, "btnSubmit")))
        s4.click()
        print(j)

















