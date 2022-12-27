import discord
from API import Cat
from discord import app_commands
from discord.ext import commands

cat = Cat()

class help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = 'help', description = 'Sends a list of commands.')

    async def help(self, interaction: discord.Interaction):
        image = cat.image()
        embed=discord.Embed(title='Help', description='These are the commands that Cat Bot currently supports.', color=discord.Colour(cat.embedColor))
        embed.add_field(name='Gif', value='Sends a cat gif.', inline=False)
        embed.add_field(name='Image', value='Sends a cat image.\nInputting a breed ID will allow you to recieve images of a specific cat breed.', inline=False)
        embed.add_field(name='Fact', value='Sends a fact about cats.', inline=False)
        embed.add_field(name='Video', value='Sends a cat video.', inline=False)
        embed.add_field(name='Breed Info', value='Provides information or statistics about a specific cat breed, or lists all supported cat breeds for the bot.', inline=False)
        embed.add_field(name='Schedule', value='The bot will send a message hourly with a random cat photo once provided with a Discord Webhook.', inline=False)
        embed.add_field(name='Help', value='Sends a list of commands.', inline=False)
        embed.set_image(url=image)
        embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(help(bot))