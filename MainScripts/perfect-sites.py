import getpass
import os
import random
import string
import time as Thread
# from datetime import date
from datetime import datetime, timedelta

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# options_new = webdriver.ChromeOptions()
# options_new.add_argument("--window-size=20X20")
# options_new.add_argument("--headless")
# options_new.add_argument("--width=100")
# options_new.add_argument("--height=100")
# options_new.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# driver1 = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options_new)


# options_new = webdriver.ChromeOptions()
# options_new.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# driver1 = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options_new)


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

machine = "dhgh"

#topic = ("robux", "vbucks")
topic = ("robux", "vbucks", "fskins", "garena", "insta", "fb", "cash", "among","pokemon", "tiktok", "onlyfans", "brawl", "coin", "igfollowers")
# topic = ("fskins", "robux","vbucks","garena")
# topic = ("onlyfans", "coin","brawl")


driver.get("http://demos.codexworld.com/add-wysiwyg-html-editor-to-textarea-website/")

for z in range(0, 10):
    for x in range(len(topic)):

        file = topic[x]
        if topic[x] == "robux" or topic[x] == "vbucks":
            numrep = 10
        else:
            numrep = 5

        if machine == "vm":
            dir = 'z:\\MYNEW\\a\\'
            a = "z:\\MYNEW\\a\\files\\"
        else:
            dir = 'E:\\connect\\MYNEW\\a\\'
            a = "E:\\connect\\MYNEW\\a\\files\\"

        full_path = os.path.join(dir, file)

        presentday = datetime.now()
        nextday = presentday + timedelta(1)
        d2 = presentday.strftime('%d-%m-%Y')

        for i in range(0, numrep):
            b = a + file

            with open(full_path + ".csv", 'r') as f:
                lines = f.readlines()

            # num = random.randrange(0, len(lines))
            num = random.randrange(0, 2)
           klist = (lines[num])

            # num = random.randrange(0, len(lines))
            num1 = random.randrange(0, 5)
           klist1 = (lines[num1])

            # path of randome files
            niche = random.choice(os.listdir(b))


            #######

            def random_string_generator(str_size, allowed_chars):
                return ''.join(random.choice(allowed_chars) for x in range(str_size))


            chars = string.ascii_letters + string.ascii_uppercase + string.digits
            chars1 = string.digits
            chars2 = string.ascii_letters

            size1 = 4
            size2 = 4

            size3 = 6

            randomNum = (random_string_generator(size1, chars1))
            randomChar = (random_string_generator(size2, chars2))
            onlineusers = (random_string_generator(size2, chars1))
            mega = (random_string_generator(size3, chars))

            with open(b + "\\" + niche, encoding='utf-8') as f:
                lines = f.readlines()
            f = ''.join(lines)
            f = f.replace('COOL', randomChar)
            f = f.replace('MYDOMAINLINK', 'https://kenhacks.com/' + file)

            f = f.replace('99999', onlineusers)
            f = f.replace('MYKEYWORD', (klist.upper() + " - " +klist1.upper()))
            f = f.replace('DATETIME', d2)
            f = f.replace('MEGA', mega)
            f = f.replace("\n", "")
            f = f.replace("'", "")
            print(b + "\\" + niche)

            # element2 = WebDriverWait(driver, 8000).until(
            #     EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'edit_content_link btn')]")))
            #
            # element2.click()
            #
            # element3 = WebDriverWait(driver, 8000).until(
            #     EC.element_to_be_clickable((By.ID, 'eportfolio_entry_name')))
            # element3.send_keys(randomChar)
            # Thread.sleep(1)

            print("Page Title of urlA : " + driver.title)

            driver.switch_to.frame("myTextarea2_ifr")

            text_area1 = driver.find_element_by_id('tinymce')
            text_area1.send_keys(Keys.CONTROL, 'a')
            text_area1.send_keys(Keys.BACKSPACE)
            driver.switch_to_default_content()

            driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % f)
            driver.switch_to.frame("myTextarea2_ifr")

            text_area1.send_keys(Keys.CONTROL, 'a')
            text_area1.send_keys(Keys.CONTROL, 'c')
            driver.switch_to_default_content()

            Thread.sleep(1)

            # text_area1.click()

            # driver.switch_to_default_content()
            try:
                driver.execute_script("window.open('');")
                # switch to new window with switch_to.window()
                driver.switch_to.window(driver.window_handles[1])
                driver.get("https://sites.google.com/u/0/create?usp=sites_home&ths=true")
                print("Page Title of urlA : " + driver.title)

            except:
                driver.execute_script("window.open('');")
                # switch to new window with switch_to.window()
                driver.switch_to.window(driver.window_handles[1])
                driver.get("https://sites.google.com/u/0/create?usp=sites_home&ths=true")

            abc2 = WebDriverWait(driver, 8000).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='wWGgfe']/div/div/div")))
            abc2.click()
            Thread.sleep(1)

            element = driver.find_element_by_xpath("//div[@role='textbox']//p[1]")
            element.send_keys(Keys.CONTROL, 'v')

            doo1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
            doo1.click()
            doo1.send_keys(Keys.CONTROL, 'a')
            # pyperclip.copy("("+randomChar+") " +klist1 + "[" +randomNum+"]")
            pyperclip.copy(klist.upper() + "- " +klist1.upper() + "(" + randomNum + ")")

            doo1.send_keys(Keys.CONTROL, 'v')

            Thread.sleep(1)

            abc1 = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Your page title']")))
            abc1.click()
            abc1.send_keys(Keys.CONTROL, 'a')

            pyperclip.copy(klist.upper() + "-" +klist1.upper() + "{" + randomChar + "}")

            abc1.send_keys(Keys.CONTROL, 'v')

            lol = driver.find_element_by_xpath("//div[13]/div/span")
            lol.click()

            # abc1 = WebDriverWait(driver, 7).until(
            #     EC.element_to_be_clickable((By.XPATH, "//div[13]/div/span")))
            # abc1.click()
            ###################
            mike =klist1[0:23]
            ###################

            abc4 = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//label[text()='Web address']/following::input")))
            abc4.click()
            abc4.clear()
            abc4.send_keys(mike + "-" + randomChar)
            nice = abc4.get_attribute('value')

            try:

                wait = WebDriverWait(driver, 10)
                men_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                        '#yDmH0d > div.NBxL9e.iWO5td > div > div.I7OXgf.B6r3ub.JKIKje.ZEeHrd.Inn9w.iWO5td > span > div > div.noiLqd > div.uxEN2b > div.W9wDc.D3oBEe.x4uME.uQUqpd.svmwUe.CDELXb > div.n9IS1.oJeWuf.rXTzdc > span > span > svg')))
                print("Found")


            except:

                print("not Found")
                abc4.clear()
                abc4.send_keys(randomChar + "-" + mega)
                nice = abc4.get_attribute('value')

            abc9 = WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='Manage']")))
            abc9.click()

            print("switched")
            abc10 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     "html>body>div>div>div:nth-of-type(2)>span>c-wiz>div>div>div>div:nth-of-type(2)>c-wiz>div>div>div>div>div>div:nth-of-type(2)>div>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div>div>div>div>div>div>div>div>span:nth-of-type(2)>div>span>span")))
            abc10.click()
            abc11 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[text()='tellhi']")))
            abc11.click()
            # try catch block here
            abc12 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//li[@data-value='5']")))
            abc12.click()
            Thread.sleep(1)

            abc13 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Done'])[2]")))
            abc13.click()

            driver.switch_to_default_content()

            abc8 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//div[@data-id='j6LnYe']//span)[3]")))
            abc8.click()
            Thread.sleep(1)

            element3 = WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, 'flipthis-wrapper')))

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            if machine == "vm":
                saveto = "z:\\MYNEW\\sites.txt"
            else:
                saveto = "E:\\connect\\\sites.txt"

            with open(saveto, "a") as myfile:

                link1 = "https://web.sites.google.com/gamecode.site/" + nice
                link2 = "https://amp.sites.google.com/gamecode.site/" + nice
                link3 = "https://mobile.sites.google.com/gamecode.site/" + nice

                myfile.write('<a href="' + link1 + '">' + randomChar + '</a>' + '\n')
                # myfile.write('<a href="' + link2 + '">' + randomChar + '</a>' + '\n')
                # myfile.write('<a href="' + link3 + '">' + randomChar + '</a>' + '\n')

                # with open('E:\\connect\\\linkss.txt', "a") as myfile1:
                #     myfile1.write(link1+ '\n')
                #     myfile1.write(link2+ '\n')

                print("Done=" + (str(i)))
                print(topic[x])

    with open(saveto, "a") as myfile:

        myfile.write("-------------------------\n")
        print("LOOP=" + (str(z)))
