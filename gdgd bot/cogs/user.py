import discord
from discord.ext import commands
from discord.ext.commands.core import command
import json

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
    aliases=["Аватар", "аватар", "Аватарка", "аватарка", "Avatar", ],
    description='посмотреть аватарку игрока',
    usage='аватар <@ник>')


    async def avatar(self, ctx, member: discord.Member = None):
        user = ctx.message.author if (member == None) else member

        embed = discord.Embed(title=f'Аватарка {user}', color=0x2b86fd)

        embed.set_image(url=user.avatar_url)
        embed.set_footer(text="Все права защищены")
        await ctx.send(embed=embed)

    @commands.command()
    async def setcolor(self, ctx, color):
        with open("colorsm.json", "r") as f:
            a = json.load(f)
        b = a["1"]
        print(b)



def setup(bot):
	bot.add_cog(User(bot))