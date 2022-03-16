import os
import random
import string
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from  conData import  data

MAINTITLE = "<h1>" + (klist + " - " + klist1 + "{" + random1 + "}") + "</h1>"
DATETIME = "<h2>" + ("Updated: " + d2 + "|{onlineusers:" + onlineusers + "}") + "</h2>"
LINKD = "https://kenhacks.com/" + file

with open(b + "\\" + niche, encoding='utf-8') as f:
    if typepost == "html":
        soup = BeautifulSoup(f, 'html.parser')

        f = (soup.prettify())

        MYDOMAINLINK = "<a href=" + LINKD + ">" + "CLICK HERE TO USE THIS HACK" + "</a></br>"

        f = f.replace('MAINTITLE', MAINTITLE.upper())
        f = f.replace('DATETIME', DATETIME.upper())

        f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
        # f = f.replace('</br>',"\n\n")
    else:
        # f = BeautifulSoup(f, "lxml").text
        soup = BeautifulSoup(f, 'html.parser')

        f = (soup.prettify())
        print("enrscsc")

        # MYDOMAINLINK = "CLICK HERE TO USE THIS HACK :"+LINKD+"\n"
        MYDOMAINLINK = "`CLICK HERE TO USE Hack. <" + LINKD + ">`__\n\n" + "`CLICK HERE TO USE Hack. <" + LINKD + ">`__\n\n"

        f = f.replace('MAINTITLE', MAINTITLE.upper() + "~~~~~~~~~~~~")
        f = f.replace('DATETIME', DATETIME.upper())
        f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
        f = f.replace('<H1>', "")
        f = f.replace('</H1>', "\n")
        f = f.replace('<H2>', "")
        f = f.replace('\t</p>', "\n")
        f = f.replace('<p>', "")

        print(f)
