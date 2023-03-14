import discord
import json
from discord.ext import commands
from utils import Cat

# Variables
cat = Cat()

# Command
class schedule(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name='schedule', description='Sends a cat image on an hourly basis.' )
    @discord.app_commands.describe(type='Whether to add, remove, or view your webhook from the schedule.', webhook='The webhook to add to the schedule.')
    @discord.app_commands.choices(type=[
        discord.app_commands.Choice(name='add', value='Add'),
        discord.app_commands.Choice(name='remove', value='Remove'),
        discord.app_commands.Choice(name='view', value='View')
    ])

    async def schedule(self, interaction: discord.Interaction, type: discord.app_commands.Choice[str], webhook: str = ''):
        webhook = webhook.strip()

        if interaction.user.guild_permissions.administrator:
            if type.value == 'Add':
                await addWebhook(interaction, webhook)

            elif type.value == 'Remove':
               await removeWebhook(interaction, webhook)

            elif type.value == 'View':
                await viewWebhook(interaction)
        else:
            await handleResponse(interaction, 'Error', 'You need to be an administrator to use this command.')

async def addWebhook(interaction: discord.Interaction, webhook: str):
    if webhook.startswith('https://discord.com/api/webhooks/'):
        with open('data.json', 'r', encoding='utf8') as f:
            data = json.load(f)

        if webhook not in data['webhooks'].values():
            await handleResponse(interaction, 'Success', 'Your webhook was added to the schedule.')

            data['webhooks'][str(interaction.guild.id)] = webhook
            with open('data.json', 'w', encoding='utf8') as f:
                f.write(json.dumps(data))
        else:
            await handleResponse(interaction, 'Error', 'This webhook is already registered.')
    else:
        await handleResponse(interaction, 'Error', 'You need to provide a valid webhook url.')

async def removeWebhook(interaction: discord.Interaction, webhook: str):
    if webhook.startswith('https://discord.com/api/webhooks/'):
        with open('data.json', 'r', encoding='utf8') as f:
            data = json.load(f)

        if data['webhooks'][str(interaction.guild.id)] == webhook:
            data['webhooks'].pop(str(interaction.guild.id))

            with open('data.json', 'w', encoding='utf8') as f:
                f.write(json.dumps(data))

            await handleResponse(interaction, 'Success', 'Your webhook was removed from the schedule.')

        else:
            await handleResponse(interaction, 'Error', 'This webhook is not registered for this server.')
    else:
        await handleResponse(interaction, 'Error', 'You need to provide a valid webhook url.')

async def viewWebhook(interaction: discord.Interaction):
    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)

    if str(interaction.guild.id) in data['webhooks'].keys():
        await handleResponse(interaction, 'Success', f'Your webhook is:\n\n{data["webhooks"][str(interaction.guild.id)]}')
    else:
        await handleResponse(interaction, 'Error', 'No webhooks for this server were found.')

# Function to handle responses so my code doesn't look unnecessarily bloated
async def handleResponse(interaction, type, text):
    image = cat.image()[0]['url']
    embed = discord.Embed(title=type, description=text)

    if type == 'Success':
        embed.color = discord.Colour(cat.embedColor)
    elif type == 'Error':
        embed.color = discord.Colour.red()

    embed.set_image(url=image)
    await interaction.response.send_message(embed=embed, ephemeral=True)

# Cog setup
async def setup(bot: commands.Bot):
    await bot.add_cog(schedule(bot))