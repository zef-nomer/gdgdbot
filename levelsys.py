import discord
from discord import message
from discord.ext import commands
from pymongo import MongoClient 

bot_channel = 726108461708083211
talk_channel = [712351587678552124,722692373498560552,725672367820505168,870206586063298600]

level = ["🌳╎New bio", "🏮╎Advanced", "⛩╎Founder", "🦋╎Wonderful", "🍁╎Captain", "🛸┆Space", "🐳╎Merciful", "🔑╎Unreal", "🎸╎Omg 0_o", "🪄╎Hacker", "⚡╎God"]
levelnum = [5,10,20,30,40,50,60,70,80,90,100]

cluster = MongoClient("mongodb+srv://Zef1r:<J6a9i8k7>@xtench.y6pt9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

levelling = cluster["discord"]["lvl"]

class levelsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("online")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channel:
            stats = levelling.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id, "xp": 100}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id":message.author.id}, {"$set":{"xp":xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2)) + (50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2)) + (50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"Так стой, {message.author.mention}, дай подумаю... Так, я тебя поздровляю, ты повысл свой уровень! Текущий уровень: {lvl}")
                        for i in range(len(level)):
                            if lvl  == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name = level[i]))
                                embed = discord.Embed(title = "Уровни", description = f"{message.author.mention}, ты получил **{level[i]}**!")
                                embed.set_thumbnail(url = message.author.avatar_url)
                                embed.set_footer(text=f"lvl:{lvl}||{message.guild.name}")
                                await message.channel.send(embed=embed)

    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            await ctx.send("rank")


