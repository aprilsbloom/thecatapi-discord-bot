import discord
import random
import requests
from API import Cat
from discord import app_commands
from discord.ext import commands

cat = Cat()

class fact(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = 'fact', description = 'Sends a fact about cats.')

    async def fact(self, interaction: discord.Interaction):
        try:
            image = cat.image()
            randnum = random.randint(0, 1)
            if randnum == 0:
                r = requests.get('https://gist.githubusercontent.com/paintingofblue/657d0c4d1202374889ce4a98a6b7f35f/raw/fd635f48f69ea9c2d2d07f67e7ab310a6408fddf/catfacts.txt')
                facts = r.text.splitlines()
                fact = random.choice(facts)
                
                embed=discord.Embed(title='Here\'s a cat fact:', description=fact, color=discord.Colour(cat.embedColor))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)
            else:
                r = requests.get('https://catfact.ninja/fact')
                fact = r.json()['fact']
                
                embed=discord.Embed(title='Here\'s a cat fact:', description=fact, color=discord.Colour(cat.embedColor))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)
        except:
            image = cat.image()
            embed = discord.Embed(title='Error', description='An error occured while running this command. Please try again.', color=discord.Colour(cat.embedColor))
            embed.set_image(url=image)
            embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
            await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(fact(bot))