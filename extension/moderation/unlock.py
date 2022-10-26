import discord
from discord.ext import commands
from discord.commands import slash_command, permissions
import akito
class UnlockCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "unlock",
        description = "To unlock, locked text channel for everyone"
    )
    @commands.has_permissions(manage_channels=True)
    async def unlock(
        self, ctx, 
        channel: discord.Option(discord.TextChannel, 'TextChannel that you want to unlock for everyone', required=False, default=None)
    ):
        channel = channel or ctx.channel
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(
            title=f"<:moderation:881782591060062288> Channel Unlocked!",
            colour=discord.Color.blue(),
            description=f"{channel.mention} has been **Unlocked**.",
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(UnlockCmd(bot))
