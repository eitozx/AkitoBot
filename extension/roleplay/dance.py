import discord
import json
import random
from discord.ext import commands


class DanceCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # dance
    @commands.command(
        name= "dance",
        aliases=["dances","dancing"],
        usage = "(Member)",
        description = "Image/GIF: Dance",
        help = None
    )
    async def dance(self, ctx, *args):

        with open("data/RPAction.json") as f:
            data = json.load(f)
            gif = " ".join(random.choices(data["dance"]))

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
                title=f"{ctx.author.display_name} dancing for {user.name}",
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
                title=f"{ctx.author.display_name} dancing",
                description=f"{message}",
                colour=ctx.author.color,
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(DanceCmd(bot))
