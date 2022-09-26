import discord
import requests
import random
from discord import app_commands
from discord.ext import commands

apikeys = []


class gif(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="gif",
        description="Sends a cat gif.")
    async def gif(self, interaction: discord.Interaction):
        gif = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif",
                           headers={'x-api-key': random.choice(apikeys)}).json()[0]['url']
        embed = discord.Embed(title="Here\'s a cat gif:",
                              color=discord.Colour(0x3498DB))
        embed.set_image(url=gif)  # fetching gif
        embed.set_footer(text='Made by @gifkitties',
                         icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(gif(bot))
