import ensurepip

ensurepip.bootstrap()
import os

os.system('py -m pip install discord')
os.system('py -m pip install py-cord')
os.system('py -m pip install disnake')
os.system('py -m pip install profanity')
os.system('py -m pip install ast')
os.system('py -m pip install discord --upgrade')
os.system('py -m pip install py-cord --upgrade')
os.system('py -m pip install disnake --upgrade')
os.system('py -m pip install profanity --upgrade')
os.system('py -m pip install ast --upgrade')
import ast

import Functions
import random
import disnake as discord
from disnake.ext import commands
import datetime
import subprocess
import sys
import profanity
from profanity import profanity
import tracemalloc
import ctypes
from datetime import datetime
import secrets
from discord.utils import get


def check_user_is_admin(user):
    admin_data = {'HRLO77', 'Sniperfirst21', 'Nvm!', 'bruisedbeans',
                  'Trismo', 'GlitchBotGaming', 'Zain.W', 'Jiyaa', 'E-BAG', 'Jilal'}
    if any(i in user for i in admin_data):
        return True
    else:
        return False


def get_memory(memory):
    return ctypes.cast(memory, ctypes.py_object).value


def convert_to_memory(value):
    return id(value)


def convert_to_list(string):
    cache = ''
    data = []
    for i in string.replace(' ', ''):
        if i == ',':
            data.append(cache)
            cache = ''
        else:
            cache = f'{cache}{i}'
    data.append(cache)
    return data


# json_data = json.load((open("reacting_data.json", 'r')))
# for i in convert_to_list(list(json_data.keys())):
#     for val in i:


# If you want to create a system to provides a default role when a member reacts, follow the dict syntax below.
# Remember to enter integers for all of the ID's, and a string for the emoji! You can create multiple default roles for different messages in your channel using this dictionary syntax!
reacting = {('guild_id', 'message_id_to_react'): ('default_role_id_to_add', 'emoji_to_react')}

# Test the secrets module
a = [secrets.token_bytes(), secrets.token_hex(), secrets.token_urlsafe()]
print(a)

muted_channel = False
tracemalloc.start()
spam = 2
content = 2

