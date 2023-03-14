import discord
from discord.ext import commands
from utils import Cat

# Variables
cat = Cat()

# Command
class help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name = 'help', description = 'Sends a list of commands.')

    async def help(self, interaction: discord.Interaction):
        image = cat.image()[0]['url']

        embed=discord.Embed(title='Help', description='This bot was made by [@gifkitties](https://twitter.com/gifkitties) on Twitter, and the source code can be found [here](https://github.com/paintingofblue/thecatapi-discord-bot).\n\nHere are the commands that Cat Bot currently supports:\n', color=discord.Colour(cat.embedColor))

        embed.add_field(name='Gif', value='Sends a cat gif.', inline=False)
        embed.add_field(name='Image', value='Sends a cat image.\nInputting a breed ID will allow you to recieve images of a specific cat breed.', inline=False)
        embed.add_field(name='Fact', value='Sends a fact about cats.', inline=False)
        embed.add_field(name='Video', value='Sends a cat video.', inline=False)
        embed.add_field(name='Breeds', value='Provides information or statistics about a specific cat breed, or lists all supported cat breeds for the bot.', inline=False)
        embed.add_field(name='Schedule', value='The bot will send a message hourly with a random cat photo once provided with a Discord Webhook.', inline=False)
        embed.add_field(name='Help', value='Sends a list of commands.', inline=False)
        embed.set_image(url=image)

        await interaction.response.send_message(embed=embed)

# Cog setup
async def setup(bot: commands.Bot):
    await bot.add_cog(help(bot))