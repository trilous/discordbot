import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# !mexico
@bot.command()
async def mexico(ctx):
	await ctx.send("https://cdn.britannica.com/86/167886-050-E0D50805/Metropolitan-Cathedral-Mexico-City.jpg")

# !helsinki
@bot.command()
async def helsinki(ctx):
	await ctx.send("https://a.cdn-hotels.com/gdcs/production0/d1589/6d9eed40-c31d-11e8-9739-0242ac110006.jpg")

# !tallin
@bot.command()
async def tallin(ctx):
    await ctx.send("https://static.visitestonia.com/images/3560294/1600_900_false_false_20f95cd72116f9e05019b27bc25f5ea4.jpg")

bot.run(DISCORD_TOKEN)
 