explicit_data5 = {'s x', 's*', 's x', '*x', 'd!ck', 'd!c*', 'd!ck', 'd!*k', 'd!ck', 'd*ck', 'd!ck', '*!ck', 'n * g g a',
                  'n*gg*', 'n * g g a', 'n*g*a', 'n * g g a', 'n**ga', 'n * g g a', 'n*gga', 'n * g g a', '**gga',
                  'fac', 'fa*', 'fac', 'f*c', 'fac', '*ac', 'p*ssy', 'p*ss*', 'p*ssy', 'p*s*y', 'p*ssy', 'p**sy',
                  'p*ssy', 'p*ssy', 'p*ssy', '**ssy', 'puss', 'pus*', 'puss', 'pu*s', 'puss', 'p*ss', 'puss', '*uss',
                  'hitler', 'hitle*', 'hitler', 'hitl*r', 'hitler', 'hit*er', 'hitler', 'hi*ler', 'hitler', 'h*tler',
                  'hitler', '*itler', 'damn', 'dam*', 'damn', 'da*n', 'damn', 'd*mn', 'damn', '*amn', 'p!ss', 'p!s*',
                  'p!ss', 'p!*s', 'p!ss', 'p*ss', 'p!ss', '*!ss', 'lana', 'lan*', 'lana', 'la*a', 'lana', 'l*na',
                  'lana', '*ana', 'th*t', 'th**', 'th*t', 'th*t', 'th*t', 't**t', 'th*t', '*h*t', 'rupe', 'rup*',
                  'rupe', 'ru*e', 'rupe', 'r*pe', 'rupe', '*upe', 'c ! c k', 'c!c*', 'c ! c k', 'c!*k', 'c ! c k',
                  'c*ck', 'c ! c k', '*!ck', 'cock', 'coc*', 'cock', 'co*k', 'cock', 'c*ck', 'cock', '*ock', 'prod',
                  'pro*', 'prod', 'pr*d', 'prod', 'p*od', 'prod', '*rod', 'seggs', 'segg*', 'seggs', 'seg*s', 'seggs',
                  'se*gs', 'seggs', 's*ggs', 'seggs', '*eggs', 'arse', 'ars*', 'arse', 'ar*e', 'arse', 'a*se', 'arse',
                  '*rse', 'p * s', 'p**', 'p * s', 'p*s', 'p * s', '**s', 'r a p e', 'rap*', 'r a p e', 'ra*e',
                  'r a p e', 'r*pe', 'r a p e', '*ape', 'p i s', 'pi*', 'p i s', 'p*s', 'p i s', '*is', 'p u s', 'pu*',
                  'p u s', 'p*s', 'p u s', '*us', 'c r * p', 'cr**', 'c r * p', 'cr*p', 'c r * p', 'c**p', 'c r * p',
                  '*r*p', 'p * r n', 'p*r*', 'p * r n', 'p**n', 'p * r n', 'p*rn', 'p * r n', '**rn', 'frick', 'fric*',
                  'frick', 'fri*k', 'frick', 'fr*ck', 'frick', 'f*ick', 'frick', '*rick', 'shut', 'shu*', 'shut',
                  'sh*t', 'shut', 's*ut', 'shut', '*hut', 'f r i c k', 'fric*', 'f r i c k', 'fri*k', 'f r i c k',
                  'fr*ck', 'f r i c k', 'f*ick', 'f r i c k', '*rick', 'c*nt', 'c*n*', 'c*nt', 'c**t', 'c*nt', 'c*nt',
                  'c*nt', '**nt', 'dip', 'di*', 'dip', 'd*p', 'dip', '*ip', 'rob', 'ro*', 'rob', 'r*b', 'rob', '*ob',
                  's*ck', 's*c*', 's*ck', 's**k', 's*ck', 's*ck', 's*ck', '**ck', 'p*ss', 'p*s*', 'p*ss', 'p**s',
                  'p*ss', 'p*ss', 'p*ss', '**ss', 't i t', 'ti*', 't i t', 't*t', 't i t', '*it', 't h o t', 'tho*',
                  't h o t', 'th*t', 't h o t', 't*ot', 't h o t', '*hot', 'piss', 'pis*', 'piss', 'pi*s', 'piss',
                  'p*ss', 'piss', '*iss', 'tit', 'ti*', 'tit', 't*t', 'tit', '*it', 'b i t c h', 'bitc*', 'b i t c h',
                  'bit*h', 'b i t c h', 'bi*ch', 'b i t c h', 'b*tch', 'b i t c h', '*itch', 'p*rn', 'p*r*', 'p*rn',
                  'p**n', 'p*rn', 'p*rn', 'p*rn', '**rn', 'cr*p', 'cr**', 'cr*p', 'cr*p', 'cr*p', 'c**p', 'cr*p',
                  '*r*p', 'rape', 'rap*', 'rape', 'ra*e', 'rape', 'r*pe', 'rape', '*ape', 'btch', 'btc*', 'btch',
                  'bt*h', 'btch', 'b*ch', 'btch', '*tch', 't h * t', 'th**', 't h * t', 'th*t', 't h * t', 't**t',
                  't h * t', '*h*t', 'hit', 'hi*', 'hit', 'h*t', 'hit', '*it', 'a r s e', 'ars*', 'a r s e', 'ar*e',
                  'a r s e', 'a*se', 'a r s e', '*rse', 'dick', 'dic*', 'dick', 'di*k', 'dick', 'd*ck', 'dick', '*ick',
                  'dayum', 'dayu*', 'dayum', 'day*m', 'dayum', 'da*um', 'dayum', 'd*yum', 'dayum', '*ayum', 'bang',
                  'ban*', 'bang', 'ba*g', 'bang', 'b*ng', 'bang', '*ang', 'd * c k', 'd*c*', 'd * c k', 'd**k',
                  'd * c k', 'd*ck', 'd * c k', '**ck', 'cunt', 'cun*', 'cunt', 'cu*t', 'cunt', 'c*nt', 'cunt', '*unt',
                  'b t c h', 'btc*', 'b t c h', 'bt*h', 'b t c h', 'b*ch', 'b t c h', '*tch', 'c!ck', 'c!c*', 'c!ck',
                  'c!*k', 'c!ck', 'c*ck', 'c!ck', '*!ck', 'fruck', 'fruc*', 'fruck', 'fru*k', 'fruck', 'fr*ck', 'fruck',
                  'f*uck', 'fruck', '*ruck', 'c r u d', 'cru*', 'c r u d', 'cr*d', 'c r u d', 'c*ud', 'c r u d', '*rud',
                  'p o r n', 'por*', 'p o r n', 'po*n', 'p o r n', 'p*rn', 'p o r n', '*orn', 'fort', 'for*', 'fort',
                  'fo*t', 'fort', 'f*rt', 'fort', '*ort', 'porn', 'por*', 'porn', 'po*n', 'porn', 'p*rn', 'porn',
                  '*orn', 'mur', 'mu*', 'mur', 'm*r', 'mur', '*ur', 'p * s s', 'p*s*', 'p * s s', 'p**s', 'p * s s',
                  'p*ss', 'p * s s', '**ss', 'xxx', 'xx*', 'xxx', 'x*x', 'xxx', '*xx', 'n!gga', 'n!gg*', 'n!gga',
                  'n!g*a', 'n!gga', 'n!*ga', 'n!gga', 'n*gga', 'n!gga', '*!gga', 'r * p e', 'r*p*', 'r * p e', 'r**e',
                  'r * p e', 'r*pe', 'r * p e', '**pe', 'f l i p', 'fli*', 'f l i p', 'fl*p', 'f l i p', 'f*ip',
                  'f l i p', '*lip', 'p i s s', 'pis*', 'p i s s', 'pi*s', 'p i s s', 'p*ss', 'p i s s', '*iss', 'rod',
                  'ro*', 'rod', 'r*d', 'rod', '*od', 'n*zi', 'n*z*', 'n*zi', 'n**i', 'n*zi', 'n*zi', 'n*zi', '**zi',
                  'robl', 'rob*', 'robl', 'ro*l', 'robl', 'r*bl', 'robl', '*obl', 'peg', 'pe*', 'peg', 'p*g', 'peg',
                  '*eg', 'nigga', 'nigg*', 'nigga', 'nig*a', 'nigga', 'ni*ga', 'nigga', 'n*gga', 'nigga', '*igga',
                  'b * s t * r d', 'b*st*r*', 'b * s t * r d', 'b*st**d', 'b * s t * r d', 'b*st*rd', 'b * s t * r d',
                  'b*s**rd', 'b * s t * r d', 'b**t*rd', 'b * s t * r d', 'b*st*rd', 'b * s t * r d', '**st*rd', 'fuck',
                  'fuc*', 'fuck', 'fu*k', 'fuck', 'f*ck', 'fuck', '*uck', 'c o c k', 'coc*', 'c o c k', 'co*k',
                  'c o c k', 'c*ck', 'c o c k', '*ock', 'stfu', 'stf*', 'stfu', 'st*u', 'stfu', 's*fu', 'stfu', '*tfu',
                  'idg', 'id*', 'idg', 'i*g', 'idg', '*dg', 'dum', 'du*', 'dum', 'd*m', 'dum', '*um', 'c r a p', 'cra*',
                  'c r a p', 'cr*p', 'c r a p', 'c*ap', 'c r a p', '*rap', 'i d i o t', 'idio*', 'i d i o t', 'idi*t',
                  'i d i o t', 'id*ot', 'i d i o t', 'i*iot', 'i d i o t', '*diot', 'd ! c k', 'd!c*', 'd ! c k',
                  'd!*k', 'd ! c k', 'd*ck', 'd ! c k', '*!ck', 'lmb', 'lm*', 'lmb', 'l*b', 'lmb', '*mb', 'i d o i t',
                  'idoi*', 'i d o i t', 'ido*t', 'i d o i t', 'id*it', 'i d o i t', 'i*oit', 'i d o i t', '*doit',
                  'suck', 'suc*', 'suck', 'su*k', 'suck', 's*ck', 'suck', '*uck', 'nite', 'nit*', 'nite', 'ni*e',
                  'nite', 'n*te', 'nite', '*ite', 'bastard', 'bastar*', 'bastard', 'basta*d', 'bastard', 'bast*rd',
                  'bastard', 'bas*ard', 'bastard', 'ba*tard', 'bastard', 'b*stard', 'bastard', '*astard', 'p * s s y',
                  'p*ss*', 'p * s s y', 'p*s*y', 'p * s s y', 'p**sy', 'p * s s y', 'p*ssy', 'p * s s y', '**ssy',
                  'pis', 'pi*', 'pis', 'p*s', 'pis', '*is', 'stick', 'stic*', 'stick', 'sti*k', 'stick', 'st*ck',
                  'stick', 's*ick', 'stick', '*tick', 'r u p e', 'rup*', 'r u p e', 'ru*e', 'r u p e', 'r*pe',
                  'r u p e', '*upe', 't!t', 't!*', 't!t', 't*t', 't!t', '*!t', 's * x', 's**', 's * x', 's*x', 's * x',
                  '**x', 'dam', 'da*', 'dam', 'd*m', 'dam', '*am', 'p!s', 'p!*', 'p!s', 'p*s', 'p!s', '*!s', 'segs',
                  'seg*', 'segs', 'se*s', 'segs', 's*gs', 'segs', '*egs', 'b ! t c h', 'b!tc*', 'b ! t c h', 'b!t*h',
                  'b ! t c h', 'b!*ch', 'b ! t c h', 'b*tch', 'b ! t c h', '*!tch', 'crud', 'cru*', 'crud', 'cr*d',
                  'crud', 'c*ud', 'crud', '*rud', 'job', 'jo*', 'job', 'j*b', 'job', '*ob', 'f u c', 'fu*', 'f u c',
                  'f*c', 'f u c', '*uc', 'd i c k', 'dic*', 'd i c k', 'di*k', 'd i c k', 'd*ck', 'd i c k', '*ick',
                  'c r * d', 'cr**', 'c r * d', 'cr*d', 'c r * d', 'c**d', 'c r * d', '*r*d', 'bitch', 'bitc*', 'bitch',
                  'bit*h', 'bitch', 'bi*ch', 'bitch', 'b*tch', 'bitch', '*itch', 'fuk', 'fu*', 'fuk', 'f*k', 'fuk',
                  '*uk', 'trash', 'tras*', 'trash', 'tra*h', 'trash', 'tr*sh', 'trash', 't*ash', 'trash', '*rash',
                  'kil', 'ki*', 'kil', 'k*l', 'kil', '*il', 's e x', 'se*', 's e x', 's*x', 's e x', '*ex', 'gai',
                  'ga*', 'gai', 'g*i', 'gai', '*ai', 'fr*ck', 'fr*c*', 'fr*ck', 'fr**k', 'fr*ck', 'fr*ck', 'fr*ck',
                  'f**ck', 'fr*ck', '*r*ck', 'n ! g g a', 'n!gg*', 'n ! g g a', 'n!g*a', 'n ! g g a', 'n!*ga',
                  'n ! g g a', 'n*gga', 'n ! g g a', '*!gga', 'sh*t', 'sh**', 'sh*t', 'sh*t', 'sh*t', 's**t', 'sh*t',
                  '*h*t', 'crap', 'cra*', 'crap', 'cr*p', 'crap', 'c*ap', 'crap', '*rap', 'idit', 'idi*', 'idit',
                  'id*t', 'idit', 'i*it', 'idit', '*dit', 'sx', 's*', 'sx', '*x', 'sht', 'sh*', 'sht', 's*t', 'sht',
                  '*ht', 'sta', 'st*', 'sta', 's*a', 'sta', '*ta', 'danm', 'dan*', 'danm', 'da*m', 'danm', 'd*nm',
                  'danm', '*anm', 'suc', 'su*', 'suc', 's*c', 'suc', '*uc', 'f u k', 'fu*', 'f u k', 'f*k', 'f u k',
                  '*uk', 't ! t', 't!*', 't ! t', 't*t', 't ! t', '*!t', 'cu', 'c*', 'cu', '*u', 'v*gina', 'v*gin*',
                  'v*gina', 'v*gi*a', 'v*gina', 'v*g*na', 'v*gina', 'v**ina', 'v*gina', 'v*gina', 'v*gina', '**gina',
                  'dummy', 'dumm*', 'dummy', 'dum*y', 'dummy', 'du*my', 'dummy', 'd*mmy', 'dummy', '*ummy', 'shit',
                  'shi*', 'shit', 'sh*t', 'shit', 's*it', 'shit', '*hit', 'nigger', 'nigge*', 'nigger', 'nigg*r',
                  'nigger', 'nig*er', 'nigger', 'ni*ger', 'nigger', 'n*gger', 'nigger', '*igger', 'p u s s', 'pus*',
                  'p u s s', 'pu*s', 'p u s s', 'p*ss', 'p u s s', '*uss', 'thot', 'tho*', 'thot', 'th*t', 'thot',
                  't*ot', 'thot', '*hot', 'pussy', 'puss*', 'pussy', 'pus*y', 'pussy', 'pu*sy', 'pussy', 'p*ssy',
                  'pussy', '*ussy', 'naz*', 'naz*', 'naz*', 'na**', 'naz*', 'n*z*', 'naz*', '*az*', 'a s r e', 'asr*',
                  'a s r e', 'as*e', 'a s r e', 'a*re', 'a s r e', '*sre', 'fck', 'fc*', 'fck', 'f*k', 'fck', '*ck',
                  'prn', 'pr*', 'prn', 'p*n', 'prn', '*rn', 'b a s t a r d', 'bastar*', 'b a s t a r d', 'basta*d',
                  'b a s t a r d', 'bast*rd', 'b a s t a r d', 'bas*ard', 'b a s t a r d', 'ba*tard', 'b a s t a r d',
                  'b*stard', 'b a s t a r d', '*astard', 'hac', 'ha*', 'hac', 'h*c', 'hac', '*ac', 'a s s', 'as*',
                  'a s s', 'a*s', 'a s s', '*ss', 'pus', 'pu*', 'pus', 'p*s', 'pus', '*us', 'pok', 'po*', 'pok', 'p*k',
                  'pok', '*ok', 't * t', 't**', 't * t', 't*t', 't * t', '**t', 'stup', 'stu*', 'stup', 'st*p', 'stup',
                  's*up', 'stup', '*tup', 's t f u', 'stf*', 's t f u', 'st*u', 's t f u', 's*fu', 's t f u', '*tfu',
                  'dumb', 'dum*', 'dumb', 'du*b', 'dumb', 'd*mb', 'dumb', '*umb', 't*t', 't**', 't*t', 't*t', 't*t',
                  '**t', 'fuc', 'fu*', 'fuc', 'f*c', 'fuc', '*uc', 'f r * c k', 'fr*c*', 'f r * c k', 'fr**k',
                  'f r * c k', 'fr*ck', 'f r * c k', 'f**ck', 'f r * c k', '*r*ck', 'lma', 'lm*', 'lma', 'l*a', 'lma',
                  '*ma', 'asre', 'asr*', 'asre', 'as*e', 'asre', 'a*re', 'asre', '*sre', 'sex', 'se*', 'sex', 's*x',
                  'sex', '*ex', 'f u c k', 'fuc*', 'f u c k', 'fu*k', 'f u c k', 'f*ck', 'f u c k', '*uck', 'nazi',
                  'naz*', 'nazi', 'na*i', 'nazi', 'n*zi', 'nazi', '*azi', 'flip', 'fli*', 'flip', 'fl*p', 'flip',
                  'f*ip', 'flip', '*lip', 'fack', 'fac*', 'fack', 'fa*k', 'fack', 'f*ck', 'fack', '*ack', 'vagina',
                  'vagin*', 'vagina', 'vagi*a', 'vagina', 'vag*na', 'vagina', 'va*ina', 'vagina', 'v*gina', 'vagina',
                  '*agina', 'c * c k', 'c*c*', 'c * c k', 'c**k', 'c * c k', 'c*ck', 'c * c k', '**ck', 'n * g g e r',
                  'n*gge*', 'n * g g e r', 'n*gg*r', 'n * g g e r', 'n*g*er', 'n * g g e r', 'n**ger', 'n * g g e r',
                  'n*gger', 'n * g g e r', '**gger', 'geno', 'gen*', 'geno', 'ge*o', 'geno', 'g*no', 'geno', '*eno',
                  'i d i t', 'idi*', 'i d i t', 'id*t', 'i d i t', 'i*it', 'i d i t', '*dit', 'butt', 'but*', 'butt',
                  'bu*t', 'butt', 'b*tt', 'butt', '*utt', 'sh!t', 'sh!*', 'sh!t', 'sh*t', 'sh!t', 's*!t', 'sh!t',
                  '*h!t', 's h t', 'sh*', 's h t', 's*t', 's h t', '*ht', 'ass', 'as*', 'ass', 'a*s', 'ass', '*ss',
                  'clusterfuc', 'clusterfu*', 'clusterfuc', 'clusterf*c', 'clusterfuc', 'cluster*uc', 'clusterfuc',
                  'cluste*fuc', 'clusterfuc', 'clust*rfuc', 'clusterfuc', 'clus*erfuc', 'clusterfuc', 'clu*terfuc',
                  'clusterfuc', 'cl*sterfuc', 'clusterfuc', 'c*usterfuc', 'clusterfuc', '*lusterfuc', 'idoit', 'idoi*',
                  'idoit', 'ido*t', 'idoit', 'id*it', 'idoit', 'i*oit', 'idoit', '*doit', 'mutil', 'muti*', 'mutil',
                  'mut*l', 'mutil', 'mu*il', 'mutil', 'm*til', 'mutil', '*util', 'idiot', 'idio*', 'idiot', 'idi*t',
                  'idiot', 'id*ot', 'idiot', 'i*iot', 'idiot', '*diot', 'fu', 'f*', 'fu', '*u', 'neo', 'ne*', 'neo',
                  'n*o', 'neo', '*eo', 'dump', 'dum*', 'dump', 'du*p', 'dump', 'd*mp', 'dump', '*ump', 'f r u c k',
                  'fruc*', 'f r u c k', 'fru*k', 'f r u c k', 'fr*ck', 'f r u c k', 'f*uck', 'f r u c k', '*ruck',
                  'blo', 'bl*', 'blo', 'b*o', 'blo', '*lo', 'come', 'com*', 'come', 'co*e', 'come', 'c*me', 'come',
                  '*ome', 's*x', 's**', 's*x', 's*x', 's*x', '**x', 'f*ck', 'f*c*', 'f*ck', 'f**k', 'f*ck', 'f*ck',
                  'f*ck', '**ck', 'p ! s', 'p!*', 'p ! s', 'p*s', 'p ! s', '*!s', 'f u', 'f*', 'f u', '*u', 'd*mn',
                  'd*m*', 'd*mn', 'd**n', 'd*mn', 'd*mn', 'd*mn', '**mn', 's h ! t', 'sh!*', 's h ! t', 'sh*t',
                  's h ! t', 's*!t', 's h ! t', '*h!t', 'fuke', 'fuk*', 'fuke', 'fu*e', 'fuke', 'f*ke', 'fuke', '*uke',
                  'n ! g g e r', 'n!gge*', 'n ! g g e r', 'n!gg*r', 'n ! g g e r', 'n!g*er', 'n ! g g e r', 'n!*ger',
                  'n ! g g e r', 'n*gger', 'n ! g g e r', '*!gger', 'anal', 'ana*', 'anal', 'an*l', 'anal', 'a*al',
                  'anal', '*nal', 's h * t', 'sh**', 's h * t', 'sh*t', 's h * t', 's**t', 's h * t', '*h*t',
                  'p u s s y', 'puss*', 'p u s s y', 'pus*y', 'p u s s y', 'pu*sy', 'p u s s y', 'p*ssy', 'p u s s y',
                  '*ussy', 'f a c l', 'fac*', 'f a c l', 'fa*l', 'f a c l', 'f*cl', 'f a c l', '*acl', 'n!gger',
                  'n!gge*', 'n!gger', 'n!gg*r', 'n!gger', 'n!g*er', 'n!gger', 'n!*ger', 'n!gger', 'n*gger', 'n!gger',
                  '*!gger', 'n*gger', 'n*gge*', 'n*gger', 'n*gg*r', 'n*gger', 'n*g*er', 'n*gger', 'n**ger', 'n*gger',
                  'n*gger', 'n*gger', '**gger', 'slap', 'sla*', 'slap', 'sl*p', 'slap', 's*ap', 'slap', '*lap',
                  's u c k', 'suc*', 's u c k', 'su*k', 's u c k', 's*ck', 's u c k', '*uck', 's u c', 'su*', 's u c',
                  's*c', 's u c', '*uc', 'v * g i n a', 'v*gin*', 'v * g i n a', 'v*gi*a', 'v * g i n a', 'v*g*na',
                  'v * g i n a', 'v**ina', 'v * g i n a', 'v*gina', 'v * g i n a', '**gina', 'x x x', 'xx*', 'x x x',
                  'x*x', 'x x x', '*xx', 'gay', 'ga*', 'gay', 'g*y', 'gay', '*ay', 'f a c', 'fa*', 'f a c', 'f*c',
                  'f a c', '*ac', 'fk', 'f*', 'fk', '*k'}

