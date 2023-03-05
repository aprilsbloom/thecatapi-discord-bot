import discord
import json
from discord.ext import commands
from utils import Cat

cat = Cat()

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
        if interaction.user.guild_permissions.administrator:
            if type.value == 'Add':
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

            elif type.value == 'Remove':
                if webhook.startswith('https://discord.com/api/webhooks/'):
                    with open('data.json', 'r', encoding='utf8') as f:
                        data = json.load(f)

                    if data['webhooks'][str(interaction.guild.id)] == webhook:
                        await handleResponse(interaction, 'Success', 'Your webhook was removed from the schedule.')
                        data['webhooks'].pop(str(interaction.guild.id))

                        with open('data.json', 'w', encoding='utf8') as f:
                            f.write(json.dumps(data))
                    else:
                        await handleResponse(interaction, 'Error', 'This webhook is not registered for this server.')
                else:
                    await handleResponse(interaction, 'Error', 'You need to provide a valid webhook url.')

            elif type.value == 'View':
                with open('data.json', 'r', encoding='utf8') as f:
                    data = json.load(f)

                if str(interaction.guild.id) in data['webhooks'].keys():
                    await handleResponse(interaction, 'Success', f'Your webhook is: `{data["webhooks"][str(interaction.guild.id)]}`.')
                else:
                    await handleResponse(interaction, 'Error', 'No webhooks for this server were found.')
        else:
            await handleResponse(interaction, 'Error', 'You need to be an administrator to use this command.')

async def handleResponse(interaction, type, text):
    image = cat.image()
    embed = discord.Embed(title=type, description=text)

    if type == 'Success':
        embed.color = discord.Colour(cat.embedColor)
    elif type == 'Error':
        embed.color = discord.Colour.red()

    embed.set_image(url=image)
    embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
    await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(schedule(bot))