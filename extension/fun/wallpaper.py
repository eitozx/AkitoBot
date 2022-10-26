import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class WallpaperCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "wallpaper",
        description = "Get high resolution wallpaper for your device."
    )
    async def wallpaper(self, ctx):
        result = await akito.nsfw('wallpaper')

        embed = discord.Embed(title="🏞️ Wallpaper", color=ctx.author.top_role.color)
        embed.set_image(url=result["image"])
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(WallpaperCmd(bot))
