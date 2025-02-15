import discord
from discord.ext import commands
import os
from utils.database import Database

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
db = Database()

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} успешно запущен!')
    await load_cogs()
    
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(TOKEN)
