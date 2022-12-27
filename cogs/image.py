import discord
import urllib.parse
from API import Cat
from discord import app_commands
from discord.ext import commands

cat = Cat()

class buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(emoji='❤️', style=discord.ButtonStyle.grey)
    async def favorite(self, interaction: discord.Interaction, button: discord.ui.Button):
        imgID = interaction.message.embeds[0].image.url.split('/')[-1].split('.')[0]
        subID = urllib.parse.quote(str(interaction.message.author.id))
        result = cat.favourite(imgID, subID)
        image = cat.image()
        embed = discord.Embed(color=discord.Colour(cat.embedColor))
        embed.set_image(url=image)

        if result['message'] == 'SUCCESS':
            embed.title = 'Success'
            embed.description = 'You favorited this image.'
        else:
            embed.title = 'Error'
            embed.description = 'An error occured, please try again later.'
        
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(emoji='💔', style=discord.ButtonStyle.grey)
    async def unfavorite(self, interaction: discord.Interaction, button: discord.ui.Button):
        imgID = interaction.message.embeds[0].image.url.split('/')[-1].split('.')[0]
        subID = urllib.parse.quote(str(interaction.message.author.id))
        result = cat.unfavourite(imgID, subID)
        image = cat.image()
        embed = discord.Embed(color=discord.Colour(cat.embedColor))
        embed.set_image(url=image)
        
        if result['message'] == 'SUCCESS':
            embed.title = 'Success'
            embed.description = 'You unfavorited this image.'
        else:
            embed.title = 'Error'
            embed.description = 'An error occured, please try again later.'
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(emoji='👍', style=discord.ButtonStyle.green)
    async def upvote(self, interaction: discord.Interaction, button: discord.ui.Button):
        imgID = interaction.message.embeds[0].image.url.split('/')[-1].split('.')[0]
        subID = urllib.parse.quote(str(interaction.message.author.id))
        result = cat.upvote(imgID, subID)
        image = cat.image()
        embed = discord.Embed(color=discord.Colour(cat.embedColor))
        embed.set_image(url=image)
        
        if result['message'] == 'SUCCESS':
            embed.title = 'Success'
            embed.description = 'You upvoted this image.'
        else:
            embed.title = 'Error'
            embed.description = 'An error occured, please try again later.'
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(emoji='👎', style=discord.ButtonStyle.red)
    async def downvote(self, interaction: discord.Interaction, button: discord.ui.Button):
        imgID = interaction.message.embeds[0].image.url.split('/')[-1].split('.')[0]
        subID = urllib.parse.quote(str(interaction.message.author.id))
        result = cat.downvote(imgID, subID)
        image = cat.image()
        embed = discord.Embed(color=discord.Colour(cat.embedColor))
        embed.set_image(url=image)
        
        if result['message'] == 'SUCCESS':
            embed.title = 'Success'
            embed.description = 'You downvoted this image.'
        else:
            embed.title = 'Error'
            embed.description = 'An error occured, please try again later.'
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

class image(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = 'image', description = 'Sends a cat image.')

    async def image(self, interaction: discord.Interaction, breed: str = ''):
        view = buttons()
        embed = discord.Embed(color=discord.Colour(cat.embedColor))
        embed.set_footer(text='Made by @kittiesgif', icon_url='https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif')
        
        if breed == '':
            image = cat.image()
            embed.title = 'Here\'s a cat image:'
            embed.set_image(url=image)
        else:
            if breed in Cat.breedList:
                image = cat.image(breed)
                breedname = Cat.get_breed_info(self, breed)['name']
                embed.title = 'Here\'s a cat image:'
                embed.description = f'Breed: {breedname}'
                embed.set_image(url=image)
            else:
                image = cat.image()
                embed.title = 'Error'
                embed.description = 'This breed doesn\'t exist. Please check your spelling and try again.'
                embed.set_image(url=image)
        
        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(image(bot))