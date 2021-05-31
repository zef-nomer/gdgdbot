import hmtai
import discord
from discord.ext import commands


class name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(hmtai.useHM("v1", "hentai"))
        else:
            ctx.send('Используйте эту команду только в nsfw каналах!')


def setup(bot):
	bot.add_cog(name(bot))