from discord.ext import commands
from asyncio import sleep
import discord
import hmtai
import requests
import urllib
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from urllib.request import urlretrieve
import os
import color
import json


bot = commands.Bot(command_prefix=('*'), intents = discord.Intents.all())
bot.remove_command( 'help' )
@bot.event
async def on_member_join(member):
        channel = bot.get_channel(833053710955184158) #здесь айди канала которому хочешь отправить сообщение
        mjoin = discord.Embed(title=f"Member Join", color=discord.Colour.purple())
        mjoin.set_author(icon_url= f"{member.avatar_url}", name=f"{member.name}")
        mjoin.add_field(name="Пользователь", value=member.mention)
        mjoin.add_field(name="ID Пользователя:", value=member.id)
        mjoin.add_field(name="Имя Пользователя:", value=member.name)
        mjoin.set_thumbnail(url = member.avatar_url)
        await channel.send(embed=mjoin)

@bot.event
async def on_ready():
    print("Я запущен!", os.name)
    #await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name='NBS😇'))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
    #await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="NBS😇"))
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
    
    while True:
        await sleep(15)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="NBS😇"))
        await sleep(15)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="*help"))
    a = input("[Y] Завершить\n")
    if a == "Y":
        quit("Бот выключен!")


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

#inviteq
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
async def bug(ctx, *, str = None):
    
    if str is None:
        await ctx.send("Неправильно")
    else:
        with open("counters.json", "r") as f:
            bugs = json.load(f)

            bugs["bug"] += 1
    
        with open("counters.json", "w") as f:
            json.dump(bugs,f)

        with open("counters.json", "r") as f:
            bugs = json.load(f)

        bug = bugs["bug"]

        await ctx.send(f'Ваш баг - **`{str}`** - отправлен модерации \nНомер бага - {bug}')
        channel = bot.get_channel(824717463107141652)
        report = bot.get_user(595998891934220339)
        await report.send(f'**Новый репорт бага №!** \n `{str} - необходимо решить проблему.`')
        await channel.send(f'**Новый репорт бага №!** \n `{str} - необходимо решить проблему.`')

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
        try:
            urlretrieve(f'https://picsum.photos/{size}', 'one1.jpg')
            await ctx.send(f'Квадратная картика размером {size}', file = discord.File(r'one1.jpg') )
        except:
            eri = discord.Embed(title='🛑Ошибка🛑', description='Попробуйте изменить значения комманды',
                                 colour=discord.Colour.red())
            await ctx.send(embed = eri)
    elif size2 is not None:
        try:
        #r = requests.get(f'https://picsum.photos/1080/1920')
        #res = r.json()
            urlretrieve(f'https://picsum.photos/{size}/{size2}', 'one.jpg')
        #emb = discord.Embed(title='Картинка', colour = discord.Colour.purple())
        #url = res['url']
        #emb.set_image(url = url)
        #await print(r)
            #await ctx.send(embed=emb)
            await ctx.send(f'Картинка размером {size}*{size2}', file=discord.File(r'one.jpg'))
        except:
            eri1 = discord.Embed(title='🛑Ошибка🛑', description='Попробуйте изменить значения комманды', colour=discord.Colour.red())
            await ctx.send(embed = eri1)


'''
@bot.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
'''




#clear
@bot.command(aliases = ['c'])
async def clear(ctx, amount = 1000):
    cemb = discord.Embed(title='Успешно!', description=f'Очищенно {amount} сообщений!', colour=discord.Colour.green())
    cemb.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(embed = cemb, delete_after=15.0)

#lvl system
#os.chdir(r'C:\Python1\12344\venv')
#@bot.event
#async def on_message(message):
    #with open('lvl.json','r') as f:
        #users = json.load(f)
    #async def update_data(users,user):
        #if not user in users:
            #users[user] = {}
            #users[user]['exp'] = 0
            #users[user]['lvl'] = 1
    #async def add_exp(users,user,exp):
        #users[user]['exp'] += exp
    #async def add_lvl(users,user):
        #exp = users[user]['exp']
        #lvl = users[user]['lvl']
        #if exp > lvl:
            #await message.channel.send(f'{message.author.mention} повысил свой уровень!')
            #users[user]['exp'] = 0
            #users[user]['lvl'] = lvl + 1
    #await update_data(users,str(message.author.id))
    #await add_exp(users,str(message.author.id),1)
    #await add_lvl(users,str(message.author.id))
    #with open('lvl.json','w') as f:
        #json.dump(users,f)

@bot.command()
@commands.has_permissions(administrator=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    try:
        getrole = discord.utils.get(ctx.guild.roles, id = role.id)
        await member.add_roles(getrole)
    except Exception:
        await ctx.send(f'Неверное имя пользователя или роль! ({member}, {role})')

@bot.command()
async def list(ctx, serv = None):
    memberss = discord.Guild.members
    await ctx.send(memberss)


@bot.command()
async def qwe(ctx):
    for guild in bot.guilds:
        q = await discord.TextChannel.position(1)
        print(q)


#cogs
@bot.command()
async def load(ctx, extension):
	if ctx.author.id == 595998891934220339:
		bot.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded!")
	else:
		await ctx.send("Ты бота разработал??? Мне кажется нет...")


@bot.command()
async def unload(ctx, extension):
	if ctx.author.id == 595998891934220339:
		bot.unload_extension(f"cogs.{extension}")
		await ctx.send("Cogs is unloaded!")
	else:
		await ctx.send("Ты бота разработал??? Мне кажется нет...")


@bot.command()
async def reload(ctx, extension):
	if ctx.author.id == 595998891934220339:
		bot.unload_extension(f"cogs.{extension}")
		bot.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs is reloaded!")
	else:
		await ctx.send("Ты бота разработал??? Мне кажется нет...")


for filename in os.listdir("cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")




import psutil
from psutil import Process, virtual_memory

@bot.command()
async def ram( ctx):
    ram = virtual_memory().total
    used = virtual_memory().used

    field = []
    while len(field) != 5:

        if round(used, 1) >= ram / 5:
            used -= ram / 5
            field.append("🟥 ")

        elif round(used, 1) >= ram / 10:
            used -= ram / 10
            field.append("🟨 ")

        elif used <= ram / 10:
            used = 0
            field.append("🟦 ")

        print(used)

    msg = ''
    for i in range(len(field)):
        msg += field[i]

    embed=discord.Embed(title="Used RAM", description=msg)
    embed.set_footer(text=f"{round(virtual_memory().used /1024/1024/1024, 2)} GB out of {round(ram /1024/1024/1024, 2)} GB")
    await ctx.send(embed=embed)


@bot.command()
async def e(ctx):
    await ctx.send("<:811941999066349578:820372742523977748>")


bot.run(color.TOKEN)







'''
@client.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
'''