from discord.ext import commands
from discord import Embed
import sqlite3


class Notes(commands.Cog):
    """
    A set of commands to work with notes : Add, view, delete.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='newnote')
    async def add_note(self, ctx, *, info):
        """
        Use this command to add notes.
        syntax: bot.newnote <title>-<description>
        """
        title, description = info.split('-', 1)
        conn = sqlite3.connect('goldengators.db')
        c = conn.cursor()
        title = title.lower()
        notes_info = (title, description)
        c.execute('INSERT INTO notes VALUES (?, ?)', notes_info)
        conn.commit()
        conn.close()
        await ctx.send(f'`{title}` note added !')

    @commands.command(name='note')
    async def view_note(self, ctx, title=None):
        """
        Use this command to view note/notes.
        syntax: bot.note <title>
        """
        conn = sqlite3.connect('goldengators.db')
        c = conn.cursor()
        embed = Embed()
        embed.colour = 0x68c290
        if title is None:
            embed.title = 'All Notes'
            embed.description = ''
            c.execute('SELECT * from notes')
            data = c.fetchall()
            if not data:
                embed.description += 'None'
            else:
                for item in data:
                    embed.description += item[0] + '\n'
        else:
            c.execute('SELECT * FROM notes WHERE title = ?', (title,))
            data = c.fetchone()
            embed.title = data[0].capitalize()
            embed.description = "``` " + str(data[1]) + "```"
        await ctx.send(embed=embed)

    @commands.command(name='delnote')
    async def delete_note(self, ctx, title):
        """
        Use this command to delete notes.
        syntax: bot.delnote <title>
        """
        conn = sqlite3.connect('goldengators.db')
        c = conn.cursor()
        c.execute('DELETE FROM notes WHERE title= ?', (title,))
        conn.commit()
        conn.close()
        await ctx.send(f'`{title}` note has been removed!')


def setup(bot):
    bot.add_cog(Notes(bot))
