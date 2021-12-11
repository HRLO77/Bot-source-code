import random
import ctx
import discord
import Functions
import datetime
from datetime import datetime
import requests
import sys
import profanity
from profanity import profanity
import tracemalloc
import ctypes
from discord.ext import commands
from datetime import datetime
import csv
from discord import guild
import pbwrap
from pbwrap import pbwrap

muted_channel = False
tracemalloc.start()
spam = 0
content = 0

explicit_data5 = {'shit', 'fuck', 'fck', 'fu', 'f u', 'f u k', 'fuk', 'f u c k', 'sh!t', 'sht', 'f*ck', 'd*mn', 's h t',
                  's h ! t',
                  'sh*t', 's h * t', 'btch', 'bitch', 'b i t c h', 'b ! t c h', 'b t c h', 's u c', 'suc', 'suck',
                  's*ck', 's u c k', 'sex', 's e x', 'sx', 's x', 's * x', 's*x', 'xxx', 'x x x', 'porn', 'prn',
                  'p o r n', 'p*rn', 'p * r n', 'tit', 't!t', 't*t', 't i t', 't * t', 't ! t', 'bastard',
                  'b a s t a r d', 'b * s t * r d', 'rape', 'r a p e', 'r * p e', 'rupe', 'r u p e', 'dick', 'd i c k',
                  'd * c k', 'd ! c k', 'd!ck', 'cock', 'c o c k', 'c * c k', 'c ! c k', 'c!ck', 'pussy', 'p u s s y',
                  'p*ssy', 'p * s s y', 'vagina',
                  'v*gina', 'fack', 'f a c', 'fac', 'f a c l', 'v * g i n a', 'crap', 'c r a p', 'c r u d', 'cr*p',
                  'c r * p', 'idiot', 'idit', 'i d i o t', 'idoit', 'i d o i t', 'i d i t', 'piss', 'p*ss', 'p!ss',
                  'p i s s', 'pis', 'p i s', 'p * s s', 'p!s', 'p * s', 'p ! s', 'fuc', 'f u c', 'f u k', 'ass', 'arse',
                  'a s s', 'asre', 'a r s e', 'a s r e', 'puss', 'p u s', 'p u s s', 'stfu', 's t f u', 'fu', 'f u',
                  'nigga', 'nigger', 'n!gga', 'n!gger', 'n*gger', 'n ! g g e r', 'n * g g a', 'n * g g e r',
                  'n ! g g a',
                  'flip', 'f l i p', 'frick', 'f r i c k', 'dam', 'dayum', 'anal', 'butt', 'lana', 'seggs', 'segs',
                  'peg', 'damn', 'danm', 'shut', 'cunt', 'c*nt', 'clusterfuc', 'nazi', 'naz*', 'n*zi', 'neo', 'fk',
                  'fuke', 'trash', 'bang', 'hit', 'slap', 'gay', 'gai', 'hitler', 'geno', 'kil', 'mur', 'mutil',
                  'sta', 'blo', 'job', 'rob', 'robl', 'fort', 'nite', 'stup', 'dum', 'dam', 'dumb', 'dummy', 'lma',
                  'lmb', 'idg', 'pus', 'cu', 'come', 'dump', 'hac', 'dip', 'stick', 'rod', 'prod', 'pok', 'dum', 'thot',
                  't h o t', 'th*t', 't h * t', 'crud', 'crap', 'c r * d', 'fruck', 'f r u c k', 'fr*ck', 'f r * c k'}
