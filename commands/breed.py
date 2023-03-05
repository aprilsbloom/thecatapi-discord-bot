import discord
from discord.ext import commands
from utils import Cat

# Variables
cat = Cat()
greenStar = ':green_square:'
blackStar = ':black_large_square:'

# Buttons
class pages(discord.ui.View):
    def __init__(self, interaction: discord.Interaction, pages: list):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.pages = pages
        self.current_page = 0

    @discord.ui.button(label='Previous', style=discord.ButtonStyle.grey, disabled=True)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page -= 1
        image = cat.image()
        self.pages[self.current_page].set_image(url=image)

        if self.current_page == 0:
            for i in self.children:
                if i.label == 'Previous':
                    i.disabled = True
                elif i.label == 'Next':
                    i.disabled = False
        else:
            for i in self.children:
                if i.label == 'Previous':
                    i.disabled = False
                elif i.label == 'Next':
                    i.disabled = False

        await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)

    @discord.ui.button(label='Next', style=discord.ButtonStyle.grey)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page += 1
        image = cat.image()
        self.pages[self.current_page].set_image(url=image)

        if self.current_page == len(self.pages) - 1:
            for i in self.children:
                if i.label == 'Next':
                    i.disabled = True
                elif i.label == 'Previous':
                    i.disabled = False
        else:
            for i in self.children:
                if i.label == 'Next':
                    i.disabled = False
                elif i.label == 'Previous':
                    i.disabled = False

        await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)

    async def interaction_check(self, interaction: discord.Interaction, /) -> bool:
        if interaction.user.id != self.interaction.user.id:
            image = cat.image()

            embed = discord.Embed(title='Error', description="You can't use this button because you didn\'t start the command. Try running </breeds:1> and selecting \"list\".", color=discord.Colour.red())
            embed.set_image(url=image)
            embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

            await interaction.response.send_message(embed=embed, ephemeral=True)
            return False
        else:
            return True

    async def on_timeout(self):
        for i in self.children:
            i.disabled = True

# Command
class breeds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name='breeds', description='Sends info on a cat breed.')
    @discord.app_commands.describe(breed='Your breed of choice that you want to know more about.')
    @discord.app_commands.choices(type=[
        discord.app_commands.Choice(name='information', value='Information'),
        discord.app_commands.Choice(name='stats', value='Stats'),
        discord.app_commands.Choice(name='list', value='List')
    ])

    async def breeds(self, interaction: discord.Interaction, type: discord.app_commands.Choice[str], breed: str = ''):
        breeds = cat.get_breeds()
        breedIDs = [i['id'] for i in breeds]

        if type.value == 'Information':
            if breed in breedIDs:
                image = cat.image(breed=breed)
                breedData = cat.get_breed_info(breed)

                embed = discord.Embed(title=breedData['name'], description=breedData['description'], color=discord.Colour(cat.embedColor))
                embed.add_field(name='Stats', value=f'''
**Weight**\n{breedData['weight']['imperial']} lbs / {breedData['weight']['metric']} kg\n
**Temperament**\n{breedData['temperament']}\n
**Origin**\n{breedData['origin']}\n
**Life Span**\n{breedData['life_span']} years\n
**Wikipedia URL**\n{breedData['wikipedia_url']}\n''', inline=True)
                embed.set_image(url=image)

                await interaction.response.send_message(embed=embed)

            else:
                image = cat.image()

                embed = discord.Embed(title='Error', description="This breed doesn't exist.\nPlease check you entered the corresponding 4 letter code for your chosen breed by running </breeds:1> and selecting \"list\".",color=discord.Colour.red())
                embed.set_image(url=image)
                embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

                await interaction.response.send_message(embed=embed)

        elif type.value == 'Stats':
            if breed in breedIDs:
                image = cat.image(breed=breed)
                breedData = cat.get_breed_info(breed)

                embed=discord.Embed(title=breedData['name'], color=discord.Colour(cat.embedColor))
                embed.add_field(name='Adaptability', value=f'{greenStar * breedData["adaptability"]}{blackStar * (5 - breedData["adaptability"])}', inline=True)
                embed.add_field(name='Affection Level', value=f'{greenStar * breedData["affection_level"]}{blackStar * (5 - breedData["affection_level"])}', inline=True)
                embed.add_field(name='Child Friendly', value=f'{greenStar * breedData["child_friendly"]}{blackStar * (5 - breedData["child_friendly"])}', inline=True)
                embed.add_field(name='Dog Friendly', value=f'{greenStar * breedData["dog_friendly"]}{blackStar * (5 - breedData["dog_friendly"])}', inline=True)
                embed.add_field(name='Energy Level', value=f'{greenStar * breedData["energy_level"]}{blackStar * (5 - breedData["energy_level"])}', inline=True)
                embed.add_field(name='Grooming', value=f'{greenStar * breedData["grooming"]}{blackStar * (5 - breedData["grooming"])}', inline=True)
                embed.add_field(name='Health Issues', value=f'{greenStar * breedData["health_issues"]}{blackStar * (5 - breedData["health_issues"])}', inline=True)
                embed.add_field(name='Intelligence', value=f'{greenStar * breedData["intelligence"]}{blackStar * (5 - breedData["intelligence"])}', inline=True)
                embed.add_field(name='Shedding Level', value=f'{greenStar * breedData["shedding_level"]}{blackStar * (5 - breedData["shedding_level"])}', inline=True)
                embed.add_field(name='Social Needs', value=f'{greenStar * breedData["social_needs"]}{blackStar * (5 - breedData["social_needs"])}', inline=True)
                embed.add_field(name='Stranger Friendly', value=f'{greenStar * breedData["stranger_friendly"]}{blackStar * (5 - breedData["stranger_friendly"])}', inline=True)
                embed.add_field(name='Vocalisation', value=f'{greenStar * breedData["vocalisation"]}{blackStar * (5 - breedData["vocalisation"])}', inline=True)
                embed.set_image(url=image)

                await interaction.response.send_message(embed=embed)
            else:
                image = cat.image()

                embed = discord.Embed(title='Error', description='This breed doesn\'t exist.\nPlease check you entered the corresponding 4 letter code for your chosen breed by running </breeds:1> and selecting "list".', color=discord.Colour.red())
                embed.set_image(url=image)
                embed.set_footer(text='Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')

                await interaction.response.send_message(embed=embed)

        elif type.value == 'List':
            embeds = []
            count = 0

            for i in range(0, len(breeds), 10):
                count += 1
                embed = discord.Embed(title='Breed List', description=f'The bot currently supports a total of {len(breeds)} breeds.\nTo get any information about the breeds listed below, you can run the </breeds:1> command and select either "information" or "statistics".', color=discord.Colour(cat.embedColor))

                for breed in breeds[i:i+10]:
                    embed.add_field(name=breed['name'], value=breed['id'], inline=True)

                embed.set_footer(text=f'Page {count} of {len(breeds) // 10 + 1} - Made by @gifkitties', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
                embeds.append(embed)

            embeds[0].set_image(url=cat.image())
            await interaction.response.send_message(embed=embeds[0], view=pages(interaction, embeds))

# Cog setup
async def setup(bot: commands.Bot):
    await bot.add_cog(breeds(bot))