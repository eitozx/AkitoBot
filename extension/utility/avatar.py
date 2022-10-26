import discord
from discord.ext import commands
from discord.commands import slash_command
import akito

class display_avatarCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "avatar",
        description = "Avatar of user"
    )
    async def avatar(
        self, ctx, 
        user: discord.Option(discord.Member,'User of which you want to see the avatar', default=None)
    ):
        user = user or ctx.author

        embed = discord.Embed(
            title=f"{user.name}(#{user.discriminator})'s Avatar",
            colour=discord.Color.blue(),
            url=user.display_avatar,
        )

        embed.set_image(url=user.display_avatar)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(display_avatarCmd(bot))
