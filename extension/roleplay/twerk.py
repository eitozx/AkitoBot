import discord
import json
import random
from discord.ext import commands


class TwerkCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # smirk
    @commands.command(
        name= "twerk",
        aliases=["twerks","twerking"],
        usage = "(Member)",
        description = "Image/GIF: Baka",
        help = None
    )
    async def twerk(self, ctx, *args):
        with open("data/RPAction.json") as f:
            data = json.load(f)
            gif = " ".join(random.choices(data["twerk"]))

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
                title=f"{ctx.author.display_name} is Twerked {user.name}",
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
                title=f"{ctx.author.display_name} is twerking",
                description=f"{message}",
                colour=ctx.author.color,
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(TwerkCmd(bot))
