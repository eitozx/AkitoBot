import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class EmbedCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "embed",
        description = "To make easy embed"
    )
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def embed(
        self, ctx, *, 
        message: discord.Option(str, 'Message that you want in the embed', required=True)
    ):
        embed = discord.Embed(colour=discord.Color.blue(), description=f"""{message}""")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(EmbedCmd(bot))
