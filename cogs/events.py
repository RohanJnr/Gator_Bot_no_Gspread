from discord.ext import commands


# import libs here


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(error + " : Please provide all the necessary arguments.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("The following command does not exist.")


def setup(bot):
    bot.add_cog(Events(bot))
    # add this cog in main.py as well in the cogs list as the file name
