import discord
import asyncio
import configparser
from discord import app_commands
configuration = configparser.ConfigParser()
configuration.read('config.ini')
token = configuration['DEFAULT']['token']
commands = discord.app_commands
intents = discord.Intents.none()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
class OtherButtons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Button",style=discord.ButtonStyle.blurple)
    async def useless1(self,interaction:discord.Interaction, button:discord.ui.Button):
        pass
    @discord.ui.button(label="Button", style=discord.ButtonStyle.green)
    async def useless(self,interaction:discord.Interaction, button:discord.ui.Button):
        pass
    @discord.ui.button(label="Button", style=discord.ButtonStyle.red)
    async def grey_button(self,interaction:discord.Interaction, button:discord.ui.Button):
        pass
class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Button",style=discord.ButtonStyle.red)
    # view=self lead to the addition of the same button under every bot answer
    async def grey_button(self,interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content=f"This is an edited button response!", view=OtherButtons())


@tree.command(name = "slashtest", description = "My first application Command")
async def first_command(interaction):
    await interaction.response.send_message("You're the worst employee of the month, no work for you!")

@tree.command(name="buttontest", description="My first button Command")
async def second_command(interaction):
    await interaction.response.send_message("You're the worst employee of the month, no work for you!", view=Buttons())

def bidule():
    pass
@client.event
async def on_ready():
    # According to examples, if guildid is not specified, slash command registration can take up to one hour.
    # guild id format : guild=discord.Object(id=12417128931)
    # New command added to the bot also need a reload of discord client, userside, or new command does not appears
    await tree.sync()
if __name__ == "__main__":
    client.run(token)