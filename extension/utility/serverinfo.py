import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class ServerinfoCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # serverinfo command
    @slash_command(
        name = "serverinfo", 
        description = "To get server info"
    )
    async def serverinfo(self, ctx):

        des = ctx.guild.description
        if not des:
            des = ""

        embed = discord.Embed(
            title=f"{ctx.guild.name} Info",
            description=f":id: **Server ID:** `{ctx.guild.id}`\n"
            f":earth_americas: **Server Region:** {str(ctx.guild.region).title()}\n\n{des}\n",
            colour=discord.Color.blue(),
        )
        # embed.add_field(name=f"<:ServerOwner:864765886916067359> Server Owner", value=f"{ctx.guild.owner.mention}")
        embed.add_field(name=f"<:ServerOwner:864765886916067359> Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(
            name=f"📝 Total Channels",
            value=f"**<:TextChannel:886507750060859472> Channels:** {len(ctx.guild.text_channels)}\n**<:VoiceChannel:886508400349962280> Channels:** {len(ctx.guild.voice_channels)}",
        )
        # embed.add_field(name=f"<:boost:864737209722470420> Boost", value=f"**Server Boosts:** {ctx.guild.premium_subscription_count}\n**Boost Level:** {ctx.guild.premium_tier}")
        embed.add_field(name=f"👥 Total Members", value=f"{ctx.guild.member_count}")
        embed.add_field(name=f"🎭 Roles", value=f"{len(ctx.guild.roles)}")
        embed.add_field(name=f"🤡 Stickers", value=f"{len(ctx.guild.stickers)}")
        embed.add_field(
            name=f"⭐ Emotes", value=f"{len(ctx.guild.emojis)}/{ctx.guild.emoji_limit}"
        )
        embed.add_field(
            name=f"🔇 AFK",
            value=f"{ctx.guild.afk_channel} | {int((ctx.guild.afk_timeout)/60)} Mins",
        )
        embed.add_field(
            name=f"✅ Verification Level", value=f"{ctx.guild.verification_level}"
        )
        notification = (
            str(ctx.guild.default_notifications)[18:].title().replace("_", " ")
        )
        embed.add_field(name=f"🔔 Notification Type", value=f"{notification}")
        date = ctx.guild.created_at.timestamp()
        embed.add_field(name=f"📆 Created On", value=f"<t:{round(date)}:D>")

        feature = ctx.guild.features
        if not feature:
            feature = "No Features Active in this Server."
        else:
            feature = ", ".join(feature).replace("_", " ").title()
        embed.add_field(name=f"🌠 Features", value=feature, inline=False)

        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon)

        if ctx.guild.banner:
            embed.set_image(url=ctx.guild.banner)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(ServerinfoCmd(bot))
