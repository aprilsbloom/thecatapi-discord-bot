# <-- Imports -->
import grequests
import requests
import asyncio
import json
import os
import discord
from datetime import datetime
from discord.ext import tasks, commands
from utils import Cat, Logger

# <-- Classes -->
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix='')

    async def setup_hook(self):
        [await self.load_extension(f'commands.{os.path.splitext(i)[0]}') for i in os.listdir('commands') if i.endswith('.py')]

        await bot.tree.sync()

    async def on_ready(self):
        await self.wait_until_ready()
        print(f'Logged in as {self.user}.')

        hourlyPhoto.start()
        scrapeVideos.start()
        rpc.start()

# <-- Tasks -->
@tasks.loop(minutes=1)
async def rpc():
    activity = discord.Activity(type=discord.ActivityType.listening, name=f"/help in {len(bot.guilds)} servers")
    await bot.change_presence(activity=activity)

@tasks.loop(hours=1)
async def scrapeVideos():
    log.info('Scraping videos from Reddit.')

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

    for i, r in enumerate(responses):
        try:
            subData = r.json()['data']['children']

            for i in subData:
                obj = i['data']

                if not obj['is_video']:
                    continue

                # Parse only the data that I need, and add it to the videos array in data.json
                data['videos'].append(
                    {
                        'title': obj['title'].encode().decode('utf8'),
                        'author': obj['author'],
                        'subreddit': obj['subreddit'],
                        'permalink': f'https://www.reddit.com{obj["permalink"]}',
                        'video': obj['secure_media']['reddit_video']['fallback_url'].split('?')[0]
                    }
                )

        except Exception:
            log.error(f"Error scraping videos from r/{cat.subList[i]}.")

    with open('data.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data))

    log.success('Finished scraping videos from Reddit!')

@tasks.loop(hours=1)
async def hourlyPhoto():
    log.info('Sending photos to webhooks.')

    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)

    pfp = bot.user.display_avatar

    image = cat.image()[0]['url']
    for i in dict(data['webhooks']):
        url = data['webhooks'][i]

        postData = {
            "username": "Cat Bot",
            "avatar_url": pfp,
            "embeds": [
                {
                    "title": "Hourly Cat Photo",
                    "color": 0x3498DB,
                    "image": {
                        "url": image
                    }
                }
            ]
        }

        result = requests.post(url, json=postData)

        if result.status_code == 404:
            log.error(f'Error sending photo to webhook. Removing from schedule')
            data['webhooks'].pop(i)

        await asyncio.sleep(2.5)

    with open('data.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data))

    log.success('Finished sending photos to webhooks.')

# <-- Variables -->
bot = Bot()
cat = Cat()
log = Logger()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Cat Bot - https://github.com/paintingofblue/thecatapi-discord-bot'
}

# This is to ensure that the hourly cat photo
# is sent at the same time every hour
log.warning('Waiting for the next hour to start.')
previousHour = datetime.now()

while True:
    currentHour = datetime.now()
    if currentHour.hour != previousHour.hour:
        break

bot.run(cat.token)