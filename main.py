import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!',intents=discord.Intent.all())

# คำสั่ง bot พร้อมใช้งาน
@bot.event
async def on_ready():
    print("Bot Online !!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

# แจ้งคนเข้า - ออก server
async def on_member_join(member):
    channel = bot.get_channal(1280636600296017931/1280636600916906006) #ID Room
    text = f"welcom to the server, {member.mention}!"
    
    emmbed = discord.Embed(title = 'Welcom to the server',
                           description = text,
                           color = 0x66FFFF)
    await channel.send(text) #ส่งข้อความไปที่ห้องนี้
    await channel.send(emmbed = emmbed) #ส่ง Embed ไปที่ห้องนี้
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัวของ member
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1280636600296017931/1280636600916906006) #ID Room
    text = f"{member.name} has left the server !"
    await channel.send(text) # ส่งข้อความไปที่ห้องนี้
    
server_on()

bot.run(os.getenv('TOKEN'))
