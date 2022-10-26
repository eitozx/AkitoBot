import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class UnbanCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "unban",
        description = "To unban user from server"
    )
    @commands.has_permissions(ban_members=True)
    async def unban(
        self, ctx, 
        user: discord.Option(discord.User, 'User whom you want to unban from the server', required=True)
    ):
        await ctx.guild.unban(user)
        embed = discord.Embed(
            title=f"<:moderation:881782591060062288> Member Unbanned!",
            colour=discord.Color.blue(),
            description=f"**{user} has been Unbanned By** {ctx.author.mention}.",
        )
        await ctx.respond(embed=embed)
        return

def setup(bot):
    bot.add_cog(UnbanCmd(bot))
