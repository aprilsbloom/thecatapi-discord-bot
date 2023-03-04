import discord
from discord.ext import commands
from utils import Cat

cat = Cat()

class fact(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name = 'fact', description = 'Sends a fact about cats.')

    async def fact(self, interaction: discord.Interaction):
        image = cat.image()
        fact = cat.fact()

        embed=discord.Embed(title="Here's a cat fact:", description=fact, color=discord.Colour(cat.embedColor))
        embed.set_image(url=image)
        embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(fact(bot))