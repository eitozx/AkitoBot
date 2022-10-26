import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class PollCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # poll command
    @slash_command(
        name = "poll",
        description = "To make easy poll"
    )
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def poll(
        self, ctx, 
        question: discord.Option(str, 'Question of the poll', required=True), 
        *options: discord.Option(str, 'Options of the poll, make sure that every option is in quotations (" ")', required=False, default=0)
    ):
        if len(options) == 0:
            embed = discord.Embed(title=question, colour=discord.Color.blue())
            message = await ctx.respond(embed=embed)

            # await message.delete()
            await message.add_reaction("🔼")
            await message.add_reaction("🔽")
            return

        elif len(options) <= 1:
            embed = await akito.Embed.missingrequiredargument(self, ctx)
            await ctx.respond(embed=embed)
            return

        elif len(options) > 10:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Excessive Required Argument",
                colour=discord.Color.red(),
                description=f"*You can have upto **10 options only**"
                f'\n\nCorrect Usage: `/ poll "[question]" "(options)"*`',
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            embed.set_footer(text=f"Join My Server For Additional Help!")
            await ctx.respond(embed=embed)
            return

        if len(options) == 2 and options[0] == "yes" and options[1] == "no":
            reactions = ["🔼", "🔽"]
        else:
            reactions = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "🔟"]

        description = []
        for x, option in enumerate(options):
            description += "\n {} {}".format(reactions[x], option)

        embed = discord.Embed(
            title=question, colour=discord.Color.blue(), description="".join(description)
        )
        react_message = await ctx.respond(embed=embed)
        # await react_message.delete()
        for reaction in reactions[: len(options)]:
            await react_message.add_reaction(reaction)

def setup(bot):
    bot.add_cog(PollCmd(bot))
