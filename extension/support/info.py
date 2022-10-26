import psutil
import discord
from akito import Var, Link, final
from discord.ext import commands
from discord.commands import slash_command


class InfoCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @staticmethod
    def usercount(self):
        count = 0
        for i in self.bot.guilds:
            count += i.member_count
        return count

    async def description(self):
        info = await self.bot.application_info()
        return (info.description).splitlines()[0]

    @slash_command(
        name = "info", 
        description = "To get brief information about bot."
    )
    async def info(self, ctx):

        dev = await self.bot.fetch_user(981649911151992832)

        embed = discord.Embed(
            title="<a:Tick:884027409123397682> About!", colour=discord.Color.blue()
        )
        embed.add_field(
            name="<a:BotDeveloper:882865916352806922> Developer",
            value=dev,
            inline=False,
        )

        embed.add_field(
            name="<:Welcome:884733549171843123> Server",
            value=f"[Join Here.]({Link.server.value})",
        )
        embed.add_field(
            name="<:DarlingHeart:884029459487928330> Vote",
            value=f"[Vote Here.]({Link.topgg.value})",
        )
        embed.add_field(name="** **", value=f"** **")

        embed.add_field(
            name="🏷️ Features",
            value= await self.description(),
            inline=False,
        )

        embed.add_field(
            name="<:settings:881782626946539540> System Stats:",
            value=f"**Bot Latency: {round(self.bot.latency* 1000)}ms**\n"
                f"**RAM Usage: {round((psutil.virtual_memory().used / psutil.virtual_memory().total) * 100)}%**\n"
                f"**CPU Usage: {round(psutil.cpu_percent(interval=1, percpu=False))}%**\n"
            
        )

        embed.add_field(
            name="<:Discord:882864757743431722> Bot Stats:",
            value = f"**Total Commands: {len(self.bot.application_commands)}**\n"
                f"**Total Users: {InfoCmd.usercount(self)}**\n"
                f"**Total Servers: {len(self.bot.guilds)}**\n"
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.set_image(url=Link.banner.value)

        # button
        info = await self.bot.application_info()
        button = discord.ui.View()

        button.add_item(item=discord.ui.Button(label="Terms Of Service", url=info.terms_of_service_url),)
        button.add_item(item=discord.ui.Button(label="Privacy Policy", url=info.privacy_policy_url))
        button.add_item(item=discord.ui.Button(label="Invite Link", url=Link.bot.value))

        await ctx.respond(embed=embed, view=button)


def setup(bot):
    bot.add_cog(InfoCmd(bot))
