import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class BlowjobCmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        
    @slash_command(
        name = "blowjob", 
        description = "NSFW Category: Blowjob"
    )
    @akito.votelock()
    @commands.is_nsfw()
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.cooldown(55, 1, commands.BucketType.default)
    async def blowjob(self, ctx):
        result = await akito.nsfw('bj')

        embed = discord.Embed(
            title = "🔞 Blowjob",
            color = ctx.author.top_role.color
        )
        embed.set_image(url = result['image'])
        await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(BlowjobCmd(bot))