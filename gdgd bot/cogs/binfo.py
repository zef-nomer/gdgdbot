import discord
from discord.ext import commands
import color

class Info(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title = "Инфо о боте.", description = "<:error~1:844250054210617405>")
		await ctx.send(embed=embed)

	@commands.command()
	async def binfo(self, ctx):
		embed = discord.Embed(
			title = "Инфо о боте",
			description = "<:error:844540322829828126>*Изначально бот задумывался в качестве __личного__ бота, но автора переклинило, и он сделал общедоступного бота(некоторые фишки до сих пор доступны для одного сервера)*\n\n"
			"Создатель: **Zef1rchik#0632**\n\n"
			"Начальный префикс: *(в скором времени будет изменено)\n\n"
			"Помощь по коммандам: *help",
			colour = color.red
		)
		await ctx.send(embed = embed)

#711677614024294402   :animal_cat_kruto_ubeyte:
def setup(bot):
	bot.add_cog(Info(bot))