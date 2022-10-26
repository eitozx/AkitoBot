import json
import akito
import random
import discord
from discord.ext import commands
from discord.commands import slash_command

class DareCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "dare", 
        description = "Dare instance, of Truth - Dare Game."
    )
    async def dare(self, ctx):
        with open("data/CmdData.json", "r", encoding="utf-8") as f:
            # the data folder has been deleted & not provided in this public repo
            data = json.load(f)
            response = random.choice(data["dare"])

        embed = discord.Embed(
            title="<:PepeEvil:881628151363534868> Dare",
            description=f"**{response}**",
            colour=discord.Color.blue(),
        )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(DareCmd(bot))
