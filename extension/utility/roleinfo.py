import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class RoleinfoCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # roleinfo command
    @slash_command(
        name = "roleinfo", 
        description = "To get role info"
    )
    async def roleinfo(
        self, ctx, 
        role: discord.Option(discord.Role, 'Role of which you want to retrieve the info', required=False, default=None)
    ):
        role = role or ctx.author.top_role

        embed = discord.Embed(
            title=f"{role.name} Info",
            description=f"Here is some info about {role.mention}"
            f"\n:id: **Role ID:** `{role.id}`",
            colour=discord.Color.blue(),
        )

        embed.add_field(name=f"✏ Name", value=f"{role.name}")
        embed.add_field(name=f"🔢 Position", value=f"{role.position}")
        embed.add_field(name=f"❄ Role Color", value=f"{role.color}")
        embed.add_field(name=f"🔶 Displayed Separately", value=f"{role.hoist}")
        embed.add_field(name=f"👥 Members", value=f"{len(role.members)}")
        embed.add_field(name=f"🎩 Mentionable", value=f"{role.mentionable}")

        perm_list = (", ".join([perm[0] for perm in role.permissions if perm[1]]).title().replace("_", " "))
        
        if "Administrator" in perm_list:
            perm_list = "**Administrator**"
        if not perm_list:
            perm_list = "None"
        embed.add_field(name="Permissions", value=perm_list, inline=False)

        date = role.created_at.timestamp()
        embed.add_field(name=f"📆 Created On", value=f"<t:{round(date)}:D>")
        
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(RoleinfoCmd(bot))
