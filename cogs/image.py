import discord
from cogs.API import Cat
from discord import app_commands
from discord.ext import commands

cat = Cat()

class image(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "image", description = "Sends a cat image.")

    async def image(self, interaction: discord.Interaction, breed: str = ''):
        if breed == '':
            image = cat.image('')
            embed=discord.Embed(title="Here\'s a cat image:", color=discord.Colour(cat.embedColor))
            embed.set_image(url=image)
            embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
            await interaction.response.send_message(embed=embed)
        else:
            if breed in Cat.breedList:
                image = cat.image(breed)
                breedname = Cat.get_breed_info(self, breed)['name']
                embed=discord.Embed(title="Here\'s a cat image:", description=f"Breed: {breedname}", color=discord.Colour(cat.embedColor))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)
            else:
                image = cat.image('')
                embed=discord.Embed(title="Error", description="This breed doesn't exist. Please check your spelling and try again.", color=discord.Colour(cat.embedColor))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(image(bot))