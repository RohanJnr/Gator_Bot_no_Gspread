import discord
from discord.ext import commands

from bot.constants import Channels

class Moderation(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx: commands.Context, cog_name: str):
        """
        to check load of cogs
        OWNER COMMAND.
        """

        try:
            self.bot.unload_extension('cogs.' + cog_name)
            self.bot.load_extension('cogs.' + cog_name)
        except ModuleNotFoundError:
            await ctx.send("Module \"" + cog_name + "\"wasnt found")
            return 0
        except Exception as e:
            await ctx.send("Unknown error " + str(e) + "has occured !")

        await ctx.send("All modules loaded successfully !")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # sql = mysql_query('SELECT logs FROM command_status WHERE guild_id = %s', (426566445124812813,))
        log_channel = Channels.bot_logs
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.title = f'Message edited\nby {before.author} in #{before.channel}'
        embed.description = ''
        embed.add_field(name='Before', value=before.content, inline=False)
        embed.add_field(name='After', value=after.content, inline=False)
        channel = self.bot.get_channel(log_channel)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        log_channel = Channels.bot_logs
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.title = f'Message deleted\nby {message.author} in #{message.channel}'
        embed.description = message.content
        channel = self.bot.get_channel(log_channel)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
