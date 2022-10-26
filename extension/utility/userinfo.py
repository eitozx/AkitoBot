import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class UserinfoCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "userinfo", 
        description = "To get user info"
    )
    async def userinfo(
        self, ctx, 
        user: discord.Option(discord.Member, 'User of which you want to retrieve the info', required=False, default=None)
    ):

        user = user or ctx.author
        if user.premium_since != None:
            boosted = user.premium_since.strftime("%d-%m-%Y")
        else:
            boosted = "Not Boosted"

        uuser = await self.bot.fetch_user(user.id)

        # badge = "** **"
        # flag = user.public_flags
        # if flag.staff:
        #     badge += "<:DiscordStaff:882863808748613654>"
        # if flag.partner:
        #     badge += "<:DiscordPartner:882863890961170492>"
        # if flag.hypesquad:
        #     badge += "<:HypesquadEventsMember:882866963083325461>"
        # if flag.bug_hunter:
        #     badge += "<:BugHunter:882864315147907172>"
        # if flag.bug_hunter_level_2:
        #     badge += "<:BugHunterLevel2:882865392228392980>"
        # if flag.hypesquad_bravery:
        #     badge += "<:HypeSquadBravery:882863731833454622>"
        # if flag.hypesquad_brilliance:
        #     badge += "<:HypeSquadBrilliance:882864065456779334>"
        # if flag.hypesquad_balance:
        #     badge += "<:HypeSquadBalance:882864051619762216>"
        # if flag.early_supporter:
        #     badge += "<:EarlySupporter:882864498615152671>"
        # if flag.verified_bot:
        #     badge += "<:VerifiedBot:882864930112569344>"
        # if flag.early_verified_bot_developer:
        #     badge += "<:EarlyVerifiedBotDeveloper:882945599366905906>"
        # if badge == "** **":
        #     badge = "No Badge"

        # status = ""
        # s = user.status
        # if s == discord.Status.online:
        #     status += "<:online:885521973965357066>"
        # if s == discord.Status.offline:
        #     status += "<:offline:885522151866777641>"
        # if s == discord.Status.idle:
        #     status += "<:idle:885522083545772032>"
        # if s == discord.Status.dnd:
        #     status += "<:dnd:885522031536394320>"

        embed = discord.Embed(
            # title=f"{status} {user.name}'s Info.",
            title=f"{user.name}'s Info.",
            description=f"Here is some info about {user.name}"
            f"\n:id: **User ID:** `{user.id}`",
            colour=discord.Color.blue(),
        )

        embed.add_field(name=f"✏ Display Name", value=f"{user.display_name}")
        embed.add_field(name=f"🔷 Mention", value=f"{user.mention}")
        embed.add_field(name=f"⬆ Highest Role", value=f"{user.top_role.mention}")
        embed.add_field(
            name=f"<:boost:864737209722470420> Boosted On", value=f"{boosted}"
        )

        joined = user.joined_at.timestamp()
        embed.add_field(name=f"📆 Joined On", value=f"<t:{round(joined)}:D>")

        created = user.created_at.timestamp()
        embed.add_field(name=f"📆Created On", value=f"<t:{round(created)}:D>")

        role_string = "".join([r.mention for r in user.roles])
        embed.add_field(name="Roles", value=f"\u200b{role_string}", inline=False)

        # embed.add_field(name=f"Badges" , value=f"{badge}" , inline=False)

        perm_list = (
            ", ".join([perm[0] for perm in user.guild_permissions if perm[1]])
            .title()
            .replace("_", " ")
        )
        if "Administrator" in perm_list:
            perm_list = "**Administrator**"
        embed.add_field(name="Permissions", value=perm_list, inline=False)

        if uuser.banner:
            embed.set_image(url=uuser.banner)

        embed.set_thumbnail(url=user.display_avatar)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(UserinfoCmd(bot))
