import discord
import requests
import random
from discord import app_commands
from discord.ext import commands

breedlist = 'abys aege abob acur asho awir amau amis bali bamb beng birm bomb bslo bsho bure buri cspa ctif char chau chee csho crex cymr cypr drex dons lihu emau ebur esho hbro hima jbob java khao kora kuri lape mcoo mala manx munc nebe norw ocic orie pers pixi raga ragd rblu sava sfol srex siam sibe sing snow soma sphy tonk toyg tang tvan ycho'
apikeys = []


class fact(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="fact",
        description="Sends a fact about cats.")
    async def fact(self, interaction: discord.Interaction):
        image = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png',
                             headers={'x-api-key': random.choice(apikeys)}).json()[0]['url']
        with open("text/catfact.txt", "r", encoding="utf_8") as file:
            embed = discord.Embed(title="Here\'s a cat fact:", description=random.choice(
                file.read().splitlines()), color=discord.Colour(0x3498DB))
            embed.set_image(url=image)
            embed.set_footer(text='Made by @gifkitties',
                             icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(fact(bot))
