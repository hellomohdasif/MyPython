import os
import random
import string
# from datetime import date
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from conData import topics
import pdfkit
from conData import topics


## IN LAST KEYWORDS
topics.manintopics()
topic = topics.topic

typepost = "html"

machine = "22"
choice = "6"

get = "34"

if get == "1":
    path = "C:\\Users\\Administrator\\Desktop\\1\\"
elif get == "2":

    path = "C:\\Users\\Administrator\\Desktop\\2\\"

else:
    path = "C:\\Users\\Asif\\Desktop\\1\\"

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

for z in range(0, 1):
    for x in range(len(topic)):

        file = topic[x]
        if topic[x] == "robux" or topic[x] == "vbucks" or topic[x] == "cash":
            # if topic[x] == "robux":

            numrep = 200
        else:
            numrep = 5

        if machine == "vm":
            dir = 'z:\\MYNEW\\a\\'
            a = "z:\\MYNEW\\a\\files\\"
        else:
            dir = 'C:\\Users\\Asif\\Desktop\\connect\\MYNEW\\a\\'
            a = "C:\\Users\\Asif\\Desktop\\connect\\MYNEW\\a\\files\\"

        full_path = os.path.join(dir, file)

        presentday = datetime.now()
        nextday = presentday + timedelta(1)
        d2 = presentday.strftime('%d-%m-%Y')
        d3 = nextday.strftime("%B %d, %Y")

        for i in range(0, numrep):
            b = a + file

            with open(full_path + ".csv", 'r') as f:
                lines = f.readlines()

            # num = random.randrange(0, len(lines))
            num = random.randrange(0, len(lines))
            klist = (lines[num])
            klist = klist.replace('\n', '')

            # num = random.randrange(0, len(lines))
            num1 = random.randrange(0, len(lines))
            klist1 = (lines[num1])
            klist1 = klist1.replace('\n', '')

            # path of randome files
            niche = random.choice(os.listdir(b))
            print(niche)


            #######

            # random_number = random.randint(0, 16777215)
            # hex_number = str(hex(random_number))
            # hex_number = '#' + hex_number[2:]

            def random_string_generator(str_size, allowed_chars):
                return ''.join(random.choice(allowed_chars) for x in range(str_size))


            chars = string.ascii_letters + string.ascii_uppercase + string.digits
            chars1 = string.digits
            chars2 = string.ascii_letters

            size1 = 6
            size2 = 6

            size3 = 6

            random1 = (random_string_generator(size1, chars1)).lower()
            randomChar = (random_string_generator(size2, chars2)).lower()
            onlineusers = (random_string_generator(size2, chars1)).lower()
            mega = (random_string_generator(size3, chars)).lower()
            vers = round(random.uniform(1, 5), 3)

            MAINTITLE = ("<h1>["+randomChar+"](" + (klist + "){" + klist1 + "}") + "</h1>").upper()
            DES = (klist+ "|" + klist1 +"("+randomChar+")").upper()

            # MAINTITLE = ("<h1>(" + (klist + "){" + klist1 + "}") + "[" + randomChar + "]</h1>").upper()
            # DES = ("(" + (klist + "){" + klist1 + "}[" + randomChar + "]")).upper()

            DATETIME = "<h3>" + ("Updated: " + d3 + " ( onlineusers:" + onlineusers + ") ") + "=> [VERSION :" + (
                str(vers)) + "]</h3>"
            # LINKD = "https://kenhacks.com/" + file
            LINKD = "https://gamecode.site/" + file

            with open(b + "\\" + niche, encoding='utf-8') as f:

                soup = BeautifulSoup(f, 'html.parser')

                f = (soup.prettify())
                # MYDOMAINLINK = "<h2><a href=" + '"' + LINKD + '"'">" + "CLICK HERE TO USE THIS HACK" + "</a></h2>"
                MYDOMAINLINK = "<center><a href=" + '"' + LINKD + '"'">" + "<img src='https://lh3.googleusercontent.com/-Ow6nYoqryvE/YdAc4UzqfpI/AAAAAAAABM0/nlDTCmGn7TA1IT0YjRQpSuDZHLyBpF0owCNcBGAsYHQ/h78/buttom.jpg'>" + "</a></center>"
                MAINTITLE = MAINTITLE + DATETIME + MYDOMAINLINK

                # f = f.replace('MAINTITLE', MAINTITLE.upper())
                # f = f.replace('DATETIME', DATETIME.upper())
                #
                # f = f.replace('MYDOMAINLINK', MYDOMAINLINK)
                f = f.replace("\n", "")
                f = f.replace("'", "")

            f = MAINTITLE + f


            print(b + "\\" + niche)
            print(klist)

            klist = klist.replace(' ', '-')

            klist1 = klist1.replace(' ', '-')

            # filename="E:\\connect\\\pdf-files\\"+randomChar+".pdf"
            if choice == "1":
                filename = path + klist1 + "-" + randomChar + ".pdf"
            elif choice == "2":
                filename = path + klist + "-" + klist1 + "-" + randomChar + ".pdf"
            else:
                filename = path + randomChar + ".pdf"
            # background: rgba(0, 128, 0, 0.3)

            print(filename)
            coders = """<style>
            body{
              background-color: #ccffe6;

            }

                img{
                # width:50%;
                #  padding-top: 10px;
                #   padding-right: 60px;
                #   padding-bottom: 10px;
                #   padding-left: 200px;}            
                h1 {
                  font-size: 36px;
                   font-family:Georgia, serif;


                }

                h2 {
                  font-size: 30px;
                }
                h3{
                  # font: normal normal normal 20px/1 Helvetica, arial, sans-serif;
                  # border-bottom: 2px solid #000;
                  # background:red;
                  # color:#fff;
                  # 
                  # display:inline-block;
                  # padding:7px 15px;
                  # margin-left:10px;
                }



                p {
                 font-family: Georgia, serif;



                  font-size: 18px;
                   line-height: 38px;   /* within paragraph */
                  margin-bottom: 30px; /* between paragraphs */
                }
                a {
                    line-height: 1em;
                    display: inline-block;
                    text-decoration: none;
                    padding: 10;
                    margin: 5x;
            }

                </style>
                """
            klist = klist.replace('-', ' ')
            klist1 = klist1.replace('-', ' ')
            random.shuffle(lines)
            print(lines)


            lines = ('| '.join(lines))
            print(lines)


            # title=klist.upper() + " | " + klist1.upper() + " " + randomChar
            # title = "{ " + randomChar + " } " + lines.upper()

            metacode = '<meta name="pdfkit-title" content="' + (str(lines)) + '"/>'
            # lines = (str(lines)).replace('\n', '')

            # print(*lines, sep=", ")

            # lines = [w.replace('\n', '') for w in lines]

            keysearched = "<p><strong>" + (str(lines)) + "</strong></p>"
            print(lines)

            f = coders + metacode + f + keysearched
            # f = coders + metacode + keysearched + f


            pdfkit.from_string(f, filename.lower(), configuration=config)

            print("Done=" + (str(i)))
            print(topic[x])




