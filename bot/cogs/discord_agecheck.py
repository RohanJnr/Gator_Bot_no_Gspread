import datetime

import discord
from discord.ext import commands

from bot.constants import Channels, Client, Roles


class DiscordAgeCheck(commands.Cog):
    """A cog to check how long people have been in our server."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='check', invoke_without_command=True)
    async def days_check(self, ctx):
        """Check how old the members/trials are in the server."""
        await ctx.invoke(self.bot.get_command("help"), "check")

    @days_check.command(name='members')
    async def member_days_check(self, ctx, no_of_days=90):
        """shows members who are more than 90 days old in the server."""
        guild = self.bot.get_guild(id=Client.guild)
        # channel = discord.utils.get(guild.channels, id=Channels.bot_logs)
        member_role = discord.utils.get(guild.roles, id=Roles.member)
        embed = discord.Embed()
        embed.colour = 0x01d277
        embed.title = f'Members who have stayed in the server for more than {no_of_days} days !'
        message = ''
        for member in member_role.members:
            today = datetime.datetime.now()
            days_stayed = (today-member.joined_at).days

            if days_stayed > no_of_days:

                message += '{:<{}s}'.format(member.name, 30) + ' - ' + str(days_stayed) + ' days. \n'
            else:
                pass
        embed.description = '```' + message + '```'
        await ctx.send(embed=embed)

    @days_check.command(name='trials')
    async def trials_days_check(self, ctx, number_of_days=14):
        """shows trials who are more than 14 days old in the server."""
        guild = self.bot.get_guild(id=Client.guild)
        # channel = discord.utils.get(guild.channels, id=Channels.bot_logs)
        member_role = discord.utils.get(guild.roles, id=Roles.trial)
        embed = discord.Embed()
        embed.colour = 0x01d277
        embed.title = f'Trials who have stayed in the server for more than {number_of_days} days !'
        message = ''
        for member in member_role.members:
            today = datetime.datetime.now()
            days_stayed = (today - member.joined_at).days

            if days_stayed > number_of_days:

                message += '{:<{}s}'.format(member.name, 30) + ' - ' + str(days_stayed) + ' days. \n'
            else:
                pass
        embed.description = '```' + message + '```'
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(DiscordAgeCheck(bot))
