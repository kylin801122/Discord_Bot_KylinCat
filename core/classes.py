#導入discord相關模組
import discord
from discord.ext import commands

#類別Cog_Extension繼承commands.Cog的類別(本區塊待研究)
class Cog_Extension(commands.Cog):
    def __init__(self,bot): #初始化屬性
        self.bot=bot #使class裡面的bot等同於外面傳入的bot(?)