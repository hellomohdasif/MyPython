import getpass
import os
import random
import string
import time as Thread
# from datetime import date
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

### git check
## get check 2


profile = "1"

if profile == "2":
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

else:
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

# topic = ("fb","insta")
topic = ("robux", "vbucks", "fskins", "garena")


# topic = ("robux", "vbucks", "fskins", "garena", "insta", "fb", "cash", "among",
# "pokemon", "tiktok","onlyfans","brawl","coin","igfollowers")


# topic = ("fskins", "robux","vbucks","garena")
# topic = ("onlyfans", "coin","brawl")
# s = "jonathanfulltmp"
# def createRandomSortedList(num, start=1, end=16):
#     arr = []
#     tmp = random.randint(start, end)
#
#     for x in range(num):
#
#         while tmp in arr:
#             tmp = random.randint(start, end)
#
#         arr.append(tmp)
#
#     arr.sort()
#
#     return arr
#
#
# print(createRandomSortedList(5))
# listnum = (createRandomSortedList(5))
#
# for i in listnum:
#     s = s[:i] + "." + s[i:]  # as suggested in your link
#     s = s.replace("..", ".")
#     # s = s.replace("++", ".")
#
# finalemail=s+"@gmail.com"
# print(finalemail)


def changeme():
    for x in range(len(topic)):

        file = topic[x]
        if topic[x] == "robux" or topic[x] == "vbucks" or topic[x] == "garena" or topic[x] == "fskins":
            numrep = 21
        else:
            numrep = 31

        dir = 'E:\\connect\\MYNEW\\a'
        a = "E:\\connect\\MYNEW\\a\\files\\"

        full_path = os.path.join(dir, file)

        presentday = datetime.now()
        nextday = presentday + timedelta(1)
        d2 = presentday.strftime('%d-%m-%Y')
        d3 = nextday.strftime('%d-%m-%Y')

        for i in range(0, numrep):

            b = a + file

            with open(full_path + ".csv", 'r') as k:
                lines = f.readlines()

            num = random.randrange(0, 5)

            klist = str(lines[num])
            klist = klist.replace('\n', '')

            num = random.randrange(0, len(lines))
            klist1 = (lines[num])

            # path of randome files
            niche = random.choice(os.listdir(b))

            #######
            driver.switch_to.window(driver.window_handles[0])
            driver.get("https://maccaboard.paulmccartney.com/user/register")

            # driver.get("https://maccaboard.paulmccartney.com/user/123451/edit")
            # Thread.sleep(2)
            # driver.refresh()


            def random_string_generator(str_size, allowed_chars):
                return ''.join(random.choice(allowed_chars) for x in range(str_size))


            chars = string.ascii_letters + string.ascii_uppercase + string.digits
            chars1 = string.digits
            chars2 = string.ascii_letters

            size1 = 4
            size2 = 4

            size3 = 6

            random1 = (random_string_generator(size1, chars1)).lower()
            randomChar = (random_string_generator(size2, chars2)).lower()
            onlineusers = (random_string_generator(size2, chars1)).lower()
            mega = (random_string_generator(size3, chars)).lower()

            MAINTITLE = ("<h1>" + (klist + " - " + klist1 + "{" + randomChar + "}") + "</h1>").upper()
            DATETIME = "<h3>" + ("Updated: " + d3 + " ( onlineusers:" + onlineusers + ") ") + "</h3>"
            # LINKD = "https://kenhacks.com/" + file
            LINKD = "https://gamecode.site/" + file

            with open(b + "\\" + niche, encoding='utf-8') as f:

                f = ''.join(lines)

                soup = BeautifulSoup(f, 'html.parser')

                f = (soup.prettify())
                # MYDOMAINLINK = "<h2><a href=" + '"' + LINKD + '"'">" + "CLICK HERE TO USE THIS HACK" + "</a></h2>"
                MYDOMAINLINK = "<h2><a href=" + '"' + LINKD + '"'">" + "<img src='https://i.imgur.com/0cnfd07.png'>" + "</a></h2>"
                MAINTITLE = MAINTITLE + DATETIME + MYDOMAINLINK

                # f = f.replace('MAINTITLE', MAINTITLE.upper())
                # f = f.replace('DATETIME', DATETIME.upper())
                #
                # f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                print("===================================")
                print(f)


                f = MAINTITLE + f
                print(f)
                f = f.replace("\n", "")
                f = f.replace("'", "")

                print(b + "\\" + niche)
                print(klist)

                klist = klist.replace(' ', '-')

                klist1 = klist1.replace(' ', '-')
                # driver.get("https://maccaboard.paulmccartney.com/user?verified=1")

                fla = True
                while fla:

                    try:
                        # b411 = WebDriverWait(driver, 5).until(
                        #     EC.element_to_be_clickable((By.ID, 'edit-submit')))
                        #
                        # b411.click()

                        b33 = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="ipe-item--field_user_fun_facts"]/div')))

                        b33.click()

                        frame = driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
                        driver.switch_to.frame(frame)
                        body11 = driver.find_element(By.TAG_NAME, 'body')
                        # body11.send_keys("213123")


                        driver.execute_script("arguments[0].innerHTML ='" + f + "'", body11)
                        Thread.sleep(1)
                        driver.switch_to_default_content()

                        Thread.sleep(1)

                        driver.switch_to.parent_frame()
                        Thread.sleep(3)
                        button = driver.find_element_by_css_selector(
                            "div#ipe-item--field_user_fun_facts > form[method='post'] input[name='ipe-form--submit']")
                        button.click()
                        fla = False
                        Thread.sleep(1)
                    except UnexpectedAlertPresentException as e:
                        print("Entered")
                        driver.refresh()

                    else:

                        profile = (
                            driver.find_element_by_xpath('//*[@id="tabs-row"]/div/ul/li/a').get_attribute('href'))
                        print(profile)

                        # button1 = driver.find_element_by_css_selector(
                        #     "button#c-menu--secondary--mobile-actions--user-menu")
                        # button1.click()
                        #
                        # button2 = driver.find_element_by_css_selector(
                        #     "nav#c-menu--user  .last.leaf.o-menu--item > a")
                        # button2.click()

                        Thread.sleep(10)

                        with open('E:\\connect\\final.txt', "a") as myfile:
                            klist = klist.upper().replace(' ', '-')
                            print(klist)
                            # ouuu = "https://maccaboard.paulmccartney.com/users/" + str(profile)

                            # myfile.write('<a href="' + ouuu + '">' + randomChar + '</a>' + '\n')
                            myfile.write('<a href="' + profile + '">' + randomChar + '</a>' + '\n')

                            print("Done=" + (str(i)))

                # b1 = WebDriverWait(driver, 5).until(
                #     EC.element_to_be_clickable((By.LINK_TEXT, "Verify")))
                # print(b1)
                # b1.click()


changeme()
