from bs4 import BeautifulSoup
import requests
import time as Thread

URL = 'https://www.namecheap.com/market/buynow/?size=100&page=8&filter=%5B%7B%22id%22%3A%22price%22%2C%22value%22%3A%5B0%2C10%5D%7D%2C%7B%22id%22%3A%22noHyphens%22%2C%22value%22%3Atrue%7D%2C%7B%22id%22%3A%22noNumbers%22%2C%22value%22%3Atrue%7D%2C%7B%22id%22%3A%22nameLength%22%2C%22value%22%3A%5B0%2C8%5D%7D%5D'


content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')

Thread.sleep(6)

for a in soup.find_all('a', href=True):
    print(a['href'])