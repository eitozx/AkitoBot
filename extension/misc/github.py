import akito
import discord
import aiohttp
from discord.ui import Button
from discord.ext import commands
from discord.commands import slash_command

class GithubCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "github", 
        description = "Get Github Account info"
    )
    async def github(self, ctx, username: discord.Option(str, 'Enter the Github username', required=True)):
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://api.github.com/users/{username}"
                response = await session.get(url)
                data = await response.json(content_type=None)

            name = data["name"]
            if not name:
                title = f"<:Github:885097226752385054> {data['login']}"
            else:
                title = f"<:Github:885097226752385054> {data['login']} ({data['name']})".replace("('", "").replace("',)", "")

            embed = discord.Embed(
                title=title,
                description=data["bio"],
                colour=discord.Color.blue(),
                url=data["html_url"],
            )

            location = data["location"]
            if not location:
                location = "Not Set"
            embed.add_field(name="📍 Location", value=location)

            embed.add_field(name="👥 Followers", value=data["followers"])
            embed.add_field(name="👤 Following", value=data["following"])
            embed.add_field(name="📚 Repos", value=data["public_repos"])
            embed.add_field(name="📝 Gists", value=data["public_gists"])

            company = data.get("company")
            if company:
                if company.startswith("@"):
                    company = (
                        f"[{company}](https://github.com/{company.replace('@','')})"
                    )
                embed.add_field(name="🏢 Company", value=company)

            email = data.get("email")
            if not email:
                email = "No Data"
            embed.add_field(name="📧 Email", value=email)
            embed.add_field(name="📅 Created On", value=data["created_at"].split("T")[0])
            embed.add_field(name="📅 Last Update", value=data["updated_at"].split("T")[0])
            embed.set_thumbnail(url=data["avatar_url"])

            button = discord.ui.View()
            button.add_item(
                item=Button(
                    emoji="<:Github:885097226752385054>",
                    label=f" {data['login']}",
                    url=data["html_url"],
                )
            )

            twitter = data.get("twitter_username")
            if twitter:
                button.add_item(
                    item=Button(
                        emoji="<:Twitter:885114838727151616>",
                        label=data["twitter_username"],
                        url=f"https://twitter.com/{twitter}",
                    )
                )

            await ctx.respond(embed=embed, view=button)

        except KeyError:
            embed = discord.Embed(
                title=f"<:oh:881566351783780352> Data Not Found",
                colour=discord.Color.red(),
                description=f"{ctx.author.mention} I don't seem to find data for `{username}`",
            )
            embed.set_footer(text=f"Join My Server For Additional Help!")
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            await ctx.respond(embed=embed)

        except:
            raise


def setup(bot):
    bot.add_cog(GithubCmd(bot))
