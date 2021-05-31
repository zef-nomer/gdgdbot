import discord
from discord.ext import commands
import wikipedia


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="w")
    async def wiki(self, ctx, *, arg = None):
        if arg is None:
            embed = discord.Embed(
                title="🛑Ошибка🛑",
                description="Укажите объект, про которого нужно найти ниформацию в википедии.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            wikipedia.set_lang("ru")
            info = wikipedia.summary(arg, sentences=2)
            title = wikipedia.page(arg).title
            embed = discord.Embed(title=title,
                                      description=f"```{info}```",
                                      color=discord.Color.orange())
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_footer(text="Wikipedia\nGDGD")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wiki(bot))