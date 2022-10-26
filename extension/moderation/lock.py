import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class LockCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "lock",
        description = "To lock text channel for everyone"
    )
    @commands.has_permissions(manage_channels=True)
    async def lock(
        self, ctx, 
        channel: discord.Option(discord.TextChannel, 'Channel you want to lock for EVERYONE', required=False, default=None)
    ):
        channel = channel or ctx.channel
        embed = discord.Embed(
            title=f"<:moderation:881782591060062288> Channel Locked!",
            colour=discord.Color.blue(),
            description=f"{channel.mention} has been **locked**.",
        )
        await ctx.respond(embed=embed)
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)

def setup(bot):
    bot.add_cog(LockCmd(bot))
