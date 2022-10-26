import discord
from akito import Var, Link, final
from discord.ext import commands
from discord.commands import slash_command

class VoteCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name= "vote",
        description = "To Vote bot"
    )
    async def vote(self, ctx):

        dev = await self.bot.fetch_user(981649911151992832)

        embed = discord.Embed(
            title="<a:Tick:884027409123397682> Vote!", colour=discord.Color.blue()
        )
        embed.add_field(name="<a:BotDeveloper:882865916352806922> Developer", value=dev)
        embed.add_field(
            name="<:Welcome:884733549171843123> Server",
            value=f"[Join Here.]({Link.server.value})",
        )
        embed.add_field(
            name="By Voting You Unlock Following Commands:",
            value = "• All NSFW commands.\n"
                    "• Tic-Tac-Toe, poll, ship, wallpaper, say, embed, MAL, etc.",
            inline = False
        
        )

        embed.set_image(url=Link.banner.value)
        embed.set_thumbnail(url=self.bot.user.display_avatar)

        view = discord.ui.View()
        view.add_item(item=discord.ui.Button(label="Vote Me", url=Link.topgg.value))

        await ctx.respond(embed=embed, view=view)

def setup(bot):
    bot.add_cog(VoteCmd(bot))
