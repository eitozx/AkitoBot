import discord
import aiohttp
from discord.ext import commands


class BakaCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # hug
    @commands.command(
        name= "baka",
        aliases=[],
        usage = "(Member)",
        description = "Image/GIF: Baka",
        help = None
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def baka(self, ctx, *args):

        url = f"http://api.nekos.fun:8080/api/baka"
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            data = await response.json(content_type=None)
        gif = data["image"]

        try:
            id = int(str(args[0]).replace("<@!", "").replace(">", ""))
            user = self.bot.get_user(id)

            message = (
                str(args[1:])
                .replace("('", "")
                .replace("',)", "")
                .replace(", ", " ")
                .replace("')", "")
                .replace("'", "")
                .replace("()", "** **")
            )

            embed = discord.Embed(
                title=f"{user.name} you baka",
                description=f" {message}",
                colour=ctx.author.color,
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)

        except:
            message = (
                str(args)
                .replace("('", "")
                .replace("',)", "")
                .replace(", ", " ")
                .replace("')", "")
                .replace("'", "")
                .replace("()", "** **")
            )

            embed = discord.Embed(
                title=f"Bakaa", description=f"{message}", colour=ctx.author.color
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(BakaCmd(bot))
