import discord
from discord.ext import commands
from discord.commands import slash_command

class LoadCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="load",
        description="To load extension"
    )
    @commands.is_owner()
    async def load(self, ctx, ext):
        self.bot.load_extension(f"extension.{ext}")
        embed = discord.Embed(
            title=f"<:PepeKing:881628200877293649> Extension Loaded",
            colour=ctx.author.color,
            description=f"**Extension Loaded Successfully**: `extension.{ext}`",
        )
        await ctx.respond(embed=embed)

    @slash_command(
        name="reload",
        description="To reload extension"
    )
    @commands.is_owner()
    async def reload(self, ctx, ext):
        self.bot.reload_extension(f"extension.{ext}")
        embed = discord.Embed(
            title=f"<:PepeKing:881628200877293649> Extension Reloaded",
            colour=ctx.author.color,
            description=f"**Extension Reloaded Successfully**: `extension.{ext}`",
        )
        await ctx.respond(embed=embed)

    @slash_command(
        name="unload",
        description="To unload extension"
    )
    @commands.is_owner()
    async def unload(self, ctx, ext):
        self.bot.unload_extension(f"extension.{ext}")
        embed = discord.Embed(
            title=f"<:PepeKing:881628200877293649> Extension Unloaded",
            colour=ctx.author.color,
            description=f"**Extension Unloaded Successfully**: `extension.{ext}`",
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(LoadCmd(bot))