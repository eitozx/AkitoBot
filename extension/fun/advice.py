import akito
import aiohttp
import discord
from discord.ext import commands
from discord.commands import slash_command


class AdviceCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "advice",
        description = "Ask for Advice if You Need One!"
    )
    async def advice(self, ctx):
        async with aiohttp.ClientSession() as session:
            response = await session.get("https://api.adviceslip.com/advice")
            data = await response.json(content_type=None)
            embed = discord.Embed(
                title=f"👍 Advice",
                description=data["slip"]["advice"],
                colour=discord.Color.blue(),
            )
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(AdviceCmd(bot))
