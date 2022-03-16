import random
import string
import pyperclip
import pandas

outttt = []

for i in range(0,400):


    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    size1 = 3
    size2 = 2
    random1 = (random_string_generator(size1, chars))
    random2 = (random_string_generator(size2, chars))
    maino=(random1.upper() + "-" + random2.upper())

    outttt.append(maino)

res = '\n'.join([str(item) for item in outttt])
pyperclip.copy(res)

print(res)



