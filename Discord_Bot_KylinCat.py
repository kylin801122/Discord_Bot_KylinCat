#導入discord相關模組
import discord
from discord.ext import commands
#導入檔案讀取儲存相關模組
import json
#導入文件目錄操作模組
import os
#導入時間戳記
import datetime

#建置bot實體給予變數bot
bot=commands.Bot(command_prefix='!') #在Discord軟體中使用指定符號下命令給機器人

#導入所有commands資料夾內的.py檔(免去一個一個手寫導入)
for filename in os.listdir('./commands'):
    if filename.endswith('.py'): #字尾是.py才讀檔
        bot.load_extension(f"commands.{filename[:-3]}") #讀檔import，[:-3]去掉.py三個字

#開啟檔案，模式為'r'讀取，使用UTF-8解碼(因為可能有中文)，忽略讀取錯誤，檔案暫時命名為jFile
#如果不想每次手動關閉檔案，或怕自己忘記關閉檔案，可以使用 with 關鍵字實作
with open("setting.json",mode='r',encoding='UTF-8',errors='ignore') as jFile:
    jdata=json.load(jFile) #將jFile的內容儲存到jdata中

#自動監聽觸發性的bot事件
@bot.event
async def on_ready(): #當機器人準備好接收數據時觸發
    print("< Bot is online >")

#使用者輸入指令的bot事件
bot.remove_command('help') #移除預設help指令
@bot.command()
async def help(ctx): #自訂help指令
    embed=discord.Embed(title="貓肉球指令詢問區",url="http://www.meetpets.org.tw/pets/cat",description="< 以下為可愛的貓咪指令介紹 >",\
    colour=0xc8ffff,timestamp=datetime.datetime.utcnow())
    embed.set_author(name=ctx.message.author.name,url="https://www.facebook.com/kylin801122",icon_url="https://i.imgur.com/lkyGOPA.jpg")
    embed.set_thumbnail(url="https://i.imgur.com/d9T0yFr.jpg")
    embed.add_field(name="!help", value="查詢所有指令",inline=True)
    embed.add_field(name="!ping", value="查詢延遲時間",inline=True)
    embed.add_field(name="!time", value="查詢各地時間",inline=True)
    embed.add_field(name="!貓咪",value="顯示隨機的可愛貓貓圖",inline=True)
    embed.set_image(url="https://i.imgur.com/YHeIh3G.png")
    embed.set_footer(text=" ※ 投資一定有風險，貓貓投資有賺有賠，申購前應詳閱公開說明書。",icon_url="https://i.imgur.com/RhAGSQR.png")
    await ctx.send(embed=embed)

#開啟檔案，讀取模式，暫時命名為Token_File並存到token中
with open("token.json",mode='r') as Token_File:
    token=json.load(Token_File)
#bot的token
if __name__ == "__main__":
    bot.run(token['TOKEN'])