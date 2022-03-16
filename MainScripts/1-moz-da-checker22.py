import getpass
import os
import random
import string
import time as Thread
from selenium.webdriver.common.keys import Keys
import pyperclip

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

else:
    options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # options.add_argument('headless')

    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')


with open("C:\\Users\\Asif\\Desktop\\nameheap.txt", 'r') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    lines = [line.replace('  ', '') for line in lines]

lnth=620
j=620
driver.refresh()

while(lnth<len(lines)):
    driver.get("https://www.dapachecker.org/")

    lnth += 20
    b = 0
    ken = []

    while (j < lnth):
        ken.append(lines[j])
        # print(ken)
        j = j + 1

    ab = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'urls')))
    ab.click()

    ken = ' '.join([str(elem) for elem in ken])
    ken = ken.replace(" ", "\n")

    pyperclip.copy(ken)
    ab.send_keys(Keys.CONTROL, 'v')

    Thread.sleep(2)

    ab11 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "exclude_domain")))
    ab11.click()

    b = driver.find_element_by_id("checkBtnCap")
    driver.execute_script("arguments[0].click();", b)

    Thread.sleep(5)
    # ab1 = WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html//button[@id='checkBtnCap']")))
    # ab1.click()
    # Thread.sleep(5)

    l = 0
    # k=1

    while (l <= 5):

        try:

            ab = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[2]')))

            domainname = (ab.text)

            ab1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[3]')))
            losse = (ab1.text)

            newname = int(losse)

            mozr = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[6]')))

            mozrt = (mozr.text)
            mozra = float(mozrt)

            if (newname > 10 and mozra >= 2):
                print(domainname)
                with open('C:\\Users\\Asif\\Desktop\\domains.txt', "a") as myfile:
                    myfile.write(domainname + "\n")



        except:
            driver.execute_script("arguments[0].click();", b)

            pass
        l = l + 1

    print("=======")

    while (l <= 11):
        try:
            ab = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[2]')))

            domainname = (ab.text)

            ab1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[3]')))
            losse = (ab1.text)

            newname = int(losse)

            mozr = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[6]')))

            mozrt = (mozr.text)
            mozra = float(mozrt)

            if (newname > 10 and mozra >= 2):
                print(domainname)
                with open('C:\\Users\\Asif\\Desktop\\domains.txt', "a") as myfile:
                    myfile.write(domainname + "\n")

        except:
            pass
        l = l + 1
    print("=======")

    while (l <= 17):

        try:
            ab = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[2]')))

            domainname = (ab.text)

            ab1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[3]')))
            losse = (ab1.text)

            newname = int(losse)

            mozr = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[6]')))

            mozrt = (mozr.text)
            mozra = float(mozrt)

            if (newname > 10 and mozra >= 2):
                print(domainname)
                with open('C:\\Users\\Asif\\Desktop\\domains.txt', "a") as myfile:
                    myfile.write(domainname + "\n")


        except:
            pass
        l = l + 1

    print("=======")

    while (l <= 23):

        try:
            ab = WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[2]')))

            domainname = (ab.text)

            ab1 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[3]')))
            losse = (ab1.text)

            newname = int(losse)

            mozr = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//tr[' + str(l) + ']/td[6]')))

            mozrt = (mozr.text)
            mozra = float(mozrt)

            if (newname > 10 and mozra >= 2):
                print(domainname)
                with open('C:\\Users\\Asif\\Desktop\\domains.txt', "a") as myfile:
                    myfile.write(domainname + "\n")

        except:
            pass
        l = l + 1

    print("CHECKED DOMAIN= " + str(lnth))
















