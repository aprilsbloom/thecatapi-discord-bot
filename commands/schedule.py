import discord
import json
import typing
from utils import cat
from discord import app_commands
from discord.ext import commands

cat = cat()

class schedule(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='schedule', description='Sends a cat image on an hourly basis.' )
    @app_commands.describe(type='Whether to add, remove, or view your webhook from the schedule.', webhook='The webhook to add to the schedule.')
    @app_commands.choices(type=[
        app_commands.Choice(name='add', value='Add'),
        app_commands.Choice(name='remove', value='Remove'),
        app_commands.Choice(name='view', value='View')
    ])
    
    async def schedule(self, interaction: discord.Interaction, type: app_commands.Choice[str], webhook: str = ''):
        if interaction.user.guild_permissions.administrator:
            if type.value == 'Add':
                if webhook.startswith('https://discord.com/api/webhooks/'):
                    with open('data.json', 'r', encoding='utf8') as f:
                        data = json.load(f)

                    if webhook not in data['webhooks'].values():
                        handleResponse(interaction, 'Success', 'Your webhook was added to the schedule.')

                        data['webhooks'][str(interaction.guild.id)] = webhook
                        with open('data.json', 'w', encoding='utf8') as f:
                            f.write(json.dumps(data))
                    else:
                        handleResponse(interaction, 'Error', 'This webhook is already registered.')
                else:
                    handleResponse(interaction, 'Error', 'You need to provide a valid webhook url.')
            
            elif type.value == 'Remove':
                if webhook.startswith('https://discord.com/api/webhooks/'):
                    with open('data.json', 'r', encoding='utf8') as f:
                        data = json.load(f)

                    if data['webhooks'][str(interaction.guild.id)] == webhook:
                        handleResponse(interaction, 'Success', 'Your webhook was removed from the schedule.')

                        data['webhooks'].pop(str(interaction.guild.id))
                        with open('data.json', 'w', encoding='utf8') as f:
                            f.write(json.dumps(data))
                    else:
                        handleResponse(interaction, 'Error', 'This webhook is not registered for this server.')
                else:
                    handleResponse(interaction, 'Error', 'You need to provide a valid webhook url.')
            
            elif type.value == 'View':
                with open('data.json', 'r', encoding='utf8') as f:
                    data = json.load(f)
                
                if str(interaction.guild.id) in data['webhooks'].keys():
                    handleResponse(interaction, 'Success', f'Your webhook is: `{data["webhooks"][str(interaction.guild.id)]}`.')
                else:
                    handleResponse(interaction, 'Error', 'No webhooks for this server were found.')   
        else:
            handleResponse(interaction, 'Error', 'You need to be an administrator to use this command.')

async def handleResponse(interaction, type, text):
    image = cat.image()
    embed = discord.Embed(title=type, description=text, color=discord.Colour(cat.embedColor))
    embed.set_image(url=image)
    embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
    await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(schedule(bot))