explicit_data4 = {'cunt', 'mur', 'pussy', 'sex', 'pis', 'frick', 'nigga', 'nazi', 'sht', 'sh*t', 'rape', 'crap',
                  'n*gger', 'xxx', 'neo', 'rupe', 'naz*', 'dam', 'asre', 'dummy', 'th*t', 'fort', 'thot', 'fk', 'prod',
                  'v*gina', 'pok', 'gay', 'lmb', 'peg', 'hac', 'geno', 'dayum', 'hit', 'job', 'n!gger', 'p*rn', 'flip',
                  'p*ss', 'idoit', 'damn', 'p*ssy', 'dump', 'nigger', 'p!s', 'fck', 'sta', 'crud', 'segs', 'shit',
                  'c!ck', 's*ck', 'bastard', 'kil', 'fuc', 'porn', 'cu', 't!t',
                  'tit', 'fack', 'sh!t', 'butt', 'danm', 'dip', 's*x', 'd!ck', 'gai', 'idit', 'cock', 'fuke', 'puss',
                  'trash', 'slap', 'seggs', 'anal', 'sx', 'fac', 'idiot', 'c*nt', 'stup', 'fr*ck', 'n!gga', 'rob',
                  'mutil', 'dumb', 't*t', 'stfu', 'clusterfuc', 'blo', 'hitler', 'lana', 'rod', 'fuk', 'nite', 'suck',
                  'fuck', 'btch', 'lma', 'pus', 'p!ss', 'idg', 'cr*p', 'n*zi', 'robl', 'piss', 'shut', 'ass', 'bitch',
                  'fu', 'prn', 'arse', 'stick', 'fruck', 'suc', 'bang', 'dum', 'vagina', 'come', 'dick'}
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
           'u', 'i', 'o', 'y', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'}
filter4 = {'!', '@', '#', '$', '%', '&', '*'}
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
             "Do you want to summon my wrath?", "Piss off before I'm forced to use %0.0000023 of my bot power.")
greetings = ('Hello', 'Nice to see you', 'Welcome',
             'Hi', 'Hey there', 'Bonjour', 'Hi there')
byes = ('Bye', 'Come back soon', 'See you later', 'Have fun')

intents = discord.Intents.all()
client = discord.ext.commands.Bot(command_prefix='>>>', intents=intents)
profanity.load_words(explicit_data2)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message: discord.Message):
    global spam
    global content
    print(datetime.now(), message.guild.id, message.channel.id, message.author.id, message.id, message.content,
          message.author.bot, spam, content,
          f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}')
    test = str(str(message.content).replace(' ', '')).lower()
    if message.author.bot:
        await client.process_commands(message)
        return
    else:
        pass
    cache = ''
    if spam == 1:
        count = 0
        for index, value in enumerate(test):
            if value == cache:
                count += 1
            if value in special_chars:
                count += 1
            if not(value in valid_chars):
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
            if value in special_chars:
                count += 1
            if not(value in valid_chars):
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
            if not(value in valid_chars):
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
    if client.user in message.mentions:
        for i in message.guild.members:
            if i.guild_permissions.administrator:
                await i.send(
                    f'**{message.author}** pinged bot at https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}.')
            else:
                pass
    await client.process_commands(message)


@client.event
async def on_member_join(ctx, *, member: discord.Member):
    await ctx.send(f'{member.mention} joined.')
    await ctx.send(':wave:')


@client.event
async def on_member_remove(ctx, *, member: discord.member):
    await ctx.send(f'{member.mention} left.')
    await ctx.send(':wave:')


@client.command(aliases=('call', 'request'))
async def ping(ctx):
    await ctx.send(f'{client.latency * 1000} ms.')


@client.command(aliases=('delete', 'purge', 'clean'))
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=int(amount) + 1)


@client.command(aliases=('8ball', '8bal'))
async def _8ball(ctx, *, question):
    _8ball = ("As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
              "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.",
              "Most likely.",
              "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.",
              "Reply hazy, try again.",
              "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.",
              "You may rely on it.")
    await ctx.send(random.choice(_8ball))


@client.command(aliases=('remove', 'kick_user', 'kick_member', 'remove_user', 'remove_member'))
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason='None'):
    await member.kick(reason=reason)
    await ctx.send(f'''**{ctx.message.author.mention}** kicked **{member.mention}**:
    **{reason}**.''')
    await member.send(f'''You were kicked from {ctx.guild} by **{ctx.author}**:
**{reason}**.''')


