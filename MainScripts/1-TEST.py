from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import getpass
import hashlib

import time as Thread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("start-maximized")
options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))

# options.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
range1="16"
range2="25"
namelength="12"

s = Service('C:\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)



driver.refresh()
driver.get("https://www.namecheap.com/market/buynow/?filter=%5B%7B%22id%22%3A%22tld%22%2C%22value%22%3A%5B%22com%22%2C%22net%22%2C%22org%22%2C%22news%22%5D%7D%5D")


price1 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/input')))
price1.clear()
price1.clear()

price1.clear()

price1.send_keys(range2)

price = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div/div/div[2]/div/div/div[2]/div/input')))
price.send_keys(range1)

# abc = driver.find_element_by_xpath('//*[@id="root"]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/input')
# driver.execute_script("arguments[0].value ='" + range2 + "'", abc)
# Thread.sleep(3)



namel = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div/div/div[2]/div/div[2]/div[2]/div[2]/input')))
namel.clear()
namel.clear()

namel.send_keys(namelength)



bb = driver.find_element_by_xpath('//*[@id="root"]/div[4]/div/div/div[2]/div/div[4]/div[2]/div/div/label')
driver.execute_script("arguments[0].click();", bb)

aabb = driver.find_element_by_xpath('//*[@id="root"]/div[4]/div/div/div[2]/div/div[4]/div[2]/div[3]/div/label/span')
driver.execute_script("arguments[0].click();", aabb)

# b31 = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div/div/div[2]/div/div[4]/div[2]/div/div/label')))
# b31.click()
# Thread.sleep(1)
# b32 = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div/div/div[2]/div/div[4]/div[2]/div[3]/div/label/span')))
# b32.click()
# b.find_element_by_xpath("//select[@name='MuiNativeSelect-root']/option[text()='100']").click()

sel = Select(driver.find_element_by_xpath('//*[@id="root"]/div[4]/div/div/div[3]/div[2]/div[2]/select'))
#select by select_by_visible_text() method
sel.select_by_visible_text("100")

for z in range(0, 100):
    print(z)
    Thread.sleep(3)

    # b = driver.find_element_by_xpath("//li[9]/button")
    # driver.execute_script("arguments[0].click();", b)

    # b321 = WebDriverWait(driver, 40).until(
    #     EC.element_to_be_clickable((By.XPATH,'//li[9]/button')))
    # b321.click()


    # page='&filter=%5B%7B"id"%3A"price"%2C"value"%3A%5B11%2C20%5D%7D%2C%7B"id"%3A"noHyphens"%2C"value"%3Atrue%7D%2C%7B"id"%3A"noNumbers"%2C"value"%3Atrue%7D%2C%7B"id"%3A"nameLength"%2C"value"%3A%5B0%2C8%5D%7D%2C%7B"id"%3A"tld"%2C"value"%3A%5B"com"%2C"net"%2C"org"%5D%7D%5D'
    # page='&filter=%5B%7B"id"%3A"price"%2C"value"%3A%5B6%2C10%5D%7D%2C%7B"id"%3A"noHyphens"%2C"value"%3Atrue%7D%2C%7B"id"%3A"nameLength"%2C"value"%3A%5B0%2C8%5D%7D%5D'
    # urls='https://www.namecheap.com/market/buynow/?size=100&page='+(str(z))+'&filter=[{"id":"price","value":[' + str(range1) + ',' + str(range2) + ']},{"id":"tld","value":["com","net","org","news"]}]'
    # urls = "https://www.namecheap.com/market/buynow/?size=100&page="+(str(i))+page
    # driver.get(urls)








    b33 = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[5]/div[2]/div/div/div/table/tbody/tr/td/div/div/label')))

    # if b33.is_displayed():
    #     print("Element found")
    # else:
    #     print("Element not found")



    element = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@id="root"]/div[5]/div[2]/div/div/div[2]/div')))

    get_source = driver.page_source
    soup = BeautifulSoup(get_source, 'html.parser')

    res = []
    datanew = []

    data = soup.findAll('div', attrs={'class': 'tw-flex'})
    for div in data:
        links = div.findAll('a')
        for a in links:
            datanew = (a['href'])
            datanew = datanew.replace("/market/", "")
            datanew = datanew.replace("/", "")
            datanew = datanew.replace("auctions", "")
            datanew = datanew.replace("buynow", "")
            res.append(datanew)

    datanew = list(dict.fromkeys(res))





    while ("" in datanew):
        datanew.remove("")
    print(datanew)

    for element in datanew:
        with open('C:\\Users\\Asif\\Desktop\\base.txt', "r+") as f:
            if element in f.read():
                print("Already Exits")
            else:
                with open('C:\\Users\\Asif\\Desktop\\nameheap.txt', "a") as myfile:
                    myfile.write(element + "\n")

                    f.write(element + "\n")

                    print("SAVED!!")

    b = driver.find_element_by_xpath("//li[9]/button")
    driver.execute_script("arguments[0].click();", b)












