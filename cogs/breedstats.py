from hashlib import sha1
from sqlite3 import adapt
import discord
import requests
import random
from discord import app_commands
from discord.ext import commands

breedlist = 'abys aege abob acur asho awir amau amis bali bamb beng birm bomb bslo bsho bure buri cspa ctif char chau chee csho crex cymr cypr drex dons lihu emau ebur esho hbro hima jbob java khao kora kuri lape mcoo mala manx munc nebe norw ocic orie pers pixi raga ragd rblu sava sfol srex siam sibe sing snow soma sphy tonk toyg tang tvan ycho'
apikeys = []

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


class breedstats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="breedstats",
        description="Sends the stats of a cat breed.")
    @app_commands.describe(
        breed="Your breed of choice that you want to know more about.",
    )
    async def breedstats(self, interaction: discord.Interaction, breed: str = 'aaa'):
        if breed in breedlist:
            r = requests.get(f'https://api.thecatapi.com/v1/breeds/{breed}', headers={
                             'x-api-key': random.choice(apikeys)})
            image = requests.get(f'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&breed_ids={breed}', headers={
                                 'x-api-key': random.choice(apikeys)}).json()[0]['url']

            name = r.json()['name']
            adaptability = r.json()['adaptability']
            affection_level = r.json()['affection_level']
            child_friendly = r.json()['child_friendly']
            dogfriendly = r.json()['dog_friendly']
            energy_level = r.json()['energy_level']
            grooming = r.json()['grooming']
            healthissues = r.json()['health_issues']
            intelligence = r.json()['intelligence']
            shedding = r.json()['shedding_level']
            socialneeds = r.json()['social_needs']
            strangerfriendly = r.json()['stranger_friendly']
            vocalisation = r.json()['vocalisation']
            star = ':star:'

            embed = discord.Embed(title=name)
            embed.add_field(name="Adaptability", value=star *
                            adaptability, inline=True)
            embed.add_field(name="Affection Level",
                            value=star * affection_level, inline=True)
            embed.add_field(name="Child Friendly", value=star *
                            child_friendly, inline=True)
            embed.add_field(name="Dog Friendly", value=star *
                            dogfriendly, inline=True)
            embed.add_field(name="Energy Level", value=star *
                            energy_level, inline=True)
            embed.add_field(name="Grooming", value=star *
                            grooming, inline=True)
            embed.add_field(name="Health Issues", value=star *
                            healthissues, inline=True)
            embed.add_field(name="Intelligence", value=star *
                            intelligence, inline=True)
            embed.add_field(name="Shedding Level",
                            value=star * shedding, inline=True)
            embed.add_field(name="Social Needs", value=star *
                            socialneeds, inline=True)
            embed.add_field(name="Stranger Friendly",
                            value=star * strangerfriendly, inline=True)
            embed.add_field(name="Vocalisation", value=star *
                            vocalisation, inline=True)
            embed.set_image(url=image)
            await interaction.response.send_message(embed=embed)
        else:
            image = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png',
                                 headers={'x-api-key': random.choice(apikeys)}).json()[0]['url']
            embed = discord.Embed(
                title="Error", description="This breed doesn't exist.\nPlease check you entered the corresponding 4 letter code for your chosen breed from the PasteBin link in </help:1>.", color=discord.Colour(0x3498DB))
            embed.set_image(url=image)
            embed.set_footer(text='Made by @gifkitties',
                             icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(breedstats(bot))