explicit_data4 = {'lma', 'lm*', 'lma', 'l*a', 'lma', '*ma', 'pis', 'pi*', 'pis', 'p*s', 'pis', '*is', 's*ck', 's*c*',
                  's*ck', 's**k', 's*ck', 's*ck', 's*ck', '**ck', 'butt', 'but*', 'butt', 'bu*t', 'butt', 'b*tt',
                  'butt', '*utt', 'kil', 'ki*', 'kil', 'k*l', 'kil', '*il', 'flip', 'fli*', 'flip', 'fl*p', 'flip',
                  'f*ip', 'flip', '*lip', 'rape', 'rap*', 'rape', 'ra*e', 'rape', 'r*pe', 'rape', '*ape', 'segs',
                  'seg*', 'segs', 'se*s', 'segs', 's*gs', 'segs', '*egs', 'prod', 'pro*', 'prod', 'pr*d', 'prod',
                  'p*od', 'prod', '*rod', 's*x', 's**', 's*x', 's*x', 's*x', '**x', 'btch', 'btc*', 'btch', 'bt*h',
                  'btch', 'b*ch', 'btch', '*tch', 'c*nt', 'c*n*', 'c*nt', 'c**t', 'c*nt', 'c*nt', 'c*nt', '**nt',
                  'trash', 'tras*', 'trash', 'tra*h', 'trash', 'tr*sh', 'trash', 't*ash', 'trash', '*rash', 'sx', 's*',
                  'sx', '*x', 'thot', 'tho*', 'thot', 'th*t', 'thot', 't*ot', 'thot', '*hot', 'suc', 'su*', 'suc',
                  's*c', 'suc', '*uc', 'bastard', 'bastar*', 'bastard', 'basta*d', 'bastard', 'bast*rd', 'bastard',
                  'bas*ard', 'bastard', 'ba*tard', 'bastard', 'b*stard', 'bastard', '*astard', 'pok', 'po*', 'pok',
                  'p*k', 'pok', '*ok', 'lana', 'lan*', 'lana', 'la*a', 'lana', 'l*na', 'lana', '*ana', 'n!gger',
                  'n!gge*', 'n!gger', 'n!gg*r', 'n!gger', 'n!g*er', 'n!gger', 'n!*ger', 'n!gger', 'n*gger', 'n!gger',
                  '*!gger', 'geno', 'gen*', 'geno', 'ge*o', 'geno', 'g*no', 'geno', '*eno', 'mutil', 'muti*', 'mutil',
                  'mut*l', 'mutil', 'mu*il', 'mutil', 'm*til', 'mutil', '*util', 't*t', 't**', 't*t', 't*t', 't*t',
                  '**t', 'fuck', 'fuc*', 'fuck', 'fu*k', 'fuck', 'f*ck', 'fuck', '*uck', 'shut', 'shu*', 'shut', 'sh*t',
                  'shut', 's*ut', 'shut', '*hut', 'clusterfuc', 'clusterfu*', 'clusterfuc', 'clusterf*c', 'clusterfuc',
                  'cluster*uc', 'clusterfuc', 'cluste*fuc', 'clusterfuc', 'clust*rfuc', 'clusterfuc', 'clus*erfuc',
                  'clusterfuc', 'clu*terfuc', 'clusterfuc', 'cl*sterfuc', 'clusterfuc', 'c*usterfuc', 'clusterfuc',
                  '*lusterfuc', 'job', 'jo*', 'job', 'j*b', 'job', '*ob', 'dam', 'da*', 'dam', 'd*m', 'dam', '*am',
                  'crap', 'cra*', 'crap', 'cr*p', 'crap', 'c*ap', 'crap', '*rap', 'th*t', 'th**', 'th*t', 'th*t',
                  'th*t', 't**t', 'th*t', '*h*t', 'stfu', 'stf*', 'stfu', 'st*u', 'stfu', 's*fu', 'stfu', '*tfu',
                  'hitler', 'hitle*', 'hitler', 'hitl*r', 'hitler', 'hit*er', 'hitler', 'hi*ler', 'hitler', 'h*tler',
                  'hitler', '*itler', 'tit', 'ti*', 'tit', 't*t', 'tit', '*it', 'p!s', 'p!*', 'p!s', 'p*s', 'p!s',
                  '*!s', 'piss', 'pis*', 'piss', 'pi*s', 'piss', 'p*ss', 'piss', '*iss', 'cr*p', 'cr**', 'cr*p', 'cr*p',
                  'cr*p', 'c**p', 'cr*p', '*r*p', 'suck', 'suc*', 'suck', 'su*k', 'suck', 's*ck', 'suck', '*uck',
                  'idiot', 'idio*', 'idiot', 'idi*t', 'idiot', 'id*ot', 'idiot', 'i*iot', 'idiot', '*diot', 'rob',
                  'ro*', 'rob', 'r*b', 'rob', '*ob', 'sh!t', 'sh!*', 'sh!t', 'sh*t', 'sh!t', 's*!t', 'sh!t', '*h!t',
                  't!t', 't!*', 't!t', 't*t', 't!t', '*!t', 'fu', 'f*', 'fu', '*u', 'v*gina', 'v*gin*', 'v*gina',
                  'v*gi*a', 'v*gina', 'v*g*na', 'v*gina', 'v**ina', 'v*gina', 'v*gina', 'v*gina', '**gina', 'prn',
                  'pr*', 'prn', 'p*n', 'prn', '*rn', 'c!ck', 'c!c*', 'c!ck', 'c!*k', 'c!ck', 'c*ck', 'c!ck', '*!ck',
                  'p!ss', 'p!s*', 'p!ss', 'p!*s', 'p!ss', 'p*ss', 'p!ss', '*!ss', 'p*ssy', 'p*ss*', 'p*ssy', 'p*s*y',
                  'p*ssy', 'p**sy', 'p*ssy', 'p*ssy', 'p*ssy', '**ssy', 'idg', 'id*', 'idg', 'i*g', 'idg', '*dg',
                  'fruck', 'fruc*', 'fruck', 'fru*k', 'fruck', 'fr*ck', 'fruck', 'f*uck', 'fruck', '*ruck', 'danm',
                  'dan*', 'danm', 'da*m', 'danm', 'd*nm', 'danm', '*anm', 'come', 'com*', 'come', 'co*e', 'come',
                  'c*me', 'come', '*ome', 'nazi', 'naz*', 'nazi', 'na*i', 'nazi', 'n*zi', 'nazi', '*azi', 'robl',
                  'rob*', 'robl', 'ro*l', 'robl', 'r*bl', 'robl', '*obl', 'sta', 'st*', 'sta', 's*a', 'sta', '*ta',
                  'gay', 'ga*', 'gay', 'g*y', 'gay', '*ay', 'idit', 'idi*', 'idit', 'id*t', 'idit', 'i*it', 'idit',
                  '*dit', 'fk', 'f*', 'fk', '*k', 'rod', 'ro*', 'rod', 'r*d', 'rod', '*od', 'n!gga', 'n!gg*', 'n!gga',
                  'n!g*a', 'n!gga', 'n!*ga', 'n!gga', 'n*gga', 'n!gga', '*!gga', 'sht', 'sh*', 'sht', 's*t', 'sht',
                  '*ht', 'frick', 'fric*', 'frick', 'fri*k', 'frick', 'fr*ck', 'frick', 'f*ick', 'frick', '*rick',
                  'stup', 'stu*', 'stup', 'st*p', 'stup', 's*up', 'stup', '*tup', 'peg', 'pe*', 'peg', 'p*g', 'peg',
                  '*eg', 'neo', 'ne*', 'neo', 'n*o', 'neo', '*eo', 'dum', 'du*', 'dum', 'd*m', 'dum', '*um', 'bang',
                  'ban*', 'bang', 'ba*g', 'bang', 'b*ng', 'bang', '*ang', 'cu', 'c*', 'cu', '*u', 'seggs', 'segg*',
                  'seggs', 'seg*s', 'seggs', 'se*gs', 'seggs', 's*ggs', 'seggs', '*eggs', 'stick', 'stic*', 'stick',
                  'sti*k', 'stick', 'st*ck', 'stick', 's*ick', 'stick', '*tick', 'dummy', 'dumm*', 'dummy', 'dum*y',
                  'dummy', 'du*my', 'dummy', 'd*mmy', 'dummy', '*ummy', 'sh*t', 'sh**', 'sh*t', 'sh*t', 'sh*t', 's**t',
                  'sh*t', '*h*t', 'dump', 'dum*', 'dump', 'du*p', 'dump', 'd*mp', 'dump', '*ump', 'arse', 'ars*',
                  'arse', 'ar*e', 'arse', 'a*se', 'arse', '*rse', 'crud', 'cru*', 'crud', 'cr*d', 'crud', 'c*ud',
                  'crud', '*rud', 'mur', 'mu*', 'mur', 'm*r', 'mur', '*ur', 'rupe', 'rup*', 'rupe', 'ru*e', 'rupe',
                  'r*pe', 'rupe', '*upe', 'dumb', 'dum*', 'dumb', 'du*b', 'dumb', 'd*mb', 'dumb', '*umb', 'fuk', 'fu*',
                  'fuk', 'f*k', 'fuk', '*uk', 'bitch', 'bitc*', 'bitch', 'bit*h', 'bitch', 'bi*ch', 'bitch', 'b*tch',
                  'bitch', '*itch', 'dip', 'di*', 'dip', 'd*p', 'dip', '*ip', 'fck', 'fc*', 'fck', 'f*k', 'fck', '*ck',
                  'cock', 'coc*', 'cock', 'co*k', 'cock', 'c*ck', 'cock', '*ock', 'cunt', 'cun*', 'cunt', 'cu*t',
                  'cunt', 'c*nt', 'cunt', '*unt', 'fuc', 'fu*', 'fuc', 'f*c', 'fuc', '*uc', 'hit', 'hi*', 'hit', 'h*t',
                  'hit', '*it', 'pus', 'pu*', 'pus', 'p*s', 'pus', '*us', 'pussy', 'puss*', 'pussy', 'pus*y', 'pussy',
                  'pu*sy', 'pussy', 'p*ssy', 'pussy', '*ussy', 'hac', 'ha*', 'hac', 'h*c', 'hac', '*ac', 'vagina',
                  'vagin*', 'vagina', 'vagi*a', 'vagina', 'vag*na', 'vagina', 'va*ina', 'vagina', 'v*gina', 'vagina',
                  '*agina', 'asre', 'asr*', 'asre', 'as*e', 'asre', 'a*re', 'asre', '*sre', 'dick', 'dic*', 'dick',
                  'di*k', 'dick', 'd*ck', 'dick', '*ick', 'lmb', 'lm*', 'lmb', 'l*b', 'lmb', '*mb', 'anal', 'ana*',
                  'anal', 'an*l', 'anal', 'a*al', 'anal', '*nal', 'fac', 'fa*', 'fac', 'f*c', 'fac', '*ac', 'fuke',
                  'fuk*', 'fuke', 'fu*e', 'fuke', 'f*ke', 'fuke', '*uke', 'fort', 'for*', 'fort', 'fo*t', 'fort',
                  'f*rt', 'fort', '*ort', 'fr*ck', 'fr*c*', 'fr*ck', 'fr**k', 'fr*ck', 'fr*ck', 'fr*ck', 'f**ck',
                  'fr*ck', '*r*ck', 'sex', 'se*', 'sex', 's*x', 'sex', '*ex', 'n*zi', 'n*z*', 'n*zi', 'n**i', 'n*zi',
                  'n*zi', 'n*zi', '**zi', 'p*ss', 'p*s*', 'p*ss', 'p**s', 'p*ss', 'p*ss', 'p*ss', '**ss', 'shit',
                  'shi*', 'shit', 'sh*t', 'shit', 's*it', 'shit', '*hit', 'ass', 'as*', 'ass', 'a*s', 'ass', '*ss',
                  'slap', 'sla*', 'slap', 'sl*p', 'slap', 's*ap', 'slap', '*lap', 'nigger', 'nigge*', 'nigger',
                  'nigg*r', 'nigger', 'nig*er', 'nigger', 'ni*ger', 'nigger', 'n*gger', 'nigger', '*igger', 'p*rn',
                  'p*r*', 'p*rn', 'p**n', 'p*rn', 'p*rn', 'p*rn', '**rn', 'dayum', 'dayu*', 'dayum', 'day*m', 'dayum',
                  'da*um', 'dayum', 'd*yum', 'dayum', '*ayum', 'nite', 'nit*', 'nite', 'ni*e', 'nite', 'n*te', 'nite',
                  '*ite', 'blo', 'bl*', 'blo', 'b*o', 'blo', '*lo', 'fack', 'fac*', 'fack', 'fa*k', 'fack', 'f*ck',
                  'fack', '*ack', 'n*gger', 'n*gge*', 'n*gger', 'n*gg*r', 'n*gger', 'n*g*er', 'n*gger', 'n**ger',
                  'n*gger', 'n*gger', 'n*gger', '**gger', 'damn', 'dam*', 'damn', 'da*n', 'damn', 'd*mn', 'damn',
                  '*amn', 'xxx', 'xx*', 'xxx', 'x*x', 'xxx', '*xx', 'porn', 'por*', 'porn', 'po*n', 'porn', 'p*rn',
                  'porn', '*orn', 'gai', 'ga*', 'gai', 'g*i', 'gai', '*ai', 'idoit', 'idoi*', 'idoit', 'ido*t', 'idoit',
                  'id*it', 'idoit', 'i*oit', 'idoit', '*doit', 'nigga', 'nigg*', 'nigga', 'nig*a', 'nigga', 'ni*ga',
                  'nigga', 'n*gga', 'nigga', '*igga', 'd!ck', 'd!c*', 'd!ck', 'd!*k', 'd!ck', 'd*ck', 'd!ck', '*!ck',
                  'naz*', 'naz*', 'naz*', 'na**', 'naz*', 'n*z*', 'naz*', '*az*', 'puss', 'pus*', 'puss', 'pu*s',
                  'puss', 'p*ss', 'puss', '*uss'}

