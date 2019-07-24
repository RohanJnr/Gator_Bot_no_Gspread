import logging

import discord
from discord.ext import commands
from discord.utils import get

from bot.constants import Channels, Roles
from bot.checks import in_guild


logger = logging.getLogger(__name__)


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    # @in_guild(251099476243120128)
    async def on_member_join(self, member: discord.Member):

        guild = member.guild
        elder = guild.get_role(Roles.elder)
        co_leader = guild.get_role(Roles.co_leader)

        message = f"Welcome {member.mention}. To apply please post a screenshot of your WAR BASE " \
                  f"and PLAYER PROFILE, as well as your age and location (time zone). " \
                  f"Once your posts are up an {elder.mention} or {co_leader.mention} will be with you" \
                  f" as soon as they can. Be patient if it isn't immediate. Be prepared " \
                  f"to discuss your history playing COC, favorite attack strategies, " \
                  f"and your approach to attack planning.   In the meantime, familiarize " \
                  f"yourself with our rules in #gators-information. Thank you for your " \
                  f"interest in Golden Gators!-Leadership Team"
        channel = get(member.guild.channels, name='applications')
        role = guild.get_role(Roles.candidate)
        if Roles.candidate not in [role.id for role in member.roles]:
            await member.add_roles(role)
        await channel.send(message)

    @commands.Cog.listener()
    # @in_guild(251099476243120128)
    async def on_member_remove(self, member):
        channel = get(member.guild.channels, id=Channels.bot_logs)
        await channel.send(f"{member.name} has left the server!")


def setup(bot):
    bot.add_cog(Events(bot))
    # add this cog in main.py as well in the cogs list as the file name
