import discord
from API import Cat
from discord import app_commands
from discord.ext import commands

cat = Cat()

class gif(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = 'gif', description = 'Sends a cat gif.')

    async def gif(self, interaction: discord.Interaction):
        gif = cat.gif()
        embed=discord.Embed(title='Here\'s a cat gif:', color=discord.Colour(cat.embedColor))
        embed.set_image(url=gif) 
        embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(gif(bot))