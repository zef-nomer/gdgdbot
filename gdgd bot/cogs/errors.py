import discord
from discord.ext import commands
import json


class Error(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed=discord.Embed(description=f'** {ctx.author.name}, тебе не кажется что команды нет? что то мне подсказывает...**',
                                               color=discord.Color.red())
        
            
            with open("counters.json", "r") as f:
                count = json.load(f)

            count["uncorrect"] += 1
    
            with open("counters.json", "w") as f:
                json.dump(count,f)

            with open("counters.json", "r") as f:
                q = json.load(f)

            uncorrect = q["uncorrect"]

            embed.set_footer(text=f"Ты ввёл {uncorrect} неправильную комманду!")

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Error(bot))
