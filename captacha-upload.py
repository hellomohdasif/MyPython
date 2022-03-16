import getpass
import os
import random
import string
import time as Thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

get="1"

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
    uploadpath = "C:\\Users\\Administrator\\Desktop\\2.txt"

else:
    options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # options.add_argument('headless')

    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

    path = "E:\\1\\"
    uploadpath = "C:\\Users\\Asif\\Desktop\\1.txt"


base1 = "https://forages.oregonstate.edu/sites/dce.oregonstate.edu/files/"
a = os.listdir(path)

i = 0

while (i < len(a)):
    driver.get(
        "https://dce.oregonstate.edu/sa-submissions")
    Thread.sleep(1)


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    chars1 = string.digits
    chars2 = string.ascii_letters

    size1 = 3
    size2 = 4
    size3 = 8

    randomNum = (random_string_generator(size1, chars1))
    randomChar = (random_string_generator(size2, chars))
    randomChar = (random_string_generator(size2, chars2))
    onlineusers = (random_string_generator(size2, chars1))
    mega = (random_string_generator(size3, chars))

    # check = WebDriverWait(driver, 8).until(
    #     EC.element_to_be_clickable((By.XPATH, "//div[2]/div/input[2]")))
    # s1 = WebDriverWait(driver, 8).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#field_gx9l")))
    # s1.send_keys("ASdasd")

    s3 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-upload-upload")))
    s3.send_keys(path + a[i])

    # element = driver.find_element(By.XPATH, '//*[@id="webform-client-form-402"]/div/fieldset/div/div[2]/span')
    # text = element.text
    # print(text)

    abc = text
    split_string = abc.split("+", 1)
    substring = split_string[0]
    substring1 = split_string[1]
    substring1=substring1.replace(" =","")
    substring1=substring1.replace(" ","")

    captcha=int(substring)+int(substring1)
    # print(captcha)
    #
    #
    #
    # print(substring)
    # print(substring1)

    s4 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-captcha-response")))
    s4.send_keys(captcha)



    s6 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.XPATH,"//input[@name='op']")))
    s6.click()

    try:
        check = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//div[3]/div/div/div/div[3]")))
    except:
        pass

    print("Done=" + str(i))
    # print("Done=" + str(i + 1))

    with open(uploadpath, "a") as myfile:
        link1 = base1 + a[i]


        myfile.write('<a href="' + link1 + '">' + randomChar + '</a>' + '\n')
        i = i + 1
