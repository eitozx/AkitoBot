import akito
import os
import discord
import redditeasy
from discord.ext import commands
from discord.commands import slash_command


class MemeCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name= "meme", 
        description = "Get memes like Dank Memer"
    )
    async def meme(self, ctx):
        reddit = redditeasy.Subreddit(
            client_id=os.getenv("PRAW_ID"),
            client_secret=os.getenv("PRAW_SECRET"),
            user_agent=os.getenv("PRAW_DEV"),
        )
        post = reddit.get_post(subreddit="memes")

        try:

            embed = discord.Embed(
                title=post.title, 
                colour=discord.Color.blue(), 
                url=post.post_url
            )
            embed.set_image(url=post.content)
            await ctx.respond(embed=embed)

        except:
            raise


def setup(bot):
    bot.add_cog(MemeCmd(bot))
