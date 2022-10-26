import discord
import aiohttp

from discord.ext import commands


class KissCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # kiss
    @commands.command(
        name= "kiss",
        aliases=["kisses","kissing"],
        usage = "(Member)",
        description = "Image/GIF: Kiss",
        help = None
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def kiss(self, ctx, *args):

        url = f"http://api.nekos.fun:8080/api/kiss"
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
                title=f"{ctx.author.display_name} kissed {user.name}",
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
                title=f"{ctx.author.display_name} is kissing",
                description=f"{message}",
                colour=ctx.author.color,
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(KissCmd(bot))
