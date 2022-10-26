import discord
from akito import Var, Link, final
from discord.ui import Button
from discord.ext import commands
from discord.commands import slash_command

class InviteCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "invite",
        description = "To get invite link of support server & bot."
    )
    async def invite(self, ctx):

        dev = await self.bot.fetch_user(981649911151992832)

        embed = discord.Embed(
            title=f"<a:Tick:884027409123397682> Invite!",
            colour=discord.Color.blue(),
            description="** **",
        )
        embed.add_field(name="<a:BotDeveloper:882865916352806922> Developer", value=dev)
        embed.add_field(
            name="<:Welcome:884733549171843123> Server",
            value=f"[Join Here.]({Link.server.value})",
        )
        embed.set_image(url=Link.banner.value)

        button = discord.ui.View()
        button.add_item(item=Button(label="Bot Invite Link", url=Link.bot.value))
        button.add_item(item=Button(label="Server Invite Link", url=Link.server.value))

        await ctx.respond(embed=embed, view=button)


def setup(bot):
    bot.add_cog(InviteCmd(bot))
