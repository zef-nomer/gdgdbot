import discord
from discord.ext import commands
from asyncio import sleep


class Say(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def say(self, ctx, *, str = None):
		if str is None:
			sayerror = discord.Embed(description='Не правильный синтаксис команды. *say [тескст]', colour=discord.Colour.red())
			await ctx.author.send(embed=sayerror)
			await sleep(3)
			await ctx.message.delete()
		else:
			embed = discord.Embed(description = str, colour = discord.Colour.purple())
			await ctx.send(embed=embed)
			await sleep(3)
			await ctx.message.delete()

	@commands.command()
	async def embed(self, ctx, *, arg = None):
		def check(message):
			return message.author == ctx.author and message.channel == ctx.channel

		await ctx.send('Укажите `title`')
		title = await self.bot.wait_for('message', check=check)

		await ctx.send('Укажите `description`')
		desc = await self.bot.wait_for('message', check=check)

		embed = discord.Embed(title=title.content, description=desc.content, color=0xff6700)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Say(bot))