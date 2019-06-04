import random

import discord
from discord.ext import commands


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
    async def get_reddit(self, ctx, subreddit=None):
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
        embed.title = post['data']['title']
        embed.description = post['data']['selftext'][0:50]
        embed.set_image(url=imageURL)

        embed.description += f'\n**{post["data"]["ups"]}** {upvote} '
        embed.description += f'**{post["data"]["downs"]}** {downvote} '
        embed.description += f'\n**{post["data"]["num_comments"]}** {comment} '

        embed.set_footer(text=f'Posted by {post["data"]["author"]} in r/{subreddit}.')
        embed.url = post['data']['url']

        await ctx.send(embed=embed)

