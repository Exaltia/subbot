import discord
from discord import option
import configparser
configuration = configparser.ConfigParser()
configuration.read('config.ini')
token = configuration['DEFAULT']['token']

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command()
@option("number", description="enter the number of parts needed", min_value=1, max_value=9999)
@option('submarine_type', description="Choose the submarine type", choices=["Shark", "Whale", "Coelacanth", "Unkiu"])
@option("part_type", description="Choose the submarine part type", choices=["Stern", "Bow", "Hull", "Bridge"])
@option("modified", description="Choose Modifier if you build modified parts", choices=["Modified", "Normal"])
async def hello(ctx: discord.ApplicationContext, number: int, submarine_type: str, part_type: str, modified: str):
    await ctx.respond(f"Order of {number} {modified} {submarine_type} {part_type} submarines added! (or not)")

bot.run(token)