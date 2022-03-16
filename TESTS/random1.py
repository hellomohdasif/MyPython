import getpass
import os
import random
import string
import time as Thread
from xlwt import Workbook
i = 3

while (i < 100):

    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    chars1 = string.digits
    chars2 = string.ascii_letters

    size1 = 3
    size2 = 4
    size3 = 5

    randomNum = (random_string_generator(size1, chars1))
    randomChar = (random_string_generator(size2, chars))
    randomChar = (random_string_generator(size2, chars2))
    onlineusers = (random_string_generator(size2, chars1))
    mega = (random_string_generator(size3, chars))


    wb = Workbook()


    sheet1 = wb.add_sheet('Sheet 1')

    sheet1.write(i, 1,randomNum)


    wb.save('xlwt example.xls')




    i = i + i


