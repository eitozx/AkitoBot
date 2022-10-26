import akito
import discord
from discord.ext import commands
from discord.commands import slash_command

class HentaiCmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        
    @slash_command(
        name = "hentai",
        description = "NSFW Category: Anime Porn",
    )
    @akito.votelock()
    @commands.is_nsfw()
    @commands.cooldown(1 , 3 , commands.BucketType.user)
    @commands.cooldown(55, 1, commands.BucketType.default)
    async def hentai(self, ctx):
        result = await akito.nsfw('feet')

        embed = discord.Embed(
            title = "🔞 Hentai",
            color = ctx.author.top_role.color
        )
        embed.set_image(url = result['image'])
        await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(HentaiCmd(bot))