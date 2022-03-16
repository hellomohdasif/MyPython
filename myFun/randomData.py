import random
import string
global random1
global onlineusers
global randomChar
global random3
global mega


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

chars = string.ascii_letters + string.ascii_uppercase + string.digits
chars1 = string.digits+string.ascii_letters
chars2 = string.ascii_letters
chars3 = string.digits


size1 = 6
size2 = 4
size3 = 8

random1 = (random_string_generator(size1, chars1))
randomChar = (random_string_generator(size2, chars))
random3 = (random_string_generator(size2, chars2))
onlineusers = (random_string_generator(size2, chars3))
mega = (random_string_generator(size3, chars))
