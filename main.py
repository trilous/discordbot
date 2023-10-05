import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connected! {bot.user}')
  
@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return

load_dotenv()


DISCORD_TOKEN = "MTE1ODQ3NDI2MjE2ODk5Nzk4MA.GmfpHk.McejjRNWDDlCg7UBzia1IS2bXvYUKTvCFEqMS8"


intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	
	guild_count = 0

	
	for guild in bot.guilds:
		
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("hey blackie")

# !mexico
@bot.command()
async def mexico(ctx):
	await ctx.send("https://cdn.britannica.com/86/167886-050-E0D50805/Metropolitan-Cathedral-Mexico-City.jpg")

# !helsinki
@bot.command()
async def helsinki(ctx):
	await ctx.send("https://maps.app.goo.gl/A95afA6hoz351tBv6")
//nvim

bot.run(DISCORD_TOKEN)
