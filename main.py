import disnake
from disnake.ext import commands

import os
from datetime import datetime
from data import save, load, default_server_data, default_user_data
from data import servers_data, create_server_space, check_users_data, archive_server, restore_server
# CLIENT = BOT
client = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

# XXX : EVENTS
# ON READY
@client.event
async def on_ready():
    try:
        pass
    except Exception as error:
        print(error)
# ON GUILD JOIN
@client.event
async def on_guild_join(guild: disnake.Guild):
    try:
        pass
    except Exception as error:
        print(error)
# ON GUILD REMOVE
@client.event
async def on_guild_remove(guild: disnake.Guild):
    try:
        pass
    except Exception as error:
        print(error)
# ON GUILD UPDATE
@client.event
async def on_guild_update(before: disnake.Guild, after: disnake.Guild):
    try:
        pass
    except Exception as error:
        print(error)
# ON MEMBER JOIN
@client.event
async def on_member_join(member: disnake.Member):
    try:
        pass
    except Exception as error:
        print(error)
# ON MEMBER REMOVE
@client.event
async def on_member_remove(member: disnake.Member):
    try:
        pass
    except Exception as error:
        print(error)
# ON MEMBER UPDATE
@client.event
async def on_member_update(before: disnake.Member, after: disnake.Member):
    try:
        pass
    except Exception as error:
        print(error)
# ON ROLE CREATE
@client.event
async def on_guild_role_create(role: disnake.Role):
    try:
        pass
    except Exception as error:
        print(error)
# ON ROLE DELETE
@client.event
async def on_guild_role_delete(role: disnake.Role):
    try:
        pass
    except Exception as error:
        print(error)
# ON ROLE UPDATE
@client.event
async def on_guild_role_update(before: disnake.Role, after: disnake.Role):
    try:
        pass
    except Exception as error:
        print(error)
# ON CHANNEL CREATE
@client.event
async def on_guild_channel_create(channel: disnake.abc.GuildChannel):
    try:
        pass
    except Exception as error:
        print(error)
# ON CHANNEL DELETE
@client.event
async def on_guild_channel_delete(channel: disnake.abc.GuildChannel):
    try:
        pass
    except Exception as error:
        print(error)
# ON CHANNEL UPDATE
@client.event
async def on_guild_channel_update(before: disnake.abc.GuildChannel, after: disnake.abc.GuildChannel):
    try:
        pass
    except Exception as error:
        print(error)
# ON MESSAGE
@client.event
async def on_message(message: disnake.Message):
    try:
        pass
    except Exception as error:
        print(error)
# ON MESSAGE EDIT
@client.event
async def on_message_edit(before: disnake.Message, after: disnake.Message):
    try:
        pass
    except Exception as error:
        print(error)
# ON MESSAGE DELETE
@client.event
async def on_message_delete(message: disnake.Message):
    try:
        pass
    except Exception as error:
        print(error)

# XXX : SLASH_COMMANDS

@client.slash_command()
@commands.default_member_permissions(administrator=True)
async def blank_command(inter: disnake.ApplicationCommandInteraction):
    try:
        pass
    except Exception as error:
        print(error)

# XXX : RUN

client.run(open("TOKEN", "r").read())
