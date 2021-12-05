import math
import ctypes


def get_char(charget, strget):
    try:
        strget = str(strget)
    except ValueError:
        return ','
    cache1 = ''
    listcache1 = []
    listcache2 = []
    for i in strget:
        if not i == ' ':
            cache1 = f'{cache1}{i}'
        else:
            listcache2.append(cache1)
            cache1 = ''
        listcache1.append(i)
    if charget in strget:
        print(
            f'{charget} in strget == True, frequency == {strget.count(charget)}, charcache1 == {listcache1}, charcache2 == {listcache2}.')
        return f'{charget} in strget == True, frequency == {strget.count(charget)}, charcache1 == {listcache1}, charcache2 == {listcache2}.'
    else:
        print(
            f'{charget} in strget == False, charcache1 == {listcache1}, charcache2 == {listcache2}.')
        return f'{charget} in strget == False, charcache1 == {listcache1}, charcache2 == {listcache2}.'


def rational_round(to_round, round_to):
    try:
        to_round = float(to_round)
        round_to = float(round_to)
    except ValueError:
        return ','
    return round(to_round / round_to) * round_to


def perf_sqrt(number):
    try:
        number = float(number)
    except ValueError:
        return f','
    if math.sqrt(number) == round(math.sqrt(number)):
        return [True, math.sqrt(number)]
    else:
        return [False, math.sqrt(number)]


def str_to_list(Str):
    try:
        Str = str(Str)
    except ValueError:
        return ','
    listcache3 = []
    for i in Str:
        listcache3.append(i)
    return listcache3


def list_to_str(List):
    return ''.join(List)


def str_calc(to_calc):
    # Creates sets to check if looped values are in the sets, and other data types for later use.
    numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}
    operations = {'+', '*', '/', '^', '-'}
    local_numbers = []
    local_operations = []
    cache = ''
    test = []
    i_cache = ''
    is_negative = False
    # Take each character from the string and append it into the char_lookup list.
    char_lookup = []
    for i in str(to_calc):
        i_cache = i
        try:
            i = float(i)
            char_lookup.append(i_cache)
        except ValueError:
            char_lookup.append(i_cache)
    # Filter indexes from char_lookup, if they are operations they go in local_operations, if numbers then they go in
    # local_numbers.
    for index, value in enumerate(char_lookup):
        if value in numbers:
            test.append(value)
        elif value in operations:
            #  lots of elif statements to determine which scenario the '-' operator is being used in.
            if value == '-' and char_lookup[index - 1] == '-':
                local_operations.append('+')
                test = []
            elif value == '-' and not char_lookup[index - 1] == '-' and char_lookup[index - 1] in operations:
                is_negative = True
            elif value == '-' and not char_lookup[index + 1] == '-' and char_lookup[index + 1] in operations:
                return ','
            elif is_negative:
                local_numbers.append(0 - float(list_to_str(test)))
                local_operations.append(value)
                test = []
                is_negative = False
            elif not list_to_str(test) == '' and not is_negative:
                local_numbers.append(float(list_to_str(test)))
                local_operations.append(value)
                test = []
            else:
                return ','
        else:
            return','
    # Switches '-' for '+' in local_operations list and makes
    if is_negative:
        local_numbers.append(0 - float(list_to_str(test)))
    elif not is_negative:
        local_numbers.append(float(list_to_str(test)))
    test = []
    is_negative = False
    # Run defensive tests.
    if len(local_numbers) != len(local_operations) + 1:
        return ','
    else:
        print()
        # Defensive test passed.
    # Calculate operator positions and calculate expression
    for i in (len(local_operations) + 1) * 'i':
        if '^' in local_operations:
            for index, value in enumerate(local_operations):
                if value == '^':
                    try:
                        local_numbers[index] ** local_numbers[index + 1]
                    except OverflowError:
                        return ','
                    string_cache = local_numbers[index] ** local_numbers[index + 1]
                    local_numbers.pop(index + 1)
                    local_numbers[index] = string_cache
                    local_operations.pop(index)
    for i in (len(local_operations) + 1) * 'i':
        if '*' in local_operations or '/' in local_operations:
            for index, value in enumerate(local_operations):
                if value == '*':
                    try:
                        local_numbers[index] * local_numbers[index + 1]
                    except OverflowError:
                        return ','
                    string_cache = local_numbers[index] * local_numbers[index + 1]
                    local_numbers.pop(index + 1)
                    local_numbers[index] = string_cache
                    local_operations.pop(index)
                elif value == '/':
                    try:
                        local_numbers[index] / local_numbers[index + 1]
                    except OverflowError:
                        return ','
                    string_cache = local_numbers[index] / local_numbers[index + 1]
                    local_numbers.pop(index + 1)
                    local_numbers[index] = string_cache
                    local_operations.pop(index)
    for i in (len(local_operations) + 1) * 'i':
        if '+' in local_operations or '-' in local_operations:
            for index, value in enumerate(local_operations):
                if value == '+':
                    try:
                        local_numbers[index] + local_numbers[index + 1]
                    except OverflowError:
                        return ','
                    string_cache = local_numbers[index] + local_numbers[index + 1]
                    local_numbers.pop(index + 1)
                    local_numbers[index] = string_cache
                    local_operations.pop(index)
                elif value == '-':
                    try:
                        local_numbers[index] - local_numbers[index + 1]
                    except OverflowError:
                        return ','
                    string_cache = local_numbers[index] - local_numbers[index + 1]
                    local_numbers.pop(index + 1)
                    local_numbers[index] = string_cache
                    local_operations.pop(index)
    # returns debug values as the code is still in development.
    return local_numbers


def firstEven(mIndex):
    # Accepts tuples and lists as a parameter.
    try:
        list(mIndex)
    except ValueError:
        try:
            tuple(mIndex)
        except ValueError:
            return ','
    for index, value in enumerate(mIndex):
        try:
            float(value)
        except ValueError:
            continue
        if value / 2 == round(value / 2):
            return index, value,
    return 'None'


def spliceOutWords(string):
    try:
        str(string)
    except ValueError:
        return ','
    cache = ''
    cacheList = []
    for index, value in enumerate(string):
        if value == ' ':
            cacheList.append(cache)
            cache = ''
        else:
            cache = f'{cache}{value}'
    cacheList.append(cache)
    return cacheList


def check_auth(tup):
    auth_score = 0
    instances = [0, 0, 0]
    for i in tup:
        if i in open('dtbase1.txt', 'r').read():
            auth_score = auth_score + -1
            instances[0] = instances[0] + 1
        elif i in open('dtbase0.txt', 'r').read():

            auth_score = auth_score + 1
            instances[1] = instances[1] + 1
        else:
            instances[2] = instances[2] + 1
            auth_score = auth_score + .1
    return (auth_score, (instances[0] + instances[1] + instances[2] / 3), auth_score + (instances[0] + instances[1] + instances[2] / 3) / 2)


def get_memory(memory):
    ctypes.cast(memory, ctypes.py_object).value