import discord
import json
import random
from discord.ext import commands


class HypeCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # hype
    @commands.command(
        name= "hype",
        aliases=["hyped"],
        usage = "(Member)",
        description = "Image/GIF: Hype",
        help = None
    )
    async def hype(self, ctx, *args):
        with open("data/RPEmotion.json") as f:
            data = json.load(f)
            gif = " ".join(random.choices(data["hype"]))

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
                title=f"{ctx.author.display_name} hyped for {user.name}",
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
                title=f"{ctx.author.display_name} is Hyped",
                description=f"{message}",
                colour=ctx.author.color,
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(HypeCmd(bot))
