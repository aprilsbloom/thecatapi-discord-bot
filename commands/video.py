import discord
import json
import random
from discord.ext import commands
from utils import Cat

# Variables
cat = Cat()
spoilerText = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'

# Command
class Video(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name = 'video', description = 'Sends a cat video.')

    async def video(self, interaction: discord.Interaction):
        with open('data.json', 'r', encoding='utf8') as f:
            data = json.load(f)['videos']
            video = data[random.randint(0, len(data) - 1)]

        # I'm utilizing a bug with spoilers here to hide the video link at the end of the message
        await interaction.response.send_message(f'**{video["title"]}**\nPosted by u/{video["author"]} in r/{video["subreddit"]}\n\n<{video["permalink"]}> {spoilerText} {video["video"]}')

# Cog setup
async def setup(bot: commands.Bot):
    await bot.add_cog(Video(bot))