import discord
import json
from cogs.API import Cat
from discord import app_commands
from discord.ext import commands

cat = Cat()

class schedule(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="schedule", description="Sends a cat image on an hourly basis." )
    @app_commands.describe(type="Whether to add, remove, or view your webhook from the schedule.", webhook="The webhook to add to the schedule.")
    @app_commands.choices(type=[
        app_commands.Choice(name="Add", value="Add"),
        app_commands.Choice(name="Remove", value="Remove"),
        app_commands.Choice(name="View", value="View")
    ])

    async def schedule(self, interaction: discord.Interaction, type: app_commands.Choice[str], webhook: str = ''):
        if interaction.user.guild_permissions.administrator:
            if type.value == 'Add':
                if webhook.startswith("https://discord.com/api/webhooks/"):
                    with open("data.json", "r", encoding="utf8") as f:
                        data = json.load(f)

                    if webhook not in data["webhooks"].values():
                        image = cat.image('')
                        embed = discord.Embed(title="Success", description="Your webhook was added to the schedule.", color=discord.Colour(cat.embedColor))
                        embed.set_image(url=image)
                        embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                        await interaction.response.send_message(embed=embed, ephemeral=True)

                        data["webhooks"][str(interaction.guild.id)] = webhook
                        with open("data.json", "w", encoding="utf8") as f:
                            f.write(json.dumps(data))
                    else:
                        image = cat.image('')
                        embed = discord.Embed(title="Error", description="This webhook is already registered.", color=discord.Colour(cat.embedColor))
                        embed.set_image(url=image)
                        embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    image = cat.image('')
                    embed = discord.Embed(title="Error", description="You need to provide a valid webhook url.", color=discord.Colour(cat.embedColor))
                    embed.set_image(url=image)
                    embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            
            elif type.value == 'Remove':
                if webhook.startswith("https://discord.com/api/webhooks/"):
                    with open("data.json", "r", encoding="utf8") as f:
                        data = json.load(f)

                    if data["webhooks"][str(interaction.guild.id)] == webhook:
                        image = cat.image('')
                        embed = discord.Embed(title="Success", description="Removed your webhook from the schedule successfully.", color=discord.Colour(cat.embedColor))
                        embed.set_image(url=image)
                        embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                        await interaction.response.send_message(embed=embed, ephemeral=True)

                        data["webhooks"].pop(str(interaction.guild.id))
                        with open("data.json", "w", encoding="utf8") as f:
                            f.write(json.dumps(data))
                    else:
                        image = cat.image('')
                        embed = discord.Embed(title="Error", description="The provided webhook wasn't found for the current guild.", color=discord.Colour(cat.embedColor))
                        embed.set_image(url=image)
                        embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                        await interaction.response.send_message(embed=embed, ephemeral=True)    
                else:
                    image = cat.image('')
                    embed = discord.Embed(title="Error", description="You need to provide a valid webhook url.", color=discord.Colour(cat.embedColor))
                    embed.set_image(url=image)
                    embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            
            elif type.value == 'View':
                with open("data.json", "r", encoding="utf8") as f:
                    data = json.load(f)
                
                if str(interaction.guild.id) in data["webhooks"].keys():
                    image = cat.image('')
                    embed = discord.Embed(title="Success", description=f"The webhook {data['webhooks'][str(interaction.guild.id)]} is registered for scheduling.", color=discord.Colour(cat.embedColor))
                    embed.set_image(url=image)
                    embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    image = cat.image('')
                    embed = discord.Embed(title="Error", description="No webhooks for the current guild were found.", color=discord.Colour(cat.embedColor))
                    embed.set_image(url=image)
                    embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
                    await interaction.response.send_message(embed=embed, ephemeral=True)    
        else:
            image = cat.image('')
            embed = discord.Embed(title="Error", description="You need to be an administrator to use this command.", color=discord.Colour(cat.embedColor))
            embed.set_image(url=image)
            embed.set_footer(text="Made by @kittiesgif", icon_url="https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif")
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(schedule(bot))
