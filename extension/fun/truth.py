import json
import random
import discord
import akito
from discord.ext import commands
from discord.commands import slash_command

class TruthCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "truth", 
        description = "Truth instance, of Truth - Dare Game."
    )
    async def truth(self, ctx):
        with open("data/CmdData.json", "r", encoding="utf-8") as f:
            # the data folder has not been provded in this public repo
            data = json.load(f)
            response = random.choice(data["truth"])

        embed = discord.Embed(
            title="<:PepeEvil:881628151363534868> Truth",
            description=f"**{response}**",
            colour=discord.Color.blue(),
        )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(TruthCmd(bot))
