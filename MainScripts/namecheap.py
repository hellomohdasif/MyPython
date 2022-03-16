import requests
from bs4 import BeautifulSoup



i=1
for i in range(i,563):

    urls = "https://www.namecheap.com/market/buynow/?size=100&page="+(str(i))+"&filter=%5B%7B%22id%22%3A%22price%22%2C%22value%22%3A%5B0%2C10%5D%7D%2C%7B%22id%22%3A%22noHyphens%22%2C%22value%22%3Atrue%7D%2C%7B%22id%22%3A%22noNumbers%22%2C%22value%22%3Atrue%7D%2C%7B%22id%22%3A%22nameLength%22%2C%22value%22%3A%5B0%2C8%5D%7D%5D"
    print(urls)

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    reqs = requests.get(urls, headers=headers)
    reddit1Content = BeautifulSoup(reqs.content, "lxml")

    for link in reddit1Content.find_all('a'):
        print(link.get('href'))



    # data = reddit1Content.findAll('span', attrs={'class':'tw-text-black tw-text-opacity-0'})
    # for span in data:
    #     links = span.findAll('a')
    #     for a in links:
    #         with open('E:\\connect\\11.txt', "a") as myfile:
    #             myfile.write(a['href'] + "\n")
    #


               #Thread.sleep(2)


            #print(a['href'])


        #f.write(str(data))

        #f.write("\n")


