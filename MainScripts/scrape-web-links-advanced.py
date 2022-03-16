import requests
from bs4 import BeautifulSoup




for i in range(1,563):
    urls = "https://rexdl.com/page/" + (str(i))

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    reqs = requests.get(urls, headers=headers)
    reddit1Content = BeautifulSoup(reqs.content, "lxml")



    data = reddit1Content.findAll('h2', attrs={'class':'post-title'})
    for h2 in data:
        links = h2.findAll('a')
        for a in links:
            with open('E:\\connect\\rexdl.txt', "a") as myfile:
                myfile.write(a['href'] + "\n")



               #Thread.sleep(2)


            #print(a['href'])


        #f.write(str(data))

        #f.write("\n")


