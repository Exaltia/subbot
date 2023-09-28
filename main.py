import discord
import asyncio
import configparser
configuration = configparser.ConfigParser()
configuration.read('config.ini')
token = configuration['DEFAULT']['token']
commands = discord.app_commands
intents = discord.Intents.none()
# intents.message_content = True
client = discord.Client(intents=intents)
def bidule():
    pass

if __name__ == "__main__":
    client.run(token)