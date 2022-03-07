from explicit_data import *
from disnake.ext import tasks
from disnake.utils import get
import secrets
import tracemalloc
from profanity import profanity
import sys
import subprocess
import datetime
from disnake.ext import commands
import disnake as discord
import random
import Functions
import importlib as ilib
import asyncio
import json
from datetime import datetime
TOKEN = 'TOKEN'


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


def check(cache):
    length = 0
    for index, value in enumerate(cache):
        if value == '*':
            length += 1
    if length > len(cache) / 3 + 1:
        return False
    return True


def log(to_log: tuple, guild):
    with open('logs.json', 'r') as json_file:
        json_data = json.load(json_file)
    text = json_data[str(guild)]
    text = f'{text}\n'
    for i in to_log:
        text = f'{text}{i} '
    try:
        json.loads(json.dumps(text))
        with open('logs.txt', 'r') as txt:
            file_state = txt.read()
        with open('logs.txt', 'w') as file:
            file.writelines(text)
        with open('logs.txt', 'r') as txt:
            txt.read()
        with open('logs.txt', 'w') as file:
            file.writelines(file_state)
    except (json.JSONDecodeError, TypeError, UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError, UnicodeWarning, discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
        print(f"Couldn't log data for guild {guild}")
        return
    json_data[str(guild)] = text
    with open('logs.json', 'w') as json_file:
        json.dump(json_data, json_file)


# json_data = json.load((open("reacting_data.json", 'r')))
# for i in convert_to_list(list(json_data.keys())):
#     for val in i:


# If you want to create a system to provides a default role when a member reacts, follow the dict syntax below.
# Remember to enter integers for all of the ID's, and a string for the emoji! You can create multiple default roles for different messages in your channel using this dictionary syntax!
reacting = {('guild_id', 'reacting_message_id'): ('role_id_to_add', 'emoji_to_react')}


muted_channel = False
tracemalloc.start()
sniped_messages = dict()
filtering = dict()
spam = 1
content = 1


intents = discord.Intents.all()
bot = discord.ext.commands.Bot(command_prefix=['>>>', '>'], intents=intents, case_insensitive=True)


def full_delete():
    data = {}
    for guild in bot.guilds:
        data[str(guild.id)] = ""
    with open('logs.json', 'w') as file:
        json.dump(data, file)


def reset_logs(guild_id):
    with open('logs.json', 'r') as file:
        data = json.load(file)
    data[str(guild_id)] = ""
    with open('logs.json', 'w') as file:
        json.dump(data, file)
    with open('warns.json', 'r') as json_file:
        try:
            data = json.load(json_file)
        except (json.JSONDecodeError):
            data = {}
            for guild in bot.guilds:
                data[str(guild.id)] = {"0": 0}
            with open('warns.json', 'w') as json_file:
                json.dump(data, json_file)
        else:
            if str(guild_id) in data.keys():
                pass
            else:
                data[str(guild_id)] = {"0": 0}
            with open('warns.json', 'w') as json_file:
                json.dump(data, json_file)


class event_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        reset_logs(guild.id)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        reset_logs(guild.id)

    @commands.Cog.listener()
    async def on_ready(self):
        global filtering
        print(f'There are {len(self.bot.users)} users.')
        print(f'We have logged in as {self.bot.user}')
        await self.bot.change_presence(activity=discord.Game(f'{self.bot.command_prefix[-1]}fetch_docs'))
        full_delete()
        with open('warns.json', 'r') as json_file:
            try:
                data = json.load(json_file)
            except (json.JSONDecodeError):
                data = {}
                for guild in self.bot.guilds:
                    data[str(guild.id)] = {"0": 0}
            else:
                for guild in self.bot.guilds:
                    if str(guild.id) in data.keys():
                        pass
                    else:
                        data[str(guild.id)] = {"0": 0}
        for i in self.bot.guilds:
            filtering[str(i.id)] = (1, 1)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        global filtering
        if not(message.guild is None):
            try:
                filtering[str(message.guild.id)]
            except KeyError:
                filtering[str(message.guild.id)] = (1, 1)
        async def syspurgeban(member_id, limit=10, bulk: bool = False):
            list_messages = []
            messages = 0
            async for i in message.channel.history(limit=99999999999999999):
                if messages >= limit:
                    if bulk:
                        await message.channel.delete_messages(list_messages)
                    return
                if i.author.id == member_id:
                    if not(bulk):
                        messages += 1
                        await i.delete()
                    elif bulk:
                        messages += 1
                        list_messages.append(i)
                else:
                    continue

        def check_for_spam(m):
            return m.author == message.author
        if any(i in (str(message.content).replace(' ', '')) for i in ('dQw4w9WgXcQ', 'astley')) and not(message.author.bot):
            await message.channel.send(f'{message.author.mention} {random.choice(rickrolls)}.')
            await message.author.send(f'{message.author.mention} bruh why?')
        try:
            print('Full message log: \n', datetime.now(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                  message.channel, message.author, message.content,
                  message.author.bot, (filtering[str(message.guild.id)][1]), (filtering[str(message.guild.id)][0]),
                  f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}')
            log(('Full message log: \n', datetime.now(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                 message.channel, message.author, message.content,
                 message.author.bot, (filtering[str(message.guild.id)][1]), (filtering[str(message.guild.id)][0]),
                 f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}'), message.guild.id)
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print('Direct message log: \n', datetime.now(), message.guild, message.channel, message.author, message.id, message.channel.id,
                  message.content, message.author.bot,
                  f'https://discord.com/channels/@me/{message.channel.id}/{message.id}')
            return
        except (AttributeError, discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, discord.Forbidden):
            print('Message log error.')
        test = str(str(message.content).replace(' ', '')).lower()
        if message.author.bot:
            return
        else:
            pass
        cache = ''
        if (filtering[str(message.guild.id)][1]) == 1:
            count = 0
            for index, value in enumerate(test):
                if value == cache:
                    count += 1
                cache = value
            count -= 1
            if len(test) > 950 or count > 27:
                await message.delete()
        elif (filtering[str(message.guild.id)][1]) == 2:
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
        elif (filtering[str(message.guild.id)][1]) == 3:
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
        elif (filtering[str(message.guild.id)][1]) == 4:
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
        if (filtering[str(message.guild.id)][0]) == 1:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data2):
                await message.delete()
        elif (filtering[str(message.guild.id)][0]) == 2:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data3):
                await message.delete()
        elif (filtering[str(message.guild.id)][0]) == 3:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data4):
                await message.delete()
            for i in filter4:
                test = test.replace(i, '*')
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data4):
                await message.delete()
        elif (filtering[str(message.guild.id)][0]) == 4:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data5):
                await message.delete()
            for i in filter5:
                test = test.replace(i, '*')
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data5):
                await message.delete()
        # syspurgeban(message.author.id, 10, 1)
        # await message.author.timeout(duration=60.0, reason='Spam')
        # await message.author.send(
        #     f'{message.author.mention} you\'ve been muted in **{message.guild}** for spamming for **60** seconds.')
        # await message.channel.send(f'{message.author.mention} please do not spam.')
        if (filtering[str(message.guild.id)][1]) == 1:
            try:
                await bot.wait_for('message', timeout=1, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 5, 1)
        elif (filtering[str(message.guild.id)][1]) == 2:
            try:
                await bot.wait_for('message', timeout=2, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 15, 1)
        elif (filtering[str(message.guild.id)][1]) == 3:
            try:
                await bot.wait_for('message', timeout=8.5, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 25, 1)
                await message.author.timeout(duration=30.0, reason='Spam')
                await message.author.send(
                    f'{message.author.mention} you\'ve been muted in **{message.guild}** for spamming for **30** seconds.')
        elif (filtering[str(message.guild.id)][1]) == 4:
            try:
                await bot.wait_for('message', timeout=15, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 30, 1)
                await message.author.timeout(duration=60.0, reason='Spam')
                await message.author.send(
                    f'{message.author.mention} you\'ve been muted in **{message.guild}** for spamming for **60** seconds.')


    @commands.Cog.listener()
    async def on_message_edit(self, old_message: discord.Message, message: discord.Message):
        if any(i in (str(message.content).replace(' ', '')) for i in ('dQw4w9WgXcQ', 'rick', 'astley')) and not(message.author.bot):
            await message.channel.send(f'{message.author.mention} {random.choice(rickrolls)}.')
            await message.author.send(f'{message.author.mention} bruh why?')
        global spam
        global content
        try:
            print('Full message edit log: \n', datetime.now(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                  message.channel, message.author, message.content,
                  message.author.bot, (filtering[str(message.guild.id)][1]), (filtering[str(message.guild.id)][0]),
                  f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}')
            log(('Full message edit log: \n', datetime.now(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                 message.channel, message.author, message.content,
                 message.author.bot,
                 f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}'), message.guild.id)
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print('Direct message edit log: \n', datetime.now(), message.guild, message.channel, message.author, message.id, message.channel.id,
                  message.content, message.author.bot,
                  f'https://discord.com/channels/@me/{message.channel.id}/{message.id}')
            return
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print('Message edit log error.')
        test = str(str(message.content).replace(' ', '')).lower()
        if message.author.bot:
            return
        else:
            pass
        cache = ''
        if (filtering[str(message.guild.id)][1]) == 1:
            count = 0
            for index, value in enumerate(test):
                if value == cache:
                    count += 1
                cache = value
            count -= 1
            if len(test) > 950 or count > 27:
                await message.delete()
        elif (filtering[str(message.guild.id)][1]) == 2:
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
        elif (filtering[str(message.guild.id)][1]) == 3:
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
        elif (filtering[str(message.guild.id)][1]) == 4:
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
        if (filtering[str(message.guild.id)][0]) == 1:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data2):
                await message.delete()
        elif (filtering[str(message.guild.id)][0]) == 2:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data3):
                await message.delete()
        elif (filtering[str(message.guild.id)][0]) == 3:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data4):
                await message.delete()
            for i in filter4:
                test = test.replace(i, '*')
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data4):
                await message.delete()
        elif (filtering[str(message.guild.id)][0]) == 4:
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data5):
                await message.delete()
            for i in filter5:
                test = test.replace(i, '*')
            if profanity.contains_profanity(test) or any(i in test for i in explicit_data5):
                await message.delete()


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await member.send(f'{member.mention} Welcome to **{member.guild.name}**!')
        await member.send(':wave:')


    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        await member.send(f'{member.mention} see you soon in **{member.guild.name}**')
        await member.send(':wave:')


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title=f"An error occurred:", description=f'{error}')
        embed.color = ctx.author.color
        icon = self.bot.user.avatar
        if not(icon is None):
            icon = icon.url
        else:
            icon = self.bot.user.default_avatar.url
        embed.set_author(icon_url=icon, name=self.bot.user)
        icon = ctx.author.avatar
        if not(icon is None):
            icon = icon.url
        else:
            icon = ctx.author.default_avatar.url
        embed.set_footer(icon_url=icon, text=f'{ctx.author} ran a command ran at {str(ctx.message.created_at).rsplit(".")[0] + " GMT"} in the {ctx.message.channel} channel within {ctx.message.guild}.')
        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
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


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
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


    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload: discord.RawMessageDeleteEvent):
        global sniped_messages
        guild = None
        if payload.guild_id is not None:
            guild = await bot.fetch_guild(payload.guild_id)
            sniped_messages[str(guild.id)] = payload
        try:
            print('Full delete log: \n', datetime.now(), payload.guild_id, payload.channel_id, payload.cached_message.author.id, guild.name, (await guild.fetch_channel(payload.channel_id)).name, payload.cached_message.author, payload.cached_message.content, payload.cached_message.author.bot)
            log(('Full delete log: \n', datetime.now(), payload.guild_id, payload.channel_id, payload.cached_message.author.id, guild.name, (await guild.fetch_channel(payload.channel_id)).name, payload.cached_message.author, payload.cached_message.content, payload.cached_message.author.bot), payload.guild_id)
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            if not(payload.cached_message is None):
                print('Direct message delete log: \n', datetime.now(), payload.channel_id, payload.cached_message.author.id,
                          payload.cached_message.channel, payload.cached_message.author, payload.cached_message.content)
            else:
                print('Message delete log error.')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print('Message delete log error.')


