# import ensurepip
#
# ensurepip.bootstrap()
log_channels = dict()
import requests
import os
import calendar
from better_profanity import profanity
profanity.MAX_NUMBER_COMBINATIONS = 20
from disnake.ui import Button
import math
from disnake.ext import tasks
from disnake.utils import get
import tracemalloc
import sys
import subprocess
from datetime import timedelta
from disnake.ext import commands
import disnake as discord
import random
import Functions
import importlib as ilib
import asyncio
import json
from datetime import datetime
TOKEN = 'TOKEN'

content_check = dict()


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
# ('guild_id', 'reacting_message_id'): ('role_id_to_add', 'emoji_to_react')
reacting = {('guild_id', 'message_id_to_react'): ('role_id_to_add', 'emoji_to_react')}

topics = list()
success = {True: 0, False: 0, 'last': False}

muted_channel = False
tracemalloc.start()
sniped_messages = dict()
filtering = dict()
default_roles = dict()
spam = 2
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


    # @commands.Cog.listener("on_member_ban")
    # async def on_member_ban(self, guild: discord.Guild, user: discord.User):
    #     logs = await (await guild.audit_logs(limit=100, action=discord.AuditLogAction.ban)).flatten()
    #     action = None
    #     for i in logs:
    #         try:
    #             if i.target.id == user.id:
    #                 action = i
    #                 break
    #         except BaseException:
    #             continue
    #     embed = discord.Embed(color=discord.Color.red, title='Ban', description=f'{user.mention} was banned on {discord.utils.format_dt(action.created_at)} by {action.user.mention} because {action.reason}.')
    #     try:
    #         await (await guild.fetch_channel(log_channels[guild.id])).send(embed=embed)
    #     except (discord.NotFound, discord.HTTPException, discord.Forbidden):
    #         channel = await guild.create_channel(name='mod-logs')
    #         await channel.send(embed=embed)
    #         logs_channel[guild.id] = channel.id
    #
    #
    #
    # @commands.Cog.listener("on_member_unban")
    # async def on_member_unban(self, guild: discord.Guild, user: discord.User):
    #     logs = await guild.audit_logs(limit=100, action=discord.AuditLogAction.unban).flatten()
    #     action = None
    #     for i in logs:
    #         try:
    #             if i.target.id == user.id:
    #                 action = i
    #                 break
    #         except BaseException:
    #             continue
    #     embed = discord.Embed(color=discord.Color.green, title='Unban', description=f'{user.mention} was unbanned on {discord.utils.format_dt(action.created_at)} by {action.user.mention} because {action.reason}.')
    #     try:
    #         await (await guild.fetch_channel(log_channels[guild.id])).send(embed=embed)
    #     except (discord.NotFound, discord.HTTPException, discord.Forbidden):
    #         channel = await guild.create_channel(name='mod-logs')
    #         await channel.send(embed=embed)
    #         logs_channel[guild.id] = channel.id


    @commands.Cog.listener("on_disconnect")
    async def on_disconnect(self):
        print('Wolfram Alpha session closed.')
        session.terminate()


    @commands.Cog.listener("on_guild_add")
    async def on_guild_join(self, guild):
        reset_logs(guild.id)


    @commands.Cog.listener("on_guild_remove")
    async def on_guild_remove(self, guild):
        reset_logs(guild.id)


    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        global filtering
        print(f'There are {len(self.bot.users)} users.')
        print(f'We have logged in as {self.bot.user}')
        await self.bot.change_presence(activity=discord.Game(f'{self.bot.command_prefix[-1]}fetch_docs'))
        full_delete()
        with open('warns.json', 'w+') as json_file:
            try:
                data = json.load(json_file)
            except (json.JSONDecodeError):
                data = {}
                for guild in self.bot.guilds:
                    data[str(guild.id)] = {"0": 0}
            else:
                for guild in self.bot.guilds:
                    if str(guild.id) in data.keys():
                        continue
                    else:
                        data[str(guild.id)] = {"0": 0}
            json.dump(data, json_file)
        for i in self.bot.guilds:
            filtering[str(i.id)] = 1


    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):
        global filtering
        if not(message.guild is None):
            try:
                filtering[str(message.guild.id)]
            except KeyError:
                filtering[str(message.guild.id)] = 1
            try:
                content_check[str(message.guild.id)]
            except KeyError:
                content_check[str(message.guild.id)] = 1
        async def syspurgeban(member_id, limit=10, bulk: bool = False):
            list_messages = []
            messages = 0
            async for i in message.channel.history(limit=None):
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
            if m.guild is None:
                return False
            return m.author == message.author or m.content.lower().replace(' ', '') in message.content.lower().replace(' ', '') or message.content.lower().replace(' ', '') in m.content.lower().replace(' ', '') or len(m.mentions) > round(7 / filtering[str(m.guild.id)]) or (filtering[str(m.guild.id)] > 2 and m.content.isupper())
        if any(i in (str(message.content).replace(' ', '')) for i in ('dQw4w9WgXcQ', 'astley')) and not(message.author.bot):
            await message.channel.send(f'{message.author.mention} {random.choice(rickrolls)}.')
            await message.author.send(f'{message.author.mention} bruh why?')
        try:
            print('Full message log: \n', datetime.utcnow(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                  message.channel, message.author, message.content,
                  message.author.bot, (filtering[str(message.guild.id)]),
                  message.jump_url)
            log(('Full message log: \n', datetime.utcnow(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                 message.channel, message.author, message.content,
                 message.author.bot, (filtering[str(message.guild.id)]),
                 message.jump_url), message.guild.id)
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print('Direct message log: \n', datetime.utcnow(), message.guild, message.channel, message.author, message.id, message.channel.id,
                  message.content, message.author.bot,
                  message.jump_url)
            return
        except (AttributeError, discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, discord.Forbidden):
            print('Message log error.')
        if message.guild is None:
            return
        test = str(str(message.content).replace(' ', '')).lower()
        if message.author.bot:
            return
        else:
            pass
        cache = ''
        if (filtering[str(message.guild.id)]) == 1:
            count = 0
            for index, value in enumerate(test):
                if value == cache:
                    count += 1
                if value.isupper():
                    count += 1
                if not(value.isascii()):
                    count += 1
                cache = value
            count -= 1
            if len(test) > 950 or count > 27 or len(message.mentions) > round(7 / filtering[str(message.guild.id)]):
                await message.delete()
        elif (filtering[str(message.guild.id)]) == 2:
            count = 0
            for index, value in enumerate(test):
                if value == cache:
                    count += 1
                if not (value.lower() in valid_chars):
                    count += 1
                if value.isupper():
                    count += 1
                if not(value.isascii()):
                    count += 1
                cache = value
            count -= 1
            if len(test) > 450 or count > 15 or len(message.mentions) > round(7 / filtering[str(message.guild.id)]):
                await syspurgeban(message.author.id, 10, 1)
        elif (filtering[str(message.guild.id)]) == 3:
            count = 0
            for index, value in enumerate(test):
                if value == cache:
                    count += 1
                if value.lower() in special_chars:
                    count += 1
                if not (value.lower() in valid_chars):
                    count += 0.5
                if not(value.isascii()):
                    count += 2
                cache = value
            count -= 1
            if len(test) > 195 or count > 11 or len(message.mentions) > round(7 / filtering[str(message.guild.id)]) or message.content.isupper():
                await syspurgeban(message.author.id, 25, 1)
                await message.author.timeout(duration=300.0, reason='Spam')
                await message.author.send(
                    f'{message.author.mention} you\'ve been muted in **{message.guild}** for spamming for **5** minutes.')
        elif (filtering[str(message.guild.id)]) == 4:
            count = 0
            for index, value in enumerate(test):
                if value == cache:
                    count += 1
                if value in special_chars:
                    count += 1
                if not (value in valid_chars):
                    count += 1
                if value.isupper():
                    count += 1
                if not(value.isascii()):
                    count += 1
                cache = value
            count -= 1
            if len(test) > 90 or count > 5 or len(message.mentions) > round(7 / filtering[str(message.guild.id)]) or message.content.isupper():
                await syspurgeban(message.author.id, 30, 1)
                await message.author.timeout(duration=600.0, reason='Spam')
                await message.author.send(
                    f'{message.author.mention} you\'ve been muted in **{message.guild}** for spamming for **10** minutes.')
        if bool(content_check[str(message.guild.id)]):
            if profanity.contains_profanity(message.content.lower()):
                await message.delete()
        if (filtering[str(message.guild.id)]) == 1:
            try:
                await bot.wait_for('message', timeout=1, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 5, 1)
        elif (filtering[str(message.guild.id)]) == 2:
            try:
                await bot.wait_for('message', timeout=2, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 15, 1)
        elif (filtering[str(message.guild.id)]) == 3:
            try:
                await bot.wait_for('message', timeout=8.5, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 25, 1)
                await message.author.timeout(duration=300.0, reason='Spam')
                await message.author.send(
                    f'{message.author.mention} you\'ve been muted in **{message.guild}** for spamming for **5** minutes.')
        elif (filtering[str(message.guild.id)]) == 4:
            try:
                await bot.wait_for('message', timeout=15, check=check_for_spam)
            except asyncio.exceptions.TimeoutError:
                pass
            else:
                await syspurgeban(message.author.id, 30, 1)
                await message.author.timeout(duration=600.0, reason='Spam')
                await message.author.send(
                    f'{message.author.mention} you\'ve been muted in **{message.guild}** for spamming for **10** minutes.')


    @commands.Cog.listener("on_message_edit")
    async def on_message_edit(self, old_message: discord.Message, message: discord.Message):
        if any(i in (str(message.content).replace(' ', '')) for i in ('dQw4w9WgXcQ', 'rick', 'astley')) and not(message.author.bot):
            await message.channel.send(f'{message.author.mention} {random.choice(rickrolls)}.')
            await message.author.send(f'{message.author.mention} bruh why?')
        global spam
        global content
        try:
            print('Full message edit log: \n', datetime.utcnow(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                  message.channel, message.author, message.content,
                  message.author.bot, (filtering[str(message.guild.id)]),
                  f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}')
            log(('Full message edit log: \n', datetime.utcnow(), message.guild.id, message.channel.id, message.author.id, message.id, message.guild,
                 message.channel, message.author, message.content,
                 message.author.bot,
                 f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}'), message.guild.id)
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print('Direct message edit log: \n', datetime.utcnow(), message.guild, message.channel, message.author, message.id, message.channel.id,
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
        if (filtering[str(message.guild.id)]) == 1:
            count = 0
            for index, value in enumerate(test):
                if value == cache:
                    count += 1
                cache = value
            count -= 1
            if len(test) > 950 or count > 27:
                await message.delete()
        elif (filtering[str(message.guild.id)]) == 2:
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
        elif (filtering[str(message.guild.id)]) == 4:
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
        if profanity.contains_profanity(message.content.lower()):
            await message.delete()


    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member: discord.Member):
        if member.public_flags.spammer:
            await member.kick(reason='Marked as spammer.')
            return
        await member.send(f'{member.mention} Welcome to **{member.guild.name}**!')
        await member.send(':wave:')


    # @commands.Cog.listener('on_member_update')
    # async def on_member_update(self, before: discord.Member, after: discord.Member):
    #     if isinstance(after.current_timeout, datetime):
    #         logs = await after.guild.audit_logs(limit=100, action=discord.AuditLogAction.member_update).flatten()
    #         action = None
    #         print('Done!')
    #         for i in logs:
    #             try:
    #                 if i.target.id == user.id and not isinstance(i.target.current_timeout, None) is None:
    #                     action = i
    #                     break
    #             except BaseException:
    #                 continue
    #         if action is None:
    #             return
    #         embed = discord.Embed(color=discord.Color.yellow, title='Mute',
    #                               description=f'{after.mention} was muted on {discord.utils.format_dt(action.created_at)} by {action.user.mention} because {action.reason}.')
    #         try:
    #             await (await after.guild.fetch_channel(log_channels[after.guild.id])).send(embed=embed)
    #         except (discord.NotFound, discord.HTTPException, discord.Forbidden):
    #             channel = await after.  guild.create_channel(name='mod-logs')
    #             await channel.send(embed=embed)
    #             logs_channel[after.guild.id] = channel.id



    @commands.Cog.listener("on_meber_remove")
    async def on_member_remove(self, member: discord.Member):
        await member.send(f'{member.mention} see you soon in **{member.guild.name}**!')
        await member.send(':wave:')
        # logs = await member.guild.audit_logs(limit=100, action=discord.AuditLogAction.kick).flatten()
        # action = None
        # for i in logs:
        #     try:
        #         if i.target.id == member.id:
        #             action = i
        #             break
        #     except BaseException:
        #         continue
        # if action is None:
        #     return
        # embed = discord.Embed(color=discord.Color.orange, title='Kick',
        #                       description=f'{user.mention} was kicked on {discord.utils.format_dt(action.created_at)} by {action.user.mention} because {action.reason}.')
        # try:
        #     await (await member.guild.fetch_channel(log_channels[member.guild.id])).send(embed=embed)
        # except (discord.NotFound, discord.HTTPException, discord.Forbidden):
        #     channel = await member.guild.create_channel(name='mod-logs')
        #     await channel.send(embed=embed)
        #     logs_channel[member.guild.id] = channel.id


    # s
    @commands.Cog.listener("on_raw_reaction_add")
    async def on_raw_reaction_add(self, payload):
        data = reacting.get((payload.guild_id, payload.message_id))
        if type(data) == tuple:
            pass
        else:
            return
        if str(payload.emoji) == data[1]:
            guild = await bot.fetch_guild(payload.guild_id)
            member = await guild.getch_member(payload.user_id)
            role = guild.get_role(data[0])
            await member.add_roles(role)
            try:
                await member.send(f'You got the **{role.name}** role in **{guild.name}** for reacting!')
            except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {str(member)}')


    @commands.Cog.listener("on_raw_reaction_remove")
    async def on_raw_reaction_remove(self, payload):
        data = reacting.get((payload.guild_id, payload.message_id))
        if type(data) == tuple:
            pass
        else:
            return
        if str(payload.emoji) == data[1]:
            guild = await bot.fetch_guild(payload.guild_id)
            member = await guild.getch_member(payload.user_id)
            role = guild.get_role(data[0])
            await member.remove_roles(role)
            try:
                await member.send(f'You lost the **{role.name}** role in **{guild.name}** for unreacting!')
            except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {str(member)}')


    @commands.Cog.listener("on_raw_message_delete")
    async def on_raw_message_delete(self, payload: discord.RawMessageDeleteEvent):
        global sniped_messages
        guild = None
        if payload.guild_id is not None:
            guild = await bot.fetch_guild(payload.guild_id)
            sniped_messages[(guild.id, int(payload.channel_id))] = payload
            sniped_messages[guild.id] = payload
        try:
            print('Full delete log: \n', datetime.utcnow(), payload.guild_id, payload.channel_id, payload.cached_message.author.id, guild.name, (await guild.fetch_channel(payload.channel_id)).name, payload.cached_message.author, payload.cached_message.content, payload.cached_message.author.bot)
            log(('Full delete log: \n', datetime.utcnow(), payload.guild_id, payload.channel_id, payload.cached_message.author.id, guild.name, (await guild.fetch_channel(payload.channel_id)).name, payload.cached_message.author, payload.cached_message.content, payload.cached_message.author.bot), payload.guild_id)
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            if not(payload.cached_message is None):
                print('Direct message delete log: \n', datetime.utcnow(), payload.channel_id, payload.cached_message.author.id,
                          payload.cached_message.channel, payload.cached_message.author, payload.cached_message.content)
            else:
                print('Message delete log error.')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print('Message delete log error.')


    # @commands.Cog.listener("on_command_error")
    # async def on_command_error(self, ctx, error):
    #     embed = discord.Embed(title=f"An error occurred:", description=f'{error}')
    #     embed.color = ctx.author.color
    #     icon = self.bot.user.avatar
    #     if not (icon is None):
    #         icon = icon.url
    #     else:
    #         icon = self.bot.user.default_avatar.url
    #     embed.set_author(icon_url=icon, name=self.bot.user)
    #     icon = ctx.author.avatar
    #     if not (icon is None):
    #         icon = icon.url
    #     else:
    #         icon = ctx.author.default_avatar.url
    #     embed.set_footer(icon_url=icon,
    #                      text=f'{ctx.author} ran a command ran at {str(ctx.message.created_at).rsplit(".")[0] + " GMT"} in the {ctx.message.channel} channel within {ctx.message.guild}.')
    #     await ctx.send(embed=embed)


class kick_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that are related to kicking members.'


    @commands.command(aliases=('remove', 'kick_user', 'kick_member', 'remove_user', 'remove_member'), description = 'Removes <member> from the current guild.', brief = 'Kicks <member>.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='None'):
        user = await bot.getch_user(member.id)
        await member.kick(reason=reason)
        await ctx.send(f'''**{ctx.message.author.mention}** kicked **{member.mention}**:
    **{reason}**.''')
        try:
            await user.send(f'''{user.mention} you were kicked from **{ctx.guild}** by **{ctx.author}**:
        **{reason}**''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')


    @commands.command(aliases=('remove_members', 'kick_users', 'remove_users'), description = 'Removes multiple member ids from the current guild.', brief = 'Kicks multiple members.')
    @commands.has_permissions(kick_members=True)
    async def kick_members(self, ctx, *, member_ids):
        try:
            list(member_ids)
        except ValueError:
            raise ValueError('Invalid list for "member_ids".')
        tup = convert_to_list(member_ids)
        for i in tup:
            print(i)
            user = await bot.getch_user(int(i))
            member = await ctx.guild.getch_member(int(i))
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
        self.description = 'Commands that are related to muting members/managing timeouts.'


    @commands.command(aliases=('vc_mute', 'voice_mute'), description='Mutes a member in all vcs.', brief='Disables a member to speak.')
    @commands.has_permissions(mute_members=True)
    async def vcmute(self, ctx, member: discord.Member, *, reason: str='None'):
        await member.edit(mute=True, reason=reason)
        await ctx.message.reply(f'{member.mention} was voice muted because *{reason}*.')


    @commands.command(aliases=('vc_unmute', 'voice_unmute'), description='Unmutes a member in all vcs.', brief='Enables a member to speak.')
    @commands.has_permissions(mute_members=True)
    async def vcunmute(self, ctx, member: discord.Member, *, reason: str='None'):
        await member.edit(mute=False, reason=reason)
        await ctx.message.reply(f'{member.mention} was voice unmuted because *{reason}*.')


    @commands.command(aliases=('vc_kick', 'voice_kick'), description='Removes a member from the current vc.', brief='Disconnects a member from a vc.')
    @commands.has_permissions(mute_members=True)
    async def vckick(self, ctx, member: discord.Member, *, reason: str='None'):
        if member.voice is None:
            return
        await member.edit(voice_channel=None, reason=reason)
        await ctx.message.reply(f'{member.mention} was kicked from voice because *{reason}*.')


    @commands.command(description = 'Adds a timeout to <member> for time specified with reason [reason].', brief = 'Mutes a member.')
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, days: int=1, hours: int=0, minutes: int=0, *, reason='None'):
        duration = timedelta(days=days, minutes=minutes, hours=hours)
        await member.timeout(duration=duration, reason=reason)
        try:
            await member.send(f'''{member.mention} you were put in the timeout chair by **{ctx.author}** for {duration}, because:
**{reason}**.''')
        except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {str(member)}.')
        await ctx.send(f'''{ctx.author.mention} put {member.mention} in the timeout chair for {duration}, because:
**{reason}**.''')


    @commands.command(description = 'Removes timeout from <member>.', brief = 'Unmutes a member.')
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


class ticket_cog(commands.Cog):
    global default_roles


    def __init__(self, bot):
        self.bot = bot
        self.roles = dict()
        self.description = 'Commands that are related to managing/creating tickets in the current server.'


    @commands.command(aliases=['cancel_ticket'], description = 'Closes an opened ticket channel passed.', brief = 'Closes an opened ticket.')
    async def close_ticket(self, ctx, channel: discord.TextChannel):
        def predicate(self, ctx):
            try:
                self.roles[ctx.guild.id]
            except KeyError:
                if ctx.author.guild_permissions.moderate_members:
                    return True
                else:
                    return False
            else:
                for role in self.roles[ctx.guild.id]:
                    try:
                        if ctx.guild.get_role(role) in ctx.author.roles:
                            return True
                        if ctx.author.guild_permissions.moderate_members:
                            return True
                    except (discord.NotFound, discord.Forbidden, discord.HTTPException):
                        print(f'Could not find role {role} in guild {ctx.guild.id} for ticket viewing.')
                return False
        if predicate(self, ctx):
            pass
        else:
            return await ctx.message.reply('You may not close this ticket.')
        if channel.name.startswith('ticket-'):
            async for entry in ctx.guild.audit_logs(limit=None, action=discord.AuditLogAction.channel_create, user=ctx.guild.me):
                if entry.target == channel:
                    await channel.delete()
                    return await ctx.message.reply(f'`{channel.name}` closed.')
            await ctx.send(f'Invalid channel.')
        await ctx.send(f'Invalid channel.')


    @commands.command(aliases=('viewing_role', 'view_ticket'), description = 'Allows <role> to view/close opened tickets.', brief = 'Allows a role to manage tickets.')
    @commands.has_permissions(moderate_members=True)
    async def ticket_role(self, ctx, role: discord.Role):
        try:
            guild = self.roles[ctx.guild.id]
        except KeyError:
            self.roles[ctx.guild.id] = list()
            self.roles[ctx.guild.id].append(role.id)
            await ctx.message.reply(f'Members with role **{role.name}** can now view opened tickets.')
        else:
            if role.id in self.roles[ctx.guild.id]:
                return await ctx.message.reply(f'Members with role **{role.name}** can already view opened tickets.')
            self.roles[ctx.guild.id].append(role.id)
            await ctx.message.reply(f'Members with role **{role.name}** can now view opened tickets.')


    @commands.command(aliases=('open_ticket', 'start_ticket'), description = 'Opens a ticket channel in the current guild.', brief = 'Creates a ticket.')
    @commands.cooldown(1, 600, commands.BucketType.member)
    async def ticket(self, ctx, *, reason: str='None'):
        bot_author = ctx.guild.me
        cached_message = None
        truth = False
        while not(truth):
            integer = random.randint(0, 9999)
            truth = False
            for channel in ctx.guild.channels:
                if isinstance(channel, discord.TextChannel) and not(f'ticket-{integer}' in channel.name):
                    truth = True
                    break
        icon = ctx.author.avatar
        if icon is None:
            icon= ctx.author.default_avatar.url
        else:
            icon = icon.url
        ticket =  await ctx.guild.create_text_channel(name=f'ticket-{integer}')
        embed = discord.Embed(title=f'Ticket-{integer}', description=f'{ctx.author.mention} run `@{bot_author.name} close` to close this ticket.', color=(bot_author.color))
        embed.set_author(name=f'{ctx.author} requested a ticket', icon_url=icon)
        icon = ctx.guild.icon
        if icon is None: 
            icon = ctx.author.avatar
            if icon is None:
                icon = ctx.author.default_avatar.url
            else:
                icon = icon.url
        else:
            icon = icon.url
        embed.set_footer(text=f'{ctx.author} requested a ticket on {str(ticket.created_at).rsplit(".")[0]} in {ctx.guild}.', icon_url=icon)
        embed.add_field(name=f'Reason', value=f'{reason}')
        try:
            self.roles[ctx.guild.id]
        except KeyError:
            pass
        else:
            string = str()
            if len(self.roles[ctx.guild.id]) > 1:
                for index, role in enumerate(self.roles[ctx.guild.id]):
                    role = ctx.guild.get_role(role)
                    if not((index + 1) == len(self.roles[ctx.guild.id])):
                        string = f'{string}{role.mention}, '
                    else:
                        string = f'{string}{role.mention}'
            else:
                string = ctx.guild.get_role(self.roles[ctx.guild.id][0]).mention
            embed.add_field(name='Roles that can view this ticket', value=string, inline=False)
        await ticket.send(content='If this channel does not recieve a message within 10 minutes, the ticket will be closed.', embed=embed)
        await ticket.set_permissions(ctx.guild.default_role, view_channel=False)
        try:
            await ticket.set_permissions(get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id]), view_channel=False)
        except BaseException:
            pass
        await ticket.set_permissions(await ctx.guild.getch_member(ctx.author.id), view_channel=True)
        try:
            roles = self.roles[ctx.guild.id]
        except KeyError:
            pass
        else:
            for role in roles:
                try:
                    await ticket.set_permissions(ctx.guild.get_role(role), view_channel=True)
                except (discord.Forbidden, discord.HTTPException, discord.NotFound):
                    print(f'Could not whitelist role {role} in guild {ctx.guild.id} for ticket viewing.')
        while True:
            try:
                cached_message = await self.bot.wait_for('message', timeout=600)
            except asyncio.exceptions.TimeoutError:
                await ticket.delete()
                await ctx.author.send(f'{ctx.author.mention} `ticket-{integer}` was closed in **{ctx.guild}** due to inactivity.')
                return
            else:
                if len(cached_message.content.rsplit(' ')) == 2:
                    if bot_author.mentioned_in(cached_message) and 'close' in cached_message.content.lower().rsplit(' ')[1] and cached_message.author == ctx.author and cached_message.channel == ticket:
                        await ticket.delete()
                        await ctx.author.send(
                            f'{ctx.author.mention} `ticket-{integer}` was closed in **{ctx.guild}** by you.')
                        return



class messages_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that are related to managing/viewing messages.'


    @commands.command(description='Creates an embed with json data provided, read documentation at https://pastebin.com/9w4Fp110', brief='Sends a highly customizable embed.')
    async def custom_embed(self, ctx):
        if len(ctx.message.attachments) == 1:
            if ctx.message.attachments[0].filename.rsplit('.')[-1] == 'json':
                contents = ((await ctx.message.attachments[0].read()).decode())
                try:
                    data = json.loads(contents)
                except BaseException:
                    return await ctx.send('Could not create embed with sent json data.')
                else:
                    try:
                        color = data.get('color') if data.get('color') is not None else discord.Embed.Empty
                        description = data.get('description') if data.get('description') is not None else discord.Embed.Empty
                        title = data.get('title') if data.get('title') is not None else discord.Embed.Empty
                        author = data.get('author') if data.get('author') is not None else discord.Embed.Empty
                        footer = data.get('footer') if data.get('footer') is not None else discord.Embed.Empty
                        author_icon = data.get('author_icon') if data.get('author_icon') is not None else discord.Embed.Empty
                        footer_icon = data.get('footer_icon') if data.get('footer_icon') is not None else discord.Embed.Empty
                        fields = list()
                        for name, value in data.get('fields'):
                            fields.append((name, value))
                    except BaseException:
                        embed = discord.Embed(color=discord.Color.from_rgb(r=color[0], g=color[1], b=color[2]), description=description, title=title)
                        embed.set_footer(icon_url=footer_icon, text=footer)
                        embed.set_author(icon_url=author_icon, name=author)
                        for tup in fields:
                            embed.add_field(name=tup[0], value=tup[1])
                        await ctx.send(embed=embed)


    @commands.command(description = 'Finds the last message deleted in the current guild/channel passed.', brief = 'Finds the last message deleted.')
    @commands.has_permissions(view_audit_log=True)
    async def snipe(self, ctx, channel: discord.TextChannel = None):
        global sniped_messages
        try:
            if channel is None:
                payload = sniped_messages[ctx.guild.id]
            else:
                payload = sniped_messages[(ctx.guild.id, channel)]
        except KeyError:
            if channel is None:
                await ctx.author.send(
                    f'{ctx.author.mention} no deleted messages within **{ctx.guild}** in the current session.')
            else:
                await ctx.author.send(
                    f'{ctx.author.mention} no deleted messages in the channel **{channel}** within **{ctx.guild}** in the current session.')
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
                embed.add_field(name='Message', value=f'{payload.cached_message.content}', inline=False)
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


    @commands.command(aliases=('delete', 'purge', 'clean'), description = 'Deletes a [limit] messages with [bulk] bulk deletion.', brief = 'Deletes messages in the current channel.')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 10, bulk: bool = False):
        await ctx.channel.purge(limit=amount + 1, bulk=bulk)


    @commands.command(aliases=('purge_messages', 'clean_messages', 'delete_messages'), description = 'Clears a list of message ids passed.', brief = 'Deletes message ids.')
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


    @commands.command(aliases=['purgeban'], description = 'Same as clear, but deletes message from a certain member in the channel.', brief = 'Deletes messages from a member.')
    @commands.has_permissions(manage_messages=True)
    async def purge_ban(self, ctx, member: discord.Member, limit: int = 10, bulk: bool = False):
        list_messages = []
        messages = 0
        index = 0
        async for message in (ctx.channel.history(limit=None)):
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
        self.description = 'Commands that are related to managing warnings in the current guild.'


    @commands.command(aliases=('alert', 'notify', 'inform'), description = 'Adds a warn to a <member> with reason <reason>', brief = 'Warns a member.')
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


    @commands.command(description = 'Removes [count] warns from <member>.', brief = 'Removes warnings from member.')
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
            await ctx.message.reply(f'There are no warns in this server.')
            return
        try:
            dictionary[str(member.id)] -= count
        except (KeyError, TypeError):
            with open('warns.json', 'w') as file:
                json.dump(data, file)
            await ctx.message.reply(f'There are no warns in this server for {member.mention}.')
            return
        if dictionary[str(member.id)] <= 0:
            del dictionary[str(member.id)]
        data[str(ctx.guild.id)] = dictionary
        with open('warns.json', 'w') as file:
            json.dump(data, file)
        await ctx.message.reply(f'{member.mention} has been unwarned **{count}** times.')


    @commands.command(aliases=('get_warns', 'pull_warns', 'warns'), description = 'Returns warns for an entire guild, or member.', brief = 'Returns warns.')
    @commands.has_permissions(view_audit_log=True)
    async def fetch_warns(self, ctx, member: discord.Member = None):
        with open('warns.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            dictionary = data[str(ctx.guild.id)]
        except (KeyError, TypeError):
            await ctx.message.reply(f'No warns from this server.')
            return
        else:
            if member is None:
                for member in dictionary.keys():
                    try:
                        with open('Warns.txt', 'w') as file:
                            file.writelines(
                                f'{(await ctx.guild.getch_member(int(member)))} has {dictionary[str(member)]} warns.')
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
                    await ctx.author.send(
                        f'{member.mention} has **{dictionary[str(member.id)]}** warns in **{ctx.guild}**.')
                except KeyError:
                    await ctx.message.reply(f'There are no warns in this server for  {member.mention}.')


class hush_cog(commands.Cog):
    global default_roles


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that are related to moderating entire channels.'


    @commands.command(aliases=('set_role', 'set_default_role', 'defaulted_role', 'mute_role', 'muted_role'), description = 'Sets mute_role (default role for muting/hiding in cogs) for the current guild.', brief = 'Sets mute_role.')
    @commands.has_permissions(moderate_members=True)
    async def default_role(self, ctx, role: discord.Role):
        default_roles[ctx.guild.id] = role.id
        await ctx.send(f'Default role for muting is now **{role.name}**.')


    @commands.command(aliases=('silence', 'mute_channel', 'silence_channel'), description = 'Disables mute_role from sending messages in the current channels.', brief = 'Stops mute_role from sending messages in current channel.')
    @commands.has_permissions(moderate_members=True)
    async def hush(self, ctx, time: float = 5, *, reason: str = 'None'):
        channel = ctx.channel
        try:
            role = get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
        print(type(role), role.name)

        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            print(True)
            ctx.channel = ctx.author.voice.channel
        try:
            if (not((ctx.channel.overwrites_for(role)).view_channel == False)) and (ctx.channel.overwrites_for(role)).send_messages and isinstance(ctx.channel, discord.TextChannel) or ((not((ctx.channel.overwrites_for(role)).connect == False)) and (((ctx.channel.overwrites_for(role)).speak or (ctx.channel.overwrites_for(role)).stream) and isinstance(ctx.channel, discord.VoiceChannel))):
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
        await ctx.channel.set_permissions(role, overwrite=overwrite, reason=reason)
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
            if (((ctx.channel.overwrites_for(role)).view_channel) and (not((ctx.channel.overwrites_for(role)).send_messages) and isinstance(ctx.channel, discord.TextChannel))) or (not((ctx.channel.overwrites_for(role)).connect) and isinstance(ctx.channel, discord.VoiceChannel)):
                pass
            else:
                return
        except KeyError:
            return
        await ctx.channel.set_permissions(role, overwrite=overwrite)
        await channel.send(f'{ctx.author.mention}, channel has been unhushed.')


    @commands.command(aliases=('un_silence', 'unmute_channel', 'un_silence_channel', 'unhush'), description = 'Allows mute_role for current guild to send messages in current channel.', brief = 'Allows mute_role to send messages.')
    @commands.has_permissions(moderate_members=True)
    async def un_hush(self, ctx, *, reason: str = 'None'):
        channel = ctx.channel
        try:
            role = ctx.guild.get_role(default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            ctx.channel = ctx.author.voice.channel
        try:
            if (((ctx.channel.overwrites_for(role)).view_channel) and (not((ctx.channel.overwrites_for(role)).send_messages) and isinstance(ctx.channel, discord.TextChannel))) or (not((ctx.channel.overwrites_for(role)).connect) and isinstance(ctx.channel, discord.VoiceChannel)):

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
        await ctx.channel.set_permissions(role, overwrite=overwrite, reason=reason)
        await channel.send(f'''{ctx.author.mention} has unhushed the channel because:
    **{reason}**''')


    @commands.command(aliases=['unhide'], description = 'Allows mute_role for current guild to view the current channel.', brief = 'Allows mute_role to view current channel.')
    @commands.has_permissions(moderate_members=True)
    async def un_hide(self, ctx, *, reason: str = 'None'):
        channel = ctx.channel
        try:
            role = get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            ctx.channel = ctx.author.voice.channel
        try:
            if (((ctx.channel.overwrites_for(role)).view_channel == False)) or (((ctx.channel.overwrites_for(role)).connect == False) and isinstance(ctx.channel, discord.VoiceChannel)):
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
        await ctx.channel.set_permissions(role, overwrite=overwrite, reason=reason)
        await channel.send(f'''{ctx.author.mention} has unhidden the channel because:
    **{reason}**''')


    @commands.command(description = 'Hides the current channel from mute_role for current guild.', brief = 'Hides current channel.')
    @commands.has_permissions(moderate_members=True)
    async def hide(self, ctx, time: float = 5, *, reason: str = 'None'):
        channel = ctx.channel
        try:
            role = get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
        print(ctx.author.voice, type(ctx.author.voice))
        if isinstance(ctx.author.voice, discord.VoiceState):
            ctx.channel = ctx.author.voice.channel
        try:
            if (not((ctx.channel.overwrites_for(role)).view_channel == False)) or ((not((ctx.channel.overwrites_for(role)).connect == False) and isinstance(ctx.channel, discord.VoiceChannel))):

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
        await ctx.channel.set_permissions(role, overwrite=overwrite, reason=reason)
        await channel.send(f'''{ctx.author.mention} has hidden the channel for **{time}** minutes because:
    **{reason}**''')
        await asyncio.sleep(time * 60)
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = True
        overwrite.connect = True
        overwrite.send_messages = True
        overwrite.speak = True
        try:
            if (((ctx.channel.overwrites_for(role)).view_channel == False)) or (((ctx.channel.overwrites_for(role)).connect == False) and isinstance(ctx.channel, discord.VoiceChannel)):
                pass
            else:
                return
        except KeyError:
            pass
        await ctx.channel.set_permissions(role, overwrite=overwrite)
        await channel.send(f'{ctx.author.mention}, channel has been unhidden.')


class server_lock_cog(commands.Cog):
    global default_roles

    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that are related to moderating all channels in the current guild.'


    @commands.command(aliases=('unhide_guild', 'unhideserver', 'unhideguild', 'server_unhide', 'server_un_hide', 'serverunhide', 'guild_un_hide', 'guild_unhide', 'guildunhide'), description = 'Allows mute_role for current guild. to view the current guild.', brief = 'Allows mute_role to view guild.')
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def unhide_server(self, ctx, time: float = 5, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = True
        overwrite.send_messages = True
        overwrite.connect = True
        overwrite.speak = True
        try:
            role = get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
        for channel in ctx.guild.channels:
            try:
                if (((channel.overwrites_for(role)).view_channel == False)) or (((channel.overwrites_for(role)).connect == False) and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(role, overwrite=overwrite)
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unhidden.')


    @commands.command(aliases=('hide_guild', 'hideserver', 'hideguild', 'guildhide', 'serverhide', 'guild_hide', 'server_hide'), description = 'Makes current guilds mute_role unable to view current guild.', brief = 'Prevents mute_role from viewing current guild.')
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def hide_server(self, ctx, time: float = 5, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        overwrite.send_messages = False
        overwrite.connect = False
        overwrite.speak = False
        try:
            role = get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
        for channel in ctx.guild.channels:
            try:
                if (channel.overwrites_for(role).view_channel) or (channel.overwrites_for(role).connect and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(role, overwrite=overwrite, reason=reason)
                else:
                    continue
            except KeyError:
                await channel.set_permissions(role, overwrite=overwrite, reason=reason)
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
                if (((channel.overwrites_for(role)).view_channel == False)) or (((channel.overwrites_for(role)).connect == False) and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(role, overwrite=overwrite, reason=reason)
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unhidden.')


    @commands.command(aliases=('server_lockdown', 'lock', 'server_lock', 'server_hush'), description = 'Disables current guilds mute_role to send messages in channels.', brief = 'Locks guild.')
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def lockdown(self, ctx, time: float = 5, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        try:
            role = get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
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
                if (not((channel.overwrites_for(role)).view_channel == False)) or ((not((channel.overwrites_for(role)).connect == False) and isinstance(channel, discord.VoiceChannel))):
                    await channel.set_permissions(role, overwrite=overwrite, reason=reason)
                else:
                    continue
            except KeyError:
                await channel.set_permissions(role, overwrite=overwrite, reason=reason)
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
                if (((channel.overwrites_for(role)).view_channel == False)) or (((channel.overwrites_for(role)).connect == False) and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(role, overwrite=overwrite, reason=reason)
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unlocked.')


    @commands.command(aliases=('server_unlock', 'server_unhush', 'server_un_hush'), description = 'Allows current guilds mute_role to send messages in the current guild.', brief = 'Unlocks guild.')
    @commands.has_permissions(manage_channels=True, moderate_members=True)
    async def unlock(self, ctx, *, reason: str = 'None'):
        overwrite = discord.PermissionOverwrite()
        try:
            role = get(await ctx.guild.fetch_roles(), id=default_roles[ctx.guild.id])
        except BaseException:
            role = ctx.guild.default_role
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
                if (((channel.overwrites_for(role)).view_channel == False)) or (((channel.overwrites_for(role)).connect == False) and isinstance(channel, discord.VoiceChannel)):
                    await channel.set_permissions(role, overwrite=overwrite)
                else:
                    continue
            except KeyError:
                continue
        await ctx.send(f'{ctx.author.mention} server has been unlocked.')


class ban_cog(commands.Cog):


    @tasks.loop(seconds=1)
    async def check_bans(self):
        await self.bot.wait_until_ready()
        for index, key in enumerate(self.to_del):
            del self.bans_dict[key]
            self.to_del.pop(index)
        now = datetime.utcnow()
        for member in self.bans_dict.keys():
            if self.bans_dict[member] < now:
                try:
                    await member.unban(reason='Temp ban complete.')
                    self.to_del.append(member)
                except (discord.NotFound, discord.Forbidden, discord.HTTPException):
                    print(f'Could not unban user {member.id} for guild {member.guild.id}.')

    def __init__(self, bot):
        self.bot = bot
        self.description='Commands that are related to bans.'
        self.bans_dict = dict()
        self.to_del = list()
        self.check_bans.start()


    @commands.command(aliases=['tempban'], description='Bans a member for time specified.', brief='Temporarily bans a member.')
    @commands.has_permissions(ban_members=True)
    async def temp_ban(self, ctx, member: discord.Member, years: int=0, months: int=0, days: int=1, hours: int=0, reason: str='None'):
        current_time = datetime.utcnow()
        current_time = current_time + timedelta(days = days + months*30 + (years*365 + int(calendar.isleap(current_time.year))), hours = hours)
        await member.send(
            f'{member.mention} you\'ve been temp-banned in **{ctx.guild}** until {discord.utils.format_dt(current_time)} because **{reason}** by **{ctx.author.mention}**.')
        self.bans_dict[member] = current_time
        await ctx.message.reply(f'{member.mention} has been temp-banned until {discord.utils.format_dt(current_time)}.')
        await member.ban(reason=f'Tempban reason: {reason}.')


    @commands.command(aliases=('fetch_bans', 'get_bans', 'pull_bans'),
                      description='Fetches a list of bans in the current guild.', brief='Returns all bans.')
    @commands.has_permissions(ban_members=True)
    async def bans(self, ctx):
        bot = await ctx.guild.getch_member(self.bot.user.id)
        embed = disnake.Embed(color=bot.color)
        icon = ctx.guild.icon
        if icon is None:
            icon = bot.avatar
            if icon is None:
                icon = bot.default_avatar.url
            else:
                icon = icon.url
        else:
            icon = icon.url
        embed.set_author(icon_url=icon, name=ctx.guild)
        bans = await ctx.guild.audit_logs(limit=None, action=disnake.AuditLogAction.ban).flatten()
        banned = list()
        for entry in bans:
            if not isinstance(entry.reason, str) or entry.reason == '':
                entry.reason = 'None'
            for key in self.bans_dict.keys():
                if key.id == entry.target.id:
                    banned.append(
                        f'**{entry.target.name}** was banned by **{entry.user.name}**, at {disnake.utils.format_dt(entry.created_at)} because {entry.reason} until {disnake.utils.format_dt(self.bans_dict[key])}.')
                    continue
            banned.append(
                f'**{entry.target.name}** was banned by **{entry.user.name}**, at {disnake.utils.format_dt(entry.created_at)} because {entry.reason}.')
        unbans = await ctx.guild.audit_logs(limit=None, action=disnake.AuditLogAction.unban).flatten()
        unbanned = list()
        for entry in bans:
            if not isinstance(entry.reason, str) or entry.reason == '':
                entry.reason = 'None'
            banned.append(
                f'**{entry.target.name}** was unbanned by **{entry.user.name}**, at {disnake.utils.format_dt(entry.created_at)} because {entry.reason}.')
        if len(banned) > 0:
            embed.add_field(name='Bans', value="\n".join(banned))
        if len(unbanned) > 0:
            embed.add_field(name='Unbans', value="\n".join(unbanned))
        embed.set_footer(text=f'All entries logged before {datetime.utcnow().strftime("20%y-%m-%d %r")}',
                         icon_url=icon)
        await ctx.message.reply(embed=embed)


    @commands.command(aliases=('ban_users', 'ban_people'), description='Bans multiple <member_ids> from the current guild.', brief='Bans multiple members.')
    @commands.has_permissions(ban_members=True)
    async def ban_members(self, ctx, *, member_ids):
        try:
            list(member_ids)
        except ValueError:
            raise ValueError('Invalid list for "member_ids".')
        tup = convert_to_list(member_ids)
        for i in tup:
            print(i)
            user = await bot.getch_user(int(i))
            member = await ctx.guild.getch_member(int(i))
            await member.ban()
            try:
                await user.send(f'''{user.mention} you were banned from **{ctx.guild}** by **{ctx.author}**!''')
            except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {user}.')
        await ctx.send(f'{ctx.author.mention} banned members.')


    @commands.command(aliases=('unban_users', 'unban_people'), description='Unbans multiple <user_ids> from the current guild.', brief='Unbans multiple users.')
    @commands.has_permissions(ban_members=True)
    async def unban_members(self, ctx, *, user_ids):
        try:
            list(user_ids)
        except ValueError:
            raise ValueError('Invalid list for "member_ids".')
        tup = convert_to_list(user_ids)
        for i in tup:
            print(i)
            user = await bot.getch_user(int(i))
            await ctx.guild.unban(user)
            for key in self.bans_dict.keys():
                if key.id == user.id:
                    self.to_del.append(key)
            try:
                await user.send(f'''{user.mention} you were unbanned from **{ctx.guild}** by **{ctx.author}**!''')
            except (discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                    commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                print(f'Cannot direct message {user.display_name}.')
        await ctx.send('Unbanned members.')


    @commands.command(aliases=('ban_user', 'ban_member'), description='Bans <member> because <reason>.', brief='Bans a member.')
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


    @commands.command(description='Unbans <user> for the current guild because [reason]. If [link] is True, DMs the user a link to the guild.', brief='Unbans a user.')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User, link: bool=False, *, reason: str = 'None'):
        await ctx.guild.unban(user=user, reason=reason)
        for key in self.bans_dict.keys():
            if key.id == user.id:
                self.to_del.append(key)
        await ctx.send(f'''**{ctx.message.author.mention}** unbanned **{user.mention}** because:
**{reason}**''')
        try:
            await user.send(f'''**{user.mention}** you were unbanned by **{ctx.author.mention}** because:
    **{reason}**''')
        except (
                        discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                        ValueError,
                        commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
            print(f'Cannot direct message {user}.')
            return
        if link:
            await user.send(f'{(await (ctx.guild.channels[0]).create_invite()).url}')


class help_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that have info on the bot.'


    @commands.command(aliases=('get_docs', 'pull_docs'), description='Returns a pastebin document of commands, usages, aliases and arguments.', brief='Returns a pastebin of commands.')
    async def fetch_docs(self, ctx):
        await ctx.message.reply('https://pastebin.com/9w4Fp110')


    @commands.command(aliases=('get_code', 'pull_code'), description='Returns a github repository belonging to HRLO77#3508 that includes the bots source code.', brief='Returns a github repository of source code.')
    async def fetch_code(self, ctx):
        await ctx.message.reply('https://github.com/HRLO77/Bot-source-code')


class reminder_cog(commands.Cog):

    @tasks.loop(seconds=1)
    async def check_reminders(self):
        await self.bot.wait_until_ready()
        for index, key in enumerate(self.to_del):
            del self.reminders_dict[key]
            self.to_del.pop(index)
        current_time = datetime.utcnow()
        for key in self.reminders_dict.keys():
            if self.reminders_dict[key] < current_time:
                try:
                    user = await self.bot.getch_user(key[0])
                except BaseException:
                    print(f'Couldn\'t find member {key[0]} for reminder checking.')
                else:
                    await user.send(
                        f'{user.mention} your reminder is up! ({discord.utils.format_dt(self.reminders_dict[key])})')
                self.to_del.append(key)


    def __init__(self, bot):
        self.bot = bot
        self.reminders_dict = dict()
        self.to_del = list()
        self.check_reminders.start()
        self.description = 'Commands that are related to reminders.'


    @commands.command(aliases=('start_reminder', 'reminder'), description='Sets a reminder for the current user to go off on the arguments passed.', brief='Creates a reminder.')
    async def remind(self, ctx, years: int=0, months: int=0, days: int = 1, hours: int = 0, minutes: int = 0, seconds: int = 0):
        current_time = datetime.utcnow()
        current_time = current_time + timedelta(days = days + months*30 + (years*365 + int(calendar.isleap(current_time.year))), hours = hours, minutes = minutes, seconds = seconds)
        if current_time < datetime.utcnow():
            return await ctx.message.reply('Please enter values that are in the future.')
        self.reminders_dict[(ctx.author.id, random.randint(0, 99999))] = current_time
        return await ctx.author.send(f'Your reminder was set for {discord.utils.format_dt(current_time)} UTC!')


    @commands.command(aliases=('del_reminder', 'remove_reminder', 'delete_reminder', 'close_reminder'), description='Adds a reminder to deletion queue.', brief='Deletes a reminder.')
    async def clear_reminder(self, ctx):
        reminders = 0
        for key in self.reminders_dict.keys():
            if ctx.author.id == key[0]:
                reminders += 1
        if reminders == 1:
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    self.to_del.append(key)
            return await ctx.message.reply('Reminder deletion added to queue.')
        elif reminders > 1:
            keys = list()
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    keys.append(key)
            string = f'You have **{len(keys)}** reminders - '
            for index, key in enumerate(keys):
                if (index + 1) != len(keys):
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key])} UTC, '
                else:
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key])} UTC.'
            context = await ctx.author.send(
                f'{string} {ctx.author.mention} You have 60 seconds to reply to this message with the reminder to cancel(I.E 4, 7, 1).')

            def check(m):
                if m.author.id == ctx.author.id:
                    if m.reference is None:
                        return False
                    elif m.reference.message_id == context.id:
                        try:
                            if int(m.content) < len(keys) + 1 and int(m.content) > 0:
                                return True
                            else:
                                raise ValueError
                        except BaseException:
                            return False

            while True:
                try:
                    message = await self.bot.wait_for(event='message', timeout=60, check=check)
                except asyncio.exceptions.TimeoutError:
                    return await context.reply('Reminder deletion cancelled.')
                else:
                    self.to_del.append(keys[int(message.content) - 1])
                    return await message.reply(
                        f'Reminder deletion queued for {discord.utils.format_dt(self.reminders_dict[keys[int(message.content) - 1]])} UTC')
        else:
            await ctx.message.reply('You don\'t currently have any reminders set.')


    @commands.command(aliases=('check_reminder', 'check_reminders'), description='DMs a list of reminders the current user has.', brief='Returns reminders set.')
    async def reminders(self, ctx):
        reminders = 0
        for key in self.reminders_dict.keys():
            if ctx.author.id == key[0]:
                reminders += 1
        if reminders == 1:
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    return await ctx.author.send(
                        f'{ctx.author.mention} Your reminder ends on {discord.utils.format_dt(self.reminders_dict[key])} UTC!')
        elif reminders > 1:
            keys = list()
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    keys.append(key)
            string = f'You have **{len(keys)}** reminders - '
            for index, key in enumerate(keys):
                if (index + 1) != len(keys):
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key])} UTC, '
                else:
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key])} UTC.'
            return await ctx.author.send(f'{ctx.author.mention} {string}')
        else:
            return await ctx.message.reply('You do not currently have an active reminder.')


class repeater_cog(commands.Cog):

    @tasks.loop(seconds=1)
    async def check_reminders(self):
        await self.bot.wait_until_ready()
        for index, key in enumerate(self.to_del):
            del self.reminders_dict[key]
            self.to_del.pop(index)
        current_time = datetime.utcnow()
        for key in self.reminders_dict.keys():
            data = self.reminders_dict[key][1]
            time = current_time + timedelta(
                days=data[2] + (data[0] * 365 + int(calendar.isleap(current_time.year))) + data[1] * 30,
                hours=data[3], minutes=data[4], seconds=data[5])
            if self.reminders_dict[key][0] < current_time:
                try:
                    user = await self.bot.getch_user(key[0])
                except BaseException:
                    print(f'Couldn\'t find member {key[0]} for repeater checking.')
                    self.to_del.append(key)
                else:
                    await user.send(
                        f'{user.mention} your repeater is up! ({discord.utils.format_dt(self.reminders_dict[key][0])})')
                    self.reminders_dict[key] = (time, self.reminders_dict[key][1])



    def __init__(self, bot):
        self.bot = bot
        self.reminders_dict = dict()
        self.to_del = list()
        self.check_reminders.start()
        self.description = 'Commands that are related to repeaters. Repeaters are a combination of alarms and reminders, they repeat every interval of time that the user inputs, and does not delete unless specified.'


    @commands.command(aliases=('start_repeater', 'repeater'), description='Sets a repeater for the current user to go off on the arguments passed.', brief='Creates a repeater.')
    async def repeat(self, ctx, years: int=0, months: int=0, days: int = 1, hours: int = 0, minutes: int = 0, seconds: int = 0):
        current_time = datetime.utcnow()
        current_time = current_time + timedelta(days = days + months*30 + (years*365 + int(calendar.isleap(current_time.year))), hours = hours, minutes = minutes, seconds = seconds)
        if current_time < datetime.utcnow():
            return await ctx.message.reply('Please enter values that are in the future.')
        self.reminders_dict[(ctx.author.id, random.randint(0, 99999))] = (current_time, (years, months, days, hours, minutes, seconds))
        return await ctx.author.send(f'Your repeater was set for {discord.utils.format_dt(current_time)} UTC!')


    @commands.command(aliases=('del_repeater', 'remove_repeater', 'delete_repeater', 'close_repeater'), description='Adds a repeater to deletion queue.', brief='Deletes a repeater.')
    async def clear_repeater(self, ctx):
        reminders = 0
        for key in self.reminders_dict.keys():
            if ctx.author.id == key[0]:
                reminders += 1
        if reminders == 1:
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    self.to_del.append(key)
            return await ctx.message.reply('Repeater deletion added to queue.')
        elif reminders > 1:
            keys = list()
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    keys.append(key)
            string = f'You have **{len(keys)}** repeaters - '
            for index, key in enumerate(keys):
                if (index + 1) != len(keys):
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key][0])} UTC, '
                else:
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key][0])} UTC.'
            context = await ctx.author.send(
                f'{string} {ctx.author.mention} You have 60 seconds to reply to this message with the repeater to cancel(I.E 4, 7, 1).')

            def check(m):
                if m.author.id == ctx.author.id:
                    if m.reference is None:
                        return False
                    elif m.reference.message_id == context.id:
                        try:
                            if int(m.content) < len(keys) + 1 and int(m.content) > 0:
                                return True
                            else:
                                raise ValueError
                        except BaseException:
                            return False

            while True:
                try:
                    message = await self.bot.wait_for(event='message', timeout=60, check=check)
                except asyncio.exceptions.TimeoutError:
                    return await context.reply('Repeater deletion cancelled.')
                else:
                    self.to_del.append(keys[int(message.content) - 1])
                    return await message.reply(
                        f'Repeater deletion queued for {discord.utils.format_dt(self.reminders_dict[keys[int(message.content) - 1]][0])} UTC')
        else:
            await ctx.message.reply('You don\'t currently have any repeaters set.')


    @commands.command(aliases=('check_repeater', 'check_repeaters'), description='DMs a list of repeaters the current user has.', brief='Returns repeaters set.')
    async def repeaters(self, ctx):
        reminders = 0
        for key in self.reminders_dict.keys():
            if ctx.author.id == key[0]:
                reminders += 1
        if reminders == 1:
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    return await ctx.author.send(
                        f'{ctx.author.mention} Your repeater ends on {discord.utils.format_dt(self.reminders_dict[key][0])} UTC!')
        elif reminders > 1:
            keys = list()
            for key in self.reminders_dict.keys():
                if ctx.author.id == key[0]:
                    keys.append(key)
            string = f'You have **{len(keys)}** repeaters - '
            for index, key in enumerate(keys):
                if (index + 1) != len(keys):
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key][0])} UTC, '
                else:
                    string = f'{string}{discord.utils.format_dt(self.reminders_dict[key][0])} UTC.'
            return await ctx.author.send(f'{ctx.author.mention} {string}')
        else:
            return await ctx.message.reply('You do not currently have an active repeater.')


class fetch_data_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that return info or data.'


    @commands.command(aliases=('charinfo', 'char_info'), description='Returns the unicode version of <char> passed', brief='Unicode version of a character.')
    async def char(self, ctx, *, char):
        await ctx.send(f'`{char}`')


    @commands.command(aliases=('server_info', 'guild', 'guild_info', 'serverinfo', 'guildinfo'), description='Returns info and extra details of the current guild.', brief='Info on guild.')
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
        if  data >= 9999:
            data = '9999+'
        embed.add_field(name='Bans', value=f'**{data}** ban entries.')
        data = len(await (ctx.guild.audit_logs(limit=None)).flatten())
        if data >= 9999:
            data = '9999+'
        embed.add_field(name='Moderation actions', value=f'**{data}** actions.')
        embed.add_field(name='Premium', value=f'**{len(ctx.guild.premium_subscribers)}** server boosters.\n**{ctx.guild.premium_subscription_count}** boosts.\nBoost level **{ctx.guild.premium_tier}**.')
        await ctx.message.reply(embed=embed)


    @commands.command(aliases=('get_member_history', 'pull_member_history'), description='Returns [limit] message from <member> in the current channel. If [links] is True, returns link to messages.', brief='Returns messages <member> sent.')
    async def getch_member_history(self, ctx, member: discord.Member, limit: int = 10, links=False):
        try:
            bool(links)
        except ValueError:
            raise ValueError('Invalid boolean for "links".')
        member = await ctx.guild.getch_member(memberid)
        messages = []
        count = 0
        async for message in (ctx.channel.history(limit=None)):
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


    @commands.command(aliases=('bm', 'mark', 'book'), description='DMs a bookmark of the [message_id] (or replying message) and extra details.', brief='Bookmarks message.')
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



    @commands.command(aliases=('channel_member_count', 'channel_member#'), description='Number of members that can view the current channel.', brief='Members in the current channel.')
    async def channel_members(self, ctx):
        await ctx.send(f'{len(ctx.message.channel.members)} members are in the channel.')


    @commands.command(aliases=('members', 'member#'), description='Number of members in the current guild.', brief='Number of members in the current guild.')
    async def member_count(self, ctx):
        await ctx.send(f'{ctx.guild.member_count} members are in the guild.')


    @commands.command(aliases=('get_member', 'pull_member', 'member', 'info', 'info_on', 'member_info', 'member_data'), description='Returns data on member <member> for the current guild.', brief='Info on <member>.')
    async def getch_member(self, ctx, member: discord.Member):
        def is_author(payload: discord.RawReactionActionEvent):
            return (payload.guild_id is None) and ('????' in str(payload.emoji)) and (payload.user_id == ctx.author.id)
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
        logs =  0
        logs2 = 0
        async for i in (ctx.guild.audit_logs(limit=None)):
            if i.target == member:
                logs += 1
            else:
                continue
        async for i in (ctx.guild.audit_logs(limit=None, user=member)):
            if i.target == member:
                logs2 += 1
            else:
                continue
        embed.add_field(name='Moderation actions', value=f'{member} has **{logs}** actions performed on them, **{logs2}** of which were done on themselves.')
        context = await ctx.author.send(content=f'React to this message with :wave: to say hi to {member}!', embed=embed)
        await context.add_reaction('????')
        try:
            await self.bot.wait_for('raw_reaction_add', timeout=60, check=is_author)
        except asyncio.exceptions.TimeoutError:
            await context.remove_reaction(emoji='????', member=self.bot.user)
            return
        else:
            await context.remove_reaction(emoji='????', member=self.bot.user)
            try:
                await dm.send(f'{ctx.author.mention} said hi from **{ctx.guild}**!')
                await dm.send(f':wave:')
            except (
                        discord.HTTPException, discord.errors.HTTPException, discord.ext.commands.errors.CommandInvokeError,
                        ValueError, commands.CommandInvokeError, commands.CommandError, AttributeError, discord.Forbidden):
                await ctx.author.send(f'{ctx.author.mention} failed to send message to {member.mention}.')
            else:
                await ctx.author.send(f'{ctx.author.mention} successfully sent the message!')


    @commands.command(aliases=('get_user', 'pull_user', 'user', 'user_info', 'info_on_user', 'user_data'), description='Returns data on user <user>.', brief='Info on <user>.')
    async def getch_user(self, ctx, User: discord.User):
        def is_author(payload: discord.RawReactionActionEvent):
            return (payload.guild_id is None) and ('????' in str(payload.emoji)) and (payload.user_id == ctx.author.id)
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
        await context.add_reaction('????')
        try:
            await self.bot.wait_for('raw_reaction_add', timeout=60, check=is_author)
        except asyncio.exceptions.TimeoutError:
            await context.remove_reaction(emoji='????', member=self.bot.user)
            return
        else:
            await context.remove_reaction(emoji='????', member=self.bot.user)
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

    @commands.command(aliases=('e', 'eval'),
                      description='Returns the output of <python_code>, sends output in a .txt file if the lines are greater than 19',
                      brief='Evaluates output of <python_code>.')
    @commands.is_owner()
    async def evaluate(self, ctx, *, python_code: str):
        if not (ctx.message.attachments is None) and python_code is None:
            for index, attachment in enumerate(ctx.message.attachments):
                if any(i in str(attachment.filename).rsplit('.')[-1] for i in ('txt', 'py', 'python')):
                    name = f'{random.randint(0, 99999)}.{str(attachment.filename).rsplit(".")[-1]}'
                    file = await attachment.save(fp=fr'./{name}')
                    os.remove(fr'./{name}')
                    python_code = open(fr'./{name}', 'r').read()
        if python_code.startswith('```py'):
            python_code = python_code.lstrip('```py')
        elif python_code.startswith('```'):
            python_code = python_code.lstrip('```')
        elif python_code.startswith('`'):
            python_code = python_code.lstrip('`')
        if python_code.endswith('```'):
            python_code = python_code.rstrip('```')
        elif python_code.endswith('`'):
            python_code = python_code.rstrip('`')
        result = subprocess.run([sys.executable, "-c", python_code],
                                capture_output=True, text=True, timeout=5)
        if (f'''```
{result.stderr}
{result.stdout}
```'''.count('''
        ''') - 2) > 9 or len(f'''```
{result.stderr}
{result.stdout}
```''') > 1000:
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


    @commands.command(description='Owners only: Resets cooldown for command <command>.', brief='Resets a commands cooldown.')
    @commands.is_owner()
    async def reset_cooldown(self, ctx, *, command):
        command = self.bot.get_command(command)
        if command is None:
            await ctx.message.reply('Commands doesn\'t exist.')
            return
        command.reset_cooldown(ctx=ctx)
        await ctx.message.reply('Cooldown reset.')


    @commands.command(aliases=('terminate_bot', 'kill_bot', 'cut_bot'), description='Owners only: attempts to terminate the bots connection to the API.')
    @commands.is_owner()
    async def close_bot(self, ctx):
        await ctx.send('Bot terminating...')
        await bot.close()


    @commands.command(description='Owners only: Reloads the bots cogs.', brief='Owners only.')
    @commands.is_owner()
    async def restart_bot(self, ctx):
        await ctx.send(f'Reloading bot...')
        remove_cogs()
        await asyncio.sleep(2)
        add_cogs()


class print_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(description='Sends a message as the bot in the current channel.', brief='Sends a message as the bot.')
    async def print_out(self, ctx, *, message):
        member = await ctx.guild.getch_member(ctx.message.author.id)
        new_message = await ctx.message.channel.send(message)
        await member.send(
            f'{member.mention} you printed out a message in https://discord.com/channels/{ctx.guild.id}/{ctx.message.channel.id}/{new_message.id}.')
        await ctx.message.delete()


    @commands.command(description='Sends an embed as the bot in the current channel. [title] can be wrapped in quotes for multiples words.', brief='Sends an embed as the bot.')
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
        await ctx.send(embed=embed)
        await ctx.message.delete()
        if 'rule' in title.lower():
            with open('rules.json', 'r') as json_file:
                data = json.load(json_file)
            data[str(ctx.guild.id)] = text
            print(data)
            with open('rules.json', 'w') as json_file:
                json.dump(data, json_file)


@bot.command(aliases=('call', 'request'), description='Returns bots latency and other stats.', brief='Bots latency.')
async def ping(ctx):
    embed = discord.Embed(title='Status')
    if (bot.latency * 1000) > 119:
        embed.color = discord.Color.from_rgb(255, 0, 0)
    elif (bot.latency * 1000) > 79:
        embed.color = discord.Color.from_rgb(255,249,8)
    elif (bot.latency * 1000) > 39:
        embed.color = discord.Color.from_rgb(141,255,8)
    else:
        embed.color = discord.Color.from_rgb(000, 255, 000)
    embed.add_field(name='Ping', value=str(round(bot.latency * 1000)) + ' ms.')
    embed.add_field(name='Ratelimited', value=f'{bot.is_ws_ratelimited()}')
    try:
        await bot.getch_user(bot.user.id)
    except BaseException:
        embed.add_field(name='Connection', value='Down')
    else:
        embed.add_field(name='Connection', value='Working')
    async with ctx.message.channel.typing():
        try:
            await bot.wait_for(event='socket_event_type', timeout=10)
        except asyncio.exceptions.TimeoutError:
            embed.add_field(name='Websocket', value='Not recieving')
        else:
            embed.add_field(name='Websocket', value='Recieving')

        await asyncio.sleep(2)
    if success['last']:
        embed.add_field(name='Background ping', value=f'Last ping: Successful\nSuccessful pings: **{(success[True] / (success[True] + success[False])) * 100}%**')
    else:
        embed.add_field(name='Background ping', value=f'Last ping: Unsuccessful\nSuccessful pings: **{(success[True] / (success[True] + success[False])) * 100}%**')
    embed.add_field(name='Heroku status', value=f'Apps  :{requests.get("https://status.heroku.com/api/v4/current-status").json()["status"][0]["status"]}_circle:\nData  :{requests.get("https://status.heroku.com/api/v4/current-status").json()["status"][1]["status"]}_circle:\nTools :{requests.get("https://status.heroku.com/api/v4/current-status").json()["status"][2]["status"]}_circle:')
    
    await ctx.message.reply(embed=embed)


class reacting_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands related to managing reacting object keys in the current guild.'


    @commands.command(aliases=('update_react', 'add_react'), description = 'Adds a reacting object key for a message id.', brief = 'Creates a reacting object key.')
    @commands.has_permissions(manage_messages=True, manage_emojis=True)
    async def set_react(self, ctx, reacting_message_id: int, default_role_id: int, emoji_to_react: str):
        reacting[(ctx.guild.id, reacting_message_id)] = (
            default_role_id, emoji_to_react)
        await ctx.send(
            f'{ctx.author.mention} updated reacting object index: `{(ctx.guild.id, reacting_message_id)}: {(default_role_id, emoji_to_react)}`')


    @commands.command(aliases=('delete_react', 'rm_react', 'del_react'), description = 'Removes reacting data key for message id passed.', brief = 'Removes reacting data key for a message.')
    @commands.has_permissions(manage_messages=True, manage_emojis=True)
    async def remove_react(self, ctx, reacting_message_id: int):
        del reacting[(ctx.guild.id, reacting_message_id)]
        await ctx.send(f'{ctx.author.mention} deleted reacting object key: `{(ctx.guild.id, reacting_message_id)}`')


    @commands.command(aliases=('react_obj', 'react_object', 'react_dictionary'), description = 'Returns the object of reacting data for the current guild or message passed.', brief = 'Dictionary object for current guild or message.')
    async def react_dict(self, ctx, message_id: discord.Message = None):
        if message_id is None:
            d = dict()
            for key in reacting.keys():
                if key[0] == ctx.guild.id:
                    d[key] = reacting[key]
            await ctx.send(f"Reacting dictionary for current guild- `{d}`")
        else:
            await ctx.send(f"Reacting dictionary for message {message_id.id} `{'({0},{1}): {2}'.format(ctx.guild.id, message_id.id, reacting[(ctx.guild.id, message_id.id)])}`")


class filters_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands related to filters for the current guild.'

    @commands.command(aliases=('spam_filter', 'spam_check'), description = 'Sets spam filter level for the current guild.', brief = 'Sets spam filter level for the current guild.')
    @commands.has_permissions(manage_messages=True, moderate_members=True)
    async def spam(self, ctx, value):
        global filtering
        try:
            filtering[str(ctx.guild.id)]
        except KeyError:
            filtering[str(ctx.guild.id)] = 1
        if int(value) and int('-1') < int(value) < 5 or int(value) == 0:
            filtering[str(ctx.guild.id)] = int(value)
        else:
            raise ValueError('Invalid value for "spam_check".')
        await ctx.send(f'Spam filter level has been set to {value}.')


    @commands.command(aliases=('content_check', 'content_filter'), description='Turns content filtering for the current guild on or off.', brief='Enables/disables content filter.')
    @commands.has_permissions(manage_messages=True, moderate_members=True)
    async def content(self, ctx):
        message = ctx.message
        try:
            content_check[str(message.guild.id)]
        except KeyError:
            content_check[str(message.guild.id)] = 1
            return await ctx.message.reply(f'Content filtering for this guild has been set to **True**.')
        else:
            if bool(content_check[str(message.guild.id)]):
                content_check[str(message.guild.id)] = 0
            else:
                content_check[str(message.guild.id)] = 1
            return await ctx.message.reply(f'Content filtering for this guild has been set to **{content_check[str(message.guild.id)]}**.')



class channels_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that are related to modifying/managing channels in the current guild.'

    @commands.command(description = 'Creates a text channel', brief = 'Creates a text channel.')
    @commands.has_permissions(manage_channels=True)
    async def create_text_channel(self, ctx, name, *, reason='None'):
        await ctx.guild.create_text_channel(name=name, reason=reason)
        await ctx.send(f"{ctx.author.mention} create a text channel {name}.")


    @commands.command(description = 'Creates a VC.', brief = 'Creates a VC.')
    @commands.has_permissions(manage_channels=True)
    async def create_vc(self, ctx, name, *, reason='None'):
        await ctx.guild.create_voice_channel(name=name, reason=reason)
        await ctx.send(f"{ctx.author.mention} create a vc {name}.")


    @commands.command(aliases=('get_channels', 'pull_channels'), description = 'Returns all channels in the current guild. With links specified by [links]', brief = 'Returns all of the channels.')
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


    @commands.command(aliases=('remove_channels', 'end_channels'), description = 'Deletes multiple channels with ids passed.', brief = 'Deletes multiple channels.')
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


    @commands.command(aliases=('channel_clear', 'channel_clean'), description = 'Deletes and clones a channel.', brief = 'Deletes and clones a channel.')
    @commands.has_permissions(manage_channels=True)
    async def channel_purge(self, ctx, channel: discord.GroupChannel = None, *, reason='None'):
        if channel is None:
            channel = ctx.channel
        channel = ctx.channel
        new_channel = await channel.clone(name=channel.name, reason=reason)
        await channel.delete()


    @commands.command(aliases=('channel_del', 'channel_remove', 'channel_rm'), description = 'Deletes <channel> from the current guild.', brief = 'Deletes a channel.')
    @commands.has_permissions(manage_channels=True)
    async def channel_delete(self, ctx, channel: discord.GroupChannel = None, *, reason='None'):
        if channel is None:
            channel = ctx.channel
        await channel.delete()


class roles_cog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands that are related to managing roles.'


    @commands.command(description = 'Creates a role.', brief = 'Creates a role.')
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, name, *, reason='None'):
        await ctx.guild.create_role(name=name, reason=reason)
        await ctx.send(f"{ctx.author.mention} created role {name}.")


    @commands.command(aliases=('del_role', 'rm_role', 'remove_role'), description = 'Deletes a role.', brief = 'Deletes a role.')
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, role: discord.Role, *, reason='None'):
        await ctx.send(f'{ctx.author.mention} deleted role {role.name}.')
        await role.delete(reason=reason)


    #   overwrite = discord.PermissionOverwrite()
    #   overwrite.send_messages = True
    #   overwrite.read_messages = True
    #   await ctx.message.channel.set_permissions(member/role, overwrite=overwrite)


    @commands.command(aliases=('add_role', 'append_role'), description = 'Pushes a role on members specified.', brief = 'Adds a role to members.')
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
                member = await ctx.guild.getch_member(int(i))
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
        self.description = 'Commands that are related to checking rules and modifying them.'


    @commands.command(description = 'Returns a rule number [rule_int] from rules for the current guild.', brief = 'Returns a single rule.')
    async def rule(self, ctx, rule_int: int = None):
        with open('rules.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            data[str(ctx.guild.id)]
        except KeyError:
            await ctx.send(f'{ctx.author.mention} this server does not have set rules yet.')
        with open("rules.txt", 'w') as rules:
            rules.writelines(data[str(ctx.guild.id)])
        with open("rules.txt", 'r+') as rules:
            await ctx.send(rules.readlines()[rule_int - 1])


    @commands.command(description = 'Returns an embed with the current guilds rules.', brief = 'Rules for the current guild.')
    async def rules(self, ctx):
        bot_author = await ctx.guild.getch_member(self.bot.user.id)
        with open('rules.json', 'r') as json_file:
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


    @commands.command(aliases=['rule_append'], description = 'Adds a rule to the curren set of guild rules.', brief = 'Creates a new rule.')
    @commands.has_permissions(moderate_members=True, view_audit_log=True)
    async def rule_add(self, ctx, *, text: str = 'None'):
        bot_author = await ctx.guild.getch_member(self.bot.user.id)
        with open('rules.json', 'r') as json_file:
            data = json.load(json_file)
        try:
            data[str(ctx.guild.id)]
        except KeyError:
            await ctx.send(f'{ctx.author.mention} this server does not have set rules yet.')
            return
        data[str(ctx.guild.id)] = f'{data[str(ctx.guild.id)]}\n{text}'
        with open('rules.json', 'w') as json_file:
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


    @commands.command(aliases=['rule_change'], description = 'Replaces rule number [rule_ind] with a new rule.', brief = 'Replaces a rule.')
    @commands.has_permissions(moderate_members=True, view_audit_log=True)
    async def rule_replace(self, ctx, rule_ind: int, *, read: str):
        bot_author = await ctx.guild.getch_member(self.bot.user.id)
        with open('rules.json', 'r') as json_file:
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
        with open('rules.json', 'w') as json_file:
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


    @commands.command(aliases=('rule_rm', 'rule_delete', 'rule_del'), description = 'Removes rule number [rule_ind] for current guild rules.', brief = 'Removes a rule.')
    @commands.has_permissions(moderate_members=True, view_audit_log=True)
    async def rule_remove(self, ctx, rule_ind: int = 0):
        bot_author = await ctx.guild.getch_member(self.bot.user.id)
        with open('rules.json', 'r') as json_file:
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
        with open('rules.json', 'w') as json_file:
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
        self.description = 'Commands that have to do with guild logs.'


    @commands.command(aliases=('fetch_logs', 'get_logs', 'pull_logs'), description = 'Returns a .txt file of logs collected from the current bot session in the current guild.', brief = 'Returns logs for current guild.')
    @commands.has_permissions(view_audit_log=True)
    async def logs(self, ctx):
        with (open('logs.json', 'r')) as json_file:
            data = json.load(json_file)
        with open('logs.txt', 'w') as file:
            file.write(str(data[str(ctx.guild.id)]))
        await ctx.author.send(content=f'{ctx.author.mention} logs from the current bot session for **{ctx.guild}**:', file=discord.File(r'./logs.txt'))


    @commands.command(aliases=('delete_logs', 'del_logs', 'rm_logs', 'remove_logs'), description = 'Deletes all logs for the current guild.', brief = 'Deletes logs from current guild.')
    @commands.has_permissions(view_audit_log=True)
    async def clear_logs(self, ctx):
        with (open('logs.json', 'r')) as json_file:
            data = json.load(json_file)
            data[str(ctx.guild.id)] = 0
        with (open('logs.json', 'w')) as json_file:
            json.dump(data, json_file)
        await ctx.send(f'{ctx.author.mention} cleared all logs from bot session in **{ctx.guild}**.')


class extras_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.giveaways_dict = dict()
        self.description = 'Commands that do not fall into any other category.'


    @commands.command(aliases=('format_date', 'format_dt', 'format_time'), description='Formats arguments passed into discord timestamp formating.', brief='Returns a timestamp.')
    async def format(self, ctx, years: int = datetime.utcnow().year, months: int = datetime.utcnow().month,
                     days: int = datetime.utcnow().day, hours: int = datetime.utcnow().hour,
                     minutes: int = datetime.utcnow().minute, seconds: int = datetime.utcnow().second):
        current_time = datetime.utcnow()
        try:
            current_time = current_time.replace(year=years, month=months, day=days, hour=hours, minute=minutes,
                                                second=seconds)
        except BaseException:
            await ctx.message.reply('That isn\'t a valid datetime.')
        except:
            await ctx.message.reply(str(discord.utils.format_dt(current_time)))


    @commands.command(aliases=('utc_now', 'utcnow'), description='Returns the current UTC time, plus additions specified.', brief='The current time in UTC.')
    async def utc(self, ctx, years: int=0, months: int=0, days: int=0, hours: int=0, minutes: int=0):
        await ctx.message.reply(f'{discord.utils.format_dt((datetime.utcnow() + timedelta(days=days + months*30 + years*365, hours=hours, minutes=minutes)).strftime("20%y-%m-%d %r"))}, {(datetime.utcnow() + timedelta(days=days + months*30 + years*365, hours=hours, minutes=minutes)).strftime("20%y-%m-%d %r")}')


    @commands.command(aliases=['g'], description='Sends a message for users to react to, once done, randomly picks the number of members passed.', brief='Starts a giveaway.')
    @commands.cooldown(1, 600, commands.BucketType.member)
    async def giveaway(self, ctx: commands.Context, members: int=3, role_to_mention: discord.Role=None, hours: int=0, minutes: int=10):
        context = await ctx.author.send(f'{ctx.author.mention} are you sure you want to start a giveaway in **{ctx.guild}** to **{members}** users?')
        await context.add_reaction('???')
        await context.add_reaction('???')
        if members > 10 or members < 1:
            await ctx.message.reply('Please enter more than 0 users, and less than 11.')
            return ctx.command.reset_cooldown(ctx)
        while True:
            try:
                payload = await self.bot.wait_for('raw_reaction_add', timeout=120, check=lambda payload: payload.user_id == ctx.author.id and str(payload.emoji) in ('???', '???') and payload.message_id == context.id)
            except asyncio.exceptions.TimeoutError:
                await ctx.message.reply('Giveaway cancelled.')
                ctx.command.reset_cooldown(ctx)
                return
            else:
                if '???' in str(payload.emoji):
                    break
                else:
                    await ctx.message.reply('Giveaway cancelled.')
                    ctx.command.reset_cooldown(ctx)
                    return
        icon = ctx.guild.icon
        if icon is None:
            icon = self.bot.user.avatar
            if icon is None:
                icon = self.bot.user.default_avatar.url
            else:
                icon = icon.url
        else:
            icon = icon.url
        current_time = datetime.utcnow()
        current_time = current_time + timedelta(minutes=10)
        if role_to_mention is None:
            embed = discord.Embed(color=ctx.author.color, description=f'**{ctx.author}** is hosting a giveaway that ends {discord.utils.format_dt(current_time + timedelta(seconds=hours * 60 * 60 + minutes*60), style="R")} with **{members}** winners!')
        else:
            embed = discord.Embed(color=ctx.author.color, description=f'{role_to_mention.mention} **{ctx.author}** is hosting a giveaway that ends {discord.utils.format_dt(current_time + timedelta(seconds=hours * 60 * 60 + minutes*60), style="R")} with **{members}** winners!')
        embed.set_author(icon_url=icon, name=f'Giveaway in {ctx.guild}!')
        embed.set_footer(icon_url=icon, text=f'Giveaway in {ctx.guild} on {str(ctx.message.created_at).rsplit(" ")[0]} started by {ctx.author}.')

        added = list()
        class view(discord.ui.View):

            @discord.ui.button(label='Join Giveaway!', style=discord.ButtonStyle.green)
            async def callback(self: discord.ui.view, button: discord.ui.Button, interact: discord.MessageInteraction):
                if not interact.author.id in added:
                    for i in range(3):
                        added.append(interact.author.id)
                    await interact.send(ephemeral=True, content='You successfully joined the giveaway!')
                else:
                    await interact.send(ephemeral=True, content='You already joined the giveaway.')


        context = await ctx.message.reply(embed=embed, view=view())
        await asyncio.sleep(hours * 60 * 60 + minutes*60)
        await context.edit(view=None)

        winners = list()
        if len(added) > members:
            pass
        else:
            await ctx.message.reply(f'Less than **{members}** people joined the giveaway.')
            return ctx.command.reset_cooldown(ctx)
        self.giveaways_dict[(ctx.guild.id, ctx.message.channel.id, context.id)] = [added, members]
        for i in range(members):
            winner = random.choice(added)
            winners.append(ctx.guild.get_member(winner).mention)
            added.remove(winner)
        winner = '\n'.join(winners)
        embed = discord.Embed(title='Winners', description=winner)
        await context.reply(ctx.author.mention, embed=embed)


    @commands.command()
    async def reroll(self, ctx, message: discord.Message=None):
        print(self.giveaways_dict[(message.guild.id, message.channel.id, message.id)])
        if message is None and ctx.message.reference is None:
            return await ctx.send('Please reply to the giveaway message or enter an id to reroll.')
        elif isinstance(message, discord.Message):
            try:
                prev = self.giveaways_dict[(message.guild.id, message.channel.id, message.id)]
                data = self.giveaways_dict[(message.guild.id, message.channel.id, message.id)]
            except KeyError:
                return await ctx.send('Please reply to the giveaway message or enter an id to reroll.')
            else:
                print('hello', data)
                winners = list()
                for i in range(data[1]):
                    winner = random.choice(data[0])
                    winners.append(ctx.guild.get_member(winner).mention)
                thing = '\n'.join(winners)
                embed = discord.Embed(title='Winners', description=thing)
                del self.giveaways_dict[(message.guild.id, message.channel.id, message.id)]
                self.giveaways_dict[(message.guild.id, message.channel.id, message.id)] = prev
                return await message.reply(ctx.author.mention, embed=embed)
        elif not(ctx.message.reference is None):
            message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            try:
                prev = list(self.giveaways_dict[(message.guild.id, message.channel.id, message.id)])
                data = list(self.giveaways_dict[(message.guild.id, message.channel.id, message.id)])
            except KeyError:
                return await ctx.send('Please reply to the giveaway message or enter an id to reroll.')
            else:
                winners = list()
                for i in range(data[1]):
                    winner = random.choice(data[0])
                    winners.append(ctx.guild.get_member(winner).mention)
                winner = '\n'.join(winners)
                embed = discord.Embed(title='Winners', description=winner)
                del self.giveaways_dict[(message.guild.id, message.channel.id, message.id)]
                self.giveaways_dict[(message.guild.id, message.channel.id, message.id)] = prev
                return await message.reply(ctx.author.mention, embed=embed)

    @commands.command(aliases=['add_topic'], description = 'Requests a topic verification to be added by the bot owner.', brief = 'Adds a topic.')
    @commands.cooldown(1, 420, commands.BucketType.user)
    async def topic_add(self, ctx, *, topic: str):
        owner = await self.bot.getch_user(self.bot.owner_id)
        icon = ctx.message.author.avatar
        if icon is None:
            icon = ctx.message.author.default_avatar.url
        else:
            icon = icon.url
        embed = discord.Embed(title='Topic verification request', color=ctx.author.color,
                              description=f'{ctx.author.mention} is requesting verification for the topic:\n`{topic}`\n The request will be automatically denied in 10 minutes.')
        embed.set_author(name=ctx.author, icon_url=icon)
        icon = ctx.guild.icon
        if icon is None:
            icon = ctx.message.author.avatar
            if icon is None:
                icon = ctx.message.author.default_avatar.url
            else:
                icon = icon.url
        else:
            icon = icon.url
        embed.set_footer(
            text=f'{ctx.author} requested topic verification in {ctx.guild} at {str(ctx.message.created_at).rsplit(".")[0]}',
            icon_url=icon)
        context = await owner.send(embed=embed)
        await context.add_reaction('???')
        await context.add_reaction('???')
        await ctx.author.send(f'{ctx.author.mention} your topic request is being verified by the owner.')

        def check(payload: discord.RawReactionActionEvent):
            return payload.user_id == owner.id and payload.channel_id == context.channel.id and any(
                i in str(payload.emoji) for i in ('???', '???'))

        try:
            data = await self.bot.wait_for(event='raw_reaction_add', timeout=600, check=check)
        except asyncio.exceptions.TimeoutError:
            await context.reply('Request automatically denied due to inactivity.')
            await ctx.author.send(f"{ctx.author.mention} The owner did not respond to the request.")
        else:
            if '???' in str(data.emoji):
                await context.reply('Topic verification request approved!')
                await ctx.author.send(f"{ctx.author.mention} Your topic verification request has been approved!")
                topics.append((topic, ctx.message))
            else:
                await context.reply('Topic verification request denied!')
                await ctx.author.send(f"{ctx.author.mention} Your topic verification request has been denied!")
        await context.remove_reaction(emoji='???', member=self.bot.user)
        await context.remove_reaction(emoji='???', member=self.bot.user)

    @commands.command(description = 'Finds a random topic from a list entered by users.', brief = 'Picks a random topic.')
    @commands.cooldown(1, 120, commands.BucketType.channel)
    async def topic(self, ctx):
        ind = random.choice(topics)
        message = ind[1]
        embed = discord.Embed(title=str(ind[0]), color=message.author.color,
                              description='Want to add a topic? run `>topic_add <topic>` to request a topic verification by the owner!')
        icon = message.author.avatar
        if icon is None:
            icon = message.author.default_avatar.url
        else:
            icon = icon.url
        embed.set_author(icon_url=icon, name=message.author)
        icon = message.guild.icon
        if icon is None:
            icon = message.author.avatar
            if icon is None:
                icon = message.author.default_avatar.url
            else:
                icon = icon.url
        else:
            icon = icon.url
        print(icon)
        embed.set_footer(
            text=f'{message.author} added a topic in {message.guild} on {str(message.created_at).rsplit(" ")[0]}.',
            icon_url=icon)
        await ctx.message.reply(embed=embed)


    @commands.command(aliases=['nickname'], description = 'Sets <member>s nickname to [new_nick].', brief = 'Renames a member.')
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, new_nick: str=None):
        if new_nick is None:
            new_nick = f'Member-{random.randint(0, 999999)}'
        await member.edit(nick=new_nick)
        await ctx.message.reply(f'{member.mention}\'s name was changed to **{new_nick}**.')


class alarm_cog(commands.Cog):

    @tasks.loop(seconds=1)
    async def check_alarms(self):
        await self.bot.wait_until_ready()
        for index, key in enumerate(self.to_del):
            del self.alarms_dict[key]
            self.to_del.pop(index)
        now = datetime.utcnow()
        for key in self.alarms_dict.keys():
            data = self.alarms_dict[key]
            for day in data[0]:
                if data[4]:
                    if (int(self.DAYS_INT[day]) - 1):
                        if int(data[1]) == now.hour:
                            if int(now.minute) == data[2]:
                                try:
                                    user = (await self.bot.getch_user(key[0]))
                                    await user.send(f'{user.mention} alarm `{data[3]}` has gone off!')
                                    self.alarms_dict[key] = [data[0], data[1], data[2], data[3], False]
                                    await asyncio.sleep(60)
                                    try:
                                        self.alarms_dict[key]
                                    except KeyError:
                                        return
                                    else:
                                        self.alarms_dict[key] = [data[0], data[1], data[2], data[3], True]
                                    return
                                except (discord.NotFound, discord.Forbidden):
                                    print(f'Could not find user {key[0]} for alarm.')
                                    self.to_del.append(key)


    def __init__(self, bot):
        self.bot = bot
        self.alarms_dict = dict()
        self.to_del = list()
        self.DAYS_STRING = {'1??????': 'Monday', '2??????': 'Tuesday', '3??????': 'Wednesday', '4??????': 'Thursday', '5??????': 'Friday',
                            '6??????': 'Saturday', '7??????': 'Sunday'}
        self.DAYS_INT = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6,
                         'Sunday': 7}
        self.check_alarms.start()
        self.description = 'Commands related to the bots alarm system.'


    @commands.command(aliases=('set_alarm', 'new_alarm'), description = 'Creates a new alarm with name [name].', brief = 'Creates an alarm.')
    async def alarm(self, ctx, *, name: str=f'alarm-{random.randint(0, 99999)}'):
        days = list()
        hour = 0
        minute = 0
        context = await ctx.message.reply('React to this message with every day of the week(Mon-Sun) you want, and confirm.')
        for emoji in ('1??????', '2??????', '3??????','4??????', '5??????', '6??????', '7??????', '???'):
            await context.add_reaction(emoji)
        while True:
            try:
                reaction = await self.bot.wait_for(event='raw_reaction_add', timeout=60, check= lambda raw_reaction: raw_reaction.user_id == ctx.author.id and any(i in str(raw_reaction.emoji) for i in ('1??????', '2??????', '3??????','4??????', '5??????', '6??????', '7??????', '???')) and raw_reaction.message_id == context.id)
            except asyncio.exceptions.TimeoutError:
                return await context.reply('Alarm creation cancelled due to inactivity.')
            else:
                if '???' in str(reaction.emoji) and len(days) > 0 and len(days) < 8:
                    break
                elif not(str(reaction.emoji) in days):
                    days.append(str(reaction.emoji))
        await context.clear_reactions()
        context = await context.edit(content='Reply to this message with the hour you want your alarm to go off.')
        while True:
            try:
                message = await self.bot.wait_for(event='message', timeout=60, check=lambda m: m.content.isdigit() and m.author.id == ctx.author.id)
            except asyncio.exceptions.TimeoutError:
                return await context.reply('Alarm creation cancelled due to inactivity.')
            else:
                if int(message.content) > -1 and int(message.content) < 24:
                    hour = int(message.content)
                    break
                else:
                    await message.delete()
        context = await context.edit(content='Reply to this message with the minute you want your alarm to go off.')
        while True:
            try:
                message = await self.bot.wait_for(event='message', timeout=60, check=lambda m: m.content.isdigit() and m.author.id == ctx.author.id)
            except asyncio.exceptions.TimeoutError:
                return await context.reply('Alarm creation cancelled due to inactivity.')
            else:
                if message.reference is None:
                    continue
                if message.reference.message_id == context.id :
                    pass
                else:
                    continue
                if int(message.content) > -1 and int(message.content) < 60:
                    minute = int(message.content)
                    break
                else:
                    await message.delete()
        for index, emoji in enumerate(days):
            days[index] = self.DAYS_STRING[emoji]
        self.alarms_dict[(ctx.author.id, random.randint(0, 99999))] = [days, hour, minute, name, True]
        await context.edit(content=f'Alarm `{name}` successfully set!')


    @commands.command(aliases=('clear_alarm', 'delete_alarm', 'remove_alarm'), description = 'Deletes an alarm.', brief = 'Deletes an alarm.')
    async def del_alarm(self, ctx):
        found = False
        for key in self.alarms_dict.keys():
            if ctx.author.id == key[0]:
                found = True
                break
        if found:
            pass
        else:
            return await ctx.message.reply('You do not currently have any alarms set.')
        alarms = list()
        for key in self.alarms_dict.keys():
            if ctx.author.id == key[0]:
                alarms.append(key)
        string = ''
        data = list()
        for key in alarms:
            data.append(self.alarms_dict[key])
        string = f'You have **{len(data)}** alarms - '
        for index, value in enumerate(data):
                string = f'{string}alarm `{value[3]}` goes off **{len(value[0])}** days a week on {str(value[1]).zfill(2)}:{str(value[2]).zfill(2)}\n'
        context = await ctx.message.reply(content=string + '\n Reply with the name of the alarm you want to delete.')
        while True:
            try:
                m = await self.bot.wait_for('message', timeout=60, check=lambda m: m.author.id == ctx.author.id)
            except asyncio.exceptions.TimeoutError:
                return await context.reply('Deletion cancelled due to inactivity.')
            else:
                if m.reference is None:
                    continue
                elif m.reference.message_id == context.id:
                    for key in self.alarms_dict.keys():
                        if m.content.lower() in self.alarms_dict[key][3].lower():
                            if self.alarms_dict[key] in data:
                                print(key)
                                self.to_del.append(key)
                                return await context.reply(f'alarm `{m.content}` queued for deletion.')


    @commands.command(aliases=('check_alarms', 'view_alarms'), description = 'Returns all alarms for current member.', brief = 'Returns all alarms.')
    async def alarms(self, ctx):
        found = False
        for key in self.alarms_dict.keys():
            if ctx.author.id == key[0]:
                found = True
                break
        if found:
            pass
        else:
            return await ctx.message.reply('You do not currently have any alarms set.')
        alarms = list()
        for key in self.alarms_dict.keys():
            if ctx.author.id == key[0]:
                alarms.append(key)
        string = ''
        data = list()
        for key in alarms:
            data.append(self.alarms_dict[key])
        string = f'You have **{len(data)}** alarms - '
        for index, value in enumerate(data):
                string = f'{string}alarm `{value[3]}` goes off **{len(value[0])}** days a week on {str(value[1]).zfill(2)}:{str(value[2]).zfill(2)}\n'
        await ctx.message.reply(content=string)


@tasks.loop(minutes=1)
async def ping():
    global success
    await bot.wait_until_ready()
    try:
        user = await bot.getch_user(bot.user.id)
    except BaseException:
        success[False] += 1
        success['last'] = False
    else:
        success[True] += 1
        success['last'] = True

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
    bot.remove_cog(ticket_cog(bot))
    bot.remove_cog(extras_cog(bot))
    bot.remove_cog(reminder_cog(bot))
    bot.remove_cog(alarm_cog(bot))
    bot.remove_cog(repeater_cog(bot))


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
    bot.add_cog(cog=ticket_cog(bot), override=True)
    bot.add_cog(cog=extras_cog(bot), override=True)
    bot.add_cog(cog=reminder_cog(bot), override=True)
    bot.add_cog(cog=alarm_cog(bot), override=True)
    bot.add_cog(cog=repeater_cog(bot), override=True)



add_cogs()


bot.run(TOKEN)
