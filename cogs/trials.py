from discord.ext import commands
from discord import Member
import requests
import typing


class TrailMembers(commands.Cog):

    def __int__(self, bot):
        self.bot = bot

    @commands.command(name="trials")
    async def start_trials(self, ctx, user: typing.Optional[Member] = None, player_tag=None):
        if user is not None and player_tag is not None:
            """ 
            check if linked user has the same tag when compared to the given player_tag
            and proceed.
            """
            pass
        elif player_tag is not None and user is None:
            """ 
            append player with the tag to the database.
            """
            pass
        elif user is not None and player_tag is None:
            """
            Check whether the user is linked to this coc account and then proceed to add the tag
            to the database.
            """
            pass


def setup(bot):
    bot.add_cog(TrailMembers(bot))
