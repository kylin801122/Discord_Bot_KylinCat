#導入discord相關模組
import discord
from discord.ext import commands
#導入Cog核心
from core.classes import Cog_Extension
#導入檔案讀取儲存相關模組
import json
#導入隨機亂數模組
import random
#導入時間戳記
import time
import pytz
import datetime

#開啟檔案，讀取模式，UTF-8解碼，忽略讀取錯誤，暫時命名為jFile並存到jdata中
with open("setting.json",mode='r',encoding='UTF-8',errors='ignore') as jFile:
    jdata=json.load(jFile)

#使用者輸入指令的bot事件(類別Command繼承core.classes.py內Cog_Extension的類別)
class Command(Cog_Extension):
    @commands.command() #查詢bot的延遲時間
    async def ping(self,ctx):
        await ctx.send(f"目前延遲時間為:{round(self.bot.latency*1000)}(毫秒)")
    
    @commands.command() #查詢各地時間
    async def time(self,ctx):
        GMT_time=datetime.datetime.now(pytz.timezone('Etc/GMT')).strftime("%Y/%m/%d\n%H:%M:%S\n=====================")
        embed=discord.Embed(title="格林威治時間",url="https://time.artjoey.com/",description=GMT_time,\
        colour=0xc8ffff)
        tw_time=datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%Y/%m/%d\n%H:%M:%S")
        embed.add_field(name="目前台灣時間",value=tw_time,inline=True)
        jp_time=datetime.datetime.now(pytz.timezone('Japan')).strftime("%Y/%m/%d\n%H:%M:%S")
        embed.add_field(name="目前日本時間",value=jp_time,inline=True)
        await ctx.send(embed=embed)
    
    @commands.command() #貼貓咪圖片
    async def 貓咪(self,ctx):
        random_picture=random.choice(jdata['PICTURE'][0]['cat'])
        picture=discord.File(random_picture)
        await ctx.send(file=picture)

    @commands.command() #清除所有機器人訊息
    async def clean(self,ctx):
        def is_me(m):
            return m.author == self.bot.user
        await ctx.channel.purge(check=is_me,bulk=False)
    
def setup(bot):
    bot.add_cog(Command(bot))