import io
import dotenv
import discord
import aiohttp
from akito import Embed, Token, votelock
from discord.ext import commands

dotenv.load_dotenv()
class ShipCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ship 
    @commands.command(
        name = "ship",
        aliases = ["love"],
        description = "Get compatibility meter.",
        usage = "[1st Member] (2nd Member)",
        help = "• If `2nd Member` parameter is not provided, then it sets to command user."
        "\n• **Vote locked** command."
    )
    @votelock()
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ship(self, ctx, second: discord.Member, first : discord.Member = None):
        if not first:
            first = ctx.author
        
        url = f"https://weebyapi.xyz/generators/friendship?firstimage={first.display_avatar}&secondimage={second.display_avatar}&firsttext={first.display_name}&secondtext={second.display_name}&token={Token.weeby.value}"

        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            imageData = io.BytesIO(await response.read())
            file = discord.File(imageData, filename="friendship.png")

            embed = discord.Embed(colour=ctx.author.color)
            embed.set_image(url="attachment://friendship.png")
            embed.set_footer(text=f"{ctx.author} shipped {first} & {second}", icon_url=ctx.author.display_avatar)

            await ctx.respond(embed=embed, file=file)


    @ship.error
    async def comment_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = await Embed.missingrequiredargument(self, ctx)
            await ctx.respond(embed = embed, delete_after = 60)

        elif isinstance(error, commands.MemberNotFound):
            embed = await Embed.membernotfound(self, ctx)
            await ctx.respond(embed = embed, delete_after = 60)

        else:
            pass


def setup(bot):
    bot.add_cog(ShipCmd(bot))
