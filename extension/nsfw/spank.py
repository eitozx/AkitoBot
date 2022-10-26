import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class SpankCmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        

    @slash_command(
        name = "spank", 
        description = "NSFW Category: Spank",
    )
    @akito.votelock()
    @commands.is_nsfw()
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.cooldown(55, 1, commands.BucketType.default)
    async def spank(self, ctx):
        result = await akito.nsfw('spank')

        embed = discord.Embed(
            title = "🔞 Spank",
            color = ctx.author.top_role.color
        )
        embed.set_image(url = result['image'])
        await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(SpankCmd(bot))