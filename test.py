import Functions

list = []
set = {'List of swear words go hear'}
for i in set:
    for index, value in enumerate(str(i).replace(' ', '')):
        if ' ' in i:
            dat = Functions.str_to_list(Functions.list_to_str(Functions.spliceOutWords(str(i))))
            dat[index] = '*'
            list.insert(0, Functions.list_to_str(dat))
            list.insert(0, i)
        else:
            dat = Functions.str_to_list(str(i))
            dat[index] = '*'
            list.insert(0, Functions.list_to_str(dat))
            list.insert(0, i)
print(list)
