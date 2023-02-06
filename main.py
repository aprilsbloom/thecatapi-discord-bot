# <-- Imports -->
import grequests
import discord
import asyncio
import json
import os
from API import Cat
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import tasks, commands

# <-- Classes -->
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix='*')

    async def setup_hook(self):
        for i in os.listdir('cogs'):
            if i.endswith('.py'):
                await self.load_extension(f'cogs.{i[:-3]}')

        await bot.tree.sync()

    async def on_ready(self):
        await self.wait_until_ready()
        print(f'Logged in as {self.user}.')

        rpc.start()
        videoScrape.start()
        
# <-- Functions -->
def log(s):
    now = datetime.now().strftime('%H:%M:%S')
    print(f'{now} - {s}')
    
@tasks.loop(minutes=1)
async def rpc():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"/help in {len(bot.guilds)} servers"))

@tasks.loop(hours=1)
async def videoScrape():
    log('Scraping videos from subreddits')

    rs = (grequests.get(f'https://www.reddit.com/r/{u}.json?sort=hot&t=day&limit=100', headers=headers) for u in cat.subList)
    responses = grequests.map(rs)

    try:
        with open('data.json', 'r', encoding='utf8') as f:
            data = json.load(f)
            data['videos'] = []
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {
            'webhooks': {},
            'videos': []
        }
    
    for i in responses:
        subData = i.json()['data']['children']
        
        for i in subData:
            obj = i['data']
            
            if not obj['is_video']:
                continue
            
            data['videos'].append({
                'title': obj['title'].encode().decode('utf8'),
                'author': obj['author'],
                'subreddit': obj['subreddit'],
                'permalink': f'https://www.reddit.com{obj["permalink"]}',
                'video': obj['secure_media']['reddit_video']['fallback_url'].split('?')[0],
            })
    
    with open('data.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data))
                
    log('Finished scraping videos')


    # Send photos to webhook
    log('Sending photos to webhooks')

    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    
    webhooks = data['webhooks']
    for url in webhooks.values():
        webhook = DiscordWebhook(url=url, username='Cat Bot', avatar_url='https://cdn.discordapp.com/avatars/977774728540459008/99b98aa4a7368955a41fe7796cc876de.webp?size=512')

        embed = DiscordEmbed(title='Hourly Cat Photo', color=cat.embedColor)
        embed.set_image(url=cat.image())
        embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

        webhook.add_embed(embed)
        webhook.execute()

        await asyncio.sleep(2)
    
    log('Finished sending photos to webhooks')

# <-- Variables -->
bot = Bot()
cat = Cat()
token = ''
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'
}

# <-- Main -->
previoushour = datetime.now().hour
while True:
    currenthour = datetime.now().hour
    if currenthour != previoushour:
        bot.run(token)
        break