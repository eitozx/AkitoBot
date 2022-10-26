import os
import animu
import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class AnifactCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "anifact", 
        description = "To Get Facts Based on Anime Characters"
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.cooldown(5, 1, commands.BucketType.default)
    async def anifact(self, ctx):

        client = animu.Client(os.getenv("AIRI_TOKEN"))
        Object = await client.fact()

        embed = discord.Embed(
            title=f"<:Anime:881813511414611968> #{Object.id} | Anime Fact",
            colour=discord.Color.blue(),
            description=Object)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(AnifactCmd(bot))
