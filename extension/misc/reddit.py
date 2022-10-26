import os
import json
import random
import discord
import akito
import redditeasy
from discord.ext import commands
from discord.commands import slash_command

class RedditCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "reddit", 
        description = "Get posts from subreddits (both image & text are supported)."
    )
    async def reddit(self, ctx, search: discord.Option(str, 'Subreddit from which you want to retreive posts', required=True)):
        try:
            reddit = redditeasy.Subreddit(
                client_id=os.getenv("PRAW_ID"),
                client_secret=os.getenv("PRAW_SECRET"),
                user_agent=os.getenv("PRAW_DEV"),
            )

            post = reddit.get_post(subreddit=search)

            membed = discord.Embed(
                title=post.title, colour=discord.Color.blue(), url=post.post_url
            )

            if str(post.content).startswith("{"):
                object = json.dumps(post.content)
                data = json.loads((object.replace("&amp;", "&")))

                img = random.choice([i["media"] for i in data["media"]])

            else:
                img = post.content

            membed.set_image(url=img)
            membed.set_footer(
                text=f"👍 {post.score} 💬 {post.comment_count}",
                icon_url=self.bot.user.display_avatar,
            )

            pembed = discord.Embed(
                title=post.title,
                description=post.content,
                colour=discord.Color.blue(),
                url=post.post_url,
            )
            pembed.set_footer(
                text=f"👍 {post.score} 💬 {post.comment_count}",
                icon_url=self.bot.user.display_avatar,
            )

            try:

                if post.nsfw == True:
                    if ctx.channel.is_nsfw() == True:
                        if post.is_media:
                            await ctx.respond(embed=membed)
                        else:
                            await ctx.respond(embed=pembed)

                    else:
                        embed = discord.Embed(
                            title=f"<:oh:881566351783780352> NSFW Channel Required",
                            colour=discord.Color.red(),
                            description=f"{ctx.author.mention}, this command/query can be used in NSFW Channel Only",
                        )
                        embed.set_footer(text=f"Join My Server For Additional Help!")
                        embed.set_author(
                            name=ctx.author, icon_url=ctx.author.display_avatar
                        )
                        await ctx.respond(embed=embed)

                else:
                    if post.is_media:
                        await ctx.respond(embed=membed)
                    else:
                        await ctx.respond(embed=pembed)
            except:
                pass

        except:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Doesn't Exist.",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} There is no subreddit with name `{search}`."
                f"\n\nNote: I can't fetch any user's post or if a subreddit is **Private** or **Doesn't Exist.**"
                f"\nor if it **doesn't have more than 1 post**"
                f"\n\nCorrect Usage: `/ reddit [subreddit name]`\n",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(RedditCmd(bot))
