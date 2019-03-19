from discord.ext import commands
from discord import Embed
import sqlite3


class WarStrats(commands.Cog):
    """
    A cog where war strategies can be viewed from and add to the database.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="strats")
    async def war_strats(self, ctx, townhall, *, attack_name=None):
        """
        This command is used to view a war strategy by specifying the townhall and attack name
        or all attack strategies can be viewed by just passing the townhall level.
        """
        if int(townhall) > 12:
            return await ctx.send("Invalid townhall level!")
        embed = Embed()
        embed.description = ""
        embed.colour = 0x01d277
        conn = sqlite3.connect("goldengators.db")
        c = conn.cursor()
        if attack_name is None:
            c.execute("SELECT * FROM strategies WHERE townhall="+townhall+"")
            all_strats = c.fetchall()
            print(all_strats)
            if len(all_strats) == 0:
                embed.title = f'There are no attack strategies avilable for {townhall} :'
                embed.description += 'None'
            else:
                embed.title = f'Avilable strategies for TownHall {townhall} are :'
                for strat in all_strats:
                    embed.description += strat[1].capitalize() + '\n'
                conn.close()

        else:
            c.execute("SELECT * FROM strategies WHERE townhall="+townhall+" and name='"+attack_name.lower()+"'")
            strat = c.fetchone()
            if strat is None:
                return await ctx.send(f"No such strategy called {attack_name}")
            embed.title = f'{attack_name} for TownHall {townhall} :'
            embed.description = f"{strat[2]} \n Reference : {strat[3]}"

        await ctx.send(embed=embed)

    @commands.command(name="addstrat")
    async def add_strategy_to_db(self, ctx, *, info):
        """
        Add an attack strategy to the database.
        syntax : bot.addstrat <townhall level>-<attack name>-<description>-<reference(youtube or any)>
        """
        townhall, name, description, reference = info.split('-')
        if int(townhall) > 12:
            return await ctx.send("Invalid townhall level!")
        conn = sqlite3.connect("goldengators.db")
        c = conn.cursor()
        c.execute("SELECT * FROM strategies WHERE townhall=" + townhall + " and name='" + name.lower() + "'")
        strat = c.fetchone()
        if strat is None:
            c.execute("""INSERT INTO strategies VALUES (
                        """+townhall+""",
                        '"""+name.lower()+"""',
                        '"""+description+"""',
                        '"""+reference+"""'
                    )""")
            conn.commit()
            conn.close()
            await ctx.send(f'Attack strategy {name} for townhall {townhall} has been added !')
        else:
            await ctx.send(f"Attack strategy already registered.")

    @commands.command(name="removestrat")
    @commands.has_any_role(255403079669645312, 255409211385708546, 255419757895876608)
    async def remove_strat_from_db(self, ctx, *, info):
        """
        Removes a strat from the database.
        argument : Info : <townhall level>-<attack name>
        """
        townhall, name = info.split('-')
        conn = sqlite3.connect("goldengators.db")
        c = conn.cursor()
        c.execute("DELETE FROM strategies WHERE townhall=" + townhall + " and name='" + name.lower() + "'")
        conn.commit()
        conn.close()
        await ctx.send(f"Attack stratgy {name} has been removed for townhall {townhall} from the database.")

    @war_strats.error
    async def war_strats_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send("```Please specify townhall level also and in the correct order!```")
        else:
            await ctx.send(str(error))


def setup(bot):
    bot.add_cog(WarStrats(bot))
    # add this cog in main.py as well in the cogs list as the file name