@client.command(aliases=('ban_user', 'ban_member'))
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason='None'):
    await member.ban(reason=reason)
    await (f'''**{ctx.message.author.mention}** banned **{member.mention}**:
    **{reason}**.''')
    await member.send(f'''You were banned from {ctx.guild} by **{ctx.author}**:
    **{reason}**''')


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'**{ctx.message.author.mention}** unbanned **{member.mention}**')
            return


@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason='None'):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    await ctx.message.channel.set_permissions(member, overwrite=overwrite)
    await ctx.send(f'''**{member.mention}** was muted by **{ctx.message.author.mention}**:
**{reason}**''')


@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    await ctx.message.channel.set_permissions(member, overwrite=overwrite)
    await ctx.send(f'''**{member.mention}** was unmuted by **{ctx.message.author.mention}**!''')


@client.command()
@commands.has_permissions(manage_messages=True, manage_guild=True, manage_channels=True)
async def role_mute(ctx, role: discord.Role, *, reason='None'):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'''**{role.mention}** were muted by **{ctx.message.author.mention}**:
**{reason}**''')


@client.command()
@commands.has_permissions(manage_messages=True, manage_guild=True, manage_channels=True)
async def role_unmute(ctx, role: discord.Role):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'''**{role.mention}** were unmuted by **{ctx.message.author.mention}**!''')


@client.command()
@commands.has_permissions(manage_messages=True, manage_guild=True, manage_channels=True)
async def role_file_unmute(ctx, role: discord.Role):
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = True
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f"**{role.mention}** were file unmuted by **{ctx.message.author.mention}**!")


@client.command()
@commands.has_permissions(manage_messages=True, manage_guild=True, manage_channels=True)
async def role_file_mute(ctx, role: discord.Role, *, reason='None'):
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = False
    await ctx.message.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send(f'''**{role.mention}** were file muted by **{ctx.message.author.mention}**:
**{reason}**''')


@client.command()
@commands.has_permissions(administrator=True)
async def file_unmute(ctx, member: discord.Member):
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = True
    await ctx.message.channel.set_permissions(member, overwrite=overwrite)
    await ctx.send(f'''**{member.mention}** was file_unmuted by **{ctx.message.author.mention}**''')


@client.command()
@commands.has_permissions(administrator=True)
async def file_mute(ctx, member: discord.Member, *, reason='None'):
    overwrite = discord.PermissionOverwrite()
    overwrite.attach_files = True
    await ctx.message.channel.set_permissions(member, overwrite=overwrite)
    await ctx.send(f'''**{member.mention}** was file_muted by **{ctx.message.author.mention}**:
**{reason}**''')


@client.command(aliases=('channel_clear', 'channel_clean'))
@commands.has_permissions(manage_messages=True, manage_channels=True)
async def channel_purge(ctx):
    await ctx.channel.purge()
    await (f'**{ctx.message.author.mention}** purged **{ctx.message.channel}**')


@client.command(aliases=('alert', 'notify', 'inform'))
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, *, reason):
    with open('Warns.txt', 'a') as file:
        file = file.write(
            f'**{member.mention}** you were warned by **{ctx.author}**:**{reason}**\n')
    await ctx.send(f'''**{member.mention}** you were warned by **{ctx.author.mention}**:
**{reason}**''')


@client.command(aliases=('get_member_histroy', 'pull_member_history'))
async def fetch_member_history(ctx, member: discord.Member, limit=10):
    messages = []
    async for message in (ctx.channel.history(limit=limit)):
        if message.author == member:
            messages.insert(
                0, f'https://discord.com/channels/{ctx.guild.id}/{message.channel.id}/{message.id}')
    await ctx.send(messages)


@client.command(aliases=('get_messages', 'pull_messages'))
async def fetch_messages(ctx, limit=10):
    messages = []
    async for message in (ctx.channel.history(limit=limit)):
        messages.insert(
            0, f'https://discord.com/channels/{ctx.guild.id}/{message.channel.id}/{message.id}')
    await ctx.send(messages)


