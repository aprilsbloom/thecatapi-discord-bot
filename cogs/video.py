import discord
import random
import json
from discord import app_commands
from discord.ext import commands

class video(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "video", description = "Sends a cat video.")

    async def video(self, interaction: discord.Interaction):
        with open("data.json", "r", encoding="utf8") as f:
            data = json.load(f)
            dataKeys = list(data["subreddits"].keys())
            while True:
                subreddit = random.choice(dataKeys)
                jsonfile = data["subreddits"][subreddit]
                dist = random.randint(0, int(jsonfile["dist"]))
                
                try:
                    if jsonfile["children"][dist]['data']['secure_media'] != None:
                        try:
                            url = jsonfile["children"][dist]['data']['secure_media']['reddit_video']['fallback_url'].split("?source=fallback")[0]
                            author = jsonfile["children"][dist]['data']['author']
                            title = jsonfile["children"][dist]['data']['title']
                            postLink = f'<https://www.reddit.com{jsonfile["children"][dist]["data"]["permalink"]}>'

                            await interaction.response.send_message(f'**{title}**\nPosted by u/{author} in r/{subreddit}\n\n{postLink}\n{url}')
                            break
                        except:
                            pass
                except:
                    pass
                        

async def setup(bot: commands.Bot):
    await bot.add_cog(video(bot))