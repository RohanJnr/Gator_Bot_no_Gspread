from discord.ext import commands
from discord import Member, Embed
import requests
import sqlite3
import os


class ClashAPI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.base_url = 'https://api.clashofclans.com/v1/'
        self.headers = {'authorization': os.environ.get('coctoken'), 'Accept': 'application/json'}

    def api_response(self, uri, params=None):
        url = self.base_url + uri
        try:
            r = requests.get(url, params=params, headers=self.headers)
        except Exception as e:
            print(str(e))
        json_data = r.json()
        status = r.status_code
        return json_data, status

    @commands.group(name="player", invoke_without_command=True)
    async def player(self, ctx, tag=None, user: Member = None):
        """
        Use this command to view your clash profile or other clasher's profile.
        how to use :
        --> Providing tag only
            eg : bot.player <tag>
        --> Linking your account.
            Link your clash account using the command `bot.player link` first.
            And then try `bot.player`.
        --> You can also view other people's profile by tagging them provided that
            their account is linked.
        """
        if user is None and tag is None:
            conn = sqlite3.connect('goldengators.db')
            c = conn.cursor()
            c.execute("SELECT * FROM coclinks WHERE discordID = ?", (ctx.author.id, ))
            player = c.fetchone()
            tag = player[1]
            tag = tag[1:]
            conn.close()

        elif user is not None and tag is None:
            conn = sqlite3.connect('goldengators.db')
            c = conn.cursor()
            c.execute("SELECT * FROM coclinks WHERE discordID = ?", (user.id,))
            player = c.fetchone()
            tag = player[1]
            tag = tag[1:]
            conn.close()

        elif user is not None and tag is not None:
            return await ctx.send("Either tag the user or provide the tag.")

        if tag.startswith('#'):
            tag = tag[1:]

        uri = 'players/%23' + tag
        params = {}
        json_data, status_code = self.api_response(uri, params)
        if status_code >= 400:
            return await ctx.send('Player not found !')
        embed = Embed()
        embed.title = "Player Info"
        embed.description = f"```Player Tag       : {json_data['tag']}          \n"
        embed.description += f"Player Name      : {json_data['name']}         \n"
        embed.description += f"Player TonwHall  : {json_data['townHallLevel']}\n"
        embed.description += f"Player Trophies  : {json_data['trophies']}     \n"
        embed.description += f"Player WarStars  : {json_data['warStars']}     ```\n"
        embed.color = 0x01d277
        await ctx.send(embed=embed)

    @player.command(name='link')
    async def link_account(self, ctx, tag):
        """
        Link your account using this command.
        syntax : bot.player link <tag>
        """
        if not tag.startswith('#'):
            tag = '#' + tag
            tag = tag.upper()

        conn = sqlite3.connect('goldengators.db')
        c = conn.cursor()
        value_tuple = (ctx.author.id, tag)
        with conn:
            c.execute("INSERT INTO coclinks VALUES(?, ?)", value_tuple)
        conn.close()
        await ctx.send("You have been linked to your clash of clans account ! Try `bot.player` command.")

    @player.command(name='unlink')
    async def unlink_account(self, ctx):
        """
        Un link your clash account.
        """
        conn = sqlite3.connect('goldengators.db')
        c = conn.cursor()
        with conn:
            c.execute("DELETE FROM coclinks WHERE discordID = ?", (ctx.author.id,))
        conn.close()
        await ctx.send("Your account is now not linked.")

    @player.error
    async def player_cmd_error(self, ctx, error):
        await ctx.send(str(error))


def setup(bot):
    bot.add_cog(ClashAPI(bot))
