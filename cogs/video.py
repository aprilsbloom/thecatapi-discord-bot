import discord
import random
import json
from discord import app_commands
from discord.ext import commands

apikeys = []


class video(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="video",
        description="Sends a cat video.")
    async def video(self, interaction: discord.Interaction):
        with open('text/newsub.txt', 'r') as file:
            sublist = str(file.readlines()[0]).split()
        while True:
            subreddit = random.choice(sublist)
            f = open(f'json/{subreddit}.json')
            jsonfile = json.load(f)
            dist = random.randint(0, jsonfile['data']['dist'] - 1)
            if jsonfile['data']['children'][dist]['data']['secure_media'] != None:
                if "mp4" in str(jsonfile['data']['children'][dist]['data']['secure_media']):
                    url = jsonfile['data']['children'][dist]['data']['secure_media']['reddit_video']['fallback_url']
                    await interaction.response.send_message(url.split("?source=fallback")[0])
                    break


async def setup(bot: commands.Bot):
    await bot.add_cog(video(bot))
