#導入discord相關模組
import discord
from discord.ext import commands
#導入Cog核心
from core.classes import Cog_Extension
#導入檔案讀取儲存相關模組
import json

#開啟檔案，讀取模式，UTF-8解碼，忽略讀取錯誤，暫時命名為jFile並存到jdata中
with open("setting.json",mode='r',encoding='UTF-8',errors='ignore') as jFile:
    jdata=json.load(jFile)

#自動監聽觸發性的bot事件(類別Command繼承core.classes.py內Cog_Extension的類別)
class Coglistener(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member): #新成員加入時觸發
        channel=member.guild.system_channel
        if channel is not None:
            await channel.send(f"誰來了喵~ {member}")
    
    @commands.Cog.listener()
    async def on_member_remove(self,member): #成員離開時觸發
        channel=self.bot.get_channel(int(jdata['CHANNEL'][0]['00']))
        await channel.send(f"{member} 離開了喵~")
    
    @commands.Cog.listener() #訊息關鍵字觸發
    async def on_message(self,msg):
        if msg.author != self.bot.user: #非機器人訊息觸發
            hello=jdata['KEYWORD'][0]['HELLO']
            if msg.content in hello:
                await msg.channel.send("早安!")
            
            robot=jdata['KEYWORD'][0]['ROBOT']
            for robot_key in robot:
                if robot_key in msg.content:
                    await msg.channel.send("有人找我?")
            
            chinese=jdata['KEYWORD'][1]['CHINESE']
            if chinese in msg.content:
                await msg.channel.send("(我知道中文)")
            
            english=jdata['KEYWORD'][2]['ENGLISH']
            if english in msg.content.lower():
                await msg.channel.send("(I know english)")


def setup(bot):
    bot.add_cog(Coglistener(bot))