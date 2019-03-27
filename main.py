import discord
from discord.ext import commands
import logging
import asyncio
import datetime
from datetime import date
import os

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='.')

bot.owner_id = 263560579770220554


cogs = [
    'clashapi',
    'interact',
    'moderation',
    'all_user_commands',
    'war_strats',
    'notes',
    'events'  # DOES NOT WORK
]

for cog in cogs:
    bot.load_extension('cogs.' + cog)


async def background_task():

    await bot.wait_until_ready()
    while not bot.is_closed():

        if date.today().weekday() == 6:

            # Reminder for weekly meeting at 10 PM EST
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(254664901102927873)
            if int(current_hour) == 1 and int(current_minute) == 30:
                await channel.send(' ```Meeting Reminder```***@everyone meeting in 30min ! *** ')
            else:
                pass

        elif date.today().weekday() == 5:
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
    logging.info('Running as {}'.format(bot.user.name))
    logging.info(bot.user.id)
    await bot.change_presence(activity=discord.Game(name='Where\'s my Water?'))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{error} : Please provide all the necessary arguments.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("The following command does not exist.")
    else:
        await ctx.send(str(error))

bot.loop.create_task(background_task())
bot.run(os.environ.get('token'))
