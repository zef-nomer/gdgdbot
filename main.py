import discord
from discord.ext import comands
import levelsys

cogs = [levelsys]

bot = comands.Bot(command_prefix = "+/", intents = discord.Intents.all())

for i in range(len(cogs)):
    print("load")


bot.run("")
#mongodb+srv://Zef1r:<password>@xtench.y6pt9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority