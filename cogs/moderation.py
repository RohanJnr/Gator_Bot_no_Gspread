from discord.ext import commands


class Moderation:

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

    @commands.command()
    @commands.is_owner()
    async def rename(self, ctx, *, name):
        """
        owner command.
        """
        await self.bot.user.edit(username=name)


def setup(bot):
    bot.add_cog(Moderation(bot))
