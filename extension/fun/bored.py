import aiohttp
import discord
import akito
from discord.ext import commands
from discord.commands import slash_command


class BoredCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "bored",
        description = "Getting Bored? Time for Some Activity."
    )
    async def bored(self, ctx):
        async with aiohttp.ClientSession() as session:
            response = await session.get("https://www.boredapi.com/api/activity")
            data = await response.json(content_type=None)
            embed = discord.Embed(
                title=f"🥱 Bored", 
                description=data["activity"], 
                colour=discord.Color.blue()
            )
            embed.add_field(name="Type", value=data["type"])
            embed.add_field(name="Participants:", value=data["participants"])
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(BoredCmd(bot))
