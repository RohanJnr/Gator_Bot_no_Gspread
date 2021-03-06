from discord.ext import commands
import random
import requests


class FunStuff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        """
        Flips a coin
        """
        x = random.choice(['Heads', 'Tails'])
        await ctx.send(x)

    @commands.command()
    async def magic8ball(self, ctx):
        """
        Magic8ball
        """
        my_response = [
            ":8ball: It is certain ",
            ":8ball: It is decidedly so ",
            ":8ball: Without a doubt ",
            ":8ball: Yes, definitely ",
            ":8ball: You may rely on it ",
            ":8ball: As I see it, yes ",
            ":8ball: Most likely ",
            ":8ball: Outlook good ",
            ":8ball: Yes ",
            ":8ball: Signs point to yes ",
            ":8ball: Reply hazy try again ",
            ":8ball: Ask again later ",
            ":8ball: Better not tell you now ",
            ":8ball: Cannot predict now ",
            ":8ball: Concentrate and ask again ",
            ":8ball: Don't count on it ",
            ":8ball: My reply is no",
            ":8ball: My sources say no ",
            ":8ball: Outlook not so good ",
            ":8ball: Very doubtful :"
        ]
        x = random.choice(my_response)
        await ctx.send(x)

    @commands.command()
    async def rps(self, ctx, c):
        """
        Play rock, paper or scissors game with the bot.
        eg : bot.rps rock
        """
        try:
            bot_answer = random.choice(("Rock", "Paper", "Scissor"))

            if c.lower() in ("rock", "r"):
                player_answer = "Rock"

            elif c.lower() in ("paper", "p"):
                player_answer = "Paper"

            elif c.lower() in ("scissor", "s"):
                player_answer = "Scissor"

            if bot_answer == player_answer:
                return await ctx.send(f"Bot picked {bot_answer}, so did you... It's a tie!")

            if bot_answer == "Rock" and player_answer == "Scissor":
                return await ctx.send("Bot picked Rock, you picked Scissor... Bot wins!")

            if bot_answer == "Scissor" and player_answer == "Paper":
                return await ctx.send("Bot picked Scissor, you picked Paper... Bot wins!")

            if bot_answer == "Paper" and player_answer == "Rock":
                return await ctx.send("Bot picked Paper, you picked Rock... Bot wins!")

            await ctx.send(f"Bot picked {bot_answer}, you picked {player_answer}... You win!")
        except:
            await ctx.send('Please enter your answer')

    @commands.command(name="joke")
    async def get_joke(self, ctx):
        """
        Retruns a joke.
        """
        r = requests.get("https://api.icndb.com/jokes/random")
        data = r.json()
        values = data['value']
        joke = values['joke']
        await ctx.send(joke)

    @commands.command(name='random')
    async def random_number(self, ctx, number: int):
        """Returns a random number from 1-input number."""
        number_emojis = {
            '0': ':zero:',
            '1': ':one:',
            '2': ':two:',
            '3': ':three:',
            '4': ':four:',
            '5': ':five:',
            '6': ':six:',
            '7': ':seven:',
            '8': ':eight:',
            '9': ':nine:',
        }
        rand_number = str(random.randrange(1, number+1))
        message = ''
        for num in rand_number:
            emoji = number_emojis[num]
            message += emoji
        await ctx.send(message)


def setup(bot):
    bot.add_cog(FunStuff(bot))
