import discord
from discord.ext import commands


class Join(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = bot.get_channel(833053710955184158)
		mjoin = discord.Embed(title=f"Member Join", color=discord.Colour.purple())
		mjoin.set_author(icon_url= f"{member.avatar_url}", name=f"{member.name}")
		mjoin.add_field(name="Пользователь", value=member.mention)
		mjoin.add_field(name="ID Пользователя:", value=member.id)
		mjoin.add_field(name="Имя Пользователя:", value=member.name)
		mjoin.set_thumbnail(url = member.avatar_url)
		await channel.send(embed=mjoin)


def setup(bot):
	bot.add_cog(Join(bot))