class kick_cog(commands.Cog):


    def __init__(self, bot):
        self.bot =bot
    @commands.command(aliases=('remove', 'kick_user', 'kick_member', 'remove_user', 'remove_member'))
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='None'):
        user = await bot.fetch_user(member.id)
        await member.kick(reason=reason)
        await ctx.send(f'''**{ctx.message.author.mention}** kicked **{member.mention}**:
    **{reason}**.''')
        try:
            await user.send(f'''{user.mention} you were kicked from **{ctx.guild}** by **{ctx.author}**:
        **{reason}**''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')


    @commands.command(aliases=('remove_members', 'kick_users', 'remove_users'))
    @commands.has_permissions(kick_members=True)
    async def kick_members(self, ctx, *, member_ids):
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


# @staticmethod
# def can_timeout(ctx):
#     async def predicate(ctx):
#         if ctx.author.guild_permissions.moderate_members or ctx.author.guild_permissions.manage_messages:
#             return False
#         return True
#     return commands.check(predicate)


class mute_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, time: float = 10, *, reason='None'):
        print(member, time, reason)
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


    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: discord.Member, *, reason='None'):
        await member.timeout(duration=None, reason=reason)
        try:
            await member.send(f'''{member.mention} you were taken out of the timeout chair by **{ctx.author}**, because:
    **{reason}**.''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
        await ctx.send(f'''{ctx.author.mention} took {member.mention} out of  the timeout chair, because:
    **{reason}**.''')


class messages_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def snipe(self, ctx):
        global sniped_messages
        try:
            payload = sniped_messages[str(ctx.guild.id)]
        except KeyError:
            await ctx.author.send(
                f'{ctx.author.mention} no deleted messages in **{ctx.guild}** in the current session.')
        else:
            try:
                icon = payload.cached_message.author.avatar
                if not (icon is None):
                    icon = icon.url
                else:
                    icon = payload.cached_message.author.default_avatar.url
                color = payload.cached_message.author.color
                embed = discord.Embed(title=f'Sniped message by {payload.cached_message.author} in {ctx.guild}')
                embed.set_author(icon_url=icon, name=payload.cached_message.author)
                embed.add_field(name='Message', value=payload.cached_message.content, inline=False)
                embed.add_field(name='Extra data',
                                value=f'Message_ID={payload.message_id}, Channel_ID={payload.channel_id}, Guild_ID={payload.guild_id}, User_ID={payload.cached_message.author.id}',
                                inline=False)
                embed.set_footer(
                    text=f'{payload.cached_message.author} sent the message at {str(payload.cached_message.created_at).rsplit(".")[0] + " GMT"} in the {payload.cached_message.channel} channel in {payload.cached_message.guild}.',
                    icon_url=icon)
                await ctx.author.send(embed=embed)
            except (
                    discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                try:
                    await ctx.author.send(f'{ctx.author.mention} could not retrieve the last sent message.')
                except (
                        discord.HTTPException, discord.errors.HTTPException,
                        discord.ext.commands.errors.CommandInvokeError,
                        ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError,
                        discord.Forbidden):
                    await ctx.send(f'{ctx.author.mention} could not retrieve the last sent message.')


    @commands.command(aliases=('delete', 'purge', 'clean'))
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 10, bulk: bool = False):
        await ctx.channel.purge(limit=amount + 1, bulk=bulk)


    @commands.command(aliases=('purge_messages', 'clean_messages', 'delete_messages'))
    @commands.has_permissions(manage_messages=True)
    async def clear_messages(self, ctx, *, message_ids):
        try:
            list(message_ids)
        except ValueError:
            raise ValueError('Invalid list for "member_ids".')
        tup = convert_to_list(message_ids)
        for i in tup:
            print(i)
            message = await ctx.fetch_message(int(i))
            await message.delete()


    @commands.command(aliases=['purgeban'])
    @commands.has_permissions(manage_messages=True)
    async def purge_ban(self, ctx, member: discord.Member, limit: int = 10, bulk: bool = False):
        list_messages = []
        messages = 0
        index = 0
        async for message in (ctx.channel.history(limit=999999999999999999)):
            if messages >= limit or index >= limit * 5:
                if not(bulk):
                    await ctx.send(
                        f"{ctx.author.mention} deleted the last {messages} messages from {member.mention}.")
                elif bulk:
                    await ctx.channel.delete_messages(list_messages)
                    await ctx.send(
                        f"{ctx.author.mention} deleted the last {messages} messages from {member.mention} in bulk.")
                return
            if message.author.id == member.id:
                if not(bulk):
                    messages += 1
                    await message.delete()
                elif bulk:
                    messages += 1
                    list_messages.append(message)
            else:
                continue
            index += 1


class warn_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=('alert', 'notify', 'inform'))
    @commands.has_permissions(view_audit_log=True)
    async def warn(self, ctx, member: discord.Member, *, reason='None'):
        with open('warns.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            dictionary = data[str(ctx.guild.id)]
        except (KeyError, TypeError):
            data[str(ctx.guild.id)] = {"0": 0}
            dictionary = data[str(ctx.guild.id)]
        try:
            dictionary[str(member.id)] += 1
        except KeyError:
            dictionary[str(member.id)] = 1
        data[str(ctx.guild.id)] = dictionary
        with open('warns.json', 'w') as json_f:
            json.dump(data, json_f)
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


    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unwarn(self, ctx, member: discord.Member, count: int = 1):
        count = abs(count)
        with open('warns.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            dictionary = data[str(ctx.guild.id)]
        except (KeyError, TypeError):
            data[str(ctx.guild.id)] = {"0": 0}
            with open('warns.json', 'w') as file:
                json.dump(data, file)
            await ctx.send(f'{ctx.author.mention} there are no warns in this server.')
            return
        try:
            dictionary[str(member.id)] -= count
        except (KeyError, TypeError):
            with open('warns.json', 'w') as file:
                json.dump(data, file)
            await ctx.send(f'{ctx.author.mention} there are no warns in this server for {member.mention}.')
            return
        if dictionary[str(member.id)] <= 0:
            del dictionary[str(member.id)]
        data[str(ctx.guild.id)] = dictionary
        with open('warns.json', 'w') as file:
            json.dump(data, file)
        await ctx.send(f'{ctx.author.mention} {member.mention} has been unwarned **{count}** times.')


    @commands.command(aliases=('get_warns', 'pull_warns', 'warns'))
    @commands.has_permissions(view_audit_log=True)
    async def fetch_warns(self, ctx, member: discord.Member = None):
        with open('warns.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            dictionary = data[str(ctx.guild.id)]
        except (KeyError, TypeError):
            await ctx.send(f'{ctx.author.mention} no warns from this server.')
            return
        else:
            if member is None:
                for member in dictionary.keys():
                    try:
                        with open('Warns.txt', 'w') as file:
                            file.writelines(
                                f'{(await ctx.guild.fetch_member(int(member)))} has {dictionary[str(member)]} warns.')
                    except (
                            discord.HTTPException, discord.errors.HTTPException,
                            discord.ext.commands.errors.CommandInvokeError,
                            ValueError,
                            commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                        print(f'Cannot fetch {member}')
                file = discord.File(
                    r'./Warns.txt')
                await ctx.author.send(
                    content=f'{ctx.author.mention} warns from current bot session in **{ctx.guild}**:', file=file)
            else:
                try:
                    await ctx.send(
                        f'{ctx.author.mention}, {member.mention} has **{dictionary[str(member.id)]}** warns.')
                except KeyError:
                    await ctx.send(f'{ctx.author.mention} there are no warns in this server for  {member.mention}.')


class hush_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=('silence', 'mute_channel', 'silence_channel'))
    @commands.has_permissions(moderate_members=True)
    async def hush(self, ctx, time: float = 5, *, reason: str = 'None'):
        channel = ctx.channel
        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            ctx.channel = ctx.author.voice.channel
        try:
            if ((ctx.channel.overwrites_for(ctx.guild.default_role)).view_channel and (ctx.channel.overwrites_for(ctx.guild.default_role)).send_messages and isinstance(ctx.channel, discord.TextChannel)) or ((ctx.channel.overwrites_for(ctx.guild.default_role)).connect and (((ctx.channel.overwrites_for(ctx.guild.default_role)).speak or (ctx.channel.overwrites_for(ctx.guild.default_role)).stream) and isinstance(ctx.channel, discord.VoiceChannel))):
                pass
            else:
                return
        except KeyError:
            pass
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        overwrite.send_messages_in_threads = False
        overwrite.read_message_history = True
        overwrite.create_public_threads = False
        overwrite.create_private_threads = False
        overwrite.add_reactions = True
        overwrite.connect = False
        overwrite.speak = False
        overwrite.stream = False
        overwrite.external_emojis = False
        overwrite.external_stickers = False
        overwrite.embed_links = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
        await channel.send(f'''{ctx.author.mention} has hushed the channel for **{time}** minutes because:
    **{reason}**''')
        await asyncio.sleep(time * 60)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        overwrite.send_messages_in_threads = True
        overwrite.read_message_history = True
        overwrite.create_public_threads = True
        overwrite.create_private_threads = False
        overwrite.add_reactions = True
        overwrite.connect = True
        overwrite.speak = True
        overwrite.stream = True
        try:
            if (not(
            (ctx.channel.overwrites_for(ctx.guild.default_role)).send_messages) and (ctx.channel.overwrites_for(ctx.guild.default_role)).view_channel and isinstance(ctx.channel, discord.TextChannel)) or (not(
            (ctx.channel.overwrites_for(ctx.guild.default_role)).connect) and isinstance(ctx.channel, discord.VoiceChannel)):
                pass
            else:
                return
        except KeyError:
            pass
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await channel.send(f'{ctx.author.mention}, channel has been unhushed.')


    @commands.command(aliases=('un_silence', 'unmute_channel', 'un_silence_channel', 'unhush'))
    @commands.has_permissions(moderate_members=True)
    async def un_hush(self, ctx, *, reason: str = 'None'):
        channel = ctx.channel
        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            ctx.channel = ctx.author.voice.channel
        try:
            if (((ctx.channel.overwrites_for(ctx.guild.default_role)).view_channel) and not((ctx.channel.overwrites_for(ctx.guild.default_role)).send_messages) and isinstance(ctx.channel, discord.TextChannel)) or (not((ctx.channel.overwrites_for(ctx.guild.default_role)).connect) and isinstance(ctx.channel, discord.VoiceChannel)):
                pass
            else:
                return
        except KeyError:
            return
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        overwrite.send_messages_in_threads = True
        overwrite.read_message_history = True
        overwrite.create_public_threads = True
        overwrite.create_private_threads = False
        overwrite.add_reactions = True
        overwrite.connect = True
        overwrite.speak = True
        overwrite.stream = True
        overwrite.external_emojis = False
        overwrite.external_stickers = False
        overwrite.embed_links = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
        await channel.send(f'''{ctx.author.mention} has unhushed the channel because:
    **{reason}**''')


    @commands.command(aliases=['unhide'])
    @commands.has_permissions(moderate_members=True)
    async def un_hide(self, ctx, *, reason: str = 'None'):
        channel = ctx.channel
        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            ctx.channel = ctx.author.voice.channel
        try:
            if (not((ctx.channel.overwrites_for(ctx.guild.default_role)).view_channel)) or (not((ctx.channel.overwrites_for(ctx.guild.default_role)).connect) and isinstance(ctx.channel, discord.VoiceChannel)):
                pass
            else:
                return
        except KeyError:
            return
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = True
        overwrite.connect = True
        overwrite.send_messages = True
        overwrite.speak = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
        await channel.send(f'''{ctx.author.mention} has unhidden the channel because:
    **{reason}**''')


    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def hide(self, ctx, time: float = 5, *, reason: str = 'None'):
        channel = ctx.channel
        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            ctx.channel = ctx.author.voice.channel
        try:
            if ((ctx.channel.overwrites_for(ctx.guild.default_role)).view_channel) or (((ctx.channel.overwrites_for(ctx.guild.default_role)).connect and isinstance(ctx.channel, discord.VoiceChannel))):
                pass
            else:
                return
        except KeyError:
            pass
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        overwrite.connect = False
        overwrite.send_messages = False
        overwrite.speak = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
        await channel.send(f'''{ctx.author.mention} has hidden the channel for **{time}** minutes because:
    **{reason}**''')
        await asyncio.sleep(time * 60)
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = True
        overwrite.connect = True
        overwrite.send_messages = True
        overwrite.speak = True
        try:
            if (not((ctx.channel.overwrites_for(ctx.guild.default_role)).view_channel)) or (not((ctx.channel.overwrites_for(ctx.guild.default_role)).connect) and isinstance(ctx.channel, discord.VoiceChannel)):
                pass
            else:
                return
        except KeyError:
            pass
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await channel.send(f'{ctx.author.mention}, channel has been unhidden.')


class server_lock_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=('unhide_guild', 'unhideserver', 'unhideguild', 'server_unhide', 'server_un_hide', 'serverunhide', 'guild_un_hide', 'guild_unhide', 'guildunhide'))
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def unhide_server(self, ctx, time: float = 5, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = True
        overwrite.send_messages = True
        overwrite.connect = True
        overwrite.speak = True
        for channel in ctx.guild.channels:
            try:
                if not (channel.overwrites_for(ctx.guild.default_role).view_channel) or (
                        not (channel.overwrites_for(ctx.guild.default_role).connect) and isinstance(channel,
                                                                                                    discord.VoiceChannel)):
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unhidden.')


    @commands.command(aliases=('hide_guild', 'hideserver', 'hideguild', 'guildhide', 'serverhide', 'guild_hide', 'server_hide'))
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def hide_server(self, ctx, time: float = 5, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        overwrite.send_messages = False
        overwrite.connect = False
        overwrite.speak = False
        for channel in ctx.guild.channels:
            try:
                if (channel.overwrites_for(ctx.guild.default_role).view_channel) or (channel.overwrites_for(ctx.guild.default_role).connect and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
                else:
                    continue
            except KeyError:
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
        await ctx.send(f'''{ctx.author.mention} has hidden the server for **{time}** minutes because:
**{reason}**''')
        await asyncio.sleep(time * 60)
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = True
        overwrite.send_messages = True
        overwrite.connect = True
        overwrite.speak = True
        for channel in ctx.guild.channels:
            try:
                if not(channel.overwrites_for(ctx.guild.default_role).view_channel) or (not(channel.overwrites_for(ctx.guild.default_role).connect) and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unhidden.')


    @commands.command(aliases=('server_lockdown', 'lock', 'server_lock', 'server_hush'))
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def lockdown(self, ctx, time: float = 5, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True
        overwrite.send_messages_in_threads = False
        overwrite.read_message_history = True
        overwrite.create_public_threads = False
        overwrite.create_private_threads = False
        overwrite.add_reactions = True
        overwrite.connect = False
        overwrite.speak = False
        overwrite.stream = False
        overwrite.external_emojis = False
        overwrite.external_stickers = False
        overwrite.embed_links = False
        for channel in ctx.guild.channels:
            try:
                if (channel.overwrites_for(ctx.guild.default_role)).view_channel and (
                channel.overwrites_for(ctx.guild.default_role)).send_messages and isinstance(channel,
                                                                                                 discord.TextChannel) or (
                channel.overwrites_for(ctx.guild.default_role)).connect and (((channel.overwrites_for(
                        ctx.guild.default_role)).speak or (channel.overwrites_for(
                        ctx.guild.default_role)).stream) and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
                else:
                    continue
            except KeyError:
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=reason)
        await ctx.send(f'''{ctx.author.mention} has locked the server for **{time}** minutes because:
**{reason}**''')
        await asyncio.sleep(time * 60)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        overwrite.send_messages_in_threads = True
        overwrite.read_message_history = True
        overwrite.create_public_threads = True
        overwrite.create_private_threads = False
        overwrite.add_reactions = True
        overwrite.connect = True
        overwrite.speak = True
        overwrite.stream = True
        overwrite.external_emojis = False
        overwrite.external_stickers = False
        overwrite.embed_links = False
        for channel in ctx.guild.channels:
            try:
                if (((channel.overwrites_for(ctx.guild.default_role)).view_channel) and not (
                (channel.overwrites_for(ctx.guild.default_role)).send_messages) and isinstance(channel,
                                                                                                   discord.TextChannel)) or (
                        not ((channel.overwrites_for(ctx.guild.default_role)).connect) and isinstance(channel,
                                                                                                          discord.VoiceChannel)):
                    pass
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unlocked.')


    @commands.command(aliases=('server_unlock', 'server_unhush', 'server_un_hush'))
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def unlock(self, ctx, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True
        overwrite.send_messages_in_threads = True
        overwrite.read_message_history = True
        overwrite.create_public_threads = True
        overwrite.create_private_threads = False
        overwrite.add_reactions = True
        overwrite.connect = True
        overwrite.speak = True
        overwrite.stream = True
        overwrite.external_emojis = False
        overwrite.external_stickers = False
        overwrite.embed_links = False
        for channel in ctx.guild.channels:
            try:
                if (((channel.overwrites_for(ctx.guild.default_role)).view_channel) and not (
                (channel.overwrites_for(ctx.guild.default_role)).send_messages) and isinstance(channel,
                                                                                                   discord.TextChannel)) or (
                        not ((channel.overwrites_for(ctx.guild.default_role)).connect) and isinstance(channel,
                                                                                                          discord.VoiceChannel)):
                    pass
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unlocked.')


class ban_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=('ban_users', 'ban_people'))
    @commands.has_permissions(ban_members=True)
    async def ban_members(self, ctx, *, member_ids):
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
                await user.send(f'''{user.mention} you were banned from **{ctx.guild}** by **{ctx.author}**!''')
            except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {user}.')
        await ctx.send(f'{ctx.author.mention} banned members.')


    @commands.command(aliases=('unban_users', 'unban_people'))
    @commands.has_permissions(ban_members=True)
    async def unban_members(self, ctx, *, user_ids):
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


    @commands.command(aliases=('ban_user', 'ban_member'))
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='None'):
        await member.ban(reason=reason)
        await ctx.send(f'''**{ctx.message.author.mention}** banned **{member.mention}**:
    **{reason}**.''')
        try:
            await member.send(f'''{member.mention} you were banned from **{ctx.guild}** by **{ctx.author}**:
    **{reason}**''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User, *, reason: str = 'None'):
        await ctx.guild.unban(user=user, reason=reason)
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


class help_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=('get_docs', 'pull_docs'))
    async def fetch_docs(self, ctx):
        await ctx.send('https://pastebin.com/9w4Fp110')


    @commands.command(aliases=('get_code', 'pull_code'))
    async def fetch_code(self, ctx):
        await ctx.send('https://github.com/HRLO77/Bot-source-code')


class fetch_data_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=('server_info', 'guild', 'guild_info', 'serverinfo', 'guildinfo'))
    async def server(self, ctx):
        embed = discord.Embed(title=f'Server info')
        icon = ctx.guild.icon.url
        embed.color= ctx.author.color
        embed.set_author(icon_url=icon, name=ctx.guild)
        icon = ctx.guild.owner.avatar
        if icon is None:
            icon = ctx.guild.owner.default_avatar.url
        else:
            icon = icon.url
        embed.set_footer(icon_url=icon, text=f'Created on {str(ctx.guild.created_at).rsplit(" ")[0]} by {ctx.guild.owner}.')
        embed.add_field(name=f'Members', value=f'**{len(ctx.guild.members)}** members.')
        embed.add_field(name='Roles', value=f'**{len(ctx.guild.roles)}** roles.')
        embed.add_field(name='Channels', value=f'**{len(ctx.guild.channels)}** channels.')
        embed.add_field(name='Threads', value=f'**{len(await ctx.guild.active_threads())}** active threads.')
        data = len((await ctx.guild.bans()))
        if  data > 9999:
            data = '10000+'
        embed.add_field(name='Bans', value=f'**{data}** ban entries.')
        data = len(await (ctx.guild.audit_logs(limit=None)).flatten())
        if data > 9999:
            data = '9999+'
        embed.add_field(name='Moderation actions', value=f'**{data}** actions.')
        embed.add_field(name='Premium', value=f'**{len(ctx.guild.premium_subscribers)}** server boosters.\n**{ctx.guild.premium_subscription_count}** boosts.\nBoost level **{ctx.guild.premium_tier}**.')
        await ctx.message.reply(embed=embed)
      
        
    @commands.command(aliases=('get_member_history', 'pull_member_history'))
    async def fetch_member_history(self, ctx, member: discord.Member, limit: int = 10, links=False):
        try:
            bool(links)
        except ValueError:
            raise ValueError('Invalid boolean for "links".')
        member = await ctx.guild.fetch_member(memberid)
        messages = []
        count = 0
        async for message in (ctx.channel.history(limit=99999999999999999)):
            if count >= limit:
                embed = discord.Embed(title=f'Last {limit} messages from {member}.')
                embed.description = f'{messages}'
                await ctx.send(embed=embed)
                return
            if message.author == member:
                count += 1
                if links:
                    messages.append(f'https://discord.com/channels/{ctx.guild.id}/{message.channel.id}/{message.id}')
                else:
                    messages.append(message.id)


    @commands.command(aliases=('get_message', 'pull_message'))
    async def fetch_message(self, ctx, message_id: discord.Message):
        await ctx.send(f'https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message_id}')


    @commands.command(aliases=('bm', 'mark', 'book'))
    async def bookmark(self, ctx, message_id: int = -1):
        if message_id == -1:
            message_id = int(ctx.message.reference.message_id)
        message = await ctx.fetch_message(message_id)
        icon = message.author.avatar
        if not (icon is None):
            icon = icon.url
        else:
            icon = message.author.default_avatar.url
        color = message.author.color
        try:
            embed = discord.Embed(
                title=f'You bookmarked a message in {message.guild}')
            embed.description = ctx.author.mention
            embed.color = message.author.color
            embed.set_author(name=message.author,
                             icon_url=icon)
            embed.add_field(name='Bookmarked message', value=message.content, inline=False)
            embed.add_field(name='Original message',
                            value=f'[Original message]({message.jump_url})', inline=False)
            embed.set_footer(icon_url=icon,
                             text=f'Bookmarked message sent at {str(message.created_at).rsplit(".")[0] + " GMT"} in the {message.channel} channel within {message.guild} by {message.author}.')
            await ctx.author.send(embed=embed)
        except (
                discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                ValueError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            if len(message.embeds) == 1:
                embed = discord.Embed(
                    title=f'You bookmarked a message in {message.guild}')
                embed.description = ctx.author.mention
                embed.color = message.author.color
                embed.set_author(name=message.author,
                                 icon_url=icon)
                embed.add_field(name='Bookmarked message', value=(message.embeds[0]).description, inline=False)
                embed.add_field(name='Original message',
                                value=f'[Original message]({message.jump_url})', inline=False)
                embed.set_footer(icon_url=icon,
                                 text=f'Bookmarked message sent at {str(message.created_at).rsplit(".")[0] + " GMT"} in the {message.channel} channel within {message.guild} by {message.author}.')
                await ctx.author.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=f'You bookmarked a message in {message.guild}')
                embed.color = message.author.color
                embed.set_author(name=message.author,
                                 icon_url=icon)
                embed.description = ctx.author.mention
                embed.set_image(url=message.attachments[0].url)
                print(message.content)
                if len(message.content) > 0:
                    embed.add_field(name="Bookmarked message", value=f'{message.content}', inline=False)
                embed.add_field(name='Original message',
                                value=f'[Original message]({message.jump_url})', inline=False)
                embed.set_footer(icon_url=icon,
                                 text=f'Bookmarked message sent at {str(message.created_at).rsplit(".")[0] + " GMT"} in the {message.channel} channel within {message.guild} by {message.author}.')
                await ctx.author.send(embed=embed)
        except (
                discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                ValueError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            embed = discord.Embed(
                title=f'You bookmarked a message in {message.guild}')
            embed.color = message.author.color
            embed.set_author(name=message.author,
                             icon_url=icon)
            embed.add_field(name="Error", value=f'{ctx.author.mention} an error occurred while fetching the message.',
                            inline=False)
            embed.add_field(name='Original message',
                            value=f'[Original message]({message.jump_url})', inline=False)
            embed.set_footer(icon_url=icon,
                             text=f'Bookmarked message sent at {str(message.created_at).rsplit(".")[0] + " GMT"} in the {message.channel} channel within {message.guild} by {message.author}.')
            await ctx.author.send(embed=embed)
        except (
                discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                ValueError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            await ctx.send(f'Cannot direct message {ctx.author.mention}.')
            print(f'Cannot direct message {ctx.author}.')



    @commands.command(aliases=('channel_member_count', 'channel_member#'))
    async def channel_members(self, ctx):
        await ctx.send(f'{len(ctx.message.channel.members)} members are in the channel.')


    @commands.command(aliases=('members', 'member#'))
    async def member_count(self, ctx):
        await ctx.send(f'{ctx.guild.member_count} members are in the guild.')


    @commands.command(aliases=('get_member', 'pull_member', 'member', 'info', 'info_on', 'member_info', 'member_data'))
    async def fetch_member(self, ctx, member: discord.Member):
        def is_author(payload: discord.RawReactionActionEvent):
            return (payload.guild_id is None) and ('👋' in str(payload.emoji)) and (payload.user_id == ctx.author.id)
        icon = member.guild_avatar
        if not(icon is None):
            icon = icon.url
        else:
            if not(member.avatar is None):
                icon = member.avatar.url
            else:
                icon = member.default_avatar.url
            embed = discord.Embed(title=f'Info on {member} in {ctx.guild}')
        if not(member.public_flags.system):
            embed.description = f'{member.mention}{int((member.bot or member.public_flags.verified_bot)) * " is a bot user"}.'
        else:
            embed.description = f'{member.mention}{int((member.public_flags.system)) * " is a system user"}.'
        embed.color = member.color
        embed.add_field(name='Status', value=str(member.status).capitalize() + f'{int(member.is_on_mobile()) * " on mobile"}. \n {int(not(member.activity is None)) * str("*" + str(member.activity) + "*")}.')
        if member.nick is None:
            embed.set_author(name=f'{member}', icon_url=icon)
        else:
            embed.set_author(name=f'{member} A.K.A {member.nick}', icon_url=icon)
        embed.add_field(name='Roles', value=f'Has **{len(member.roles)}** roles, highest role is **{member.top_role}**.')
        embed.add_field(name='Verified', value=not member.pending)
        if not(member.premium_since is None):
            embed.add_field(name='Premium since', value=f'Subscribed since **{str(member.premium_since).rsplit(" ")[0]}**')
        if ctx.guild.owner_id != member.id:
            embed.set_footer(icon_url=icon, text=f'Joined {ctx.guild} on {str(member.joined_at).rsplit(" ")[0]}, account created on {str(member.created_at).rsplit(" ")[0] + " GMT"}.')
        else:
            embed.set_footer(icon_url=icon, text=f'Created {ctx.guild} on {str(ctx.guild.created_at).rsplit(" ")[0] + " GMT"}, account created on {str(member.created_at).rsplit(" ")[0] + " GMT"}.')
        if not(member.current_timeout is None):
            embed.add_field(name='Timeout ends at', value=f'{str(member.current_timeout).rsplit(".")[0]}.')
        else:
            permissions = list()
            for key, value in member.guild_permissions:
                if value:
                    permissions.append(key)
            perms = []
            for i in permissions[-1: -0: -1]:
                if len(str(i)) < 20:
                    perms.insert(0, i)
            embed.add_field(name='Permissions', value=f'*{", ".join(perms[-1: -5: -1]).capitalize()}* and **{len(permissions) - 4}** more.')
        flags = member.public_flags.all()
        if 'hype' in str(flags).lower():
            if 'bravery' in str(flags).lower():
                embed.add_field(name='Hypesquad', value=f'Hypesquad **bravery**.', inline=True)
            elif 'brilliance' in str(flags).lower():
                embed.add_field(name='Hypesquad', value=f'Hypesquad **brilliance**.', inline=True)
            elif 'balance' in str(flags).lower():
                embed.add_field(name='Hypesquad', value=f'Hypesquad **balance**.', inline=True)
        embed.add_field(name='Guilds', value=f'Shares **{len(member.mutual_guilds)}** guild{(len(member.mutual_guilds) != 1) * "s"} with me.')
        dm = await member.create_dm()
        embed.add_field(name='Extra',
                        value=f'Hash: {hash(member)}\nID: {member.id}\nColor: {member.color}\n{int(member.public_flags.early_supporter) * "Early supporter"}\n{int(member.public_flags.verified_bot_developer) * "Verified developer"}\n{int(member.public_flags.partner) * "Discord partner"} \n{int(member.public_flags.discord_certified_moderator) * "Certified moderator"}\n{int(not (member.public_flags.bug_hunter_level_2) and member.public_flags.bug_hunter) * "Level 1 bug hunter"}\n{int(member.public_flags.bug_hunter_level_2) * "Level 2 bug hunter"}\n{int(member.public_flags.staff and not (member.public_flags.partner)) * "Discord employee"}\n{int(member.public_flags.spammer) * "**Careful**, this user has been reported to discord for **spamming**"}')
        context = await ctx.author.send(content=f'React to this message with :wave: to say hi to {member}!', embed=embed)
        await context.add_reaction('👋')
        try:
            await self.bot.wait_for('raw_reaction_add', timeout=60, check=is_author)
        except asyncio.exceptions.TimeoutError:
            await context.remove_reaction(emoji='👋', member=self.bot.user)
            return
        else:
            await context.remove_reaction(emoji='👋', member=self.bot.user)
            try:
                await dm.send(f'{ctx.author.mention} said hi from **{ctx.guild}**!')
                await dm.send(f':wave:')
            except (
                        discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                        ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                await ctx.author.send(f'{ctx.author.mention} failed to send message to {member.mention}.')
            else:
                await ctx.author.send(f'{ctx.author.mention} successfully sent the message!')


    @commands.command(aliases=('get_user', 'pull_user', 'user', 'user_info', 'info_on_user', 'user_data'))
    async def fetch_user(self, ctx, User: discord.User):
        def is_author(payload: discord.RawReactionActionEvent):
            return (payload.guild_id is None) and ('👋' in str(payload.emoji)) and (payload.user_id == ctx.author.id)
        icon = User.avatar
        if not(icon is None):
            icon = icon.url
        else:
            icon = User.default_avatar.url
        embed = discord.Embed(title=f'Info on {User}')
        embed.description = f'{User.mention}{int(User.bot) * " is a bot user."}'
        embed.color = User.color
        embed.set_author(name=f'{User}', icon_url=icon)
        embed.set_footer(icon_url=icon, text=f'Account created on {str(User.created_at).rsplit(" ")[0] + " GMT"}.')
        flags = User.public_flags.all()
        if 'hype' in str(flags).lower():
            if 'bravery' in str(flags).lower():
                embed.add_field(name='Hypesquad', value=f'Hypesquad **bravery**.', inline=True)
            elif 'brilliance' in str(flags).lower():
                embed.add_field(name='Hypesquad', value=f'Hypesquad **brilliance**.', inline=True)
            elif 'balance' in str(flags).lower():
                embed.add_field(name='Hypesquad', value=f'Hypesquad **balance**.', inline=True)
        embed.add_field(name='Guilds', value=f'Shares **{len(User.mutual_guilds)}** guild{(len(User.mutual_guilds) != 1) * "s"} with me.')
        dm = await User.create_dm()
        embed.add_field(name='Extra', value=f'Hash: {hash(User)}\nID: {User.id}\nColor: {User.color}\n{int(User.public_flags.early_supporter) * "Early supporter"}\n{int(User.public_flags.verified_bot_developer) * "Verified developer"}\n{int(User.public_flags.partner) * "Discord partner"} \n{int(User.public_flags.discord_certified_moderator) * "Certified moderator"}\n{int(not(User.public_flags.bug_hunter_level_2) and User.public_flags.bug_hunter) * "Level 1 bug hunter"}\n{int(User.public_flags.bug_hunter_level_2) * "Level 2 bug hunter"}\n{int(User.public_flags.staff and not(User.public_flags.partner)) * "Discord employee"}\n{int(User.public_flags.spammer) * "**Careful**, this user has been reported to discord for **spamming**"}')
        context = await ctx.author.send(content=f'React to this message with :wave: to say hi to {User}!', embed=embed)
        await context.add_reaction('👋')
        try:
            await self.bot.wait_for('raw_reaction_add', timeout=60, check=is_author)
        except asyncio.exceptions.TimeoutError:
            await context.remove_reaction(emoji='👋', member=self.bot.user)
            return
        else:
            await context.remove_reaction(emoji='👋', member=self.bot.user)
            try:
                await dm.send(f'{ctx.author.mention} said hi from **{ctx.guild}**!')
                await dm.send(f':wave:')
            except (
                        discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                        ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                await ctx.author.send(f'{ctx.author.mention} failed to send message to {User.mention}.')
            else:
                await ctx.author.send(f'{ctx.author.mention} successfully sent the message!')


class owner_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=('terminate_bot', 'kill_bot', 'cut_bot'))
    @commands.is_owner()
    async def close_bot(self, ctx):
        await ctx.send('Bot terminating...')
        await bot.close()


    @commands.command()
    @commands.is_owner()
    async def restart_bot(self, ctx):
        await ctx.send(f'Reloading bot...')
        remove_cogs()
        await asyncio.sleep(2)
        add_cogs()


    @commands.command(aliases=('e', 'eval'))
    @commands.is_owner()
    async def evaluate(self, ctx, *, command):
        f = open('compile_user_code.py', 'w')
        f = f.writelines(str(command).strip('`').strip('python').strip('py'))
        result = subprocess.run([sys.executable, "-c", f"{str(command).strip('`').strip('python').strip('py')}"],
                                input=f,
                                capture_output=True, text=True, timeout=5)
        if len(result.stdout) > 45:
            o = open('out.txt', 'w')
            o = o.writelines(str(result.stdout))
            file = discord.File(
                r'./out.txt')
            await ctx.send(content='Program output too long, full output in text document:', file=file)
            o = ''
            return
        f = ''
        await ctx.send(f'''{ctx.author.mention} Your code has finished with a return code of **{result.returncode}**:
    ```
    {result.stderr}
    {result.stdout}
    ```''')


class print_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def print_out(self, ctx, *, message):
        member = await ctx.guild.fetch_member(ctx.message.author.id)
        new_message = await ctx.message.channel.send(message)
        await member.send(
            f'{member.mention} you printed out a message in https://discord.com/channels/{ctx.guild.id}/{ctx.message.channel.id}/{new_message.id}.')
        await ctx.message.delete()


    @commands.command()
    async def print_embed(self, ctx, title: str, *, text: str):
        icon = ctx.author.avatar
        if not(icon is None):
            icon = icon.url
        else:
            icon = ctx.author.default_avatar.url
        color = ctx.author.color
        embed = discord.Embed(title=title, description=text, color=color)
        embed.set_author(name=ctx.author, icon_url=icon)
        embed.set_footer(icon_url=icon, text=f'Message sent by {ctx.author} at {str(ctx.message.created_at).rsplit(".")[0] + " GMT"} in the {ctx.message.channel} channel in {ctx.guild}.')
        if 'rule' in title.lower():
            with open('dates.json', 'r') as json_file:
                data = json.load(json_file)
        data[str(ctx.guild.id)] = text
        print(data)
        with open('dates.json', 'w') as json_file:
            json.dump(data, json_file)
        await ctx.send(embed=embed)
        await ctx.message.delete()

@bot.command(aliases=('call', 'request'))
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)} ms.')


class reacting_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=('update_react', 'add_react'))
    @commands.has_permissions(manage_messages=True, manage_emojis=True)
    async def set_react(self, ctx, reacting_message_id: int, default_role_id: int, emoji_to_react: str):
        reacting[(ctx.guild.id, reacting_message_id)] = (
            default_role_id, emoji_to_react)
        await ctx.send(
            f'{ctx.author.mention} updated reacting object index: **{(ctx.guild.id, reacting_message_id)}:{(default_role_id, emoji_to_react)}**')


    @commands.command(aliases=('delete_react', 'rm_react', 'del_react'))
    @commands.has_permissions(manage_messages=True, manage_emojis=True)
    async def remove_react(self, ctx, reacting_message_id: int):
        del reacting[(ctx.guild.id, reacting_message_id)]
        await ctx.send(f'{ctx.author.mention} deleted reacting object index: **{(ctx.guild.id, reacting_message_id)}**')


    @commands.command(aliases=('react_obj', 'react_object', 'react_dictionary'))
    async def react_dict(self, ctx, message_id: discord.Message = None):
        if message_id is None:
            await ctx.send(f"Reacting dictionary for RawReactionActionEvent - **{reacting}**")
        else:
            await ctx.send(f"Reacting dictionary for message {message_id.id} - **{'({0},{1}): {2}'.format(ctx.guild.id, message_id.id, reacting[(ctx.guild.id, message_id.id)])}**")


class filters_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=('rm_swear', 'delete_swear', 'remove_swear'))
    @commands.has_permissions(moderate_members=True)
    async def del_swear(self, ctx, *, string: str):
        if content == 0:
            await ctx.message.delete()
            raise IndexError(f"Explicit data check is currently disabled.")
        elif content == 1:
            if string in explicit_data2:
                explicit_data2.remove(string)
            else:
                await ctx.message.delete()
                raise IndexError(
                    f"Explicit_data2 does not contain {string} as a value.")
        elif content == 2:
            if string in explicit_data3:
                explicit_data3.remove(string)
            else:
                await ctx.message.delete()
                raise IndexError(
                    f"Explicit_data3 does not contain {string} as a value.")
        elif content == 3:
            if string in explicit_data4:
                explicit_data4.remove(string)
            else:
                await ctx.message.delete()
                raise IndexError(
                    f"Explicit_data4 does not contain {string} as a value.")
        elif content == 4:
            if string in explicit_data5:
                explicit_data5.remove(string)
            else:
                await ctx.message.delete()
                raise IndexError(
                    f"Explicit_data5 does not contain {string} as a value.")
        await ctx.send(f"{ctx.author.mention} swear was removed from the filter.")
        await ctx.message.delete()


    @commands.command(aliases=['append_swear'])
    @commands.has_permissions(moderate_members=True)
    async def add_swear(self, ctx, *, string: str):
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


    @commands.command(aliases=['append_enhanced_swears'])
    @commands.has_permissions(moderate_members=True)
    async def add_enhanced_swears(self, ctx, *, swears):
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
                    dat = Functions.str_to_list(
                        Functions.list_to_str(Functions.spliceOutWords(str(i))))
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
        await ctx.send(f'{ctx.author.mention}, swears was added to the filter.')
        await ctx.message.delete()


    @commands.command(aliases=['append_extra_enhanced_swears'])
    @commands.has_permissions(moderate_members=True)
    async def add_extra_enhanced_swears(self, ctx, *, swears):
        try:
            list(swears)
        except ValueError:
            raise ValueError('Invalid list for "swears"')
        test = []
        set = convert_to_list(swears)
        print(set)
        cache = []
        list = []
        set = {}
        for i in set:
            for index, value in enumerate(str(i).replace(' ', '')):
                if ' ' in i:
                    dat = Functions.str_to_list(
                        Functions.list_to_str(Functions.spliceOutWords(str(i))))
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
                    moveable_cache[random.randint(0, len(i) - 1)] = '*'
                    if check(moveable_cache):
                        list.append(Functions.list_to_str(moveable_cache))
                    else:
                        continue
                    if content == 0:
                        await ctx.send('Explicit data check is currently disabled.')
                    elif content == 1:
                        explicit_data2.add(Functions.list_to_str(dat))
                        explicit_data2.add(i)
                        explicit_data2.add(Functions.list_to_str(moveable_cache))
                    elif content == 2:
                        explicit_data3.add(Functions.list_to_str(dat))
                        explicit_data3.add(i)
                        explicit_data3.add(Functions.list_to_str(moveable_cache))
                    elif content == 3:
                        explicit_data4.add(Functions.list_to_str(dat))
                        explicit_data4.add(i)
                        explicit_data4.add(Functions.list_to_str(moveable_cache))
                    elif content == 4:
                        explicit_data5.add(Functions.list_to_str(dat))
                        explicit_data5.add(i)
                        explicit_data5.add(Functions.list_to_str(moveable_cache))
        await ctx.send(f'{ctx.author.mention}, swears was added to the filter.')
        await ctx.message.delete()

        @commands.command(aliases=('spam_filter', 'spam'))
        @commands.has_permissions(manage_messages=True, moderate_members=True)
        async def spam_check(self, ctx, value):
            global filtering
            try:
                filtering[str(ctx.guild.id)]
            except KeyError:
                filtering[str(ctx.guild.id)] = (1, 1)
            if int(value) and int('-1') < int(value) < 5 or int(value) == 0:
                filtering[str(ctx.guild.id)] = (int(value), (filtering[str(ctx.guild.id)])[1])
            else:
                raise ValueError('Invalid value for "spam_check".')
            await ctx.send(f'Spam filter level has been set to {value}.')

        @commands.command(aliases=('content_filter', 'content', 'swear_check', 'profanity_filter', 'profanity_check'))
        @commands.has_permissions(manage_messages=True, moderate_members=True)
        async def content_check(self, ctx, value):
            global filtering
            try:
                filtering[str(ctx.guild.id)]
            except KeyError:
                filtering[str(ctx.guild.id)] = (1, 1)
            if int(value) and int('-1') < int(value) < 5 or int(value) == 0:
                filtering[str(ctx.guild.id)] = ((filtering[str(ctx.guild.id)])[0], int(value))
            else:
                raise ValueError('Invalid value for "content_check".')
            await ctx.send(f'Content filter level has been set to {value}.')


class channels_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def create_text_channel(self, ctx, name, *, reason='None'):
        await ctx.guild.create_text_channel(name=name, reason=reason)
        await ctx.send(f"{ctx.author.mention} create a text channel {name}.")


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def create_vc(self, ctx, name, *, reason='None'):
        await ctx.guild.create_voice_channel(name=name, reason=reason)
        await ctx.send(f"{ctx.author.mention} create a vc {name}.")


    @commands.command(aliases=('get_channels', 'pull_channels'))
    async def fetch_channels(self, ctx, links=False):
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


    @commands.command(aliases=('remove_channels', 'end_channels'))
    @commands.has_permissions(manage_channels=True)
    async def delete_channels(self, ctx, *, channels):
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


    @commands.command(aliases=('channel_clear', 'channel_clean'))
    @commands.has_permissions(manage_channels=True)
    async def channel_purge(self, ctx, channel: discord.GroupChannel = None, *, reason='None'):
        if channel is None:
            channel = ctx.channel
        channel = ctx.channel
        new_channel = await channel.clone(name=channel.name, reason=reason)
        await channel.delete()


    @commands.command(aliases=('channel_del', 'channel_remove', 'channel_rm'))
    @commands.has_permissions(manage_channels=True)
    async def channel_delete(self, ctx, channel: discord.GroupChannel = None, *, reason='None'):
        if channel is None:
            channel = ctx.channel
        await channel.delete()


class roles_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, name, *, reason='None'):
        await ctx.guild.create_role(name=name, reason=reason)
        await ctx.send(f"{ctx.author.mention} created role {name}.")


    @commands.command(aliases=('del_role', 'rm_role', 'remove_role'))
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, role: discord.Role, *, reason='None'):
        await ctx.send(f'{ctx.author.mention} deleted role {role.name}.')
        await role.delete(reason=reason)


    #   overwrite = discord.PermissionOverwrite()
    #   overwrite.send_messages = True
    #   overwrite.read_messages = True
    #   await ctx.message.channel.set_permissions(member/role, overwrite=overwrite)


    @commands.command(aliases=('add_role', 'append_role'))
    @commands.has_permissions(manage_roles=True)
    async def push_role(self, ctx, role: discord.Role, *, member_ids='all'):
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
                    await member.add_roles(role)
                except (
                        discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                        ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                    print(
                        f'An error occurred while pushing role {role.name} onto {str(member)}.')
                    pass
            await ctx.send(f'{ctx.author.mention} pushed **{role.name}** onto members.')
            return
        for i in ctx.guild.members:
            try:
                await i.add_roles(role)
            except (
                    discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    ValueError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(
                    f'An error occurred while pushing role {role.name} onto {str(i)}.')
                pass
        await ctx.send(f'{ctx.author.mention} pushed **{role.name}** onto everyone.')


class rules_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def rule(self, ctx, rule_int: int = None):
        with open('dates.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            data[str(ctx.guild.id)]
        except KeyError:
            await ctx.send(f'{ctx.author.mention} this server does not have set rules yet.')
        with open("rules.txt", 'w') as rules:
            rules.writelines(data[str(ctx.guild.id)])
        with open("rules.txt", 'r+') as rules:
            await ctx.send(rules.readlines()[rule_int - 1])


    @commands.command()
    async def rules(self, ctx):
        bot_author = await ctx.guild.fetch_member(self.bot.user.id)
        with open('dates.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            data[str(ctx.guild.id)]
        except KeyError:
            await ctx.send(f'{ctx.author.mention} this server does not have set rules yet.')
            return
        with open("rules.txt", 'w') as rules:
            rules.writelines(data[str(ctx.guild.id)])
        with open("rules.txt", 'r+') as rules:
            embed = discord.Embed(title='RULES:', description=rules.read())
            icon = bot_author.avatar
            if not(icon is None):
                icon = icon.url
            else:
                icon = bot_author.default_avatar.url
            embed.set_author(name=str(bot_author), icon_url=icon)
            embed.set_footer(icon_url=icon,
                             text=f'Message sent by {self.bot.user} at {str(ctx.message.created_at).rsplit(".")[0] + " GMT"} in the {ctx.message.channel} channel in {ctx.guild}.')
            await ctx.send(embed=embed)


    @commands.command(aliases=['rule_append'])
    @commands.has_permissions(moderate_members=True, view_audit_log=True)
    async def rule_add(self, ctx, *, text: str = 'None'):
        bot_author = await ctx.guild.fetch_member(self.bot.user.id)
        with open('dates.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            data[str(ctx.guild.id)]
        except KeyError:
            await ctx.send(f'{ctx.author.mention} this server does not have set rules yet.')
            return
        data[str(ctx.guild.id)] = f'{data[str(ctx.guild.id)]}\n{text}'
        with open('dates.json', 'w') as json_file:
            json.dump(data, json_file)
        with open("rules.txt", 'w') as rules:
            rules.writelines(data[str(ctx.guild.id)])
        with open("rules.txt", 'r+') as rules:
            embed = discord.Embed(title='RULES:', description=rules.read())
            icon = bot_author.avatar
            if not(icon is None):
                icon = icon.url
            else:
                icon = bot_author.default_avatar.url
            embed.set_author(name=str(bot_author), icon_url=icon)
            embed.set_footer(icon_url=icon,
                             text=f'Message sent by {self.bot.user} at {str(ctx.message.created_at).rsplit(".")[0] + " GMT"} in the {ctx.message.channel} channel in {ctx.guild}.')
            await ctx.send(embed=embed)


    @commands.command(aliases=['rule_change'])
    @commands.has_permissions(moderate_members=True, view_audit_log=True)
    async def rule_replace(self, ctx, rule_ind: int, *, read: str):
        bot_author = await ctx.guild.fetch_member(self.bot.user.id)
        with open('dates.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            data[str(ctx.guild.id)]
        except KeyError:
            await ctx.send(f'{ctx.author.mention} this server does not have set rules yet.')
            return
        listed = str(data[str(ctx.guild.id)]).rsplit('\n')
        listed[rule_ind - 1] = read
        text = ''
        for index, value in enumerate(listed):
            if index != len(listed) - 1:
                text = f'{text}{value}\n'
            else:
                text = f'{text}{value}'
        data[str(ctx.guild.id)] = text
        with open('dates.json', 'w') as json_file:
            json.dump(data, json_file)
        with open("rules.txt", 'w') as rules:
            for i in listed:
                rules.writelines(f'{i}\n')
        with open("rules.txt", 'r+') as rules:
            embed = discord.Embed(title='RULES:', description=rules.read())
            icon = bot_author.avatar
            if not(icon is None):
                icon = icon.url
            else:
                icon = bot_author.default_avatar.url
            embed.set_author(name=str(bot_author), icon_url=icon)
            embed.set_footer(icon_url=icon,
                             text=f'Message sent by {self.bot.user} at {str(ctx.message.created_at).rsplit(".")[0] + " GMT"} in the {ctx.message.channel} channel in {ctx.guild}.')
            await ctx.send(embed=embed)


    @commands.command(aliases=('rule_rm', 'rule_delete', 'rule_del'))
    @commands.has_permissions(moderate_members=True, view_audit_log=True)
    async def rule_remove(self, ctx, rule_ind: int = 0):
        bot_author = await ctx.guild.fetch_member(self.bot.user.id)
        with open('dates.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            data[str(ctx.guild.id)]
        except KeyError:
            await ctx.send(f'{ctx.author.mention} this server does nto have set rules yet.')
            return
        listed = str(data[str(ctx.guild.id)]).rsplit('\n')
        listed.pop(rule_ind - 1)
        text = ''
        for index, value in enumerate(listed):
            if index != len(listed) - 1:
                text = f'{text}{value}\n'
            else:
                text = f'{text}{value}'
        data[str(ctx.guild.id)] = text
        with open('dates.json', 'w') as json_file:
            json.dump(data, json_file)
        with open("rules.txt", 'w') as rules:
            for i in listed:
                rules.writelines(f'{i}\n')
        with open("rules.txt", 'r+') as rules:
            embed = discord.Embed(title='RULES:', description=rules.read())
            icon = bot_author.avatar
            if not(icon is None):
                icon = icon.url
            else:
                icon = bot_author.default_avatar.url
            embed.set_author(name=str(bot_author), icon_url=icon)
            embed.set_footer(icon_url=icon,
                             text=f'Message sent by {self.bot.user} at {str(ctx.message.created_at).rsplit(".")[0] + " GMT"} in the {ctx.message.channel} channel in {ctx.guild}.')
            await ctx.send(embed=embed)


class logs_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=('fetch_logs', 'get_logs', 'pull_logs'))
    @commands.has_permissions(view_audit_log=True)
    async def logs(self, ctx):
        with (open('logs.json', 'r')) as json_file:
            data = json.load(json_file)
        with open('logs.txt', 'w') as file:
            file.write(str(data[str(ctx.guild.id)]))
        await ctx.author.send(content=f'{ctx.author.mention} logs from the current bot session for **{ctx.guild}**:', file=discord.File(r'./logs.txt'))


    @commands.command(aliases=('delete_logs', 'del_logs', 'rm_logs', 'remove_logs'))
    @commands.has_permissions(view_audit_log=True)
    async def clear_logs(self, ctx):
        with (open('logs.json', 'r')) as json_file:
            data = json.load(json_file)
            data[str(ctx.guild.id)] = 0
        with (open('logs.json', 'w')) as json_file:
            json.dump(data, json_file)
        await ctx.send(f'{ctx.author.mention} cleared all logs from bot session in **{ctx.guild}**.')


@tasks.loop(minutes=5)
async def ping():
    await bot.wait_until_ready()
    user = await bot.fetch_user(bot.user.id)


@tasks.loop(minutes=5)
async def restart_cogs():
    await bot.wait_until_ready()
    remove_cogs()
    add_cogs()

restart_cogs.start()

ping.start()


def remove_cogs():
    bot.remove_cog(event_cog(bot))
    bot.remove_cog(rules_cog(bot))
    bot.remove_cog(hush_cog(bot))
    bot.remove_cog(warn_cog(bot))
    bot.remove_cog(ban_cog(bot))
    bot.remove_cog(messages_cog(bot))
    bot.remove_cog(kick_cog(bot))
    bot.remove_cog(logs_cog(bot))
    bot.remove_cog(filters_cog(bot))
    bot.remove_cog(channels_cog(bot))
    bot.remove_cog(server_lock_cog(bot))
    bot.remove_cog(roles_cog(bot))
    bot.remove_cog(fetch_data_cog(bot))
    bot.remove_cog(help_cog(bot))
    bot.remove_cog(mute_cog(bot))
    bot.remove_cog(reacting_cog(bot))
    bot.remove_cog(print_cog(bot))
    bot.remove_cog(owner_cog(bot))



def add_cogs():
    bot.add_cog(cog=event_cog(bot), override=True)
    bot.add_cog(cog=rules_cog(bot), override=True)
    bot.add_cog(cog=hush_cog(bot), override=True)
    bot.add_cog(cog=warn_cog(bot), override=True)
    bot.add_cog(cog=ban_cog(bot), override=True)
    bot.add_cog(cog=messages_cog(bot), override=True)
    bot.add_cog(cog=kick_cog(bot), override=True)
    bot.add_cog(cog=logs_cog(bot), override=True)
    bot.add_cog(cog=filters_cog(bot), override=True)
    bot.add_cog(cog=channels_cog(bot), override=True)
    bot.add_cog(cog=server_lock_cog(bot), override=True)
    bot.add_cog(cog=roles_cog(bot), override=True)
    bot.add_cog(cog=fetch_data_cog(bot), override=True)
    bot.add_cog(cog=help_cog(bot), override=True)
    bot.add_cog(cog=mute_cog(bot), override=True)
    bot.add_cog(cog=reacting_cog(bot), override=True)
    bot.add_cog(cog=print_cog(bot), override=True)
    bot.add_cog(cog=owner_cog(bot), override=True)


add_cogs()


bot.run(TOKEN)
