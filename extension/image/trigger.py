import discord
import aiohttp
import io

from discord.ext import commands


class TriggerCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # gae
    @commands.command(
        name = "trigger",
        aliases=["triggered"],
        description = "Get triggered version of avatar",
        usage = "(Member)",
        help = None
    )
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def trigger(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        url = (
            f"https://some-random-api.ml/canvas/triggered?avatar={user.display_avatar}"
        )
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            imageData = io.BytesIO(await response.read())
            file = discord.File(imageData, filename="triggered.gif")

            embed = discord.Embed(colour=ctx.author.color)
            embed.set_image(url="attachment://triggered.gif")
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.display_avatar)

            await ctx.respond(embed=embed, file=file)


def setup(bot):
    bot.add_cog(TriggerCmd(bot))
