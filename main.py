# Imports
import grequests
import discord
import asyncio
import json
import os
from cogs.API import Cat
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from discord.ext import tasks, commands

# Bot class
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix='*')

    async def setup_hook(self):
        for i in os.listdir("cogs"):
            if i.endswith(".py") and i != "API.py":
                await self.load_extension(f"cogs.{i[:-3]}")

        await bot.tree.sync()

    async def on_ready(self):
        await self.wait_until_ready()
        print(f"Logged in as {self.user}.")

        jsonloop.start()

# Variables
bot = Bot()
cat = Cat()
token = 'enter-token-here'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


@tasks.loop(hours=1)
async def jsonloop():
    # Scrape videos from reddit
    now = datetime.now().strftime("%H:%M:%S")
    print(f"\n{now} - Scraping...")

    rs = (grequests.get(f'https://www.reddit.com/r/{u}.json?sort=hot&t=day&limit=100', headers=headers) for u in cat.subList)
    responses = grequests.map(rs)

    try:
        with open('data.json', 'r', encoding='utf8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
        data['webhooks'] = {}
        data["subreddits"] = {}
    
    for i in responses:
        try:
            if "mp4" in str(i.text):
                subData = json.loads(i.text)
                subName = subData["data"]["children"][0]["data"]["subreddit"]
                data["subreddits"][subName] = subData["data"]
        except:
            pass
    
    with open(f'data.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data))
    
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{now} - Finished scraping.")

    # Send photos to webhook
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{now} - Sending photos to webhooks...")

    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    
    webhooks = data["webhooks"]

    for url in webhooks.values():
        webhook = DiscordWebhook(url=url, username="Cat Bot", avatar_url="https://cdn.discordapp.com/avatars/977774728540459008/99b98aa4a7368955a41fe7796cc876de.webp?size=512")

        embed = DiscordEmbed(title="Hourly Cat Photo", color=0x3498DB)
        embed.set_image(url=cat.image(''))
        embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

        webhook.add_embed(embed)
        webhook.execute()

        await asyncio.sleep(1)
    
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{now} - Finished sending photos to webhooks.")

# Run the bot
bot.run(token)