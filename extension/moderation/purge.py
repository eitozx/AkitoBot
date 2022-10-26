import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class PurgeCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "purge",
        description = "To purge/delete messages"
    )
    @commands.has_permissions(manage_channels=True)
    async def purge(
        self, ctx,
         *,
        limit: discord.Option(int, 'Number of messages to purge', required=False, default=2)
    ):
        embed = discord.Embed(
            title=f"<:moderation:881782591060062288> Messages Purged!",
            colour=discord.Color.blue(),
            description=f"**{limit} messages** Purged By {ctx.author.mention}",
        )
        await ctx.channel.purge(limit=((limit) + 1))
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(PurgeCmd(bot))
