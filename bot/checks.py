import discord
from discord.ext import commands


def in_guild(guild_id):
    async def predicate(member: discord.Member):

        if member.guild.id == guild_id:
            return True
        else:
            return False
        
    return commands.check(predicate)