explicit_data3 = {'nazi', 'd!ck', 'slap', 'bitch', 'stick', 'idoit', 'vagina', 'cunt', 'hac', 'dip', 'pis', 'dumb',
                  'dam', 'sex', 'dick', 'fruck', 'prn', 'dump', 'stfu', 'rod', 'blo', 'p!ss', 'suc', 'dummy', 'hit',
                  'n!gga', 'anal', 'rape', 'fuc', 'fac', 'geno', 'fu', 'rob', 'robl', 'suck', 'sta', 'fack', 'damn',
                  'cock', 't!t', 'crap', 'fuke', 'lmb', 'lma', 'dum', 'nite', 'dayum', 'fck', 'btch', 'seggs', 'kil',
                  'shit', 'lana', 'shut', 'flip', 'ass', 'come', 'butt', 'arse', 'gai', 'c!ck', 'fuck', 'pok', 'gay',
                  'xxx', 'fort', 'clusterfuc', 'puss', 'idg', 'mutil', 'sht', 'piss', 'frick', 'stup', 'prod', 'bang',
                  'sx', 'idit', 'nigger', 'rupe', 'danm', 'fk', 'pussy', 'asre', 'peg', 'pus', 'neo', 'mur', 'trash',
                  'p!s', 'hitler', 'idiot', 'tit', 'thot', 'segs', 'sh!t', 'nigga', 'job', 'bastard', 'fuk', 'n!gger',
                  'porn', 'cu', 'crud'}

explicit_data2 = {'cock', 'vagina', 'sex', 'anal', 'fuck',
                  'shit', 'nigga', 'piss', 'cunt', 'pussy', 'dick', 'nigger'}

filter5 = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'e',
           'u', 'i', 'o', 'y', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', ',', "'", '"', '-', '=', '_',
           '+', '\\', '|', '[', ']', '{', '}', '`', '~', ':', ';', '<', '>', '|', ' ', '!', '@', '#', '$', '%', '^',
           '&', '*', '(', ')', '.', ',', "'", '"', '-', '=', '_',
           '+', '\\', '|', '[', ']', '{', '}', '`', '~', ':', ';', '<', '>', '|', ' '}

filter4 = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', }

valid_chars = {'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'w', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'e',
               'u', 'i', 'o', 'y', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', ',', "'", '"', '-', '=', '_',
               '+', '\\', '|', '[', ']', '{', '}', '`', '~', ':', ';', '<', '>', '|', ' '}

special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', ',', "'", '"', '-', '=', '_',
                 '+', '\\', '|', '[', ']', '{', '}', '`', '~', ':', ';', '<', '>', '|', ' '}
