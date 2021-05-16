from discord.ext import commands
from asyncio import sleep
from discord.utils import get
import discord
import requests
import urllib
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from urllib.request import urlretrieve
import os
import json
from discord_slash import SlashCommand


#эж пиши здесь p.s. здесь был ASR


#-----------------------------Цвета-----------------------------#
blue = discord.Colour.blue()
blurple = discord.Colour.blurple()
dark_blue = discord.Colour.dark_blue()
dark_gold = discord.Colour.dark_gold()
dark_gray = discord.Colour.dark_gray()
dark_green = discord.Colour.dark_green()
dark_grey = discord.Colour.dark_grey()
dark_magenta = discord.Colour.dark_magenta()
dark_orange = discord.Colour.dark_orange()
dark_purple = discord.Colour.dark_purple()
dark_red = discord.Colour.dark_red()
dark_teal = discord.Colour.dark_teal()
dark_theme = discord.Colour.dark_theme()
darker_gray = discord.Colour.darker_gray()
darker_grey = discord.Colour.darker_grey()
default = discord.Colour.default()
gold = discord.Colour.gold()
green = discord.Colour.green()
greyple = discord.Colour.greyple()
light_gray = discord.Colour.light_gray()
light_grey = discord.Colour.light_grey()
lighter_gray = discord.Colour.lighter_gray()
lighter_grey = discord.Colour.lighter_grey()
magenta = discord.Colour.magenta()
orange = discord.Colour.orange()
purple = discord.Colour.purple()
random = discord.Colour.random()
red = discord.Colour.red()
teal = discord.Colour.teal()
#---------------------------------------------------------------#









































TOKEN = "NzExODI1NDg0NjE0NDY3NjA0.XsIpJA.qiErAwcOZiKF8q2sjUHUmVKCkb0"
bot = commands.Bot(command_prefix=('*'), intents = discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command( 'help' )

@bot.event
async def on_member_join(member):
        channel = bot.get_channel(833053710955184158) #здесь айди канала которому хочешь отправить сообщение
        mjoin = discord.Embed(title=f"Member Join", color=purple)
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
    emb = discord.Embed( title = 'Информация по командам(В РАЗРАБОТКЕЕЕЕЕЕ)', colour = purple )

    emb.add_field ( name = '```{}wiki```'.format ( "*" ), value = "Переход на вики-сайт" )
    emb.add_field ( name = '```{}'.format ( "*" ), value = "В разработке" )
    emb.add_field ( name = '```{}В разработке'.format ( "*" ), value = "В разработке" )
    emb.add_field ( name = '```{}В разработке'.format ( "*" ), value = "В разработке" )
    await ctx.send( embed = emb )

#jopa(сообщения с эмодзи через каждые 20 м)
@bot.command()
async def say(ctx, *, str = None):
    if str is None:
        sayerror = discord.Embed(description='Не правильный синтаксис команды. *say [тескст]', colour=red)
        await ctx.author.send(embed=sayerror)
        await ctx.message.delete()
    else:
        embed = discord.Embed(description = str, colour = purple)
        await ctx.send(embed=embed)
        await sleep(3)
        await ctx.message.delete()

#rgb основные коды
@bot.command()
async def rgb(ctx):
    emb_rgb = discord.Embed( title = 'Основные цвета в rgb', colour = purple )
    emb_rgb.add_field(name='```Red```', value="```255 0 0```")
    emb_rgb.add_field(name='```Green```', value="```0 255 0```")
    emb_rgb.add_field(name='```Blue```', value="```0 0 255```")
    emb_rgb.add_field(name='```Cyan```', value="```0 0 255```")
    await ctx.send( embed = emb_rgb )

#rgb2
@bot.command()
async def rgb2(ctx):
    emb_rgb2 = discord.Embed( title = 'Основные цвета в rgb', description = '```Red : 255 0 0``` \n ```Green : 0 255 0``` \n ```Blue : 0 0 255```', colour = purple )
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
        colour = purple
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
    global bcount
    bcount += 1
    if str is None:
        await ctx.send("Неправильно")
    else:
        await ctx.send(f'Ваш баг - **`{str}`** - отправлен модерации \nНомер бага за сегодня - {bcount}')
        channel = bot.get_channel(824717463107141652)
        report = bot.get_user(595998891934220339)
        await report.send(f'**Новый репорт бага №{bcount}!** \n `{str} - необходимо решить проблему.`')
        await channel.send(f'**Новый репорт бага №{bcount}!** \n `{str} - необходимо решить проблему.`')

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
        emb = discord.Embed(title='🐶Собачка🐶', color=purple)
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
                            colour=purple)
        await ctx.send(embed = emb)
    elif size2 is None:
        try:
            urlretrieve(f'https://picsum.photos/{size}', 'one1.jpg')
            await ctx.send(f'Квадратная картика размером {size}', file = discord.File(r'one1.jpg') )
        except:
            eri = discord.Embed(title='🛑Ошибка🛑', description='Попробуйте изменить значения комманды',
                                 colour=red)
            await ctx.send(embed = eri)
    elif size2 is not None:
        try:
            urlretrieve(f'https://picsum.photos/{size}/{size2}', 'one.jpg')
            emb = discord.Embed(title='Картинка', colour = purple)
            await ctx.send(f'Картинка размером {size}*{size2}', file=discord.File(r'one.jpg'))
        except:
            eri1 = discord.Embed(title='🛑Ошибка🛑', description='Попробуйте изменить значения комманды', colour=red)
            await ctx.send(embed = eri1)

#clear
@bot.command(aliases = ['c'])
async def clear(ctx, amount = 1000):
    cemb = discord.Embed(title='Успешно!', description=f'Очищенно {amount} сообщений!', colour=green)
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

@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = get(guild.channels, id=833715487951028245)
    await channel.edit(name = f'Пидоров - {guild.member_count}')


@bot.command()
async def e(ctx):
    await ctx.send("<:811941999066349578:820372742523977748>")


@bot.command()
async def embed(self, ctx, *, arg = None):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Укажите `title`')
    title = await self.sadness.wait_for('message', check=check)

    await ctx.send('Укажите `description`')
    desc = await self.sadness.wait_for('message', check=check)

    embed = discord.Embed(title=title.content, description=desc.content, color=0xff6700)
    await ctx.send(embed=embed)


api_key = "3e24615f9f65368c4d066633f0dc4a54"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@bot.command()
async def weather(ctx, *, city: str):

        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel

        if x["cod"] != "404":

                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(round(current_temperature - 273.15))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                embed = discord.Embed(
                    title=f"Weather forecast - {city_name}",
                    color=0x7289DA,
                    timestamp=ctx.message.created_at,
                )
                embed.add_field(
                    name="Description",
                    value=f"**{weather_description}**",
                    inline=False)
                embed.add_field(
                    name="Temperature(C)",
                    value=f"**{current_temperature_celsiuis}°C**",
                    inline=False)
                embed.add_field(
                    name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                embed.add_field(
                    name="Atmospheric Pressure(hPa)",
                    value=f"**{current_pressure}hPa**",
                    inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                print(complete_url)

                await channel.send(embed=embed)

        else:
                await channel.send(
                    f"There was no results about this place!")
9

guild_ids = [843121022651465750] # Put your server ID in this array.

@slash.slash(name="ping", description="Пинг бота")
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    ping = round(bot.latency*1000)
    await ctx.send(f"Pong! ({ping} ms)")

bot.run(TOKEN)