import discord
from akito import Embed, final
from discord.ext import commands
from discord.commands import slash_command

class VoicechannelinfoCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "voicechannelinfo", 
        description = "To get voice channel info"
    )
    async def voicechannelinfo(self, ctx, *, channel: discord.VoiceChannel = None):
        try:
            channel = channel or ctx.author.voice.channel
            if not channel.user_limit:
                channel.user_limit = "Infinite"

            embed = discord.Embed(
                title=f"{channel.name} Info",
                description=f"Here is some info about {channel.mention}\n"
                f":id:**Channel ID:** `{channel.id}`\n🌀**Channel Type:** {channel.type}",
                colour=discord.Color.blue(),
            )
            embed.add_field(name=f"📰 Name", value=f"{channel.name}")
            embed.add_field(name=f"📃 Category", value=f"{channel.category}")
            embed.add_field(
                name=f"🔉 Audio Bitrate", value=f"{round((channel.bitrate)/1000)} Kilo"
            )
            embed.add_field(name=f"🔢 Channel Position", value=f"{channel.position+1}")
            embed.add_field(name=f"👤 Member Limit", value=f"{channel.user_limit}")
            date = channel.created_at.timestamp()
            embed.add_field(name=f"📆 Created On", value=f"<t:{round(date)}:D>")

            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon)

            await ctx.respond(embed=embed)

        except AttributeError:
            embed = await Embed.missingrequiredargument(self, ctx)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(VoicechannelinfoCmd(bot))
