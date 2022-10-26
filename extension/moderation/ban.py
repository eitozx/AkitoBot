import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class BanCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "ban", 
        description = "To ban member from server"
    )
    @commands.has_permissions(ban_members=True)
    async def ban(
        self, ctx, 
        member: discord.Option(discord.Member, 'Member you want to ban from server', required=True), 
        *, reason : discord.Option(str, 'Reason for which you\'re banning the member', required=False, default=None),
    ):
        await member.ban(reason=reason)
        embed = discord.Embed(
            title=f"<:moderation:881782591060062288> Member Banned!",
            colour=discord.Color.blue(),
            description=f"**{member.mention} has been banned By** {ctx.author.mention}.\n**Reason:** {reason}.",
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BanCmd(bot))
