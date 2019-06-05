import logging
import random

import asyncio
import html5lib
import aiohttp

from bs4 import BeautifulSoup
import discord
from discord.ext import commands


logger = logging.getLogger(__name__)


class RedditCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def fetch(self, session, url):
        params = {
            'limit': 50
        }
        headers = {
            'User-Agent': 'Iceman'
        }

        async with session.get(url=url, params=params, headers=headers) as response:
            return await response.json()

    @commands.command(name='reddit')
    async def get_reddit(self, ctx, subreddit='clashofclans'):
        """
        Fetch reddit posts by using this command.

        Gets a post from r/dndmemes by default.
        """
        session = self.bot.http_session
        data = await self.fetch(session, f'https://www.reddit.com/r/{subreddit}/hot/.json')

        try:
            posts = data["data"]["children"]
        except KeyError:
            return await ctx.send('Subreddit not found!')
        if not posts:
            return await ctx.send('No posts available!')

        upvote = ':thumbsup:'
        downvote = ':thumbsdown:'
        comment = ':envelope:'
        post = random.choice(posts)
        imageURL = post['data']['url']
        embed = discord.Embed()
        embed.colour = 0xf9f586
        embed.title = str(post['data']['title'])[0:101]
        embed.description = str(post['data']['selftext'])[0:201]
        embed.set_image(url=imageURL)

        embed.description += f'\n**{post["data"]["ups"]}** {upvote} '
        embed.description += f'**{post["data"]["downs"]}** {downvote} '
        embed.description += f'\n**{post["data"]["num_comments"]}** {comment} '

        embed.set_footer(text=f'Posted by {post["data"]["author"]} in r/{subreddit}.')
        embed.url = post['data']['url']

        await ctx.send(embed=embed)

    @commands.command(name='lootindex')
    async def get_loot_index(self, ctx):
        SELECTED_URL = 'http://clashofclansforecaster.com/'

        async with aiohttp.ClientSession() as session:
            async with session.get(SELECTED_URL) as resp:
                text = await resp.read()

        sites_soup = BeautifulSoup(text.decode('utf-8'), 'html5lib')
        so = str(sites_soup.text)
        # print(so[119428:119431])
        x = so.index('lootIndexString')
        await ctx.send(so[x + 20:x + 23])


def setup(bot):
    bot.http_session = aiohttp.ClientSession()
    bot.add_cog(RedditCog(bot))
    logger.debug("Reddit cog loaded.")
