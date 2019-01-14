from discord.ext import commands
# import libs here


class ClassName:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cmd_name(self, ctx, more_parameters_here):
        # do something
        pass


def setup(bot):
    bot.add_cog(ClassName(bot))
    # add this cog in main.py as well in the cogs list as the file name
