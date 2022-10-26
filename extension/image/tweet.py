import discord
import aiohttp
import io
from akito import Embed
from discord.ext import commands


class TweetCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # gae
    @commands.command(
        name = "tweet",
        aliases = [],
        usage = "[Member] [Tweet]",
        description = "Fake Member Tweet",
        help = None
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def tweet(self, ctx, user: discord.Member = None, *, comment):
        if not user:
            user = ctx.author

        url = f"https://some-random-api.ml/canvas/tweet?avatar={user.display_avatar}&username={user.name}&comment={comment}&displayname={user.display_name}"
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            imageData = io.BytesIO(await response.read())
            file = discord.File(imageData, filename="tweet.png")

            embed = discord.Embed(colour=ctx.author.color)
            embed.set_image(url="attachment://tweet.png")
            embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.display_avatar)

            await ctx.respond(embed=embed, file=file)

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = await Embed.missingrequiredargument(self, ctx)
            await ctx.respond(embed = embed,  delete_after = 60)

        elif isinstance(error, commands.MemberNotFound):
            embed = await Embed.membernotfound(self, ctx)
            await ctx.respond(embed = embed,  delete_after = 60)

        else:
            pass


def setup(bot):
    bot.add_cog(TweetCmd(bot))
