import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://www.usnews.com/news/economy/articles/2021-09-23/jobless-claims-rise-to-351-000-above-expectations",
)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="ad-in-text-target")
print(title.string)