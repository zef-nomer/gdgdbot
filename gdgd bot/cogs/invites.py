import discord
from discord.ext import commands


class name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite1(self, ctx):
        if ctx.author.id == 595998891934220339:
            await ctx.send("guild")


def setup(bot):
    bot.add_cog(name(bot))