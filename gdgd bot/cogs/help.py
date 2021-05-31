import discord
from discord.ext import commands


class Help12(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		emb = discord.Embed( title = 'Информация по командам(В РАЗРАБОТКЕЕЕЕЕЕ)', colour = discord.Colour.purple() )
		emb.add_field ( name = 'Стандартные команды', value = "`*help` - вывести список всех доступных команд.\n"
			"`*ri [размер] [размер2]` - случайная картинка.\n"
			"`*rdog` - случайная картинка собаки.\n")
		emb.add_field ( name = 'Развлечения', value = "`*say` [что хотите сказать] - сообщение от лица бота\n" 
			"`*embed [имя] [описание]` - создать Embed с именем и описанием.\n"
													  "`*wikip [что хотите найти]` - поиск информации в Wikipedia."
													  "")
		#emb.add_field ( name = '', value = "" )
		#emb.add_field ( name = '', value = "" )
		await ctx.send( embed = emb )

	#@commands.Cog.listener() - event
	#@commands.commands() - комманда

	#async def ...(self, ctx ...) - self, параметр обязательный. После self идёт ctx.


def setup(bot):
	bot.add_cog(Help12(bot))



'''
Образец Кога

class name(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	...


def setup(bot):
	bot.add_cog(name(bot))
'''