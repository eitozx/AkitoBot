import json
import discord
from discord.ext import commands
from discord.commands import slash_command, permissions
import akito

class NukeCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "nuke",
        description = "To nuke text channel"
    )
    @commands.has_permissions(manage_channels=True)
    async def nuke(
        self, ctx, 
        channel: discord.Option(discord.TextChannel, 'Text Channel that you want to nuke', required=True)
    ):
        try:
            with open("data/MediaData.json") as f:
                data = json.load(f)
                gif = data["nuke"]

            new_channel = await channel.clone()
            await channel.delete()

            embed = discord.Embed(
                title=f"<:moderation:881782591060062288> CHANNEL NUKED!",
                colour=discord.Color.blue(),
                description=f"** **",
            )
            embed.set_image(url=gif)
            await new_channel.send(embed=embed)
            
        except:
            pass

def setup(bot):
    bot.add_cog(NukeCmd(bot))
