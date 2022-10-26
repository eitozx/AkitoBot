import os
import asyncpraw
import akito
import discord
from discord.ui import Button
from discord.ext import commands
from asyncprawcore.exceptions import Redirect
from discord.commands import slash_command


class RedditinfoCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "redditinfo",
        description = "Get subreddit info"
    )
    async def redditinfo(self, ctx, subreddit : discord.Option(str, 'Subreddit of which you want to retrieve the info', required=True)):
        try:

            reddit = asyncpraw.Reddit(
                client_id=os.getenv("PRAW_ID"),
                client_secret=os.getenv("PRAW_SECRET"),
                user_agent=os.getenv("PRAW_DEV"),
            )

            subreddit = await reddit.subreddit(subreddit, fetch=True)

            embed = discord.Embed(
                title=subreddit.title,
                description=subreddit.public_description,
                url=f"https://reddit.com/r/{subreddit}",
                colour=discord.Color.blue(),
            )
            embed.add_field(name="⚠️ Spoilers", value=subreddit.spoilers_enabled)
            embed.add_field(name="🔞 Over 18", value=subreddit.over18)
            embed.add_field(name="👥 Subscribers", value=subreddit.subscribers)
            embed.add_field(name="🆔 ID", value=subreddit.id)
            date = round(subreddit.created_utc)
            embed.add_field(name="📅 Created", value=f"<t:{date}:D>")
            button = discord.ui.View()
            Link = Button(emoji="🔗", label=subreddit.title, url=f"https://reddit.com/r/{subreddit}")
            button.add_item(Link)

            await ctx.respond(embed=embed, view=button)

        except Redirect:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Doesn't Exist.",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} There is no subreddit with name `{subreddit}`."
                f"\n\nNote: I can't fetch any user's post or if a subreddit is **Private** or **Doesn't Exist.**"
                f"\nCorrect Usage: `/ reddit [subreddit name]`\n",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)

        except:
            raise

        finally:
            await reddit.close()

def setup(bot):
    bot.add_cog(RedditinfoCmd(bot))
