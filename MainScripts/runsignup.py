import getpass
import os
import random
import string
import time as Thread
# from datetime import date
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

import pyperclip
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

### git check
## get check 2

typepost = "html"

profile="1"

if profile=="1":
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options.add_argument('headless')
    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

else:
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)


topic = ("coin","igfollowers")


# topic = ("vbucks","garena","fb","insta")
# topic = ("onlyfans", "coin","brawl")

def changeme():


    for x in range(len(topic)):


        file = topic[x]
        if topic[x] == "robux" or topic[x] == "vbucks" or topic[x] == "garena" or topic[x] == "fskins":
            numrep = 6
        else:
            numrep = 3

        dir = 'D:\\MYNEW\\a'
        a = "D:\\MYNEW\\a\\files\\"

        full_path = os.path.join(dir, file)

        presentday = datetime.now()
        nextday = presentday + timedelta(1)
        d2 = presentday.strftime('%d-%m-%Y')

        for i in range(0, numrep):



            b = a + file

            with open(full_path + ".csv", 'r') as f:
                lines = f.readlines()

            num = random.randrange(0, 5)

           klist = str(lines[num])
           klist =klist.replace('\n', '')

            num1 = random.randrange(3, len(lines))
           klist1 = (lines[num1])
           klist1 =klist1.replace('\n', '')


            # path of randome files
            niche = random.choice(os.listdir(b))

            def random_string_generator(str_size, allowed_chars):
                return ''.join(random.choice(allowed_chars) for x in range(str_size))

            chars = string.ascii_letters + string.ascii_uppercase + string.digits
            chars1 = string.digits
            chars2 = string.ascii_letters

            size1 = 4
            size2 = 4

            size3 = 6

            random1 = (random_string_generator(size1, chars1))
            randomChar = (random_string_generator(size2, chars2))
            onlineusers = (random_string_generator(size2, chars1))
            mega = (random_string_generator(size3, chars))

           klist =klist.replace(' ', '-')

            MAINTITLE = "<h1>" + (klist + " - " +klist1 + "{" + random1 + "}") + "</h1>"
            DATETIME = "<h2>" + ("Updated: " + d2 + "|{onlineusers:" + onlineusers + "}") + "</h2>"
            LINKD = "https://kenhacks.com/" + file


            with open(b + "\\" + niche, encoding='utf-8') as f:


                soup = BeautifulSoup(f, 'html.parser')

                f = (soup.prettify())
                if typepost == "html":
                    MYDOMAINLINK = "<h2><a href=" +'"'+ LINKD + '"'">" + "CLICK HERE TO USE THIS HACK" + "</a></h2></br>"

                    f = f.replace('MAINTITLE', MAINTITLE.upper())
                    f = f.replace('DATETIME', DATETIME.upper())

                    f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                    f = f.replace("\n", "")
                    f = f.replace("'", "")


                else:
                    # MYDOMAINLINK = "CLICK HERE TO USE THIS HACK :"+LINKD+"\n"
                    MYDOMAINLINK = "`CLICK HERE TO USE Hack. <" + LINKD + ">`__\n"

                    f = f.replace('MAINTITLE', MAINTITLE.upper() + "~~~~~~~~~~~~")
                    f = f.replace('DATETIME', DATETIME.upper())
                    f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                    f = f.replace('\n', "")

                    f = f.replace('<H1>', "")
                    f = f.replace('</H1>', "\n")

                    f = f.replace('<H2>', "")
                    f = f.replace('</H2>', "\n")

                    f = f.replace('</br>', "\n")

                    f = f.replace('<p>', "")

                    f = f.replace('</p>', "\n\n")
                    f = f.replace('’', "-")

                driver.get("https://runsignup.com/Race/Donate/25522/BecomeFundraiser")

                Thread.sleep(2)

                s3 = WebDriverWait(driver, 8).until(
                    EC.element_to_be_clickable(
                        (By.NAME, 'fundraiser[fundraiser_name]')))
                s3.send_keys(klist + " " + randomChar)

                s4 = WebDriverWait(driver, 8).until(
                    EC.element_to_be_clickable(
                        (By.NAME, 'fundraiser[fundraiser_tagline]')))
                s4.send_keys(klist + " " + randomChar)

                s5 = WebDriverWait(driver, 8).until(
                    EC.element_to_be_clickable(
                        (By.NAME, 'fundraiser[goal]')))
                s5.send_keys("0")
                #klist =klist.replace(' ', '-')

                s6 = WebDriverWait(driver, 8).until(
                    EC.element_to_be_clickable(
                        (By.NAME, 'fundraiser[custom_url]')))
                s6.send_keys(klist + "-" + randomChar)
                print(f)

                driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % f)

                s7 = WebDriverWait(driver, 8).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
                s7.click()
                try:
                    s8 = WebDriverWait(driver, 8).until(
                        EC.element_to_be_clickable((By.ID, "successBox")))
                    s8.click()
                    Thread.sleep(1)
                except:
                    pass





                with open('E:\\connect\\\run.txt', "a") as myfile:

                    profile = driver.current_url
                    myfile.write('<a href="' + profile + '">' + randomChar + '</a>' + '\n')
                    print("Done=" + (str(i)))
                    i = i + 1

changeme()

            # s1 = WebDriverWait(driver, 8).until(
            #     EC.element_to_be_clickable((By.ID, 'email')))
            # s1.send_keys(mega+randomChar+"@gmail.com")
            #
            # s22 = WebDriverWait(driver, 8).until(
            #     EC.element_to_be_clickable((By.ID, 'confirmEmail')))
            # s22.send_keys(mega + randomChar + "@gmail.com")
            #
            #
            # s2 = WebDriverWait(driver, 8).until(
            #     EC.element_to_be_clickable((By.XPATH, '//*[@id="createAccountFormContainer"]/div/form/div/div[8]/div/button')))
            # s2.click()
            #
            # news = WebDriverWait(driver, 8).until(
            #     EC.element_to_be_clickable((By.ID, 'successBox')))
            #
            # driver.get("https://runsignup.com/Race/Donate/90853/BecomeFundraiser")
            # Thread.sleep(1)

