import discord
import aiohttp
from akito import Embed, prefix
from discord.ext import commands


class NationCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # genshin nation command
    (
        name="genshinnation", 
        aliases=["gn", "gnation", "genshinimpactnation"],
        description="Genshin Impact Nation Info",
        usage = "(Nation Name)",
        help = "If `Nation Name` is not provided, it shows list of available nations.")
    
    async def gnation(self, ctx, *, search: str = None):
        if not search:

            url = "https://api.genshin.dev/nations"

            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                data = await response.json(content_type=None)

            nations = "\n".join(data).replace("-", " ").title()

            embed = discord.Embed(
                title="<:BarbaraPoint:889078048362733580> Genshin Impact: Nations",
                colour=discord.Color.blue(),
                description=f"**__Name__ of Nations:**\n"
                f"{nations}\n"
                f"\n**Usage:**\n"
                f"`/gnation [name]`\n",
            )
            await ctx.respond(embed=embed)

        else:
            search = search.replace(" ", "-").lower()
            url = f"https://api.genshin.dev/nations/{search}"

            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(url)
                    data = await response.json(content_type=None)

                    embed = discord.Embed(
                        title=data["name"],
                        colour=discord.Color.blue(),
                    )
                    embed.add_field(name="🌠 Element", value=data["element"])
                    embed.add_field(name="🗽 Archon", value=data["archon"])
                    embed.add_field(
                        name="⭐ Controlling Entity", value=data["controllingEntity"]
                    )

                    embed.set_thumbnail(url=f"{url}/icon")
                    await ctx.respond(embed=embed)

            except KeyError:
                embed = await Embed.datanotfound(self, ctx)
                await ctx.respond(embed=embed, =60)

            except:
                raise


def setup(bot):
    bot.add_cog(NationCmd(bot))
