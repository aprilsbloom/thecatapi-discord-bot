import discord
import requests
import random
import json
import re
from discord import app_commands
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

apikeys = []


async def find_gif_url(string):
    # Regex to find the URL on the c.tenor.com domain that ends with .gif
    regex = r"(?i)\b((https?://c[.]tenor[.]com/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))[.]gif)"
    return re.findall(regex, string)[0][0]


class submit(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="submit", description="Sends a gif to be posted on @gifkitties.")
    async def submit(self, interaction: discord.Interaction, url: str = 'hi'):
        author = f'Submission by {str(interaction.user)}.\nID: {str(interaction.user.id)}'
        if url != 'hi':
            f = open('data.json')
            jsonfile = json.load(f)
            submissioncount = jsonfile['subcount'] + 1
            jsonfile['subcount'] = submissioncount

            webhook = DiscordWebhook(
                url='enter your webhook url here',
                rate_limit_retry=True)

            if 'https' in url or 'http' in url:
                if '.gif' in url:
                    headers = {'x-api-key': random.choice(apikeys)}
                    image = requests.get(
                        "https://api.thecatapi.com/v1/images/search?mime_types=jpg,png",
                        headers=headers).json()[0]['url']
                    embed = discord.Embed(
                        title="Successfully sent your submission!",
                        color=discord.Colour(0x3498DB))
                    embed.set_image(url=image)
                    embed.set_footer(
                        text='Made by @gifkitties',
                        icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'
                    )
                    await interaction.response.send_message(embed=embed,
                                                            ephemeral=True)

                    embed = DiscordEmbed(
                        title=f'Submission #{submissioncount}',
                        color='03b2f8',
                        description=author)
                    embed.set_image(url=url)
                    webhook.add_embed(embed)
                    webhook.execute()
                    with open('data.json', 'w', encoding='utf8') as jsonwrite:
                        jsonwrite.write(json.dumps(jsonfile, indent=2))
                elif '.mp4' in url:
                    headers = {'x-api-key': random.choice(apikeys)}
                    image = requests.get(
                        "https://api.thecatapi.com/v1/images/search?mime_types=jpg,png",
                        headers=headers).json()[0]['url']
                    embed = discord.Embed(
                        title="Successfully sent your submission!",
                        color=discord.Colour(0x3498DB))
                    embed.set_image(url=image)
                    embed.set_footer(
                        text='Made by @gifkitties',
                        icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'
                    )
                    await interaction.response.send_message(embed=embed,
                                                            ephemeral=True)

                    embed = DiscordEmbed(
                        title=f'Submission #{submissioncount}',
                        color='03b2f8',
                        description=f'{url}\n\n{author}')
                    webhook.add_embed(embed)
                    webhook.execute()
                    with open('data.json', 'w', encoding='utf8') as jsonwrite:
                        jsonwrite.write(json.dumps(jsonfile, indent=2))
                elif 'tenor.com' in url:
                    headers = {'x-api-key': random.choice(apikeys)}
                    image = requests.get(
                        "https://api.thecatapi.com/v1/images/search?mime_types=jpg,png",
                        headers=headers).json()[0]['url']
                    embed = discord.Embed(
                        title="Successfully sent your submission!",
                        color=discord.Colour(0x3498DB))
                    embed.set_image(url=image)
                    embed.set_footer(
                        text='Made by @gifkitties',
                        icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'
                    )
                    await interaction.response.send_message(embed=embed,
                                                            ephemeral=True)

                    r = requests.get(url)
                    url = await find_gif_url(r.text)
                    embed = DiscordEmbed(
                        title=f'Submission #{submissioncount}',
                        color='03b2f8',
                        description=author)
                    embed.set_image(url=url)
                    webhook.add_embed(embed)
                    webhook.execute()
                    with open('data.json', 'w', encoding='utf8') as jsonwrite:
                        jsonwrite.write(json.dumps(jsonfile, indent=2))
                else:
                    headers = {'x-api-key': random.choice(apikeys)}
                    image = requests.get(
                        'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png',
                        headers=headers).json()[0]['url']
                    embed = discord.Embed(
                        title="Error",
                        description="Please check you entered a valid url and try again.",
                        color=discord.Colour(0x3498DB))
                    embed.set_image(url=image)
                    embed.set_footer(
                        text='Made by @gifkitties',
                        icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'
                    )
                    await interaction.response.send_message(embed=embed,
                                                            ephemeral=True)
            else:
                headers = {'x-api-key': random.choice(apikeys)}
                image = requests.get(
                    'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png',
                    headers=headers).json()[0]['url']
                embed = discord.Embed(
                    title="Error",
                    description="Please check you entered a valid url and try again.",
                    color=discord.Colour(0x3498DB))
                embed.set_image(url=image)
                embed.set_footer(
                    text='Made by @gifkitties',
                    icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'
                )
                await interaction.response.send_message(embed=embed,
                                                        ephemeral=True)
        else:
            headers = {'x-api-key': random.choice(apikeys)}
            image = requests.get(
                'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png',
                headers=headers).json()[0]['url']
            embed = discord.Embed(
                title="Error",
                description="Please check you entered a valid url and try again.",
                color=discord.Colour(0x3498DB))
            embed.set_image(url=image)
            embed.set_footer(
                text='Made by @gifkitties',
                icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'
            )
            await interaction.response.send_message(embed=embed,
                                                    ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(submit(bot))