responses = ('Leave me alone.',
             ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',
             '...', "Cut it out", "You little-", "I'm guessing you punks like pain?", "Prepare to be hackified!",
             'https://cutt.ly/lTFQus0', "Secret easter egg goes here.", 'Def not easter egg.',
             'ARG time: MDAxMDExMTAwMDEwMTEwMTAwMTAwMDAwMDAxMDExMTAwMDEwMTExMDAwMTAxMTEwMDAxMDExMTAwMDEwMDAwMDAwMTAxMTEwMDAxMDExMDEwMDEwMTExMDAwMTAwMDAwMDAxMDExMDEwMDEwMTEwMTAwMTAxMTAxMDAxMDExMDEwMDEwMTEwMTAwMTAwMDAwMDAxMDExMDEwMDEwMTExMDAwMTAxMTAxMDAxMDExMTAwMDEwMDAwMDAwMTAxMTAxMDAxMDExMTAwMDEwMTExMDAwMTAwMDAwMDAxMDExMDEwMDEwMTEwMTAwMTAxMTAxMDAxMDAwMDAwMDEwMTExMDAwMTAxMTEwMDAxMDExMTAwMDEwMTEwMTAwMTAwMDAwMDAxMDExMTAwMDEwMTEwMTAwMTAxMTEwMDAxMDExMTAwMDEwMDAwMDAwMTAxMTEwMDAxMDExMTAwMDEwMTEwMTAwMTAxMTAxMDAxMDExMDEwMDEwMDAwMDAwMTAxMTAxMDAxMDExMTAwMDEwMTExMDAwMTAwMDAwMDAxMDExMDEwMDEwMTExMDAwMTAwMDAwMDAxMDExMTAwMDEwMTEwMTAwMTAxMTEwMDAxMDExMTAwMDEwMDAwMDAwMTAxMTAxMDAxMDExMDEwMDEwMDAwMDAwMTAxMTAxMDAxMDExMTAwMDEwMTExMDAwMTAwMDAwMDAxMDExMDEwMDEwMTExMDAwMTAwMDAwMDAxMDExMTAwMDEwMTEwMTAwMTAxMTEwMDAxMDExMTAwMDEwMDAwMDAwMTAxMTEwMDAxMDExMTAwMDEwMTExMDAwMTAxMTAxMDAxMDExMDEwMDEwMDAwMDAwMTAxMTAxMDAxMDExMTAwMDEwMTExMDAwMTAwMDAwMDAxMDExMTAwMDEwMTExMDAwMTAxMTEwMDAxMDExMTAwMDEwMDAwMDAwMTAxMTAxMDAxMDExMTAwMDEwMTEwMTAwMTAxMTAxMDAxMDAwMDAwMDEwMTEwMTAwMTAxMTEwMDAxMDAwMDAwMDEwMTEwMTAwMTAxMTEwMDAxMDExMDEwMDEwMTEwMTAwMTAwMDAwMDAxMDExMDEwMDEwMTExMDAwMTAxMTEwMDAxMDExMDE= ',
             'Stop it, get some help.', "Don't you have anything better to do?", "" 'Mesa angeryyyyyyyyy.',
             'Piss the hell off.', 'No one asked.', 'Frick you.', "Don't make me angry",
             "Do you want to summon my wrath?", "Piss off before I'm forced to use   %0.0000023 of my bot power.")
greetings = ('Hello', 'Nice to see you', 'Welcome',
             'Hi', 'Hey there', 'Bonjour', 'Hi there')
byes = ('Bye', 'Come back soon', 'See you later', 'Have fun')

intents = discord.Intents.all()
bot = discord.ext.commands.Bot(command_prefix='>>>', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message: discord.Message):
    if message.content.startswith(">>>"):
        await bot.process_commands(message)
        return
    global spam
    global content
    try:
        print('Full log: ')
        print(datetime.now(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
              message.channel, message.author, message.content,
              message.author.bot, spam, content,
              f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Direct message log: ')
        print(datetime.now(), message.guild, message.channel, message.author, message.id, message.channel.id,
              message.content, message.author.bot, spam, content,
              f'https://discord.com/channels/@me/{message.channel.id}/{message.id}')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print('Log error.')
    test = str(str(message.content).replace(' ', '')).lower()
    if message.author.bot:
        await bot.process_commands(message)
        return
    else:
        pass
    cache = ''
    if spam == 1:
        count = 0
        for index, value in enumerate(test):
            if value == cache:
                count += 1
            cache = value
        count -= 1
        if len(test) > 950 or count > 27:
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not spam.')
    elif spam == 2:
        count = 0
        for index, value in enumerate(test):
            if value == cache:
                count += 1
            if not (value in valid_chars):
                count += 1
            cache = value
        count -= 1
        if len(test) > 450 or count > 15:
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not spam.')
    elif spam == 3:
        count = 0
        for index, value in enumerate(test):
            if value == cache:
                count += 1
            if value in special_chars:
                count += 1
            if not (value in valid_chars):
                count += 1
            cache = value
        count -= 1
        if len(test) > 195 or count > 11:
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not spam.')
    elif spam == 4:
        count = 0
        for index, value in enumerate(test):
            if value == cache:
                count += 1
            if value in special_chars:
                count += 1
            if not (value in valid_chars):
                count += 1
            cache = value
        count -= 1
        if len(test) > 90 or count > 5:
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not spam.')
    if content == 1:
        if profanity.contains_profanity(test) or any(i in test for i in explicit_data2):
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not swear.')
    elif content == 2:
        if profanity.contains_profanity(test) or any(i in test for i in explicit_data3):
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not swear.')
    elif content == 3:
        if profanity.contains_profanity(test) or any(i in test for i in explicit_data4):
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not swear.')
        for i in filter4:
            test = test.replace(i, '*')
        if profanity.contains_profanity(test) or any(i in test for i in explicit_data4):
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not swear.')
    elif content == 4:
        if profanity.contains_profanity(test) or any(i in test for i in explicit_data5):
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not swear.')
        for i in filter5:
            test = test.replace(i, '*')
        if profanity.contains_profanity(test) or any(i in test for i in explicit_data5):
            await message.delete()
            await message.channel.send(f'{message.author.mention} please do not swear.')
    if bot.user in message.mentions:
        for i in message.guild.members:
            if i.guild_permissions.moderate_members:
                try:
                    await i.send(
                        f'{i.mention} **{message.author}** needs help in **{message.guild}** in **{message.channel}** at https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}.')
                except (
                        discord.HTTPException, discord.errors.HTTPException,
                        discord.ext.commands.errors.CommandInvokeError,
                        commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                    print(f'Cannot direct message {str(i)}.')
            else:
                pass
        await message.channel.send(f'{message.author.mention} pinged Moderators.')
    await bot.process_commands(message)


@bot.event
async def on_member_join(member: discord.Member):
    await member.send(f'{member.mention} Welcome to **{member.guild.name}**!')
    await member.send(':wave:')


@bot.event
async def on_member_remove(member: discord.Member):
    await member.send(f'{member.mention} see you soon in **{member.guild.name}**')
    await member.send(':wave:')


@bot.command(aliases=('call', 'request'))
async def ping(ctx):
    await ctx.send(f'{bot.latency * 1000} ms.')


@bot.command(aliases=('delete', 'purge', 'clean'))
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount + 1)


@bot.event
async def on_raw_reaction_add(payload):
    data = reacting.get((payload.guild_id, payload.message_id))
    if type(data) == tuple:
        pass
    else:
        return
    if str(payload.emoji) == data[1]:
        guild = await bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = guild.get_role(data[0])
        await member.add_roles(role)
        try:
            await member.send(f'You got the **{role.name}** role in **{guild.name}** for reacting!')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}')


@bot.event
async def on_raw_reaction_remove(payload):
    data = reacting.get((payload.guild_id, payload.message_id))
    if type(data) == tuple:
        pass
    else:
        return
    if str(payload.emoji) == data[1]:
        guild = await bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = guild.get_role(data[0])
        await member.remove_roles(role)
        try:
            await member.send(f'You lost the **{role.name}** role in **{guild.name}** for unreacting!')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}')


@bot.command(aliases=('8ball', '8bal'))
async def _8ball(ctx):
    _8ball = ("As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
              "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.",
              "Most likely.",
              "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.",
              "Reply hazy, try again.",
              "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.",
              "You may rely on it.")
    await ctx.send(random.choice(_8ball))


@bot.command(aliases=('remove', 'kick_user', 'kick_member', 'remove_user', 'remove_member'))
@commands.has_permissions(kick_members=True)
async def kick(ctx, member_id: int, *, reason='None'):
    user = await bot.fetch_user(member_id)
    member = await ctx.guild.fetch_member(member_id)
    await member.kick(reason=reason)
    await ctx.send(f'''**{ctx.message.author.mention}** kicked **{member.mention}**:
**{reason}**.''')
    try:
        await user.send(f'''{member.mention} you were kicked from **{ctx.guild}** by **{ctx.author}**:
    **{reason}**''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')


# @staticmethod
# def can_timeout(ctx):
#     async def predicate(ctx):
#         if ctx.author.guild_permissions.moderate_members or ctx.author.guild_permissions.manage_messages:
#             return False
#         return True
#     return commands.check(predicate)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, time: float = None, *, reason='None'):
    duration = (time * 60)
    await member.timeout(duration=duration, reason=reason)
    try:
        await member.send(f'''{member.mention} you were put in the timeout chair by **{ctx.author}** for {time} minutes, because:
**{reason}**.''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'''{ctx.author.mention} put {member.mention} in the timeout chair for {time} minutes, because:
**{reason}**.''')


@bot.command()
@commands.has_permissions(moderate_members=True)
async def un_timeout(ctx, member: discord.Member, *, reason='None'):
    await member.timeout(duration=None, reason=reason)
    try:
        await member.send(f'''{member.mention} you were taken out of the timeout chair by **{ctx.author}**, because:
{reason}''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'''{ctx.author.mention} took {member.mention} out of the timeout chair, because:
**{reason}**''')


@bot.command(aliases=('un_timeout_users', 'un_timeout_people'))
@commands.has_permissions(moderate_members=True)
async def un_timeout_members(ctx, member_ids, *, reason='None'):
    try:
        tuple(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    members = convert_to_list(member_ids)
    for member in members:
        i = await ctx.guild.fetch_member(int(member))
        await i.timeout(duration=None, reason=reason)
        try:
            await i.send(f'''{i.mention} you were taken out of the timeout chair by **{ctx.author}**, because:
**{reason}**.''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(i)}.')
    await ctx.send(f'''{ctx.author.mention} took lots of members out of the timeout chair, because:
**{reason}**.''')


