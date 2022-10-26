import discord
import aiohttp
from akito import Token, final
from discord.ext import commands
from discord.commands import slash_command

class RoastCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "roast", 
        description = "Time to roast :D"
    )
    async def roast(self, ctx):

        async with aiohttp.ClientSession() as session:
            response = await session.get(f"https://weebyapi.xyz/json/roast?token={Token.weeby.value}")
            data = await response.json(content_type='application/json')

            embed = discord.Embed(
                title="<:PepeEvil:881628151363534868> Roast",
                description= f"**{data['response']}**",
                colour=discord.Color.blue(),
            )
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(RoastCmd(bot))
