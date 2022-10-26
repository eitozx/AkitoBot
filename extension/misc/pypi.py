import json
import aiohttp
import discord
from akito import Embed, final
from discord.ui import Button
from discord.ext import commands
from discord.commands import slash_command

class PypiCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = "pypi", 
        description = "Get info about python packages"
    )
    async def pypi(self, ctx, module: discord.Option(str, 'Python module/library name', required=True)):
        with open("data/MediaData.json") as f:
            data = json.load(f)
            gif = data["pypi"]
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://pypi.org/pypi/{module}/json"
                response = await session.get(url)
                data = await response.json(content_type=None)
                pkg = data["info"]

            embed = discord.Embed(
                title=f"<:pypi:884892626099265587> {pkg['name']}",
                url=pkg["package_url"],
                description=pkg["summary"],
                colour=discord.Color.blue(),
            )

            author = pkg.get("author")
            if author:
                embed.add_field(name="🧑‍💻 Author", value=pkg["author"], inline=False)

            embed.add_field(
                name="🕔 Latest Release",
                value=f"[{pkg['version']}]({pkg['release_url']})",
            )

            keyword = pkg["keywords"]
            if not keyword:
                keyword = "No Data"
            embed.add_field(name="📃 Keywords", value=keyword, inline=False)

            embed.set_thumbnail(url=gif)
            button = discord.ui.View()

            urls = pkg.get("project_urls")
            if urls:
                for i in pkg["project_urls"].items():
                    Link = Button(label=f"{i[0]}", url=f"{i[1]}")
                    button.add_item(Link)

            await ctx.respond(embed=embed, view=button)

        except json.JSONDecodeError:
            embed = await Embed.datanotfound(self, ctx)
            await ctx.respond(embed=embed)

        except:
            raise

def setup(bot):
    bot.add_cog(PypiCmd(bot))
