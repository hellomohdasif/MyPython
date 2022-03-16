import getpass
import os
import random
import string
import time as Thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

get="2"

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

    path = "E:\\1\\"
    uploadpath = "C:\\Users\\Asif\\Desktop\\1.txt"


base1 = "https://www.unl.pt/sites/default/files/webform/"

a = os.listdir(path)

i = 0

while (i < len(a)):
    driver.get(
        "https://www.unl.pt/en/supernova-online-application")


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
        EC.element_to_be_clickable((By.ID, "edit-submitted-carta-de-motivacao-upload")))
    s3.send_keys(path + a[i])

    s4 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-carta-de-recomendacao-opcional-upload")))
    s4.send_keys(path + a[i+1])

    s5 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-diploma-do-ensino-secundario-upload")))
    s5.send_keys(path + a[i + 2])

    s6 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-historico-escolar-obrigatorio-upload")))
    s6.send_keys(path + a[i + 3])

    s7 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-copia-do-passaporte-upload")))
    s7.send_keys(path + a[i + 4])

    s8 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-comprovativo-de-lingua-inglesa-upload")))
    s8.send_keys(path + a[i + 5])

    s9 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-comprovativo-de-lingua-portuguesa-upload")))
    s9.send_keys(path + a[i + 6])

    s10 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='op']")))
    s10.click()

    try:

        wait = WebDriverWait(driver, 10)
        men_menu = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                '//*[@id="block-system-main"]/div')))

        print("Found")
    except:
        pass

    print("Done=" + str(i))
    # print("Done=" + str(i + 1))

    with open(uploadpath, "a") as myfile:
        link1 = base1 + a[i]
        link2 = base1 + a[i+1]
        link3 = base1 + a[i+2]
        link4 = base1 + a[i + 3]
        link5 = base1 + a[i + 4]
        link6 = base1 + a[i + 5]
        link7 = base1 + a[i + 6]





        myfile.write('<a href="' + link1 + '">' + randomChar + '</a>' + '\n')
        myfile.write('<a href="' + link2 + '">' + randomChar + '</a>' + '\n')
        myfile.write('<a href="' + link3 + '">' + randomChar + '</a>' + '\n')
        myfile.write('<a href="' + link4 + '">' + randomChar + '</a>' + '\n')
        myfile.write('<a href="' + link5 + '">' + randomChar + '</a>' + '\n')
        myfile.write('<a href="' + link6 + '">' + randomChar + '</a>' + '\n')
        myfile.write('<a href="' + link7 + '">' + randomChar + '</a>' + '\n')



        i = i + 6


