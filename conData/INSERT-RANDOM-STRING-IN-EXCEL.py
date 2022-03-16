import random
import string
import csv
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy

my_list = []
i=2
for i in range(i,106):


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    size1 = 3
    size2 = 2
    random1 = (random_string_generator(size1, chars))
    random2 = (random_string_generator(size2, chars))
    maino=(random1.upper() + "-" + random2.upper())
    my_list.append(maino)

    rb = open_workbook(r"E:\main\all.xls")
    wb = copy(rb)

    s = wb.get_sheet(0)
    s.write(i, 1, maino)

    wb.save(r'E:\main\all.xls')

print("Done-"+my_list[0])





