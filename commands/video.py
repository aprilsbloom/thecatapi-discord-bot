import discord
import json
import random
from utils import cat
from discord import app_commands
from discord.ext import commands

cat = cat()
spoilerText = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'

class video(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = 'video', description = 'Sends a cat video.')

    async def video(self, interaction: discord.Interaction):
        try:
            with open('data.json', 'r', encoding='utf8') as f:
                data = random.choice(json.load(f)['videos'])
            
            title = data['title']
            author = data['author']
            subreddit = data['subreddit']
            video = data['video']
            postLink = data['permalink']
            
            await interaction.response.send_message(f'**{title}**\nPosted by u/{author} in r/{subreddit}\n\n<{postLink}> {spoilerText} {video}')
        
        except KeyError:
            image = cat.image()
            embed = discord.Embed(color=discord.Colour(cat.embedColor))
            embed.title = 'Error'
            embed.description = 'Unable to fetch a video —— Please try again later.'
            embed.set_image(url=image)
            
            embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

async def setup(bot: commands.Bot):
    await bot.add_cog(video(bot))