@bot.command(aliases=('timeout_users', 'timeout_people'))
@commands.has_permissions(moderate_members=True)
async def timeout_members(ctx, member_ids, time: float = None, *, reason='None'):
    duration = (time * 60)
    try:
        tuple(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    members = convert_to_list(member_ids)
    for member in members:
        i = await ctx.guild.fetch_member(int(member))
        await i.timeout(duration=duration, reason=reason)
        try:
            await i.send(f'''{i.mention} you were put in the timeout chair by **{ctx.author}** for {time} minutes, because:
**{reason}**.''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(i)}.')
    await ctx.send(f'''{ctx.author.mention} put lots of members in the timeout chair for {time} minutes, because:
**{reason}**.''')


@bot.command()
@commands.has_permissions(moderate_members=True, manage_channels=True)
async def timeout_hush(ctx, time: float = None, *, reason='None'):
    duration = (time * 60)
    for member in ctx.guild.members:
        if member.guild_permissions.moderate_members:
            continue
        else:
            pass
        await member.timeout(duration=duration, reason=reason)
        try:
            await member.send(f'''{member.mention} you were put in the timeout chair by **{ctx.author}** for {time} minutes, because:
**{reason}**.''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'''{ctx.author.mention} put the channel in the timeout chair for {time} minutes, because:
**{reason}**.''')


@bot.command()
@commands.has_permissions(moderate_members=True, manage_channels=True)
async def timeout_un_hush(ctx, *, reason='None'):
    for member in ctx.guild.members:
        if member.guild_permissions.moderate_members:
            continue
        else:
            pass
        await member.timeout(duration=None, reason=reason)
        try:
            await member.send(f'''{member.mention} you were taken out of the timeout chair by **{ctx.author}**, because:
**{reason}**.''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'''{ctx.author.mention} took the channel out of the timeout chair, because:
**{reason}**.''')


@bot.command(aliases=('ban_user', 'ban_member'))
@commands.has_permissions(ban_members=True)
async def ban(ctx, member_id: int, *, reason='None'):
    user = await bot.fetch_user(member_id)
    member = await ctx.guild.fetch_member(member_id)
    await member.ban(reason=reason)
    await ctx.send(f'''**{ctx.message.author.mention}** banned **{member.mention}**:
**{reason}**.''')
    try:
        await user.send(f'''{user.mention} you were banned from **{ctx.guild}** by **{ctx.author}**:
**{reason}**''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int, *, reason):
    banned_users = await ctx.guild.bans()
    to_unban = await bot.fetch_user(user_id)
    for ban_entry in banned_users:
        user = ban_entry.user
        if user.id == to_unban.id:
            await ctx.guild.unban(user)
            await ctx.send(f'''**{ctx.message.author.mention}** unbanned **{user.mention}** because:
**{reason}**''')
            try:
                await user.send(f'''**{user.mention}** you were unbanned by **{ctx.message.author.mention}** because:
**{reason}**''')
            except (
                    discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    ValueError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {user}.')
            return


@bot.command()
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member_id: int, *, reason='None'):
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'muted':
            role_id = i.id
            break
    if 'muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='muted')
        await ctx.send('"muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
        member = await ctx.guild.fetch_member(member_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    if member.guild_permissions.manage_messages and (
            member.guild_permissions.manage_channels or member.guild_permissions.moderate_members):
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = False
    overwrite.read_message_history = True
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await member.add_roles(role)
    await ctx.send(f'''**{member.mention}** was muted by **{ctx.message.author.mention}** because:
**{reason}**''')
    try:
        await member.send(f'''You were muted in **{ctx.guild}** by **{ctx.author}** because:
**{reason}**''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')


@bot.command()
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member_id: int):
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'muted':
            role_id = i.id
            break
    if 'muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='muted')
        await ctx.send('"muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
        member = await ctx.guild.fetch_member(member_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    if member.guild_permissions.manage_messages and (
            member.guild_permissions.manage_channels or member.guild_permissions.moderate_members):
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = False
    overwrite.read_message_history = True
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await member.remove_roles(role)
    await ctx.send(f'''**{member.mention}** was unmuted by **{ctx.message.author.mention}**!''')
    try:
        await member.send(f'''You were unmuted in **{ctx.guild}** by **{ctx.author}**!''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')


@bot.command()
@commands.has_permissions(moderate_members=True, manage_roles=True)
async def role_mute(ctx, role_id, *, reason='None'):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = False
    overwrite.read_message_history = True
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    role = get(await ctx.guild.fetch_roles(), id=role_id)
    if role.guild_permissions.manage_messages and (
            role.guild_permissions.manage_channels or role.guild_permissions.moderate_members):
        return
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'''**{role.mention}** were muted by **{ctx.message.author.mention}**:
**{reason}**''')


@bot.command()
@commands.has_permissions(moderate_members=True, manage_roles=True)
async def role_unmute(ctx, role_id: int):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = True
    overwrite.read_message_history = True
    overwrite.create_public_threads = True
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    role = get(await ctx.guild.fetch_roles(), id=role_id)
    if role.guild_permissions.manage_messages and (
            role.guild_permissions.manage_channels or role.guild_permissions.moderate_members):
        return
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'''**{role.mention}** were unmuted by **{ctx.message.author.mention}**!''')


@bot.command()
@commands.has_permissions(moderate_members=True, manage_roles=True)
async def role_file_unmute(ctx, role_id: int):
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = True
    overwrite.embed_links = True
    overwrite.external_emojis = False
    overwrite.external_stickers = False
    overwrite.add_reactions = True
    role = get(await ctx.guild.fetch_roles(), id=role_id)
    if role.guild_permissions.manage_messages and (
            role.guild_permissions.manage_channels or role.guild_permissions.moderate_members):
        return
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'''**{role.mention}** were file_unmuted by **{ctx.message.author.mention}**!''')


@bot.command()
@commands.has_permissions(moderate_members=True, manage_roles=True)
async def role_file_mute(ctx, role_id: int, *, reason='None'):
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = False
    overwrite.embed_links = False
    overwrite.external_emojis = False
    overwrite.external_stickers = False
    overwrite.add_reactions = True
    role = get(await ctx.guild.fetch_roles(), id=role_id)
    if role.guild_permissions.manage_messages and (
            role.guild_permissions.manage_channels or role.guild_permissions.moderate_members):
        return
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'''**{role.mention}** were file_muted by **{ctx.message.author.mention}**:
**{reason}**''')


