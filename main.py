import discord
from discord.ext import commands
import logging
import asyncio
import datetime
from datetime import date
import os

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='bot.')
bot.remove_command('help')

bot.owner_id = 263560579770220554



cogs = [
    'interact',
    'moderation',
    'all_user_commands'
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
            if int(current_hour) == 2 and int(current_minute) == 30:
                await channel.send(' ```Meeting Reminder```***@everyone meeting in 30min ! *** ')
            else:
                pass

        elif date.today().weekday() == 5:
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(254664901102927873)
            if int(current_hour) == 3 and int(current_minute) == 00:
                await channel.send(' ```Meeting Reminder```***@everyone meeting in 24 Hours ! *** ')
            else:
                pass


        """elif date.today().weekday() == 1 or date.today().weekday() == 4:
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(480399532253773834)
            if int(current_hour) == 00 and int(current_minute) == 00:
                await channel.send(' ```War Reminder```*** @everyone shields up ! war spin in 2 hours ! *** ')
            else:
                pass
        elif date.today().weekday() == 0 or date.today().weekday() == 3:
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(480399532253773834)
            if int(current_hour) == 2 and int(current_minute) == 00:
                await channel.send(' ```War Reminder```*** @everyone shields up ! war spin in 24 hours ! *** ')
            else:
                pass"""

        await asyncio.sleep(60)  # task runs every 60 seconds


async def background_task_2():

    await bot.wait_until_ready()
    while not bot.is_closed():

        if date.today().weekday() == 1 or date.today().weekday() == 4:
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(480399532253773834)
            if int(current_hour) == 4 and int(current_minute) == 00:
                await channel.send(' this is a test! ')
            else:
                pass

        elif date.today().weekday() == 0 or date.today().weekday() == 3:
            current_hour = datetime.datetime.now().hour
            current_minute = datetime.datetime.now().minute
            channel = bot.get_channel(480399532253773834)
            if int(current_hour) == 2 and int(current_minute) == 10:
                await channel.send(' ```War Reminder```*** @everyone shields up ! war spin in 24 hours ! *** ')
            else:
                pass

        await asyncio.sleep(60)  # task runs every 60 seconds

bot.reminder_task = bot.loop.create_task(background_task_2())


@commands.command()
async def cancelwr(ctx):
    bot.reminder_task.cancel()
    await ctx.send("war reminders are now turned off")


@commands.command()
async def runwr(ctx):
    bot.reminder_task = bot.loop.create_task(background_task_2())
    await ctx.send("war reminders are now turned on")


@bot.event
async def on_ready():
    logging.info('Running as {}'.format(bot.user.name))
    logging.info(bot.user.id)
    await bot.change_presence(activity=discord.Game(name='Where\'s my Water?'))


bot.loop.create_task(background_task())
bot.run(os.environ.get('token'))
