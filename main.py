import asyncio
import requests
import json
import discord
import os
import shutil
from discord.ext import tasks, commands

token = os.environ["token"]
headers = {
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "fr,en-US;q=0.9,en;q=0.8",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix='*')

    async def setup_hook(self):
        await self.load_extension('cogs.breedinfo')
        await self.load_extension('cogs.breedstats')
        await self.load_extension('cogs.gif')
        await self.load_extension('cogs.image')
        await self.load_extension('cogs.video')
        await self.load_extension('cogs.help')
        await self.load_extension('cogs.fact')
        await self.load_extension('cogs.submit')
        await bot.tree.sync()

    async def on_ready(self):
        jsonloop.start()
        await self.wait_until_ready()
        print(f"Logged in as {self.user}.")
        rpc.start()


@tasks.loop(minutes=1)
async def rpc():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=f"/help in {len(bot.guilds)} servers"))
    await asyncio.sleep(30)
    await bot.change_presence(activity=discord.Game(
        name="Commands not working? Check my about me for more info."))


@tasks.loop(hours=1)
async def jsonloop():
    try:
        os.mkdir('json')
    except:
        shutil.rmtree('json')
        os.mkdir('json')

    with open('text/subredditlist.txt', 'r') as file:
        subredditlist = str(file.readlines()[0]).split()
    with open('text/newsub.txt', 'w') as file:
        file.write('')
    for i in subredditlist:
        r = requests.get(f'https://www.reddit.com/r/{i}.json', headers=headers)
        if "mp4" in str(r.text):
            with open(f'json/{i}.json', 'w', encoding='utf8') as subreddit:
                subreddit.write(json.dumps(json.loads(r.text), indent=2))
            with open('text/newsub.txt', 'a') as file:
                file.write(f'{i} ')


bot = Bot()
try:
    bot.run(token)
except:
    os.system('kill 1')
