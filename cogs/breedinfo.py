import discord
from API import Cat
from discord import app_commands
from discord.ext import commands

cat = Cat()

class breedinfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="breed", description="Sends info on a cat breed.")
    @app_commands.describe(breed="Your breed of choice that you want to know more about.")
    @app_commands.choices(type=[
        app_commands.Choice(name="information", value="Information"),
        app_commands.Choice(name="stats", value="Stats"),
        app_commands.Choice(name="list", value="List")
    ])

    async def breedinfo(self, interaction: discord.Interaction, type: app_commands.Choice[str], breed: str = ''):
        if type.value == 'Information':
            if breed in cat.breedList:
                breedData = cat.get_breed_info(breed)
                image = cat.image(breed)
                
                name = breedData['name']
                weightimperial = breedData['weight']['imperial']
                weightmetric = breedData['weight']['metric']
                temperament = breedData['temperament']
                origin = breedData['origin']
                life_span = breedData['life_span']
                wikipedia_url = breedData['wikipedia_url']
                description = breedData['description']

                embed = discord.Embed(title=name, description=description, color=discord.Colour(cat.embedColor))
                embed.add_field(name="Stats", value=f"""
**Weight**\n{weightimperial} lbs / {weightmetric} kg\n
**Temperament**\n{temperament}\n
**Origin**\n{origin}\n
**Life Span**\n{life_span} years\n
**Wikipedia URL**\n{wikipedia_url}\n""", inline=True)
                embed.set_image(url=image)
                await interaction.response.send_message(embed=embed)
            else:
                image = cat.image()
                embed = discord.Embed(title="Error", description="This breed doesn't exist.\nPlease check you entered the corresponding 4 letter code for your chosen breed by running </breed:1> and selecting 'list'.",color=discord.Colour(cat.embedColor))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)
        
        elif type.value == 'Stats':
            if breed in cat.breedList:
                image = cat.image(breed)
                breedData = cat.get_breed_info(breed)

                name = breedData['name']
                adaptability = breedData['adaptability']
                affection_level = breedData['affection_level']
                child_friendly = breedData['child_friendly']
                dogfriendly = breedData['dog_friendly']
                energy_level = breedData['energy_level']
                grooming = breedData['grooming']
                healthissues = breedData['health_issues']
                intelligence = breedData['intelligence']
                shedding = breedData['shedding_level']
                socialneeds = breedData['social_needs']
                strangerfriendly = breedData['stranger_friendly']
                vocalisation = breedData['vocalisation']
                greenStar = ':green_square:'
                blackStar = ':black_large_square:'

                embed=discord.Embed(title=name, color=discord.Colour(cat.embedColor))
                embed.add_field(name="Adaptability", value=f"{greenStar * adaptability}{blackStar * (5 - adaptability)}", inline=True)
                embed.add_field(name="Affection Level", value=f"{greenStar * affection_level}{blackStar * (5 - affection_level)}", inline=True)
                embed.add_field(name="Child Friendly", value=f"{greenStar * child_friendly}{blackStar * (5 - child_friendly)}", inline=True)
                embed.add_field(name="Dog Friendly", value=f"{greenStar * dogfriendly}{blackStar * (5 - dogfriendly)}", inline=True)
                embed.add_field(name="Energy Level", value=f"{greenStar * energy_level}{blackStar * (5 - energy_level)}", inline=True)
                embed.add_field(name="Grooming", value=f"{greenStar * grooming}{blackStar * (5 - grooming)}", inline=True)
                embed.add_field(name="Health Issues", value=f"{greenStar * healthissues}{blackStar * (5 - healthissues)}", inline=True)
                embed.add_field(name="Intelligence", value=f"{greenStar * intelligence}{blackStar * (5 - intelligence)}", inline=True)
                embed.add_field(name="Shedding Level", value=f"{greenStar * shedding}{blackStar * (5 - shedding)}", inline=True)
                embed.add_field(name="Social Needs", value=f"{greenStar * socialneeds}{blackStar * (5 - socialneeds)}", inline=True)
                embed.add_field(name="Stranger Friendly", value=f"{greenStar * strangerfriendly}{blackStar * (5 - strangerfriendly)}", inline=True)
                embed.add_field(name="Vocalisation", value=f"{greenStar * vocalisation}{blackStar * (5 - vocalisation)}", inline=True)
                embed.set_image(url=image)
                await interaction.response.send_message(embed=embed)
            else:
                image = cat.image()
                embed = discord.Embed(title="Error", description="This breed doesn't exist.\nPlease check you entered the corresponding 4 letter code for your chosen breed by running </breed:1> and selecting 'list'.", color=discord.Colour(cat.embedColor))
                embed.set_image(url=image)
                embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                await interaction.response.send_message(embed=embed)
        
        elif type.value == 'List':
            breeds = cat.get_breeds()
            image = cat.image()

            embed = discord.Embed(title="Breed List", description=f"The bot currently supports a total of {len(breeds)} breeds.\nTo get any information about the breeds listed below, you can run the </breed:1> command and select either 'list' or 'statistics'.", color=discord.Colour(cat.embedColor))
            for i in range(0, len(breeds)):
                embed.add_field(name=breeds[i]['name'], value=f"Code: {breeds[i]['id']}", inline=True)
            embed.set_image(url=image)

            await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(breedinfo(bot))