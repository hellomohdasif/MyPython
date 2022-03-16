import requests
from bs4 import BeautifulSoup




for i in range(1,275):
    urls = "https://apkdownload.cc/page/" + (str(i))
    print(urls)

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    reqs = requests.get(urls, headers=headers)
    reddit1Content = BeautifulSoup(reqs.content, "lxml")



    data = reddit1Content.findAll('h5', attrs={'class':'appRowTitle'})
    for h5 in data:
        links = h5.findAll('a')
        for a in links:
            with open('C:\\Users\\Asif\\Desktop\\apkdownloadcc.txt', "a") as myfile:
                myfile.write(a['href'] + "\n")
                print((a['href'] + "\n"))



               #Thread.sleep(2)


            #print(a['href'])


        #f.write(str(data))

        #f.write("\n")


