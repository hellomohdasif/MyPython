import random
import string
import pyperclip
import csv
import pandas as pd
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy

my_list = []
i=2
for i in range(i,102):


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    size1 = 3
    size2 = 2
    random1 = (random_string_generator(size1, chars))
    random2 = (random_string_generator(size2, chars))
    maino=(random1.upper() + "-" + random2.upper())
    my_list.append('geeks')

    rb = open_workbook("C:\\Users\\Asif\\Desktop\\Main\\NEW START\\100\\CASH100.xls")
    wb = copy(rb)

    s = wb.get_sheet(0)
    s.write(i, 1, maino)

    wb.save('C:\\Users\\Asif\\Desktop\\Main\\NEW START\\100\\CASH100.xls')




