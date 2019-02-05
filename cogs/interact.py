from discord.ext import commands
import datetime
import humanify

admin_ids = ['255409211385708546', '255403079669645312', '255419757895876608']


class Commands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        msg = ''' ```1) bot.rhelp - shows help commands for recruitment. (admin cmd)
2) bot.cwlhelp - shows the help command for cwl registration.
3) bot.uhelp - shows the help command for updating data in recruitment sheets.(admin cmd)
4) bot.show_time - shows the current time in UTC``` '''
        await ctx.send(msg)

    @commands.command()
    async def cwlhelp(self, ctx):
        msg = ''' ```1) bot.cwl - Adds a players info to cwl rooster.
Usage : <IGN>-<TownHall level>-<can you war all days?(yes or no)>
Example : bot.cwl Iceman-9-yes
Example : bot.cwl Iceman-9-no
2) bot.cwlinfo - Searchs for a player and returns their info in cwl rooster
Usage  : <ign_of_member_to_search>
Example : bot.cwlinfo Iceman 

3) bot.cwlview - Shows all participants.

4) bot.summary

5) bot

```'''
        await ctx.send(msg)

    @commands.command()
    async def uhelp(self, ctx):
        if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
            msg = ''' ```1) bot.ustatus - Updates a players Recruitment Status.
        Usage  : <ign> - <new status>
        Example : bot.ustatus Iceman-Member
    2) bot.udd - Updates a players Date Decisioned
        ***Usage  : <ign> - <date in format MM/DD/YY>
        Example : bot.udd Iceman-10/13/18***               
    3) bot.uw1 - Updates a players Trails_War_1 result
        Usage : <ign> - <war 1 result without any hyphens (-)>               
        Example bot.uw1 Iceman - 1. 1star above 3 base 2. 3star below 5 base 
                    
        Note : the war 1 result can be given in any format(even words) but make sure there are no hyphens              
    4) bot.uw2 - Updates a players Trails_War_2 result
        Usage : <ign> - <war 2 result without any hyphens (-)>               
        Example bot.uw1 Iceman - 1. 1star above 3 base , 2. 3star below 5 base
                  
        Note : the war 2 result can be given in any format(even words) but make sure there are no hyphens```'''
            await ctx.send(msg)
        else:
            await ctx.send('You do not have permission to use this command !')

    @commands.command()
    async def rhelp(self, ctx):
        if admin_ids[0] or admin_ids[1] or admin_ids[2] in [role.id for role in ctx.message.author.roles]:
            msg = ''' ```1) bot.add - Adds a players info to docs.(admin cmd)
    Usage  : <@tag the user><give a space><IGN> - <TownHall level> - <PlayerTag> - <age> - <location>
    Example : bot.add @Iceman#6508 Iceman-9-#759IFLKS-16-India
    2) bot.info - Searches for a player and returns their info.(admin cmd)
    Usage  : <ign_of_member_to_search>
    Example : bot.info Iceman```'''
            await ctx.send(msg)
        else:
            await ctx.send('You do not have permission to use this command !')

    @commands.command()
    async def fun(self, ctx):
        msg = """
        ```    1)flip - flips a coin
            2)magic8ball <question>
            3)bot.rps - rock paper scissor(you can type r for rock,p for paper and s for scissor)```
        
        """
        await ctx.send(msg)

    @commands.command()
    async def show_time(self, ctx):
        current_time = datetime.datetime.now()
        await ctx.send(humanify.datetime(current_time) + ' UTC')

        """@commands.command()
    async def hello(self, ctx):
        await ctx.send('Hola !')

    @commands.command()
    async def info(self, ctx, *, member: discord.Member):
        info = discord.Embed(
            title=f'Info about {member.display_name}',
            description=f'Join at {humanify.datetime(member.joined_at)}'
        )
        await ctx.send(embed=info)

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.invoke(self.info, member = ctx.author)
            logging.info('sent info about the author : commands.MissingRequiredArgument')
    """


def setup(bot):
    bot.add_cog(Commands(bot))
