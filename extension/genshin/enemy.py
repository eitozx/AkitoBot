import akito
import discord
import aiohttp
from discord.ext import commands


class EnemyCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # genshin enemy command
    @commands.command(
        name="genshinenemy", 
        aliases=["ge", "genemy", "genshinimpactenemy"],
        description="Genshin Impact Enemy Info",
        usage = "(Enemy Name)",
        help = "If `Enemy Name` is not provided, it shows list of available enemies.")
    async def genemy(self, ctx, *, search: str = None):
        if not search:

            url = "https://api.genshin.dev/enemies/"

            async with aiohttp.ClientSession() as session:
                response = await session.get(url)
                data = await response.json(content_type=None)

            enemies = "\n".join(data).replace("-", " ").title()

            embed = discord.Embed(
                title="<:XinyanEvil:888848116923633715> Genshin Impact: Enemies",
                colour=discord.Color.blue(),
                description=f"**__Name__ of Enemies:**\n"
                f"{enemies}\n"
                f"\n**To Get Info:**\n"
                f"`/genemy [name]`\n",
            )
            await ctx.respond(embed=embed)

        else:
            search = search.replace(" ", "-").lower()
            url = f"https://api.genshin.dev/enemies/{search}"

            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(url)
                    data = await response.json(content_type=None)

                    await ctx.respond(
                        content=f"** **",
                        embed=gieinfo(ctx, data, url),
                        view=GenshinEnemy(data, ctx),
                    )

            except KeyError:
                embed = await akito.Embed.datanotfound(self, ctx)
                await ctx.respond(embed=embed, delete_after=60)

            except:
                raise


def setup(bot):
    bot.add_cog(EnemyCmd(bot))
