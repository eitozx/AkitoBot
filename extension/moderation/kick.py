import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class KickCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "kick",
        description = "To kick member from server"
    )
    @commands.has_permissions(kick_members=True)
    async def kick(
        self, ctx, 
        member: discord.Option(discord.Member, 'Member you want to kick' , required=True),
         *, 
        reason: discord.Option(str, 'Reason for which you\'re kicking the member', required=False, default=None)
    ):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title=f"<:moderation:881782591060062288> Member Kicked!",
            colour=discord.Color.blue(),
            description=f"**{member.mention} has been kicked By** {ctx.author.mention}.\n**Reason:** {reason}.",
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(KickCmd(bot))
