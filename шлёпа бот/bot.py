import discord
import asyncio
from asyncio import sleep
import json
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=('*'), intents = discord.Intents.all())

token = open('token.txt', 'r').readline()

@bot.event
async def on_ready():
    print('Запущен')


#say
@bot.command()
async def say(ctx, *, str = None):
    if str is None:
        e = discord.Embed(description='Ошибка! *say [тескст]', colour=discord.Colour.red())
        await ctx.author.send(embed=e)
    embed = discord.Embed(description=str, colour=discord.Colour.gold())
    await ctx.send(embed=embed)
    await sleep(3)
    await ctx.message.delete()


#welcome
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
async def on_message(message):
    msg = message.content.lower()
    with open('words.json','r') as f:
        mat = f
    if msg in mat:
        await message.channel.send("Дурачок")


#run
bot.run( token )