import discord
from discord.ext import commands
from utils import Cat

# Variables
cat = Cat()

# Command
class gif(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name = 'gif', description = 'Sends a cat gif.')

    async def gif(self, interaction: discord.Interaction):
        gif = cat.gif()

        embed=discord.Embed(title="Here's a cat gif:", color=discord.Colour(cat.embedColor))
        embed.set_image(url=gif)

        await interaction.response.send_message(embed=embed)

# Cog setup
async def setup(bot: commands.Bot):
    await bot.add_cog(gif(bot))