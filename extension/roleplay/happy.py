import discord
import json
import random
from discord.ext import commands


class HappyCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # happy
    @commands.command(
        name= "happy",
        aliases=[],
        usage = "(Member)",
        description = "Image/GIF: Happy",
        help = None
    )
    async def happy(self, ctx, *args):
        with open("data/RPEmotion.json") as f:
            data = json.load(f)
            gif = " ".join(random.choices(data["happy"]))

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
                title=f"{ctx.author.display_name} is happy {user.name}",
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
                title=f"{ctx.author.display_name} is happy",
                description=f"{message}",
                colour=ctx.author.color,
            )
            embed.set_image(url=gif)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(HappyCmd(bot))
