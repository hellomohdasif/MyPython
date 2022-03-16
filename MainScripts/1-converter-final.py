from docx import Document
import os
import random
import string
# # from datetime import date
# from datetime import datetime, timedelta
# from bs4 import BeautifulSoup
# from conData import topics
# import pdfkit
# from conData import topics
from docx2pdf import convert
from datetime import datetime, timedelta

presentday = datetime.now()
nextday = presentday + timedelta(1)
d2 = presentday.strftime('%d-%m-%Y')
d3 = nextday.strftime("%B %d, %Y")

setloca="C:\\Users\\Asif\\Desktop\\2\\"


path = "C:\\Users\\Asif\\Desktop\\files\\"
a = os.listdir(path)

k=0
for k in range(0,100):
    j = 0

    while (j < len(a)):

        def random_string_generator(str_size, allowed_chars):
            return ''.join(random.choice(allowed_chars) for x in range(str_size))


        chars = string.ascii_letters + string.ascii_uppercase + string.digits
        chars1 = string.digits
        chars2 = string.ascii_letters

        size1 = 4
        size2 = 3
        size3 = 8

        randomNum = (random_string_generator(size1, chars1))
        randomChar = (random_string_generator(size2, chars2))
        randomChar1 = (random_string_generator(size1, chars2))
        randomname = (random_string_generator(size3, chars2))

        onlineusers = (random_string_generator(size2, chars1))
        mega = (random_string_generator(size3, chars))

        # open the document
        doc = Document(path + a[j])
        Dictionary = {"KOOL": randomname.upper(), "DATETIME": d3.upper()}
        for i in Dictionary:
            for p in doc.paragraphs:
                if p.text.find(i) >= 0:
                    p.text = p.text.replace(i, Dictionary[i])
        # save changed document
        doc.save(setloca + randomChar + '.docx')
        docx_file = setloca + randomChar + ".docx"

        pdf_file = setloca + randomChar + ".pdf"
        convert(docx_file, pdf_file)
        os.remove(setloca + randomChar + '.docx')
        j = j + 1
        k=k+1

        print(k)



