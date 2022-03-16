import os
import time as Thread
# from datetime import date
from datetime import datetime, timedelta
import random
from myFun import randomData
from bs4 import BeautifulSoup
global topic
global typepost
globalklist
globalklist1

typepost="xcccsacs"
topic = ("robux", "vbucks")

# kniche="garenafreefire"
# topic = ("garena","#","insta")
topic = ("robux", "vbucks", "fskins", "garena", "insta", "fb", "cash", "among","pokemon", "tiktok", "onlyfans", "brawl","coin")
# topic = ("fskins", "robux","vbucks","garena")
# topic = ("onlyfans", "coin","brawl")

def filedata(x):


    file = topic[x]
    if topic[x] == "robux" or topic[x] == "vbucks" or topic[x] == "garena" or topic[x] == "fskins":
        numrep = 4
    else:
        numrep = 2
    print(topic[x])

    dir = 'D:\\MYNEW\\a'
    a = "D:\\MYNEW\\a\\files\\"

    full_path = os.path.join(dir, file)

    presentday = datetime.now()
    nextday = presentday + timedelta(1)
    d2 = presentday.strftime('%d-%m-%Y')
    for i in range(0, numrep):

        b = a + file
        globalklist
        global f
        globalklist1
        with open(full_path + ".csv", 'r') as f:
            lines = f.readlines()

        num = random.randrange(0, 5)
       klist = str(lines[num])
       klist =klist.replace('\n', '')

        num1 = random.randrange(4, len(lines))
       klist1 = (lines[num1])
       klist1 =klist1.replace('\n', '')

        # path of randome files
        niche = random.choice(os.listdir(b))

        # MAINTITLE = "\n\n" + (klist + " - " +klist1 + "{" + random1 + "}") + "\n\n"

        MAINTITLE = "<h1>" + (klist + " - " +klist1 + "{" + random1 + "}") + "</h1>"
        DATETIME = "<h2>" + ("Updated: " + d2 + "|{onlineusers:" + onlineusers + "}") + "</h2>"
        LINKD = "https://kenhacks.com/" + file

        with open(b + "\\" + niche, encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

            f = (soup.prettify())
            if typepost == "html":
                MYDOMAINLINK = "<a href=" + LINKD + ">" + "CLICK HERE TO USE THIS HACK" + "</a></br>"

                f = f.replace('MAINTITLE', MAINTITLE.upper())
                f = f.replace('DATETIME', DATETIME.upper())

                f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                # f = f.replace('</br>',"\n\n")
            else:
                # MYDOMAINLINK = "CLICK HERE TO USE THIS HACK :"+LINKD+"\n"
                MYDOMAINLINK = "`CLICK HERE TO USE Hack. <" + LINKD + ">`__\n\n" + "`CLICK HERE TO USE Hack. <" + LINKD + ">`__\n\n"

                f = f.replace('MAINTITLE', MAINTITLE.upper() + "~~~~~~~~~~~~")
                f = f.replace('DATETIME', DATETIME.upper())
                f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                f = f.replace('<H1>', "")
                f = f.replace('</H1>', "\n")

                f = f.replace('<H2>', "")
                f = f.replace('</H2>', "\n")

                f = f.replace('</br>', "\n")

                f = f.replace('<p>', "")

                f = f.replace('</p>', "\n")

                # fout = open(r"C:\Users\Asif\Desktop\outt.txt", "w", encoding='utf-8')
                # fout.write(f)

                print(f)





