import os
import random
import string
import time as Thread
# from datetime import date
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

### git check
## get check 2

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)

# topic = ("robux","vbucks")

topic = ("robux", "vbucks", "fskins", "garena", "insta", "fb", "cash", "among",
         "pokemon", "tiktok", "onlyfans", "brawl", "coin", "igfollowers")

# topic = ("fskins", "robux","vbucks","garena")
# topic = ("onlyfans", "coin","brawl")


for x in range(len(topic)):

    file = topic[x]
    if topic[x] == "robux" or topic[x] == "vbucks" or topic[x] == "garena" or topic[x] == "fskins":
        numrep = 5
    else:
        numrep = 5

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
    klist = klist.replace('\n', '')

    num = random.randrange(0, len(lines))
klist1 = (lines[num])

# path of randome files
niche = random.choice(os.listdir(b))

#######
driver.get("https://hamrosmartpasal.com/adverts/add/")
Thread.sleep(6)


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


chars = string.ascii_letters + string.ascii_uppercase + string.digits
chars1 = string.digits
chars2 = string.ascii_letters

size1 = 3
size2 = 4
size3 = 8

random1 = (random_string_generator(size1, chars1))
randomChar = (random_string_generator(size2, chars))
random3 = (random_string_generator(size2, chars2))
onlineusers = (random_string_generator(size2, chars1))
mega = (random_string_generator(size3, chars))

randomChar = randomChar.replace('\n', '')

with open(b + "\\" + niche, encoding='utf-8') as f:
    lines = f.readlines()
f = ''.join(lines)
f = f.replace('COOL', randomChar)
f = f.replace('MYDOMAINLINK', 'https://kenhacks.com/' + file)

f = f.replace('99999', onlineusers)
f = f.replace('MYKEYWORD', (klist.upper() + "-" + klist1.upper()))
f = f.replace('DATETIME', d2)
f = f.replace('MEGA', mega)
f = f.replace("\n", "")
f = f.replace("'", "")
f = f.replace("<h1>", "<strong>")
f = f.replace("</h1>", "</strong>")
print(b + "\\" + niche)

b1 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "adverts_person")))

b1.send_keys(mega)

b2 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'adverts_email')))
b2.send_keys(randomChar + random1 + "@gmail.com")

b3 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'adverts_phone')))
b3.send_keys(random1 + random1)

driver.execute_script("tinyMCE.activeEditor.setContent('%s')" % f)

# pyperclip.copy(f)
# driver.switch_to.frame("post_content_ifr")
#
# text_area1 = driver.find_element_by_id('tinymce')
# text_area1.click()
# text_area1.send_keys(Keys.CONTROL, 'a')
# text_area1.send_keys(Keys.CONTROL, 'c')
# text_area1.send_keys(Keys.CONTROL, 'v')

# b5 = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, "//span[text()='There are errors in your form. Please correct them before proceeding.']")))

b4 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'post_title')))
title = (klist.upper() + " " + klist.upper() + "-(" + randomChar + ")")

b4.send_keys(title)

b6 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@class='adverts-button adverts-cancel-unload']")))
b6.click()

b6 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='Publish Listing']")))
b6.click()
# b6 = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, "(//input[@type='submit'])[3]")))
# b6.click()

b7 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div[2]/p/a')))
b7.click()

# b7 = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, "//div[3]/p/a")))
# b7.click()

Thread.sleep(1)
with open('E:\\connect\\\12.txt', "a") as myfile:
    ouuu = driver.current_url

    myfile.write('<a href="' + ouuu + '">' + randomChar + '</a>' + '\n')
    print("Done=" + (str(i)))
