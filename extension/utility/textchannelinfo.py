import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class TextchannelinfoCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # textchannelinfo command
    @slash_command(
        name = "textchannelinfo", 
        description = "To get text channel info"
    )
    async def textchannelinfo(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel

        embed = discord.Embed(
            title=f"{str(channel.name).title()} Info",
            description=f"Here is some info about {channel.mention}\n"
            f":id:**Channel ID:** `{channel.id}`\n🌀**Channel Type:** {channel.type}",
            colour=discord.Color.blue(),
        )
        embed.add_field(name=f"📰 Name", value=f"{channel.name}")
        embed.add_field(name=f"📃 Category", value=f"{channel.category}")
        embed.add_field(name=f"📜 Topic", value=f"{channel.topic}")
        embed.add_field(name=f"🔢 Position", value=f"{channel.position+1}")
        embed.add_field(name=f"⌛ Slowmode", value=f"{channel.slowmode_delay} seconds")
        embed.add_field(name=f"👤 Members", value=f"{len(channel.members)}")
        embed.add_field(name=f"🔞 NSFW", value=f"{channel.is_nsfw()}")
        date = channel.created_at.timestamp()
        embed.add_field(name=f"📆 Created On", value=f"<t:{round(date)}:D>")

        if not ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(TextchannelinfoCmd(bot))
