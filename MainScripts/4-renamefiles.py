import os
import random
import string

# os.chdir('C:\\Users\\Administrator\\Desktop\\2\\')

# os.chdir('C:\\Users\\Administrator\\Desktop\\2\\')
os.chdir(r'C:\Users\Asif\Desktop\1')

vari=""
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))


    chars = string.ascii_letters + string.ascii_uppercase + string.digits
    chars1 = string.digits
    chars2 = string.ascii_lowercase

    size1 = 7
    size2 = 7
    size3 = 7

    randomNum = (random_string_generator(size1, chars1))
    randomChar = (random_string_generator(size2, chars))
    randomChar1 = (random_string_generator(size3, chars2))
    onlineusers = (random_string_generator(size2, chars1))

    f_name, f_ext = os.path.splitext(f)
    # f_name = randomChar1+ str(count)(count)

    f_name = vari+randomChar1

    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
