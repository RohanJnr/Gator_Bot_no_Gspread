import asyncio
import datetime
import logging
import os

import discord
from discord.ext import commands

from bot.constants import Client

logging.basicConfig(level=logging.INFO)


def get_prefix(client, message):

    prefixes = Client.prefixes
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(
    command_prefix=get_prefix,
    description='A dev bot',
    owner_id=Client.owner_id,
    case_insensitive=True
)

cogs = [
    'cogs.all_user_commands',
    'cogs.clashapi',
    'cogs.discord_agecheck',
    'cogs.interact',
    # 'cogs.moderation',
    'cogs.reddit',
    'cogs.notes',
    'cogs.trials',
    'cogs.war_strats',
    'cogs.events'
]
for cog in cogs:
    bot.load_extension(cog)


@bot.event
async def on_ready():
    logging.info(f'Running as {bot.user.name}')
    logging.info(bot.user.id)
    await bot.change_presence(activity=discord.Game(name='spotify'))


async def background_task():

    await bot.wait_until_ready()
    while not bot.is_closed():

        if datetime.date.today().weekday() == 6:

            # Reminder for weekly meeting at 10 PM EST
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(254664901102927873)
            if int(current_hour) == 1 and int(current_minute) == 30:
                await channel.send(' ```Meeting Reminder```***@everyone meeting in 30min ! *** ')
            else:
                pass

        elif datetime.date.today().weekday() == 5:
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(254664901102927873)
            if int(current_hour) == 2 and int(current_minute) == 00:
                await channel.send(' ```Meeting Reminder```***@everyone meeting in 24 Hours ! *** ')
            else:
                pass
        await asyncio.sleep(60)  # task runs every 60 seconds


async def trail_update():
    """
    updates existing trial member's war results in database.
    """
    pass


@bot.event
async def on_ready():
    logging.info(f'Running as {bot.user.name}')
    logging.info(bot.user.id)
    await bot.change_presence(activity=discord.Game(name='Where\'s my water ?'))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{error} : Please provide all the necessary arguments.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("The following command does not exist.")
    else:
        await ctx.send(str(error))
        raise error


# bot.loop.create_task(background_task())
bot.run(Client.token, bot=True, reconnect=True)
