import random
import string

with open("C:\\Users\\Administrator\\Desktop\\1.txt", 'r') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    lines = [line.replace('  ', '') for line in lines]
    lines = [line.replace('  ', '') for line in lines]

    lines = [line.replace('https://mediastudies.as.virginia.edu/', 'https://cdn.ymaws.com/') for line in lines]


    for i in range(0, len(lines)):
        def random_string_generator(str_size, allowed_chars):
            return ''.join(random.choice(allowed_chars) for x in range(str_size))


        chars = string.ascii_letters + string.ascii_uppercase
        size = 8
        rannum = (random_string_generator(size, chars))



        with open('E:\\connect\\\html.txt', "a") as myfile:
            myfile.write('<a href="'+lines[i]+'">'+rannum+'</a>''\n')


