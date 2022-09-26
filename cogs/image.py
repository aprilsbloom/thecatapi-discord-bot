import discord
import requests
import random
from discord import app_commands
from discord.ext import commands

breedlist = 'abys aege abob acur asho awir amau amis bali bamb beng birm bomb bslo bsho bure buri cspa ctif char chau chee csho crex cymr cypr drex dons lihu emau ebur esho hbro hima jbob java khao kora kuri lape mcoo mala manx munc nebe norw ocic orie pers pixi raga ragd rblu sava sfol srex siam sibe sing snow soma sphy tonk toyg tang tvan ycho'
apikeys = []


class image(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="image",
        description="Sends a cat image.")
    async def image(self, interaction: discord.Interaction, breed: str = 'hi'):
        if breed == 'hi':
            image = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png",
                                 headers={'x-api-key': random.choice(apikeys)}).json()[0]['url']
            embed = discord.Embed(
                title="Here\'s a cat image:", color=discord.Colour(0x3498DB))
            embed.set_image(url=image)
            embed.set_footer(text='Made by @gifkitties',
                             icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
            await interaction.response.send_message(embed=embed)
        else:
            if breed in breedlist:
                image = requests.get(f"https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&breed_ids={breed}", headers={
                                     'x-api-key': random.choice(apikeys)}).json()[0]['url']
                breedname = requests.get(f'https://api.thecatapi.com/v1/breeds/{breed}', headers={
                                         'x-api-key': random.choice(apikeys)}).json()['name']
                embed = discord.Embed(
                    title="Here\'s a cat image:", description=f"Breed: {breedname}", color=discord.Colour(0x3498DB))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @gifkitties',
                                 icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)
            else:
                image = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png',
                                     headers={'x-api-key': random.choice(apikeys)}).json()[0]['url']
                embed = discord.Embed(
                    title="Error", description="This breed doesn't exist. Please check your spelling and try again.", color=discord.Colour(0x3498DB))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @gifkitties',
                                 icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(image(bot))
