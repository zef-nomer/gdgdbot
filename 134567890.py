from discord.ext import commands
from asyncio import sleep
import discord
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

TOKEN = "NzExODI1NDg0NjE0NDY3NjA0.XsIpJA.ji8O_03Ru6HIjwzVL-jL-sMAZho"

bot = commands.Bot(command_prefix=('*'), intents = discord.Intents.all())
bot.remove_command( 'help' )

@bot.event
async def on_member_join(member):
        channel = bot.get_channel(830719922501582849) #здесь айди канала которому хочешь отправить сообщение
        mjoin = discord.Embed(title=f"Member Join", color=discord.Colour.purple())
        mjoin.set_author(icon_url= f"{member.avatar_url}", name=f"{member.name}")
        mjoin.add_field(name="Пользователь", value=member.mention)
        mjoin.add_field(name="ID Пользователя:", value=member.id)
        mjoin.add_field(name="Имя Пользователя:", value=member.name)
        mjoin.set_thumbnail(url = member.avatar_url)
        await channel.send(embed=mjoin)

@bot.event
async def on_ready():
    print("Я запущен!")
    #await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='NBS😇'))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
    #await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="NBS😇"))
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    while True:
        await sleep(15)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="NBS😇"))
        await sleep(15)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="*help"))


@bot.command()
async def Hi(ctx):
    await ctx.send('Hi')

@bot.command()
async def test1(ctx):
    embed = discord.Embed(
        title="Привет всем!",
    )
    await ctx.send(embed=embed)

@bot.command()
async def wiki(ctx):
    embed = discord.Embed(
        title="Wikipedia",
        description="Ссылка для перехода на wiki",
        url='https://ru.wikipedia.org/wiki/Заглавная_страница',
    )
    await ctx.send(embed=embed)

@bot.command(pass_context = True)

async def help( ctx ):
    emb = discord.Embed( title = 'Информация по командам(В РАЗРАБОТКЕЕЕЕЕЕ)', colour = discord.Colour.purple() )

    emb.add_field ( name = '```{}wiki```'.format ( "*" ), value = "Переход на вики-сайт" )
    emb.add_field ( name = '{}В разработке'.format ( "*" ), value = "В разработке" )
    emb.add_field ( name = '{}В разработке'.format ( "*" ), value = "В разработке" )
    emb.add_field ( name = '{}В разработке'.format ( "*" ), value = "В разработке" )
    await ctx.send( embed = emb )

#jopa(сообщения с эмодзи через каждые 20 м)
@bot.command()
async def say(ctx, *, str = None):
    if str is None:
        sayerror = discord.Embed(description='Не правильный синтаксис команды. *say [тескст]', colour=discord.Colour.red())
        await ctx.author.send(embed=sayerror)
    embed = discord.Embed(description = str, colour = discord.Colour.purple())
    await ctx.send(embed=embed)

#rgb основные коды
@bot.command()
async def rgb(ctx):
    emb_rgb = discord.Embed( title = 'Основные цвета в rgb', colour = discord.Colour.purple() )
    emb_rgb.add_field(name='```Red```', value="```255 0 0```")
    emb_rgb.add_field(name='```Green```', value="```0 255 0```")
    emb_rgb.add_field(name='```Blue```', value="```0 0 255```")
    emb_rgb.add_field(name='```Cyan```', value="```0 0 255```")
    await ctx.send( embed = emb_rgb )

#rgb2
@bot.command()
async def rgb2(ctx):
    emb_rgb2 = discord.Embed( title = 'Основные цвета в rgb', description = '```Red : 255 0 0``` \n ```Green : 0 255 0``` \n ```Blue : 0 0 255```', colour = discord.Colour.purple() )
    #emb_rgb.add_field(name='```Blue```', value="```0 0 255```")
    #emb_rgb.add_field(name='```Cyan```', value="```0 0 255```")
    await ctx.send( embed = emb_rgb2 )

#invite
@bot.command()
async def invite(ctx):
    invemb = discord.Embed(
        title='Invite',
        description="Пригласить бота на сервер",
        url='https://discord.com/oauth2/authorize?client_id=711825484614467604&scope=bot&permissions=8',
        colour = discord.Colour.purple()
    )
    invemb.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    await ctx.send( embed = invemb )

#4567
@bot.command()
async def I(ctx):
   await ctx.send(f'You are {ctx.message.author}')

#bag reporter
bcount = 0
@bot.command()
async def bag(ctx, msg: str = None):
    global bcount
    bcount += 1
    await ctx.send(f'Ваш баг - **`{msg}`** - отправлен модерации \nНомер бага за сегодня - {bcount}')
    channel = bot.get_channel(824717463107141652)
    report = bot.get_user(595998891934220339)
    await report.send(f'**Новый репорт бага №{bcount}!** \n `{msg} - необходимо решить проблему.`')
    await channel.send(f'**Новый репорт бага №{bcount}!** \n `{msg} - необходимо решить проблему.`')

#песенки
@bot.command(aliases=["s"])
async def search(ctx, *, zapros=None):
    if zapros is None:
        await ctx.send("Введите фрагмент песни для поиска")
    else:
        reponse = requests.get(f"https://pixabay.com/images/search/{zapros}")
        otv = reponse.json()
        try:
            embed=discord.Embed(title="Genius", url=f"{otv['links']['genius']}", description=otv['lyrics'], color=0x27b201)
            embed.set_author(name=f"{otv['author']} - {otv['title']}")
            embed.set_thumbnail(url=f"{otv['thumbnail']['genius']}")
            embed.set_footer(text = f"Запросил {ctx.author.name}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Что-то пошло не так...")

bot.run(TOKEN)