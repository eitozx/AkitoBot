import discord
import json
import random
from discord.ext import commands


class ConfusionCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # confusion
    @commands.command(
        name= "confusion",
        aliases=["confused","confuse"],
        usage = "(Member)",
        description = "Image/GIF: Confusion",
        help = None
    )
    async def confusion(self, ctx, *args):
        with open("data/RPEmotion.json") as f:
            data = json.load(f)
            gif = " ".join(random.choices(data["confusion"]))

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
                title=f"{ctx.author.display_name} is confused {user.name}",
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
                title=f"{ctx.author.display_name} is confused",
                description=f"{message}",
                colour=ctx.author.color,
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(ConfusionCmd(bot))
