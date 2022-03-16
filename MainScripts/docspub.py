import getpass
import os
import random
import string
import time as Thread
from datetime import datetime, timedelta

import pyperclip
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conData import topics

# import conData.topics
topics.manintopics()
topic=topics.topic

profile = "3"
typepost="xcccsacs"
# kniche="garenafreefire"
outresult="E:\\connect\\\seltxt\\docs.txt"
if profile == "3":
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options.add_argument('headless')
    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')


else:

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
    driver = webdriver.Chrome(options=options, executable_path=r"C:\chromedriver.exe")

    # options = webdriver.ChromeOptions()
    # options.add_argument("--log-level=3")
    # options.add_argument("--disable-blink-features")
    # # options.add_argument('headless')
    #
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
    # driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)



def changeme():


    for x in range(0, len(topic)):


        file = topic[x]
        if topic[x] == "robux" or topic[x] == "vbucks" or topic[x] == "garena" or topic[x] == "fskins":
            numrep = 5
        else:
            numrep = 3

        dir = 'E:\\connect\\\MYNEW\\a'
        a = "E:\\connect\\\MYNEW\\a\\files\\"

        full_path = os.path.join(dir, file)

        presentday = datetime.now()
        nextday = presentday + timedelta(1)
        d2 = presentday.strftime('%d-%m-%Y')
        for i in range(0, numrep):

            def random_string_generator(str_size, allowed_chars):
                return ''.join(random.choice(allowed_chars) for x in range(str_size))

            chars = string.ascii_letters + string.ascii_uppercase + string.digits
            chars1 = string.digits + string.ascii_letters
            chars2 = string.ascii_letters
            chars3 = string.digits

            size1 = 6
            size2 = 4
            size3 = 8

            random1 = (random_string_generator(size1, chars1))
            randomChar = (random_string_generator(size2, chars))
            random3 = (random_string_generator(size2, chars2))
            onlineusers = (random_string_generator(size2, chars3))
            mega = (random_string_generator(size3, chars))

            b = a + file
            global klist
            global f
            global klist1
            with open(full_path + ".csv", 'r') as f:
                lines1 = f.readlines()

            num = random.randrange(0, 3)
            klist = str(lines1[num])
            klist = klist.replace('\n', '')

            num1 = random.randrange(0, len(lines1))
            klist1 = (lines1[num1])
            klist1 = klist1.replace('\n', '')

            # path of randome files
            niche = random.choice(os.listdir(b))

            # MAINTITLE = "\n\n" + (klist + " - " + klist1 + "{" + random1 + "}") + "\n\n"

            ##################################################################################

            MAINTITLE = "<h1>" + (klist + " - " + klist1 + "{" + random1 + "}") + "</h1>\n"
            DATETIME = "<h2>" + ("Updated: " + d2 + "|{onlineusers:" + onlineusers + "}") + "</h2>\n\n"
            LINKD = "https://kenhacks.com/" + file


            with open(b + "\\" + niche, encoding='utf-8') as f:


                if typepost == "html":

                    soup = BeautifulSoup(f, 'html.parser')

                    f = (soup.prettify())

                    MYDOMAINLINK = "<a href=" + LINKD + ">" + "CLICK HERE TO USE THIS HACK" + "</a></br>"
                    MAINTITLE = MAINTITLE + DATETIME + MYDOMAINLINK


                    f = f.replace('MAINTITLE', MAINTITLE.upper())
                    # f = f.replace('DATETIME', DATETIME.upper())

                    # f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                    # f = f.replace('</br>',"\n\n")
                else:

                    # f = BeautifulSoup(f, "lxml").text
                    # soup = BeautifulSoup(f, 'html.parser')
                    #
                    # f = (soup.prettify())

                    lines = f.readlines()
                    f = ''.join(lines)


                    # MYDOMAINLINK = "CLICK HERE TO USE THIS HACK :"+LINKD+"\n"
                    MYDOMAINLINK = "`CLICK HERE TO USE Hack. <" + LINKD + ">`__\n\n" + "`CLICK HERE TO USE Hack. <" + LINKD + ">`__\n\n"

                    MAINTITLE = MAINTITLE.upper()+ "~~~~~~~~~~~~\n" + DATETIME.upper() + MYDOMAINLINK

                    # f = f.replace('MAINTITLE', MAINTITLE.upper() + "~~~~~~~~~~~~")
                    # f = f.replace('DATETIME', DATETIME.upper())
                    # f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                    f = f.replace('"', "")
                    f = f.replace('”', "")
                    # f = f.replace('<p>\t', "")
                    # f = f.replace('\t<p>', "")
                    f = f.replace('<p>', "")
                    f = f.replace('</p>', "\n")


                    f=MAINTITLE+f

                    f = f.replace('<H1>', "")
                    f = f.replace('</H1>', "")
                    f = f.replace('<H2>', "")
                    f = f.replace('</H2>', "")

                    # f = re.sub(' +', ' ', f)




                    # f = f.replace('\t</p>', "\n")
                    # f = f.replace('<p>', "")


                    #######################################################################################################





                    klist1 = klist1.replace(' ', '-')
                    klist = klist.replace(' ', '-')
                    slug = random1 + "-a" + mega



                    driver.get("https://github.com/new")

                    flg = True
                    while flg:

                        try:
                            s3 = WebDriverWait(driver, 80).until(
                                EC.element_to_be_clickable((By.ID, 'repository_name')))
                            s3.send_keys(slug)
                            wait = WebDriverWait(driver, 5)
                            men_menu = wait.until(EC.visibility_of_element_located((By.XPATH,"//form[@id='new_repository']//auto-check[@src='/repositories/check-name']//dd[@class='success']")))
                            flg = False

                        except:
                            s3.clear()

                            slug = mega

                        else:
                            s4 = WebDriverWait(driver, 8).until(
                                EC.element_to_be_clickable((By.ID, 'repository_auto_init')))
                            s4.click()
                            Thread.sleep(1)

                            s5 = WebDriverWait(driver, 8).until(
                                EC.element_to_be_clickable((By.XPATH, '//div[4]/button')))
                            s5.click()

                            s7 = WebDriverWait(driver, 8).until(
                                EC.element_to_be_clickable((By.XPATH, '//*[@id="code-tab"]')))
                            s7.click()
                            Thread.sleep(1)
                            flag = True
                            while flag:

                                try:
                                    s7 = WebDriverWait(driver, 2).until(
                                        EC.element_to_be_clickable(
                                            (By.XPATH,
                                             '//*[@id="repo-content-pjax-container"]/div/div[2]/div/div[2]/details/summary/span')))
                                    s7.click()

                                    s8 = WebDriverWait(driver, 8).until(
                                        EC.element_to_be_clickable(
                                            (By.CSS_SELECTOR,
                                             '#repo-content-pjax-container > div > div.gutter-condensed.gutter-lg.flex-column.flex-md-row.d-flex > div.flex-shrink-0.col-12.col-md-9.mb-4.mb-md-0 > div.file-navigation.mb-3.d-flex.flex-items-start > details > div > ul > li:nth-child(2) > form > button')))
                                    s8.click()
                                    flag = False

                                except:
                                    driver.refresh()

                                else:
                                    s11 = WebDriverWait(driver, 8).until(
                                        EC.element_to_be_clickable(
                                            (
                                                By.NAME, 'filename')))
                                    s11.send_keys("index.rst")

                                    Thread.sleep(1)
                                    lines1 = [w.replace('\n', '') for w in lines1]

                                    keysearched = (str(lines1)) + "\n"

                                    f = f + keysearched
                                    print(f)
                                    pyperclip.copy(f)



                                    flg = True
                                    while flg:

                                        try:
                                            abc = driver.find_element_by_css_selector("pre[role='presentation']")
                                            abc.click()
                                            Thread.sleep(1)

                                            flg = False

                                        except:
                                            driver.refresh()
                                            s11.send_keys("index.rst")

                                        else:
                                            abc.send_keys(Keys.CONTROL, 'v')
                                            Thread.sleep(1)

                                            s14 = WebDriverWait(driver, 8).until(
                                                EC.element_to_be_clickable((By.XPATH, "//button[@id='submit-file']")))
                                            s14.click()
                                            Thread.sleep(1)

                                            driver.get("https://readthedocs.org/dashboard/import/manual/?")

                                            print(klist)
                                            klist = klist.replace('-', ' ')

                                            finalurl = klist + " " + random1

                                            try:
                                                s71 = WebDriverWait(driver, 10).until(
                                                    EC.element_to_be_clickable((By.ID, 'id_basics-name')))
                                                # s71.send_keys(klist+"-"+randomChar)
                                                s71.send_keys(finalurl)
                                            except:
                                                driver.execute_script("window.open('');")
                                                driver.switch_to.window(driver.window_handles[1])
                                                driver.get("https://readthedocs.org/dashboard/import/manual/?")
                                                # driver.get(
                                                #     )

                                                s71 = WebDriverWait(driver, 30).until(
                                                    EC.element_to_be_clickable((By.ID, 'id_basics-name')))
                                            else:
                                                s72 = WebDriverWait(driver, 8).until(
                                                    EC.element_to_be_clickable((By.ID, 'id_basics-repo')))
                                                s72.send_keys(
                                                    "https://github.com/sohailkh44/" + slug)

                                                s74 = WebDriverWait(driver, 8).until(
                                                    EC.element_to_be_clickable((By.ID, 'id_basics-default_branch')))
                                                s74.send_keys("main")

                                                s75 = WebDriverWait(driver, 8).until(
                                                    EC.element_to_be_clickable((By.XPATH, "//input[@value='Next']")))
                                                s75.click()
                                                Thread.sleep(6)

                                                s76 = WebDriverWait(driver, 8).until(
                                                    EC.element_to_be_clickable(
                                                        (By.XPATH,
                                                         '//*[@id="project_details"]/div/div/div[3]/div/form/input[2]')))
                                                s76.click()
                                                finalurl = finalurl.replace(' ', '-')

                                                with open(outresult, "a") as myfile:
                                                    profile = "https://" + finalurl + ".readthedocs.io/en/latest/"
                                                    # profile = "https://"+mega+".readthedocs.io/en/latest/"
                                                    profile = profile.replace('--', '-')

                                                    myfile.write(
                                                        '<a href="' + profile + '">' + randomChar + '</a>' + '\n')


for i in range(0, 1):
    changeme()
    print("Done=" + (str(i)))
