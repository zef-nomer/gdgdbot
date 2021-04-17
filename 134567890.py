from discord.ext import commands
from asyncio import sleep
import discord
import requests
import urllib
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from urllib.request import urlretrieve
import os

TOKEN = "NzExODI1NDg0NjE0NDY3NjA0.XsIpJA.-IP0W9UB8eL7IIrInaHo0utomLY"

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
    await ctx.send('https://i.picsum.photos/id/292/1920/1920.jpg?hmac=hg2sv2VPjgtehlNQm-E76aU-KSUqSwCSXb9IPakV5ZA')

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
    emb.add_field ( name = '```{}'.format ( "*" ), value = "В разработке" )
    emb.add_field ( name = '```{}В разработке'.format ( "*" ), value = "В разработке" )
    emb.add_field ( name = '```{}В разработке'.format ( "*" ), value = "В разработке" )
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
@bot.command(aliases=["l"])
async def lyrics(ctx, *, zapros=None):
    if zapros is None:
        await ctx.send("Введите фрагмент песни для поиска")
    else:
        reponse = requests.get(f"https://some-random-api.ml/lyrics?title={zapros}")
        otv = reponse.json()
        try:
            embed=discord.Embed(title="Genius", url=f"{otv['links']['genius']}", description=otv['lyrics'], color=0x27b201)
            embed.set_author(name=f"{otv['author']} - {otv['title']}")
            embed.set_thumbnail(url=f"{otv['thumbnail']['genius']}")
            embed.set_footer(text = f"Запросил {ctx.author.name}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Что-то пошло не так...")

#random dog
@bot.command(aliases=['rd','d'])
async def rdog(ctx):
    reponse = requests.get('https://some-random-api.ml/img/dog')
    otv = reponse.json()
    try:
        emb = discord.Embed(title='🐶Собачка🐶', color=discord.Colour.purple())
        emb.set_image(url = f'{otv["link"]}')
        await ctx.send(embed = emb)
    except:
        await ctx.send('🛑Ошибка🛑')


#random image
@bot.command(aliases=['ri'])
async def rimage(ctx, size = None, size2 = None):
    if size is None:
        emb = discord.Embed(title='🛑Ошибка синтаксиса🛑', description='Правильный синтаксис:\n'
                                                                       '```*ri размер - если хотите получить квадратную картинку. За место "размер" введите размер картики```\n'
                                                                       '```*ri размер1 размер2 - если хотите получить не квадратную картинку. За место "размер1" и "размер2" введите рахмер картинки```',
                            colour=discord.Colour.purple())
        await ctx.send(embed = emb)
    elif size2 is None:
        urlretrieve(f'https://picsum.photos/{size}', 'D:\pypr\one1.jpg')
        await ctx.send(f'Квадратная картика размером {size}', file = discord.File(r'D:\pypr\one1.jpg') )
    else:
        urlretrieve(f'https://picsum.photos/{size}/{size2}', 'D:\pypr\one.jpg')
        #await ctx.send(file=discord.File(r'D:\pypr\one.jpg'))
        emb = discord.Embed(title='Картинка', colour = discord.Colour.purple())
        await ctx.send(f'Картинка размером {size}*{size2}', file=discord.File(r'D:\pypr\one.jpg'))

#clear
@bot.command(aliases = ['c'])
async def clear(ctx, amount = 1000):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send('Очищенно!', delete_after=15.0)

#sre
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = 'verify')
    await member.add_roles(role)
    #channel = client.get_channel(name = "welcome")
    channel=discord.utils.get(member.guild.channels, name="welcome")
    url = str(member.avatar_url)[:-10]
    url = requests.get(url,stream = True)
    avatar = Image.open(io.BytesIO(url.content))
    welcome = Image.open('hi.png')
    welcome = welcome.convert('RGBA')
    avatar = avatar.convert('RGBA')
    avatar = avatar.resize((500,500))
    mask = Image.new('L',(1500,1500),0)
    draw = ImageDraw.Draw(mask)
    idraw = ImageDraw.Draw(welcome)
    name = member.name
    tag = member.discriminator
    at = member.created_at
    headline = ImageFont.truetype('font.ttf', size=70)
    headline2 = ImageFont.truetype('font.ttf', size=70)
    idraw.text((900, 750), f'{name}#{tag}',anchor="ms", font=headline, fill='#FFFFFF')
    idraw.text((900, 950), f'Создан {at}' [:-15],anchor="ms", font=headline2, fill='#FFFFFF')
    draw.ellipse((0,0) + (1500,1500),fill = 255)
    mask = mask.resize((500,500))
    avatar.putalpha(mask)
    welcome = welcome.resize((1800,1100))
    welcome.paste(avatar,(650,50),avatar)
    _buffer = io.BytesIO()
    welcome.save(_buffer,"png")
    _buffer.seek(0)
    await channel.send(file = discord.File(fp = _buffer,filename = f'{member.name}welcome.png'))
    await channel.send(f"{member.mention} добро пожаловать на сервер {member.guild.name}!")
    await member.send(file = discord.File(filename = f'{member.name}welcome.png'))
    await member.send(f"{member.mention} добро пожаловать на сервер {member.guild.name}!")


bot.run(TOKEN)