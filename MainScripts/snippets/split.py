import getpass
import os
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
import time as Thread
from urllib.parse import urlparse
from urllib.parse import parse_qs


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
# chrome_driver ="C:\\chromedriver.exe"
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
# driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)


with open("E:\\tech.txt", 'r') as f:
    lines = f.readlines()
    # lines = [line.replace('\n', '') for line in lines]
    # lines = [line.replace('  ', '') for line in lines]

i=0
while (i < len(lines)):

    driver.get(lines[i])
    Thread.sleep(1)



    with open("E:\\out.txt", "a") as myfile:

        abc=driver.current_url
        split_string = abc.split("?", 1)
        substring = split_string[0]

        # parsed_url = urlparse(abc)
        # captured_value = parse_qs(parsed_url.query)['response-content-disposition'][0]
        # print(captured_value)
        # # final=abc.replace(str("?response-content-disposition"+captured_value), "xcxc\n")
        # final=abc.replace(str("?response-content-disposition"+captured_value), "xcxc\n")

        print(substring)
        myfile.write(substring+"\n")


        # myfile.write('<a href="' + driver.current_url + '">' + "sdad" + '</a>' + '\n')
        print(i)
        i = i + 1




