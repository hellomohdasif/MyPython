import random
import string


with open("C:\\Users\\Administrator\\Desktop\\sites.txt", 'r') as check:
    check = check.readlines()

with open("C:\\Users\\Administrator\\Desktop\\1.txt", 'r') as f:
    lines = f.readlines()

for i in range(0, len(check)):
    for j in range(0, len(lines)):

        # lines = [line.replace('\n', '') for line in lines]
        # lines = [line.replace('  ', '') for line in lines]
        # lines = [line.replace('  ', '') for line in lines]
        jx = lines[j].replace('https://naucenter.as.virginia.edu/', check[i])
        jx=jx.replace('\n','')

        print(jx)

        # lines = [line.replace('https://mediastudies.as.virginia.edu/',check[i]) for line in lines]


        def random_string_generator(str_size, allowed_chars):
            return ''.join(random.choice(allowed_chars) for x in range(str_size))


        chars = string.ascii_letters + string.ascii_uppercase
        size = 8
        rannum = (random_string_generator(size, chars))

        with open('C:\\Users\\Administrator\\Desktop\\html.txt', "a") as myfile:
            myfile.write(jx+'\n')








