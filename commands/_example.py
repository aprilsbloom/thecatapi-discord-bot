import discord
from discord.ext import commands

class Example(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@discord.app_commands.command(name='example', description='Example command.')
	async def example(self, interaction: discord.Interaction):
		pass

# Cog setup
async def setup(bot: commands.Bot):
	await bot.add_cog(Example(bot))