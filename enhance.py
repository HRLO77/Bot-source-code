import Functions
import random


def check(cache):
    length = 0
    for index, value in enumerate(cache):
        if value == '*':
            length += 1
    if length > len(cache) / 3 + 1:
        return False
    return True

cache = []
list = []
set = {'swear words go here'}
for i in set:
    for index, value in enumerate(str(i).replace(' ', '')):
        if ' ' in i:
            dat = Functions.str_to_list(Functions.list_to_str(Functions.spliceOutWords(str(i))))
            dat[index] = '*'
            list.append(Functions.list_to_str(dat))
            list.append(i)
        else:
            dat = Functions.str_to_list(str(i))
            dat[index] = '*'
            list.append(Functions.list_to_str(dat))
            list.append(i)
        cache = Functions.list_to_str(dat)
        moveable_cache = Functions.str_to_list(cache)
        for char in (len(i) ** 2) * 'r':
            moveable_cache[random.randrange(0, len(moveable_cache) - 1)] = '*'
            if check(moveable_cache):
                list.append(Functions.list_to_str(moveable_cache))


print(list)
