import discord
import urllib.parse
from utils import cat
from discord import app_commands
from discord.ext import commands

cat = cat()
error = 'An error occured, please try again later.'

class image(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = 'image', description = 'Sends a cat image.')

    async def image(self, interaction: discord.Interaction, breed: str = ''):
        if breed == '':
            image = cat.image()
            embed = discord.Embed(title='Here\'s a cat image:', color=discord.Colour(cat.embedColor))
            embed.set_image(url=image)
            embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
        else:
            breedIDs = [i['id'] for i in cat.get_breeds()]

            if breed in breedIDs:
                image = cat.image(breed)
                breedname = cat.get_breed_info(breed)['name']
                embed = discord.Embed(title='Here\'s a cat image:', description = f'Breed: {breedname}', color=discord.Colour(cat.embedColor))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
            else:
                image = cat.image()
                embed = discord.Embed(title='Error', description = 'This breed doesn\'t exist. Please check your spelling and try again.', color=discord.Colour.red())
                embed.set_image(url=image)
                embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(image(bot))