@bot.command()
@commands.has_permissions(moderate_members=True)
async def file_unmute(ctx, member_id: int):
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'file_muted':
            role_id = i.id
            break
    if 'file_muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='file_muted')
        await ctx.send('"file_muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
        member = await ctx.guild.fetch_member(member_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    if member.guild_permissions.manage_messages and (
            member.guild_permissions.manage_channels or member.guild_permissions.moderate_members):
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = False
    overwrite.embed_links = False
    overwrite.external_emojis = False
    overwrite.external_stickers = False
    overwrite.add_reactions = True
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await member.remove_roles(role)
    await ctx.send(f'''**{member.mention}** was file_unmuted by **{ctx.message.author.mention}**!''')
    try:
        await member.send(f'''You were file_unmuted in **{ctx.guild}** by **{ctx.author}**!''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')


@bot.command()
@commands.has_permissions(moderate_members=True)
async def file_mute(ctx, member_id: int, *, reason='None'):
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'file_muted':
            role_id = i.id
            break
    if 'file_muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='file_muted')
        await ctx.send('"file_muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
        member = await ctx.guild.fetch_member(member_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    if member.guild_permissions.manage_messages and (
            member.guild_permissions.manage_channels or member.guild_permissions.moderate_members):
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = False
    overwrite.embed_links = False
    overwrite.external_emojis = False
    overwrite.external_stickers = False
    overwrite.add_reactions = True
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    await member.add_roles(role)
    await ctx.send(f'''**{member.mention}** was file_muted by **{ctx.message.author.mention}**:
**{reason}**''')
    try:
        await member.send(f'''You were file_muted in **{ctx.guild}** by **{ctx.author}**:
**{reason}**''')
    except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')


@bot.command(aliases=('channel_clear', 'channel_clean'))
@commands.has_permissions(manage_messages=True, manage_channels=True)
async def channel_purge(ctx, *, reason='None'):
    channel = ctx.channel
    new_channel = await channel.clone(name=channel.name, reason=reason)
    await channel.delete()
    await new_channel.send(f'**{ctx.message.author.mention}** purged **{ctx.message.channel}**')


@bot.command(aliases=('alert', 'notify', 'inform'))
@commands.has_permissions(moderate_members=True, view_audit_log=True)
async def warn(ctx, member: discord.Member, *, reason='None'):
    with open('Warns.txt', 'a') as file:
        file = file.write(
            f'**{member.mention}** you were warned by **{ctx.author}**:**{reason}**\n')
    await ctx.send(f'''{member.mention} you were warned by **{ctx.author.mention}**:
**{reason}**''')
    try:
        await member.send(f'''{member.mention} you were warned in {ctx.guild} by **{ctx.author}**:
**{reason}**''')
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {str(member)}.')


@bot.command(aliases=('get_member_history', 'pull_member_history'))
async def fetch_member_history(ctx, member: discord.Member, limit=10, links=False):
    try:
        bool(links)
    except ValueError:
        raise ValueError('Invalid boolean for "links".')
    messages = []
    async for message in (ctx.channel.history(limit=limit)):
        if message.author == member:
            if links:
                messages.insert(
                    0, f'https://discord.com/channels/{ctx.guild.id}/{message.channel.id}/{message.id}')
            else:
                messages.insert(0, message.id)
    await ctx.send(messages)


@bot.command(aliases=('get_messages', 'pull_messages'))
async def fetch_messages(ctx, limit=10, links=False):
    try:
        bool(links)
    except ValueError:
        raise ValueError('Invalid boolean for "links".')
    messages = []
    async for message in (ctx.channel.history(limit=limit)):
        if links:
            messages.insert(
                0, f'https://discord.com/channels/{ctx.guild.id}/{message.channel.id}/{message.id}')
        else:
            messages.insert(0, {message.id})
    await ctx.send(messages)


@bot.command(aliases=('silence', 'mute_channel', 'silence_channel'))
@commands.has_permissions(manage_messages=True, moderate_members=True, manage_channels=True)
async def hush(ctx):
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'muted':
            role_id = i.id
            break
    if 'muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='muted')
        await ctx.send('"muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = False
    overwrite.read_message_history = True
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    for i in ctx.guild.members:
        if i.guild_permissions.manage_messages and (
                i.guild_permissions.manage_channels or i.guild_permissions.moderate_members):
            continue
        else:
            await i.add_roles(role)
            try:
                await i.send(f'''You were muted in **{ctx.guild}** by **{ctx.author}**!''')
            except (
                    discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {str(i)}.')
    await ctx.send(f'{ctx.author.mention} has hushed the channel.')


@bot.command(aliases=('un_silence', 'unmute_channel', 'un_silence_channel'))
@commands.has_permissions(manage_messages=True, moderate_members=True, manage_channels=True)
async def un_hush(ctx):
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'muted':
            role_id = i.id
            break
    if 'muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='muted')
        await ctx.send('"muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = False
    overwrite.read_message_history = True
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    for i in ctx.guild.members:
        if i.guild_permissions.manage_messages and (
                i.guild_permissions.manage_channels or i.guild_permissions.moderate_members):
            continue
        else:
            await i.remove_roles(role)
            try:
                await i.send(f'''You were unmuted in **{ctx.guild}** by **{ctx.author}**!''')
            except (
                    discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {str(i)}.')
    await ctx.send(f'{ctx.author.mention} has unhushed the channel.')


@bot.command(aliases=('fetch_roles', 'pull_roles'))
async def get_roles(ctx, ids=False):
    try:
        bool(ids)
    except ValueError:
        raise ValueError('Invalid boolean for "ids".')
    roles = []
    for i in ctx.guild.roles:
        if ids:
            roles.insert(0, i.id)
        else:
            roles.insert(0, i.name)
    await ctx.send(roles)


@bot.command(aliases=('remove_channel', 'end_channel'))
@commands.has_permissions(manage_channels=True)
async def delete_channel(ctx, channel):
    is_channel = await ctx.guild.fetch_channel(int(channel))
    await is_channel.delete()
    await ctx.send('Deleted channel.')


@bot.command(aliases=('get_channels', 'pull_channels'))
async def fetch_channels(ctx, links=False):
    try:
        bool(links)
    except ValueError:
        raise ValueError('Invalid boolean for "links".')
    channels = []
    for i in ctx.guild.channels:
        if links:
            channels.insert(
                0, f'https://discord.com/channels/{ctx.guild.id}/{i.id}')
        else:
            channels.insert(0, i.id)
    await ctx.send(channels)


@bot.command(aliases=('remove_channels', 'end_channels'))
@commands.has_permissions(manage_channels=True)
async def delete_channels(ctx, *, channels):
    try:
        list(channels)
    except ValueError:
        raise ValueError('Invalid list for "channels".')
    tup = convert_to_list(channels)
    print(tup)
    for i in tup:
        print(i)
        channel = await ctx.guild.fetch_channel(int(i))
        await channel.delete()
    await ctx.send('Deleted channels.')


@bot.command(aliases=('remove_members', 'kick_users', 'remove_users'))
@commands.has_permissions(kick_members=True)
async def kick_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(member_ids)
    for i in tup:
        print(i)
        user = await bot.fetch_user(int(i))
        member = await ctx.guild.fetch_member(int(i))
        await member.kick(reason='None')
        try:
            await user.send(f'''{user.mention} you were kicked from **{ctx.guild}** by **{ctx.author}**!''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {user}.')
    await ctx.send(f'{ctx.author.mention} kicked members.')


@bot.command(aliases=('ban_users', 'ban_people'))
@commands.has_permissions(ban_members=True)
async def ban_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(member_ids)
    for i in tup:
        print(i)
        user = await bot.fetch_user(int(i))
        member = await ctx.guild.fetch_member(int(i))
        await member.ban()
        try:
            await user.send(f'''{user.mention} you were banned from {ctx.guild} by **{ctx.author}**!''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {user}.')
    await ctx.send(f'{ctx.author.mention} banned members.')


@bot.command(aliases=('unban_users', 'unban_people'))
@commands.has_permissions(ban_members=True)
async def unban_members(ctx, *, user_ids):
    try:
        list(user_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(user_ids)
    for i in tup:
        print(i)
        user = await bot.fetch_user(int(i))
        await ctx.guild.unban(user)
        try:
            await user.send(f'''{user.mention} you were unbanned from **{ctx.guild}** by **{ctx.author}**!''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {user.display_name}.')
    await ctx.send('Unbanned members.')


@bot.command(aliases=('mute_users', 'mute_people'))
@commands.has_permissions(moderate_members=True)
async def mute_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(member_ids)
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'muted':
            role_id = i.id
            break
    if 'muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='muted')
        await ctx.send('"muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = False
    overwrite.read_message_history = True
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    for i in tup:
        member = await ctx.guild.fetch_member(int(i))
        await member.add_roles(role)
        try:
            await member.send(f'''{member.mention} you were muted in {ctx.guild} by **{ctx.author}**!''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'{ctx.author.mention} muted members.')


@bot.command(aliases=('unmute_users', 'unmute_people'))
@commands.has_permissions(moderate_members=True)
async def unmute_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(member_ids)
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'muted':
            role_id = i.id
            break
    if 'muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='muted')
        await ctx.send('"muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.send_messages_in_threads = False
    overwrite.read_message_history = True
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False
    overwrite.add_reactions = True
    overwrite.speak = False
    overwrite.stream = False
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    for i in tup:
        member = await ctx.guild.fetch_member(int(i))
        await member.remove_roles(role)
        try:
            await member.send(f'''{member.mention} you were unmuted in {ctx.guild} by **{ctx.author}**!''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'{ctx.author.mention} unmuted members.')


@bot.command(aliases=('file_mute_users', 'file_mute_people'))
@commands.has_permissions(moderate_members=True)
async def file_mute_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(member_ids)
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'file_muted':
            role_id = i.id
            break
    if 'file_muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='file_muted')
        await ctx.send('"file_muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = False
    overwrite.embed_links = False
    overwrite.external_emojis = False
    overwrite.external_stickers = False
    overwrite.add_reactions = True
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    for i in tup:
        member = await ctx.guild.fetch_member(int(i))
        await member.add_roles(role)
        try:
            await member.send(f'''{member.mention} you were file_muted in {ctx.guild} by **{ctx.author}**!''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'{ctx.author.mention} file_muted members.')


@bot.command(aliases=('file_unmute_users', 'file_unmute_people'))
@commands.has_permissions(moderate_members=True)
async def file_unmute_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(member_ids)
    roles = []
    for i in ctx.guild.roles:
        roles.append(i.name)
        if i.name == 'file_muted':
            role_id = i.id
            break
    if 'file_muted' in roles:
        pass
    else:
        await ctx.guild.create_role(name='file_muted')
        await ctx.send('"file_muted" role error')
        return
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send('An error occurred.')
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = True
    overwrite.embed_links = True
    overwrite.external_emojis = False
    overwrite.external_stickers = False
    overwrite.add_reactions = True
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    for i in tup:
        member = await ctx.guild.fetch_member(int(i))
        await member.remove_roles(role)
        try:
            await member.send(f'''{member.mention} you were file_unmuted in {ctx.guild} by **{ctx.author}**!''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
    await ctx.send(f'{ctx.author.mention} file_unmuted members.')


@bot.command(aliases=('purge_messages', 'clean_messages', 'delete_messages'))
@commands.has_permissions(manage_messages=True)
async def clear_messages(ctx, *, message_ids):
    try:
        list(message_ids)
    except ValueError:
        raise ValueError('Invalid list for "member_ids".')
    tup = convert_to_list(message_ids)
    for i in tup:
        print(i)
        message = await ctx.fetch_message(int(i))
        await message.delete()


@bot.command(aliases=('spam_filter', 'spam'))
@commands.has_permissions(manage_messages=True, moderate_members=True)
async def spam_check(ctx, value):
    global spam
    if int(value) and int('-1') < int(value) < 5 or int(value) == 0:
        spam = int(value)
    else:
        raise ValueError('Invalid value for "spam_check".')
    await ctx.send(f'Spam filter level has been set to {value}.')


@bot.command(aliases=('content_filter', 'content', 'swear_check', 'profanity_filter', 'profanity_check'))
@commands.has_permissions(manage_messages=True, moderate_members=True)
async def content_check(ctx, value):
    global content
    if int(value) and int('-1') < int(value) < 5 or int(value) == 0:
        content = int(value)
    else:
        raise ValueError('Invalid value for "content_check".')
    await ctx.send(f'Explicit filter level has been set to {value}.')


@bot.command(aliases=('get_docs', 'pull_docs'))
async def fetch_docs(ctx):
    await ctx.send('https://pastebin.com/9w4Fp110')


@bot.command(aliases=('get_code', 'pull_code'))
async def fetch_code(ctx):
    await ctx.send('https://github.com/HRLO77/Bot-source-code')


@bot.command(aliases=('get_message', 'pull_message'))
async def fetch_message(ctx, message_id):
    await ctx.send(f'https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message_id}')


@bot.command(aliases=('bm', 'mark', 'book'))
async def bookmark(ctx, message_id: int=-1):
    if message_id == -1:
        message_id = int(ctx.message.reference.message_id)
    message = await ctx.fetch_message(message_id)
    try:
        await ctx.author.send(
            content=f'''{ctx.author.mention}, you bookmarked a post in **{ctx.guild.name}** within **{ctx.channel.name}** by **{message.author}**:
```
{message.content}
```https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message_id}''')
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            ValueError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.send(f'Cannot direct message {ctx.author.mention}.')
        print(f'Cannot direct message {ctx.author}.')


@bot.command(aliases=('members', 'member#'))
async def member_count(ctx):
    await ctx.send(f'{ctx.guild.member_count} members are in the guild.')


@bot.command(aliases=('online_members', 'online_member#'))
async def online_member_count(ctx):
    members = 0
    for i in ctx.guild.members:
        if i.bot:
            continue
        elif str(i.status) == 'offline':
            continue
        else:
            members += 1
    await ctx.send(f'{members} members are online in the guild.')


@bot.command(aliases=('get_member', 'pull_member'))
async def fetch_member(ctx, member_id: discord.Member):
    await ctx.send(member_id.mention)


@bot.command(aliases=('dm_members', 'dm_users', 'direct_message_users'))
@commands.has_permissions(administrator=True)
async def direct_message_members(ctx, member_ids='all', *, content='None'):
    if member_ids.lower() == 'all':
        pass
    else:
        try:
            tuple(member_ids)
        except ValueError:
            raise ValueError('Invalid list for "member_ids".')
        tup = convert_to_list(member_ids)
        for i in tup:
            member = await ctx.guild.fetch_member(int(i))
            try:
                await member.send(
                    f'''{member.mention} **{ctx.author}** said in https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}:
**{content}**''')
            except (
                    discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {str(member)}.')
                pass
        await ctx.send(f'{ctx.author.mention} direct messaged people in dms.')
        await ctx.ctx.author.send(f'{ctx.author.mention} you direct messaged people in dms in **{ctx.guild}**.')
        return
    for i in ctx.guild.members:
        try:
            await i.send(
                f'''{i.mention} **{ctx.author}** said in https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}:
**{content}**''')
        except (
                discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                ValueError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(i)}.')
            pass
    await ctx.send(f'{ctx.author.mention} direct messaged everyone in dms.')
    await ctx.ctx.author.send(f'{ctx.author.mention} you direct messaged everyone in dms in **{ctx.guild}**.')


@bot.command(aliases=('silent_direct_message_members', 'silent_dm', 'silent_direct_message' ,'silent_direct_message_users', 'silent_message_users', 'silent_dm_members', 'silent_dm_users'))
@commands.has_permissions(administrator=True)
async def silent_message_members(ctx, member_ids='all', *, content='None'):
    
    if member_ids.lower() == 'all':
        pass
    else:
        try:
            tuple(member_ids)
        except ValueError:
            raise ValueError('Invalid list for "member_ids".')
        tup = convert_to_list(member_ids)
        for i in tup:
            member = await ctx.guild.fetch_member(int(i))
            try:
                await member.send(
                    f'''{member.mention}, {content}''')
            except (
                    discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {str(member)}.')
                pass
        await ctx.author.send(f'{ctx.author.mention} you silent direct messaged members from **{ctx.guild}**.')
        await ctx.message.delete()
        return
    for i in ctx.guild.members:
        try:
            await i.send(
                f'''{i.mention} **{ctx.author}** said in https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}:
**{content}**''')
        except (
                discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                ValueError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(i)}.')
            pass
    await ctx.author.send(f'{ctx.author.mention} you silent direct messaged everyone from **{ctx.guild}**.')
    await ctx.message.delete()

@bot.command(aliases=('terminate_bot', 'kill_bot', 'cut_bot'))
@commands.has_permissions(administrator=True)
async def close_bot(ctx):
    await ctx.send('Bot terminating...')
    await bot.close()


@bot.command(aliases=('e', 'eval'))
async def evaluate(ctx, *, command):
    f = open('compile_user_code.py', 'w')
    f = f.writelines(str(command).strip('```py').strip('```').strip('```python'))
    result = subprocess.run([sys.executable, "-c", f"{str(command).strip('```py').strip('```').strip('```python')}"],
                            input=f,
                            capture_output=True, text=True, timeout=5)
    if len(result.stdout) > 45:
        o = open('out.txt', 'w')
        o = o.writelines(str(result.stdout))
        file = discord.File(r'filepath_to_out.txt')
        await ctx.send(content='Program output too long, full output in text document:', file=file)
        o = ''
        return
    f = ''
    await ctx.send(f'''{ctx.author.mention} Your code has finished with a return code of **{result.returncode}**:
```
{result.stderr}
{result.stdout}
```''')


@bot.command(aliases=('restart_bot', 'reset', 'reset_bot'))
@commands.has_permissions(administrator=True)
async def restart(ctx):
    await ctx.send('Restarting bot...')
    exec(open('restart.py').read())
    sys.exit()


@bot.command(aliases=('get_warns', 'pull_warns'))
@commands.has_permissions(moderate_members=True, view_audit_log=True)
async def fetch_warns(ctx):
    file = discord.File(r'filepath_to_Warns.txt')
    await ctx.send(content='Warns:', file=file)


@bot.command()
async def print_out(ctx, *, message):
    member = await ctx.guild.fetch_member(ctx.message.author.id)
    new_message = await ctx.message.channel.send(message)
    await member.send(
        f'{member.mention} you printed out a message in https://discord.com/channels/{ctx.guild.id}/{ctx.message.channel.id}/{new_message.id}.')
    await ctx.message.delete()


@bot.command(aliases=('update_react', 'add_react'))
@commands.has_permissions(moderate_members=True, manage_messages=True, manage_channels=True)
async def set_react(ctx, reacting_message_id: int, default_role_id: int, emoji_to_react: str):
    reacting[(ctx.guild.id, reacting_message_id)] = (default_role_id, emoji_to_react)
    await ctx.send(
        f'{ctx.author.mention} updated reacting object index: **{(ctx.guild.id, reacting_message_id)}:{(default_role_id, emoji_to_react)}**')


@bot.command(aliases=('delete_react', 'rm_react', 'del_react'))
@commands.has_permissions(moderate_members=True, manage_messages=True, manage_channels=True)
async def remove_react(ctx, reacting_message_id: int):
    del reacting[(ctx.guild.id, reacting_message_id)]
    await ctx.send(f'{ctx.author.mention} deleted reacting object index: **{(ctx.guild.id, reacting_message_id)}**')


@bot.command(aliases=('react_obj', 'react_object', 'react_dictionary'))
async def react_dict(ctx):
    await ctx.send(f"Reacting dictionary for RawReactionEvent - **{reacting}**")


@bot.command(aliases=('reset_token', 'reset_code', 'refresh_token', 'refresh_code', 'code'))
@commands.has_permissions(moderate_members=True, view_audit_log=True, manage_messages=True)
async def token(ctx, Member: int):
    member = await ctx.guild.fetch_member(Member)
    
    secret = [secrets.token_bytes(), secrets.token_hex(), secrets.token_urlsafe()]
    try:
        await member.send(
            f'''{member.mention} your code is: __{random.choice(secret[0:2])}__ and token is *{secret[2]}* in **{ctx.guild}**.
    If a staff member asks for your verification code/token, send them a picture of this message.''')
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        await ctx.author.send(f'''{ctx.author.mention}, cannot direct message {member}. Direct message {member} with this data:
code - __{random.choice(secret[0:2])}__ and token is *{secret[2]}* in **{ctx.guild}**.''')
        print(f'Cannot direct message {member}.')
        return
    try:
        await ctx.author.send(
            f'''{ctx.author.mention} you reset {member}'s token at  https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}. {member}'s data is now:
code - __{random.choice(secret[0:2])}__ and token is *{secret[2]}* in **{ctx.guild}**.''')
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f'Cannot direct message {ctx.author}.')


@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="An error occurred")
    embed.set_footer(text=error)
    await ctx.send(embed=embed)


@bot.command(aliases=('rm_swear', 'delete_swear', 'remove_swear'))
@commands.has_permissions(moderate_members=True, manage_messages=True)
async def del_swear(ctx, *, string: str):
    if content == 0:
        await ctx.message.delete()
        raise IndexError(f"Explicit data check is currently disabled.")
    elif content == 1:
        if string in explicit_data2:
            explicit_data2.remove(string)
        else:
            await ctx.message.delete()
            raise IndexError(f"Explicit_data2 does not contain {string} as a value.")
    elif content == 2:
        if string in explicit_data3:
            explicit_data3.remove(string)
        else:
            await ctx.message.delete()
            raise IndexError(f"Explicit_data3 does not contain {string} as a value.")
    elif content == 3:
        if string in explicit_data4:
            explicit_data4.remove(string)
        else:
            await ctx.message.delete()
            raise IndexError(f"Explicit_data4 does not contain {string} as a value.")
    elif content == 4:
        if string in explicit_data5:
            explicit_data5.remove(string)
        else:
            await ctx.message.delete()
            raise IndexError(f"Explicit_data5 does not contain {string} as a value.")
    await ctx.send(f"{ctx.author.mention} swear was removed from the filter.")
    await ctx.message.delete()


@bot.command(aliases=['append_swear'])
@commands.has_permissions(moderate_members=True, manage_messages=True)
async def add_swear(ctx, *, string: str):
    if content == 0:
        await ctx.message.delete()
        raise IndexError(f"Explicit data check is currently disabled.")
        return
    elif content == 1:
        explicit_data2.add(string)
    elif content == 2:
        explicit_data3.add(string)
    elif content == 3:
        explicit_data4.add(string)
    elif content == 4:
        explicit_data5.add(string)
    await ctx.send(f'{ctx.author.mention}, swear was added to the filter.')
    await ctx.message.delete()


@bot.command(aliases=['append_enhanced_swears'])
@commands.has_permissions(moderate_members=True, manage_messages=True)
async def add_enhanced_swears(ctx, *, swears):
    try:
        list(swears)
    except ValueError:
        raise ValueError('Invalid list for "swears"')
    test = []
    set = convert_to_list(swears)
    print(set)
    for i in set:
        for index, value in enumerate(str(i).replace(' ', '')):
            if ' ' in i:
                dat = Functions.str_to_list(Functions.list_to_str(Functions.spliceOutWords(str(i))))
                dat[index] = '*'
                test.insert(0, Functions.list_to_str(dat))
                test.insert(0, i)
            else:
                dat = Functions.str_to_list(str(i))
                dat[index] = '*'
                test.insert(0, Functions.list_to_str(dat))
                test.insert(0, i)
            if content == 0:
                await ctx.message.delete()
                raise IndexError(f"Explicit data check is currently disabled.")
                return
            elif content == 1:
                explicit_data2.add(Functions.list_to_str(dat))
                explicit_data2.add(i)
            elif content == 2:
                explicit_data3.add(Functions.list_to_str(dat))
                explicit_data3.add(i)
            elif content == 3:
                explicit_data5.add(Functions.list_to_str(dat))
                explicit_data5.add(i)
            elif content == 4:
                explicit_data5.add(Functions.list_to_str(dat))
                explicit_data5.add(i)
    await ctx.send(f'{ctx.author.mention}, swear was added to the filter.')
    await ctx.message.delete()


@bot.command()
async def print_embed(ctx, title, *, text):
    
    embed = discord.Embed(title=title)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
    embed.set_footer(text=text)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_text_channel(ctx, name, *, reason='None'):
    await ctx.guild.create_text_channel(name=name, reason=reason)
    await ctx.send(f"{ctx.author.mention} create a text channel {name}.")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_vc(ctx, name, *, reason='None'):
    await ctx.guild.create_voice_channel(name=name, reason=reason)
    await ctx.send(f"{ctx.author.mention} create a vc {name}.")


@bot.command()
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, name, *, reason='None'):
    await ctx.guild.create_role(name=name, reason=reason)
    await ctx.send(f"{ctx.author.mention} created role {name}.")


@bot.command(aliases=('del_role', 'rm_role', 'remove_role'))
@commands.has_permissions(manage_roles=True)
async def delete_role(ctx, role_id: int, *, reason='None'):
    try:
        role = get(await ctx.guild.fetch_roles(), id=role_id)
    except (
            discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        raise discord.HTTPException("Could not fetch role.")
    await ctx.send(f'{ctx.author.mention} deleted role {role.name}.')
    await role.delete(reason=reason)


# @bot.command()
# async def write(ctx, member_id: int, to_dict: str):
#     perms = convert_to_list(to_dict)
#     if "dict" in type(perms):
#         pass
#     else:
#         raise ValueError("Invalid dict for overwrite permissions")
#     member = await ctx.guild.fetch_member(member_id)
#     overwrite = discord.PermissionOverwrite()
#     for i in perms.keys():
#         overwrite[i] = perms.get(i)
#     await ctx.message.channel.set_permissions(member, overwrite=overwrite)


@bot.command(aliases=['purgeban'])
@commands.has_permissions(moderate_members=True, manage_messages=True)
async def purge_ban(ctx, member_id: int, limit: int = 10):
    async for message in ctx.channel.history(limit=limit):
        if message.author.id == member_id:
            await message.delete()
        else:
            continue
    await ctx.send(f"{ctx.author.mention} deleted the last {limit} messages from {(await ctx.guild.fetch_member(member_id)).mention}")


#   overwrite = discord.PermissionOverwrite()
#   overwrite.send_messages = True
#   overwrite.read_messages = True
#   await ctx.message.channel.set_permissions(member/role, overwrite=overwrite)


bot.run('token')
