import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class FourkCmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        

    @slash_command(
        name = "4k",
        description = "High Resolution NSFW Images.",
    )
    @akito.votelock()
    @commands.is_nsfw()
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.cooldown(55, 1, commands.BucketType.default)
    async def _4k(self, ctx):
        result = await akito.nsfw('4k')

        embed = discord.Embed(
            title = "🔞 4k",
            color = ctx.author.top_role.color
        )
        embed.set_image(url = result['image'])
        await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(FourkCmd(bot))