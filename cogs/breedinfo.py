import discord
import requests
import random
from discord import app_commands
from discord.ext import commands

breedlist = 'abys aege abob acur asho awir amau amis bali bamb beng birm bomb bslo bsho bure buri cspa ctif char chau chee csho crex cymr cypr drex dons lihu emau ebur esho hbro hima jbob java khao kora kuri lape mcoo mala manx munc nebe norw ocic orie pers pixi raga ragd rblu sava sfol srex siam sibe sing snow soma sphy tonk toyg tang tvan ycho'
apikeys = []

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


class breedinfo(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="breedinfo",
                          description="Sends info on a cat breed.")
    @app_commands.describe(
        breed="Your breed of choice that you want to know more about.", )
    async def breedinfo(self,
                        interaction: discord.Interaction,
                        breed: str = 'aaa'):
        if breed in breedlist:
            r = requests.get(f'https://api.thecatapi.com/v1/breeds/{breed}',
                             headers={'x-api-key': random.choice(apikeys)})
            image = requests.get(
                f'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&breed_ids={breed}',
                headers={
                    'x-api-key': random.choice(apikeys)
                }).json()[0]['url']

            weightimperial = r.json()['weight']['imperial']
            weightmetric = r.json()['weight']['metric']
            temperament = r.json()['temperament']
            origin = r.json()['origin']
            life_span = r.json()['life_span']
            wikipedia_url = r.json()['wikipedia_url']
            description = r.json()['description']

            embed = discord.Embed(title=r.json()['name'],
                                  description=description,
                                  color=discord.Colour(0x3498DB))
            embed.add_field(name="Stats",
                            value=f"""
                **Weight**\n{weightimperial} lbs / {weightmetric} kg\n
**Temperament**\n{temperament}\n
**Origin**\n{origin}\n
**Life Span**\n{life_span} years\n
**Wikipedia URL**\n{wikipedia_url}\n""",
                            inline=True)
            embed.set_image(url=image)
            await interaction.response.send_message(embed=embed)
        else:
            image = requests.get(
                'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png',
                headers={
                    'x-api-key': random.choice(apikeys)
                }).json()[0]['url']
            embed = discord.Embed(
                title="Error",
                description="This breed doesn't exist.\nPlease check you entered the corresponding 4 letter code for your chosen breed from the PasteBin link in </help:1>.",
                color=discord.Colour(0x3498DB))
            embed.set_image(url=image)
            embed.set_footer(
                text='Made by @gifkitties',
                icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif'
            )
            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(breedinfo(bot))