@client.command(aliases=('silence', 'mute_channel', 'silence_channel'))
@commands.has_permissions(manage_messages=True, manage_channels=True)
async def hush(ctx):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = True
    for i in ctx.guild.members:
        if i.guild_permissions.manage_messages and i.guild_permissions.manage_channels:
            pass
        else:
            await ctx.message.channel.set_permissions(i, overwrite=overwrite)
    await ctx.send(f'{ctx.author.mention} has hushed the channel.')


@client.command(aliases=('un_silence', 'unmute_channel', 'un_silence_channel'))
@commands.has_permissions(manage_messages=True, manage_channels=True)
async def un_hush(ctx):
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    overwrite.read_messages = True
    for i in ctx.guild.members:
        if i.guild_permissions.manage_messages and i.guild_permissions.manage_channels:
            pass
        else:
            await ctx.message.channel.set_permissions(i, overwrite=overwrite)
    await ctx.send(f'{ctx.author.mention} has unhushed the channel.')


@client.command(aliases=('fetch_roles', 'pull_roles'))
async def get_roles(ctx, ids):
    try:
        bool(ids)
    except ValueError:
        await ctx.send('Invalid value for "ids"')
        return
    roles = []
    for i in ctx.guild.roles:
        if ids:
            roles.insert(0, i.id)
        else:
            roles.insert(0, i)
    await ctx.send(roles)


@client.command(aliases=('remove_channel', 'end_channel'))
@commands.has_permissions(manage_channels=True, manage_guild=True)
async def delete_channel(ctx, channel):
    is_channel = await client.fetch_channel(int(channel))
    await is_channel.delete()
    await ctx.send('Deleted channel.')


@client.command(aliases=('get_channels', 'pull_channels'))
async def fetch_channels(ctx, link=False):
    try:
        bool(link)
    except ValueError:
        await ctx.send('Invalid boolean for "link"')
        return
    channels = []
    for i in ctx.guild.channels:
        if link:
            channels.insert(
                0, f'https://discord.com/channels/{ctx.guild.id}/{i.id}')
        else:
            channels.insert(0, i.id)
    await ctx.send(channels)


@client.command(aliases=('remove_channels', 'end_channels'))
@commands.has_permissions(manage_messages=True, manage_guild=True, manage_channels=True)
async def delete_channels(ctx, *, channels):
    try:
        list(channels)
    except ValueError:
        await ctx.send('Invalid list for "channels"')
        return
    tup = convert_to_list(channels)
    print(tup)
    for i in tup:
        print(i)
        channel = await client.fetch_channel(int(i))
        await channel.delete()
    await ctx.send('Deleted channels.')


@client.command(aliases=('remove_members', 'kick_users', 'remove_users'))
@commands.has_permissions(kick_members=True)
async def kick_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        await ctx.send('Invalid list for "members"')
        return
    tup = convert_to_list(member_ids)
    for i in tup:
        print(i)
        member = await client.fetch_user(int(i))
        await member.kick(reason='None')
        await member.send(f'''You were kicked from {ctx.guild} by **{ctx.author}**!''')
    await ctx.send('Kicked members.')

@client.command(aliases=('ban_users', 'ban_people'))
@commands.has_permissions(ban_members=True)
async def ban_members(ctx, *, member_ids):
    try:
        list(member_ids)
    except ValueError:
        await ctx.send('Invalid list for "members"')
        return
    tup = convert_to_list(member_ids)
    for i in tup:
        print(i)
        member = await client.fetch_user(int(i))
        await member.ban()
        await member.send(f'''You were banned from {ctx.guild} by **{ctx.author}**!''')
    await ctx.send('Banned members.')


@client.command(aliases=('purge_messages', 'clean_messages', 'delete_messages'))
@commands.has_permissions(manage_messages=True, manage_channels=True)
async def clear_messages(ctx, *, message_ids):
    try:
        list(message_ids)
    except ValueError:
        await ctx.send('Invalid list for "members"')
        return
    tup = convert_to_list(message_ids)
    for i in tup:
        print(i)
        message = await ctx.fetch_message(int(i))
        await message.delete()


