import discord
import aiohttp
from akito import Embed, prefix
from discord.ext import commands


class ElementCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # genshin elements command
    @commands.command(
        name="genshinelement", 
        aliases=["gel", "gelement", "genshinimpactelement"],
        description ="Genshin Impact Element Info",
        usage = "(Element Name)",
        help = "If `Element Name` is not provided, it shows list of available elements.")
    async def gelement(self, ctx, *, search: str = None):
        if not search:

            url = "https://api.genshin.dev/elements"

            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                data = await response.json(content_type=None)

            elements = "\n".join(data).replace("-", " ").title()

            embed = discord.Embed(
                title="<:BarbaraWink:889112333023080519> Genshin Impact: Elements",
                colour=discord.Color.blue(),
                description=f"**__Name__ of Elements:**\n"
                f"{elements}\n"
                f"\n**To Get Info:**\n"
                f"`/gelement [name]`\n",
            )
            await ctx.respond(embed=embed)

        else:
            search = search.replace(" ", "-").lower()
            url = f"https://api.genshin.dev/elements/{search}"

            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(url)
                    data = await response.json(content_type=None)

                    info = "\n".join(
                        [
                            f"**{i['name']}** *with {', '.join(i['elements'])}*\n{i['description']}\n"
                            for i in data["reactions"]
                        ]
                    )

                    embed = discord.Embed(
                        title=f"{data['name']}",
                        colour=discord.Color.blue(),
                        description=f"__**Reactions**__\n{info}",
                    )
                    embed.set_thumbnail(url=f"{url}/icon")
                    await ctx.respond(embed=embed)

            except KeyError:
                embed = await Embed.datanotfound(self, ctx)
                await ctx.respond(embed=embed, delete_after=60)

            except:
                raise


def setup(bot):
    bot.add_cog(ElementCmd(bot))
