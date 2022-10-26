import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class SlowmodeCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "slowmode",
        description = "To Activate slow mode in TextChannel"
    )
    @commands.has_permissions(manage_channels=True)
    async def slowmode(
        self, ctx, 
        time: discord.Option(int, 'Number of seconds for which you want to slow-down the channel', required=False, default=0)
    ):
        await ctx.channel.edit(slowmode_delay=time)
        embed = discord.Embed(
            title=f"<:moderation:881782591060062288> Slowmode Activated!",
            colour=discord.Color.blue(),
            description=f"{time} second of **slowmode activated** for {ctx.channel.mention} by {ctx.author.mention}",
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(SlowmodeCmd(bot))
