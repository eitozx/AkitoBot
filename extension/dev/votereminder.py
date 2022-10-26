import discord
from akito import Var, Link
from discord.ext import commands
from discord.commands import slash_command, permissions


class VotereminderCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="votereminder", 
        description="Ping for vote"
    )
    @commands.is_owner()
    async def votereminder(self, ctx):
        channel = self.bot.get_channel(Var.vote_logger.value)

        embed = discord.Embed(
            title=f"<a:Tick:884027409123397682> Vote Reminder",
            colour=discord.Color.blurple(),
            description=f"Your votes **matter a lot** in my growth, please consider voting <:DarlingHeart:884029459487928330>\n"
            f"Voting me gives you **Access to Development Channel** where you can test my **Experimental version** *when \n"
            f"<@{752457056442908704}> is working on any new update!*\nYou also **Unlock Vote Locked Commands!**\n"
            f"\nVoting on **top.gg** gives access for **12h**\n",
        )
        embed.set_image(url=Link.banner.value)
        button = discord.ui.View()
        button.add_item(item=discord.ui.Button(label="Vote Me", url=Link.topgg.value))

        await channel.send(content=f"<@&{Var.vote_role.value}>", embed=embed, view=button)
        await ctx.respond(channel.mention)

def setup(bot):
    bot.add_cog(VotereminderCmd(bot))
