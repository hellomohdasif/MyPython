import getpass
import os
import random
import string
import time as Thread

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

get="ads"

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
    options.add_argument("disable-infobars")

    options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    path = "E:\\1\\"
    uploadpath = "C:\\Users\\Asif\\Desktop\\1.txt"


base1 = "https://omq.uoregon.edu/sites/omq1.uoregon.edu/files/webform/"

a = os.listdir(path)

i = 0
driver.get(
    "https://omq.uoregon.edu/forms/travel-expense-form")
while (i < len(a)):



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
    new = str(i)
    print(new)

    s3 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-other-receipts-"+new+"-upload")))
    s3.send_keys(path + a[i])

    s4 = WebDriverWait(driver, 8).until(
        EC.element_to_be_clickable((By.ID, "edit-submitted-other-receipts-"+new+"-upload-button")))
    s4.click()

    element = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '#edit-submitted-other-receipts--19 > div > div.form-item.webform-component.webform-component-multiple-file.webform-component--other-receipts--18 > div.file-widget.form-managed-file.clearfix > div > div')))
    Thread.sleep(1)



    # try:
    #
    #     wait = WebDriverWait(driver, 10)
    #     men_menu = wait.until(EC.visibility_of_element_located((By.XPATH,
    #                                                             '//*[@id="block-system-main"]/div/div')))
    #
    #     print("Found")
    # except:
    #     pass

    print("Done=" + str(i))
    # print("Done=" + str(i + 1))

    with open(uploadpath, "a") as myfile:
        link1 = base1 + a[i]

        myfile.write('<a href="' + link1 + '">' + randomChar + '</a>' + '\n')

        i = i + 1


