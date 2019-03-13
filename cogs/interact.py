from discord.ext import commands
import datetime
# import humanify

admin_ids = ['255409211385708546', '255403079669645312', '255419757895876608']


class HelpCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cwlhelp(self, ctx):
        """
        shows the help command for cwl related commands.
        """
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
        """
        shows the help command for updating data in recruitment sheets.(admin cmd)
        """
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
        """
        shows help command for recruitment. (admin cmd)
        """
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


def setup(bot):
    bot.add_cog(HelpCommands(bot))
