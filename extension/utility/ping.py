import json
import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class PingCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="ping", 
        description = "To check latency of bot."
    )
    async def ping(self, ctx):
        with open("data/MediaData.json") as f:
            data = json.load(f)
            gif = data["ping"]

        embed = discord.Embed(
            title=f"__**🏓PONG**__",
            colour=discord.Color.blue(),
            description=f"**Latency:**\n`{round(self.bot.latency* 1000)}ms`",
        )
        embed.set_thumbnail(url=gif)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(PingCmd(bot))
