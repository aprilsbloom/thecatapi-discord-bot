import discord
import requests
import random
import json
from discord import app_commands
from discord.ext import commands

apikeys = []


class help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="help",
        description="Sends a list of commands.")
    async def help(self, interaction: discord.Interaction):
        image = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png",
                             headers={'x-api-key': random.choice(apikeys)}).json()[0]['url']
        embed = discord.Embed(
            title="Help", description='The list of breeds that work with </breedinfo:1>, </breedstats:1> and </image:1> can be found [here](https://pastebin.com/4V7iF7yv).', color=discord.Colour(0x3498DB))
        embed.add_field(name="Gif", value="Sends a cat gif.", inline=False)
        embed.add_field(
            name="Image", value="Sends a cat image.\nInputting a breed ID will allow you to recieve images of a specific cat breed.", inline=False)
        embed.add_field(
            name="Fact", value="Sends a fact about cats.", inline=False)
        embed.add_field(name="Video", value="Sends a cat video.", inline=False)
        embed.add_field(name="Breed Info",
                        value="Sends info on a cat breed.", inline=False)
        embed.add_field(name="Breed Stats",
                        value="Sends the stats of a cat breed.", inline=False)
        embed.add_field(
            name="Submit", value="Sends a GIF or Video to have a chance at being posted on [this account](https://twitter.com/gifkitties).", inline=False)
        embed.add_field(
            name="Help", value="Sends a list of commands.", inline=False)
        embed.set_image(url=image)  # fetch image
        embed.set_footer(text='Made by @gifkitties',
                         icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(help(bot))
