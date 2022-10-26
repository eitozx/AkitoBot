import discord
import aiohttp
import akito
from discord.ext import commands


class WallpaperCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = "wallpaper",
        aliases=["wallpapers"],
        usage = "",
        description = "Get high resolution wallpaper for your device.",
        help= "• 99% are SFW, but still 1% is NSFW."
        "\n• **Vote locked** command."
    )
    @akito.votelock()
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    async def wallpaper(self, ctx):
        async with aiohttp.ClientSession() as session:
            url = "http://api.nekos.fun:8080/api/wallpaper"
            response = await session.get(url)
            result = await response.json()

            embed = discord.Embed(title="🏞️ Wallpaper", color=ctx.author.top_role.color)
            embed.set_image(url=result["image"])
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(WallpaperCmd(bot))
