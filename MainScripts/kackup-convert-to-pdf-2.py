import os
import random
import string
# from datetime import date
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from conData import topics
import pdfkit
from conData import topics


topics.manintopics()
topic=topics.topic

# options_new = webdriver.ChromeOptions()
# options_new.add_argument("--window-size=20X20")
# options_new.add_argument("--headless")
# options_new.add_argument("--width=100")
# options_new.add_argument("--height=100")
# options_new.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# driver1 = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options_new)


# options_new = webdriver.ChromeOptions()
# options_new.add_argument("user-data-dir=C:\\Users\\Asif\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# driver1 = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options_new)
#
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
# driver = webdriver.Chrome(options=options, executable_path=r'C:\\chromedriver.exe')
typepost = "html"

machine = "dhgh"
choice = "1"
# # topic = ("cash","#")
#
# topic = ("cod","robux","fb","insta","cash", "among","pokemon", "tiktok", "onlyfans", "brawl", "coin", "igfollowers","fskins","vbucks")
# # topic = ("fskins", "robux","vbucks","garena","fb","igfollowers","onlyfans")
# # topic = ("onlyfans", "coin","brawl")

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

for z in range(0, 1):
    for x in range(len(topic)):

        file = topic[x]
        if topic[x] == "robux" or topic[x] == "vbucks" or topic[x] == "fskins" or topic[x] == "garena" or topic[x] == "cash":
            numrep = 5
        else:
            numrep = 3

        if machine == "vm":
            dir = 'z:\\MYNEW\\a\\'
            a = "z:\\MYNEW\\a\\files\\"
        else:
            dir = 'E:\\connect\\MYNEW\\a\\'
            a = "E:\\connect\\MYNEW\\a\\files\\"

        full_path = os.path.join(dir, file)

        presentday = datetime.now()
        nextday = presentday + timedelta(1)
        d2 = presentday.strftime('%d-%m-%Y')
        d3 = nextday.strftime('%d-%m-%Y')

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

            def random_string_generator(str_size, allowed_chars):
                return ''.join(random.choice(allowed_chars) for x in range(str_size))


            chars = string.ascii_letters + string.ascii_uppercase + string.digits
            chars1 = string.digits
            chars2 = string.ascii_letters

            size1 = 4
            size2 = 4

            size3 = 6

            random1 = (random_string_generator(size1, chars1)).lower()
            randomChar = (random_string_generator(size2, chars2)).lower()
            onlineusers = (random_string_generator(size2, chars1)).lower()
            mega = (random_string_generator(size3, chars)).lower()

            MAINTITLE = ("<h1>" + (klist + " - " + klist1 + "{"+"KOOL"+"}") + "</h1>").upper()
            # DATETIME = "<h3>" + ("Updated: " + d3 + " ( onlineusers:" + onlineusers + ") ") + "</h3>"
            DATETIME = "<h3>" +"DATETIME"+ "</h3>"


            LINKD = "https://kenhacks.com/" + file
            # LINKD = "https://gamecode.site/" + file

            with open(b + "\\" + niche, encoding='utf-8') as f:

                soup = BeautifulSoup(f, 'html.parser')

                f = (soup.prettify())
                # MYDOMAINLINK = "<h2><a href=" + '"' + LINKD + '"'">" + "CLICK HERE TO USE THIS HACK" + "</a></h2>"
                MYDOMAINLINK = "<h2><a href=" + '"' + LINKD + '"'">" + "<img src='https://i.imgur.com/0cnfd07.png'>" + "</a></h2>"
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
                filename = "C:\\Users\\Administrator\\Desktop\\1\\" + klist1 + "-" + randomChar + ".pdf"
            elif choice == "2":
                filename = "E:\\1\\" + klist + "-" + klist1 + "-" + randomChar + ".pdf"
            else:
                filename = "E:\\1\\" + randomChar + ".pdf"
            # background: rgba(0, 128, 0, 0.3)

            print(filename)
            coders = """<style>
                            body{
                            background-color:#abdbe3;

                            }
                img{
                width:50%;
                 padding-top: 10px;
                  padding-right: 60px;
                  padding-bottom: 10px;
                  padding-left: 200px;}            
                h1 {
                  font-size: 36px;
                   font-family: 'Times New Roman', serif;


                }

                h2 {
                  font-size: 30px;
                }
                h3{
                  width:300px;
                  font: normal normal normal 20px/1 Helvetica, arial, sans-serif;
                  border-bottom: 2px solid #000;
                  background:red;
                  color:#fff;

                  display:inline-block;
                  padding:7px 15px;
                  margin-left:10px;
                }



                p {
                   	font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;



                  font-size: 16px;
                   line-height: 32px;   /* within paragraph */
                  margin-bottom: 30px; /* between paragraphs */
                }
                a {
                    line-height: 1em;
                    display: inline-block;
                    text-decoration: none;
                    padding: 10;
                    margin: 10px;
                    font-size: 24px;
                }

                </style>
                """
            klist = klist.replace('-', ' ')
            klist1 = klist1.replace('-', ' ')
            lines = ('| '.join(lines))

            # title=klist.upper() + " | " + klist1.upper() + " " + randomChar
            title = lines.upper()

            metacode = '<meta name="pdfkit-title" content="' + title + '"/>'
            # lines = (str(lines)).replace('\n', '')

            # print(*lines, sep=", ")

            # lines = [w.replace('\n', '') for w in lines]

            keysearched = "<p><strong>" + (str(lines)) + "</strong></p>"
            print(lines)

            f = coders + metacode + f + keysearched

            pdfkit.from_string(f, filename.upper(), configuration=config)

            print("Done=" + (str(i)))
            print(topic[x])




