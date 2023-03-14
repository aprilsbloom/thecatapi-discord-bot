import discord
from discord.ext import commands
from utils import Cat

# Variables
cat = Cat()

# Command
class Fact(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name = 'fact', description = 'Sends a fact about cats.')

    async def fact(self, interaction: discord.Interaction):
        image = cat.image()[0]['url']
        fact = cat.fact()

        embed=discord.Embed(title="Here's a cat fact:", description=fact, color=discord.Colour(cat.embedColor))
        embed.set_image(url=image)

        await interaction.response.send_message(embed=embed)

# Cog setup
async def setup(bot: commands.Bot):
    await bot.add_cog(Fact(bot))