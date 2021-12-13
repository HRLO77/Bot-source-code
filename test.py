import Functions

list = []
set = {'cunt', 'mur', 'pussy', 'sex', 'pis', 'frick', 'nigga', 'nazi', 'sht', 'sh*t', 'rape', 'crap',
                  'n*gger', 'xxx', 'neo', 'rupe', 'naz*', 'dam', 'asre', 'dummy', 'th*t', 'fort', 'thot', 'fk', 'prod',
                  'v*gina', 'pok', 'gay', 'lmb', 'peg', 'hac', 'geno', 'dayum', 'hit', 'job', 'n!gger', 'p*rn', 'flip',
                  'p*ss', 'idoit', 'damn', 'p*ssy', 'dump', 'nigger', 'p!s', 'fck', 'sta', 'crud', 'segs', 'shit',
                  'c!ck', 's*ck', 'bastard', 'kil', 'fuc', 'porn', 'cu', 't!t',
                  'tit', 'fack', 'sh!t', 'butt', 'danm', 'dip', 's*x', 'd!ck', 'gai', 'idit', 'cock', 'fuke', 'puss',
                  'trash', 'slap', 'seggs', 'anal', 'sx', 'fac', 'idiot', 'c*nt', 'stup', 'fr*ck', 'n!gga', 'rob',
                  'mutil', 'dumb', 't*t', 'stfu', 'clusterfuc', 'blo', 'hitler', 'lana', 'rod', 'fuk', 'nite', 'suck',
                  'fuck', 'btch', 'lma', 'pus', 'p!ss', 'idg', 'cr*p', 'n*zi', 'robl', 'piss', 'shut', 'ass', 'bitch',
                  'fu', 'prn', 'arse', 'stick', 'fruck', 'suc', 'bang', 'dum', 'vagina', 'come', 'dick'}
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
