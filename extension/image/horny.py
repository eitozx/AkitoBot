import discord
import aiohttp
import io

from discord.ext import commands


class HornyCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # gae
    @commands.command(
        name = "horny",
        aliases = [],
        description = "Get your license to be horny",
        usage = "(Member)",
        help = None
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def horny(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        url = f"https://some-random-api.ml/canvas/horny?avatar={user.display_avatar}"
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            imageData = io.BytesIO(await response.read())
            file = discord.File(imageData, filename="horny.png")

            embed = discord.Embed(colour=ctx.author.color)
            embed.set_image(url="attachment://horny.png")
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.display_avatar)

            await ctx.respond(embed=embed, file=file)


def setup(bot):
    bot.add_cog(HornyCmd(bot))
