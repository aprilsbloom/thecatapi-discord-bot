# <-- Imports -->
import os
import discord
from datetime import datetime
from discord.ext import tasks, commands

# <-- Classes -->
class Bot(commands.Bot):
	def __init__(self):
		super().__init__(intents=discord.Intents.default(), command_prefix='')

	async def setup_hook(self):
		for i in os.listdir('commands'):
			if i.endswith('.py'):
				await self.load_extension(f'commands.{os.path.splitext(i)[0]}')

		await bot.tree.sync()

	async def on_ready(self):
		await self.wait_until_ready()
		print(f'Logged in as {self.user}.')

		rpc.start()

# <-- Tasks -->
@tasks.loop(minutes=1)
async def rpc():
	activity = discord.Activity(type=discord.ActivityType.listening, name=f"/help in {len(bot.guilds)} servers")
	await bot.change_presence(activity=activity)

# <-- Variables -->
bot = Bot()

# This is to ensure that the hourly cat photo
# is sent at the same time every hour
print('Waiting for the next hour to start.')
previousHour = datetime.now()

while True:
	currentHour = datetime.now()
	if currentHour.hour != previousHour.hour:
		break

bot.run("")