@client.command(aliases=('spam_filter', 'spam'))
@commands.has_permissions(administrator=True)
async def spam_check(ctx, value):
    global spam
    if int(value) and -1 < int(value) < 5:
        spam = int(value)
    else:
        await ctx.send('Invalid content_check value')
        return
    await ctx.send(f'Spam filter level has been set to {value}.')

@client.command(aliases=('content_filter', 'content', 'swear_check', 'profanity_filter', 'profanity_check'))
@commands.has_permissions(administrator=True)
async def content_check(ctx, value):
    global content
    if int(value) and -1 < int(value) < 5:
        content = int(value)
    else:
        await ctx.send('Invalid content_check value')
        return
    await ctx.send(f'Explicit filter level has been set to {value}.')


@client.command(aliases=('get_docs', 'pull_docs'))
async def fetch_docs(ctx):
    await ctx.send('https://pastebin.com/9w4Fp110')


@client.command(aliases=('get_code', 'pull_code'))
async def fetch_code(ctx):
    await ctx.send('https://github.com/HRLO77/Bot-source-code')


@client.command(aliases=('get_message', 'pull_message'))
async def fetch_message(ctx, message_id):
    await ctx.send(f'https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message_id}')


@client.command(aliases=('bm', 'mark', 'book'))
async def bookmark(ctx, message_id):
    member = await client.fetch_user(ctx.author.id)
    try:
        await member.send(content=f'''{ctx.author.mention}. You bookmarked a post in {ctx.guild.name} in {ctx.channel.name}.
    https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message_id}''')
    except discord.HTTPException or discord.errors.HTTPException or discord.ext.commands.errors.CommandInvokeError or commands.CommandInvokeError or commands.CommandError or AttributeError:
        await ctx.send('Cannot direct message member.')

@client.command(aliases=('members', 'member#'))
async def member_count(ctx):
    await ctx.send(f'{ctx.guild.member_count} members are in the guild.')


@client.command(aliases=('get_member', 'pull_member'))
async def fetch_member(ctx, member_id: discord.Member):
    await ctx.send(member_id.mention)


@client.command(aliases=('dm_members', 'dm_users', 'direct_message_users'))
@commands.has_permissions(administrator=True)
async def direct_message_members(ctx, member_ids='all', *, content='None'):
    if member_ids.lower() == 'all':
        pass
    else:
        try:
            tuple(member_ids)
        except ValueError:
            await ctx.send('Invalid member_ids.')
            return
        tup = convert_to_list(member_ids)
        for i in tup:
            try:
                member = await client.fetch_user(int(i))
                await member.send(
                    f'''**{ctx.author}** said in https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}:
**{content}**''')
            except discord.HTTPException or discord.errors.HTTPException or discord.ext.commands.errors.CommandInvokeError or commands.CommandInvokeError or commands.CommandError or AttributeError:
                pass
        await ctx.send(f'{ctx.author.mention} Messaged people in dms.')
        return
    for i in ctx.guild.members:
        try:
            await i.send(
                f'''**{ctx.author}** said in https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}:
**{content}**''')
        except discord.HTTPException or discord.errors.HTTPException or discord.ext.commands.errors.CommandInvokeError or commands.CommandInvokeError or commands.CommandError or AttributeError:
            pass
    await ctx.send(f'{ctx.author.mention} Messaged everyone in dms.')


@client.command(aliases=('terminate_bot', 'kill_bot', 'cut_bot'))
@commands.has_permissions(administrator=True)
async def close_bot(ctx):
    await ctx.send('Bot terminating...')
    sys.exit()


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


def convert_to_list(str):
    cache = ''
    data = []
    for i in str.replace(' ', ''):
        if i == ',':
            data.append(cache)
            cache = ''
        else:
            cache = f'{cache}{i}'
    data.append(cache)
    return data


#   overwrite = discord.PermissionOverwrite()
#   overwrite.send_messages = True
#   overwrite.read_messages = True
#   await ctx.message.channel.set_permissions(member/role, overwrite=overwrite)


client.run('token')
