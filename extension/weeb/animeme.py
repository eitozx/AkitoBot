import os
import discord
import redditeasy
from discord.ext import commands
from discord.commands import slash_command
import akito

class AnimemeCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "animeme", 
        description = "To get anime related memes"
    )
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.cooldown(1, 2, commands.BucketType.default)
    async def animeme(self, ctx):
        reddit = redditeasy.Subreddit(
            client_id=os.getenv("PRAW_ID"),
            client_secret=os.getenv("PRAW_SECRET"),
            user_agent=os.getenv("PRAW_DEV"),
        )

        post = reddit.get_post(subreddit="goodanimemes")

        try:

            embed = discord.Embed(
                title=post.title, colour=discord.Color.blue(), url=post.post_url
            )
            embed.set_image(url=post.content)
            embed.set_footer(
                text=f"👍 {post.score} 💬 {post.comment_count}",
                icon_url=self.bot.user.display_avatar,
            )

            await ctx.respond(embed=embed)

        except:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Please Try Again.",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} It Could Be that this is some Data Error, Please Try Again."
                f"\n\nNote: This is just a bug we're currently working on, please ignore & try this command again.",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(AnimemeCmd(bot))
