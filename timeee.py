import discord
from discord.ext import commands
import urllib
from urllib.request import urlretrieve
import psutil

token = ("NzExODI1NDg0NjE0NDY3NjA0.XsIpJA.K8hueTwufqqY2WD1TFZs0bL5JXE")
bot = commands.Bot(command_prefix='/')

@bot.command(aliases=['ri'])
async def rimage(ctx, size = None, size2 = None):
    if size is None:
        emb = discord.Embed(title='🛑Ошибка синтаксиса🛑', description='Правильный синтаксис:\n'
                                                                       '```*ri размер - если хотите получить квадратную картинку. За место "размер" введите размер картики```\n'
                                                                       '```*ri размер1 размер2 - если хотите получить не квадратную картинку. За место "размер1" и "размер2" введите рахмер картинки```',
                            colour=discord.Colour.purple())
        await ctx.send(embed = emb)
    elif size2 is None:
        try:
            urlretrieve(f'https://picsum.photos/{size}', 'one1.jpg')
            await ctx.send(f'Квадратная картика размером {size}', file = discord.File(r'one1.jpg') )
        except:
            eri = discord.Embed(title='🛑Ошибка🛑', description='Попробуйте изменить значения комманды',
                                 colour=discord.Colour.red())
            await ctx.send(embed = eri)
    elif size2 is not None:
        try:
            urlretrieve(f'https://picsum.photos/{size}/{size2}', 'one.jpg')
            emb = discord.Embed(title='Картинка', colour = discord.Colour.purple())
            await ctx.send(f'Картинка размером {size}*{size2}', file=discord.File(r'one.jpg'))
        except:
            eri1 = discord.Embed(title='🛑Ошибка🛑', description='Попробуйте изменить значения комманды', colour=discord.Colour.red())
            await ctx.send(embed = eri1)

bot.run(token)